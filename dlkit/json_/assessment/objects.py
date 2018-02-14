"""JSON implementations of assessment objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import importlib
import json


from bson.objectid import ObjectId
from decimal import Decimal

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote


from . import default_mdata
from .. import types
from .. import utilities
from ..id.objects import IdList
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..osid.objects import OsidObject
from ..primitives import DateTime
from ..primitives import DateTime, DisplayText
from ..primitives import Duration
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from .assessment_utilities import SIMPLE_SEQUENCE_RECORD_TYPE
from .assessment_utilities import get_assessment_part_lookup_session
from .assessment_utilities import get_assessment_section
from .assessment_utilities import get_default_part_map
from .assessment_utilities import get_default_question_map
from .assessment_utilities import get_first_part_id_for_assessment
from .assessment_utilities import get_item_lookup_session
from .assessment_utilities import get_next_part_id
from .rules import Response
from dlkit.abstract_osid.assessment import objects as abc_assessment_objects
from dlkit.abstract_osid.id.primitives import Id as abc_id
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id


ASSESSMENT_AUTHORITY = 'assessment-session'
default_language_type = Type(**types.Language().get_type_data('DEFAULT'))
default_script_type = Type(**types.Script().get_type_data('DEFAULT'))
default_format_type = Type(**types.Format().get_type_data('DEFAULT'))
UNANSWERED = 0
NULL_RESPONSE = 1


class Question(abc_assessment_objects.Question, osid_objects.OsidObject):
    """A ``Question`` represents the question portion of an assessment item.

    Like all OSID objects, a ``Question`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    """
    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='QUESTION', **kwargs)
        self._catalog_name = 'Bank'
        if 'item_id' in kwargs:
            self._item_id = kwargs['item_id']
        else:
            self._item_id = Id(kwargs['osid_object_map']['itemId'])

    @utilities.arguments_not_none
    def get_question_record(self, question_record_type):
        """Gets the item record corresponding to the given ``Question`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``question_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(question_record_type)`` is ``true`` .

        arg:    question_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.QuestionRecord) - the question
                record
        raise:  NullArgument - ``question_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(question_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(question_record_type)

    # Overide osid.Identifiable.get_id() method to cast this question id as its item id:
    def get_id(self):
        return self._item_id

    id_ = property(fget=get_id)
    ident = property(fget=get_id)

    def get_learning_objective_ids(self):
        """ This method mirrors that in the Item.

        So that questions can also be inspected for learning objectives

        """
        if 'learningObjectiveIds' not in self._my_map:  # Will this ever be the case?
            collection = JSONClientValidated('assessment',
                                             collection='Item',
                                             runtime=self._runtime)
            item_map = collection.find_one({'_id': ObjectId(Id(self._my_map['itemId']).get_identifier())})
            self._my_map['learningObjectiveIds'] = list(item_map['learningObjectiveIds'])
        return IdList(self._my_map['learningObjectiveIds'])

    learning_objective_ids = property(fget=get_learning_objective_ids)

    def get_learning_objectives(self):
        """ This method also mirrors that in the Item."""
        # This is pretty much identicial to the method in assessment.Item!
        mgr = self._get_provider_manager('LEARNING')
        lookup_session = mgr.get_objective_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_objective_bank_view()
        return lookup_session.get_objectives_by_ids(self.get_learning_objective_ids())

    learning_objectives = property(fget=get_learning_objectives)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        del obj_map['itemId']
        if 'learningObjectiveIds' not in obj_map:
            try:
                lo_ids = self.get_learning_objective_ids()
                obj_map['learningObjectiveIds'] = [str(lo_id) for lo_id in lo_ids]
            except UnicodeEncodeError:
                lo_ids = self.get_learning_objective_ids()
                obj_map['learningObjectiveIds'] = [unicode(lo_id) for lo_id in lo_ids]

        obj_map = osid_objects.OsidObject.get_object_map(self, obj_map)
        obj_map['id'] = str(self.get_id())
        return obj_map

    object_map = property(fget=get_object_map)


class QuestionForm(abc_assessment_objects.QuestionForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Questions``."""
    _namespace = 'assessment.Question'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='QUESTION', **kwargs)
        self._mdata = default_mdata.get_question_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['itemId'] = str(kwargs['item_id'])
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]

    @utilities.arguments_not_none
    def get_question_form_record(self, question_record_type):
        """Gets the ``QuestionFormRecord`` corresponding to the given question record ``Type``.

        arg:    question_record_type (osid.type.Type): the question
                record type
        return: (osid.assessment.records.QuestionFormRecord) - the
                question record
        raise:  NullArgument - ``question_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(question_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(question_record_type)


class QuestionList(abc_assessment_objects.QuestionList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``QuestionList`` provides a means for accessing ``Question`` elements sequentially either one at a time or many at a time.

    Examples: while (ql.hasNext()) { Question question =
    ql.getNextQuestion(); }

    or
      while (ql.hasNext()) {
           Question[] question = al.getNextQuestions(ql.available());
      }

    """

    def get_next_question(self):
        """Gets the next ``Question`` in this list.

        return: (osid.assessment.Question) - the next ``Question`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Question`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Question)

    __next__ = next

    next_question = property(fget=get_next_question)

    @utilities.arguments_not_none
    def get_next_questions(self, n):
        """Gets the next set of ``Question`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Question`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Question) - an array of ``Question``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(QuestionList, number=n)


class Answer(abc_assessment_objects.Answer, osid_objects.OsidObject):
    """An ``Answer`` represents the question portion of an assessment item.

    Like all OSID objects, an ``Answer`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    _namespace = 'assessment.Answer'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ANSWER', **kwargs)
        self._catalog_name = 'Bank'

    @utilities.arguments_not_none
    def get_answer_record(self, answer_record_type):
        """Gets the answer record corresponding to the given ``Answer`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``answer_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(answer_record_type)`` is ``true`` .

        arg:    answer_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.AnswerRecord) - the answer
                record
        raise:  NullArgument - ``answer_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(answer_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(answer_record_type)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        del obj_map['itemId']
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class AnswerForm(abc_assessment_objects.AnswerForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Answers``."""
    _namespace = 'assessment.Answer'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ANSWER', **kwargs)
        self._mdata = default_mdata.get_answer_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['itemId'] = str(kwargs['item_id'])
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]

    @utilities.arguments_not_none
    def get_answer_form_record(self, answer_record_type):
        """Gets the ``AnswerFormRecord`` corresponding to the given answer record ``Type``.

        arg:    answer_record_type (osid.type.Type): the answer record
                type
        return: (osid.assessment.records.AnswerFormRecord) - the answer
                record
        raise:  NullArgument - ``answer_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(answer_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(answer_record_type)


class AnswerList(abc_assessment_objects.AnswerList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AnswerList`` provides a means for accessing ``Answer`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Answer answer = al.getNextAnswer();
    }

    or
      while (al.hasNext()) {
           Answer[] answer = al.getNextAnswers(al.available());
      }

    """

    def get_next_answer(self):
        """Gets the next ``Answer`` in this list.

        return: (osid.assessment.Answer) - the next ``Answer`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Answer`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Answer)

    __next__ = next

    next_answer = property(fget=get_next_answer)

    @utilities.arguments_not_none
    def get_next_answers(self, n):
        """Gets the next set of ``Answer`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Answer`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Answer) - an array of ``Answer``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AnswerList, number=n)


class Item(abc_assessment_objects.Item, osid_objects.OsidObject, osid_markers.Aggregateable):
    """An ``Item`` represents an individual assessment item such as a question.

    Like all OSID objects, a ``Item`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    An ``Item`` is composed of a ``Question`` and an ``Answer``.

    """
    _namespace = 'assessment.Item'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ITEM', **kwargs)
        self._catalog_name = 'Bank'

    def get_learning_objective_ids(self):
        """Gets the ``Ids`` of any ``Objectives`` corresponding to this item.

        return: (osid.id.IdList) - the learning objective ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_asset_ids_template
        return IdList(self._my_map['learningObjectiveIds'])

    learning_objective_ids = property(fget=get_learning_objective_ids)

    def get_learning_objectives(self):
        """Gets the any ``Objectives`` corresponding to this item.

        return: (osid.learning.ObjectiveList) - the learning objectives
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_assets_template
        if not bool(self._my_map['learningObjectiveIds']):
            raise errors.IllegalState('no learningObjectiveIds')
        mgr = self._get_provider_manager('LEARNING')
        if not mgr.supports_objective_lookup():
            raise errors.OperationFailed('Learning does not support Objective lookup')

        # What about the Proxy?
        lookup_session = mgr.get_objective_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_objective_bank_view()
        return lookup_session.get_objectives_by_ids(self.get_learning_objective_ids())

    learning_objectives = property(fget=get_learning_objectives)

    def get_question_id(self):
        """Gets the ``Id`` of the ``Question``.

        return: (osid.id.Id) - the question ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_question().get_id()

    question_id = property(fget=get_question_id)

    def get_question(self):
        """Gets the question.

        return: (osid.assessment.Question) - the question
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        question_map = dict(self._my_map['question'])
        question_map['learningObjectiveIds'] = self._my_map['learningObjectiveIds']
        return Question(osid_object_map=question_map,
                        runtime=self._runtime,
                        proxy=self._proxy)

    question = property(fget=get_question)

    def get_answer_ids(self):
        """Gets the ``Ids`` of the answers.

        Questions may have more than one acceptable answer.

        return: (osid.id.IdList) - the answer ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.Asset.get_asset_content_ids_template
        id_list = []
        for answer in self.get_answers():
            id_list.append(answer.get_id())
        return IdList(id_list)

    answer_ids = property(fget=get_answer_ids)

    def get_answers(self):
        """Gets the answers.

        return: (osid.assessment.AnswerList) - the answers
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.Asset.get_asset_contents_template
        return AnswerList(
            self._my_map['answers'],
            runtime=self._runtime,
            proxy=self._proxy)

    def _delete(self):
        for answer in self.get_answers():
            answer._delete()
        osid_objects.OsidObject._delete(self)

    answers = property(fget=get_answers)

    @utilities.arguments_not_none
    def get_item_record(self, item_record_type):
        """Gets the item record corresponding to the given ``Item`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .

        arg:    item_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.ItemRecord) - the item record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(item_record_type)

    def get_configuration(self):
        config = dict()
        try:
            dict.update(self.get_question().get_configuration())
        except AttributeError:
            pass
        for record in self._records:
            try:
                dict.update(record.get_configuration())
            except AttributeError:
                pass
        return config  # Should this method build a real OSID configuration instead?

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['question']:
            obj_map['question'] = self.get_question().get_object_map()
        obj_map['answers'] = []
        for answer in self.get_answers():
            obj_map['answers'].append(answer.get_object_map())
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)

    def _delete(self):
        try:
            self.get_question()._delete()
        except:
            pass
        finally:
            for answer in self.get_answers():
                answer._delete()
            osid_objects.OsidObject._delete(self)

    def is_feedback_available(self):
        """is general feedback available for this Item

        to be overriden in a record extension

        """
        return False

    def get_feedback(self):
        """get general feedback for this Item
        to be overriden in a record extension

        """
        if self.is_feedback_available():
            pass  # what is feedback anyway? Just a DisplayText or something more?
        raise errors.IllegalState()

    def is_solution_available(self):
        """is a solution available for this Item (is this different than feedback?)

        to be overriden in a record extension

        """
        return False

    def get_solution(self):
        """get general feedback for this Item (is this different than feedback?)

        to be overriden in a record extension

        """
        if self.is_solution_available():
            pass
        raise errors.IllegalState()

    def is_feedback_available_for_response(self, response):
        """is feedback available for a particular response

        to be overriden in a record extension

        """
        return False

    def get_feedback_for_response(self, response):
        """get feedback for a particular response
        to be overriden in a record extension

        """
        if self.is_feedback_available_for_response(response):
            pass  # what is feedback anyway? Just a DisplayText or something more?
        raise errors.IllegalState()

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular response
        to be overriden in a record extension

        """
        return False

    def is_response_correct(self, response):
        """returns True if response evaluates to an Item Answer that is 100 percent correct

        to be overriden in a record extension

        """
        if self.is_correctness_available_for_response(response):
            pass  # return True or False
        raise errors.IllegalState()

    def get_correctness_for_response(self, response):
        """get measure of correctness available for a particular response
        to be overriden in a record extension

        """
        if self.is_correctness_available_for_response(response):
            pass  # return a correctness score 0 thru 100
        raise errors.IllegalState()

    def are_confused_learning_objective_ids_available_for_response(self, response):
        """is a learning objective available for a particular response
        to be overriden in a record extension

        """
        return False

    def get_confused_learning_objective_ids_for_response(self, response):
        """get learning objectives for a particular response

        to be overriden in a record extension

        """
        if self.are_confused_learning_objective_ids_available_for_response(response):
            pass  # return Objective IdList
        raise errors.IllegalState()


class ItemForm(abc_assessment_objects.ItemForm, osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm):
    """This is the form for creating and updating ``Items``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ItemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment.Item'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ITEM', **kwargs)
        self._mdata = default_mdata.get_item_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._learning_objectives_default = self._mdata['learning_objectives']['default_id_values']

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['learningObjectiveIds'] = self._learning_objectives_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['question'] = None
        self._my_map['answers'] = []

    def get_learning_objectives_metadata(self):
        """Gets the metadata for learning objectives.

        return: (osid.Metadata) - metadata for the learning objectives
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.get_assets_metadata_template
        metadata = dict(self._mdata['learning_objectives'])
        metadata.update({'existing_learning_objectives_values': self._my_map['learningObjectiveIds']})
        return Metadata(**metadata)

    learning_objectives_metadata = property(fget=get_learning_objectives_metadata)

    @utilities.arguments_not_none
    def set_learning_objectives(self, objective_ids):
        """Sets the learning objectives.

        arg:    objective_ids (osid.id.Id[]): the learning objective
                ``Ids``
        raise:  InvalidArgument - ``objective_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.set_assets_template
        if not isinstance(objective_ids, list):
            raise errors.InvalidArgument()
        if self.get_learning_objectives_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in objective_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            idstr_list.append(str(object_id))
        self._my_map['learningObjectiveIds'] = idstr_list

    def clear_learning_objectives(self):
        """Clears the learning objectives.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.clear_assets_template
        if (self.get_learning_objectives_metadata().is_read_only() or
                self.get_learning_objectives_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['learningObjectiveIds'] = self._learning_objectives_default

    learning_objectives = property(fset=set_learning_objectives, fdel=clear_learning_objectives)

    @utilities.arguments_not_none
    def get_item_form_record(self, item_record_type):
        """Gets the ``ItemnFormRecord`` corresponding to the given item record ``Type``.

        arg:    item_record_type (osid.type.Type): the item record type
        return: (osid.assessment.records.ItemFormRecord) - the item
                record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(item_record_type)


class ItemList(abc_assessment_objects.ItemList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ItemList`` provides a means for accessing ``Item`` elements sequentially either one at a time or many at a time.

    Examples: while (il.hasNext()) { Item item = il.getNextItem(); }

    or
      while (il.hasNext()) {
           Item[] items = il.getNextItems(il.available());
      }

    """

    def get_next_item(self):
        """Gets the next ``Item`` in this list.

        return: (osid.assessment.Item) - the next ``Item`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Item`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Item)

    __next__ = next

    next_item = property(fget=get_next_item)

    @utilities.arguments_not_none
    def get_next_items(self, n):
        """Gets the next set of ``Item`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Item`` elements requested
                which should be less than or equal to ``available()``
        return: (osid.assessment.Item) - an array of ``Item``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ItemList, number=n)


class Assessment(abc_assessment_objects.Assessment, osid_objects.OsidObject):
    """An ``Assessment`` represents a sequence of assessment items.

    Like all OSID objects, an ``Assessment`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    An ``Assessment`` may have an accompanying rubric used for assessing
    performance. The rubric assessment is established canonically in
    this ``Assessment``.

    """
    _namespace = 'assessment.Assessment'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ASSESSMENT', **kwargs)
        self._catalog_name = 'Bank'

    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        return: (osid.id.Id) - a grade ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['levelId']):
            raise errors.IllegalState('this Assessment has no level')
        else:
            return Id(self._my_map['levelId'])

    level_id = property(fget=get_level_id)

    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        return: (osid.grading.Grade) - the level
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['levelId']):
            raise errors.IllegalState('this Assessment has no level')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_level_id())
        return osid_object

    level = property(fget=get_level)

    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['rubricId'])

    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this Assessment has no rubric')
        else:
            return Id(self._my_map['rubricId'])

    rubric_id = property(fget=get_rubric_id)

    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.Assessment) - the assessment
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this Assessment has no rubric')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_lookup():
            raise errors.OperationFailed('Assessment does not support Assessment lookup')
        lookup_session = mgr.get_assessment_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        osid_object = lookup_session.get_assessment(self.get_rubric_id())
        return osid_object

    rubric = property(fget=get_rubric)

    @utilities.arguments_not_none
    def get_assessment_record(self, assessment_record_type):
        """Gets the assessment record corresponding to the given ``Assessment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_record_type)`` is ``true`` .

        arg:    assessment_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.AssessmentRecord) - the
                assessment record
        raise:  NullArgument - ``assessment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_record_type)

    def has_children(self):
        """This method can be overwritten by a record extension."""
        return self._supports_simple_sequencing() and self._my_map['childIds']

    def get_child_ids(self):
        """This method can be overwritten by a record extension."""
        if self._supports_simple_sequencing():
            return IdList(self._my_map['childIds'])
        else:
            raise errors.IllegalState()

    def has_next_assessment_part(self, assessment_part_id):
        """This supports the basic simple sequence case. Can be overriden in a record for other cases"""
        if not self.supports_child_ordering or not self.supports_simple_child_sequencing:
            raise AttributeError()  # Only available through a record extension
        if 'childIds' in self._my_map and str(assessment_part_id) in self._my_map['childIds']:
            if self._my_map['childIds'][-1] != str(assessment_part_id):
                return True
            else:
                return False
        raise errors.NotFound('the Part with Id ' + str(assessment_part_id) + ' is not a child of this Part')

    def get_next_assessment_part_id(self, assessment_part_id=None):
        """This supports the basic simple sequence case. Can be overriden in a record for other cases"""
        if assessment_part_id is None:
            part_id = self.get_id()
        else:
            part_id = assessment_part_id
        return get_next_part_id(part_id,
                                runtime=self._runtime,
                                proxy=self._proxy,
                                sequestered=True)[0]
        # if self.has_next_assessment_part(assessment_part_id):
        #     return Id(self._my_map['childIds'][self._my_map['childIds'].index(str(assessment_part_id)) + 1])

    def get_next_assessment_part(self, assessment_part_id):
        next_part_id = self.get_next_assessment_part_id(assessment_part_id)
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment_part(next_part_id)

    def are_items_sequential(self):
        """This method can be overwritten by a record extension."""
        return False

    def are_items_shuffled(self):
        """This method can be overwritten by a record extension."""
        return False

    def uses_simple_section_sequencing(self):
        """This method can be overwritten by a record extension."""
        return False

    def uses_shuffled_section_sequencing(self):
        """This method can be overwritten by a record extension."""
        return False

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if 'itemIds' in obj_map:
            del obj_map['itemIds']
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class AssessmentForm(abc_assessment_objects.AssessmentForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Assessments``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment.Assessment'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ASSESSMENT', **kwargs)
        self._mdata = default_mdata.get_assessment_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._rubric_default = self._mdata['rubric']['default_id_values'][0]
        self._level_default = self._mdata['level']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['rubricId'] = self._rubric_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['levelId'] = self._level_default
        if self._supports_simple_sequencing():
            self._my_map['childIds'] = []

    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        return: (osid.Metadata) - metadata for the grade level
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['level'])
        metadata.update({'existing_id_values': self._my_map['levelId']})
        return Metadata(**metadata)

    level_metadata = property(fget=get_level_metadata)

    @utilities.arguments_not_none
    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        arg:    grade_id (osid.id.Id): the grade level
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_level_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_id):
            raise errors.InvalidArgument()
        self._my_map['levelId'] = str(grade_id)

    def clear_level(self):
        """Clears the grade level.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_level_metadata().is_read_only() or
                self.get_level_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['levelId'] = self._level_default

    level = property(fset=set_level, fdel=clear_level)

    def get_rubric_metadata(self):
        """Gets the metadata for a rubric assessment.

        return: (osid.Metadata) - metadata for the assesment
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['rubric'])
        metadata.update({'existing_id_values': self._my_map['rubricId']})
        return Metadata(**metadata)

    rubric_metadata = property(fget=get_rubric_metadata)

    @utilities.arguments_not_none
    def set_rubric(self, assessment_id):
        """Sets the rubric expressed as another assessment.

        arg:    assessment_id (osid.id.Id): the assessment ``Id``
        raise:  InvalidArgument - ``assessment_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``assessment_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_rubric_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(assessment_id):
            raise errors.InvalidArgument()
        self._my_map['rubricId'] = str(assessment_id)

    def clear_rubric(self):
        """Clears the rubric.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_rubric_metadata().is_read_only() or
                self.get_rubric_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['rubricId'] = self._rubric_default

    rubric = property(fset=set_rubric, fdel=clear_rubric)

    @utilities.arguments_not_none
    def get_assessment_form_record(self, assessment_record_type):
        """Gets the ``AssessmentFormRecord`` corresponding to the given assessment record ``Type``.

        arg:    assessment_record_type (osid.type.Type): the assessment
                record type
        return: (osid.assessment.records.AssessmentFormRecord) - the
                assessment record
        raise:  NullArgument - ``assessment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_record_type)

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])

    def set_children(self, child_ids):
        """Set the children IDs"""
        if not self._supports_simple_sequencing():
            raise errors.IllegalState()
        self._my_map['childIds'] = [str(i) for i in child_ids]


class AssessmentList(abc_assessment_objects.AssessmentList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentList`` provides a means for accessing ``Assessment`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Assessment assessment =
    al.getNextAssessment(); }

    or
      while (al.hasNext()) {
           Assessment[] assessments = al.hetNextAssessments(al.available());
      }

    """

    def get_next_assessment(self):
        """Gets the next ``Assessment`` in this list.

        return: (osid.assessment.Assessment) - the next ``Assessment``
                in this list. The ``has_next()`` method should be used
                to test that a next ``Assessment`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Assessment)

    __next__ = next

    next_assessment = property(fget=get_next_assessment)

    @utilities.arguments_not_none
    def get_next_assessments(self, n):
        """Gets the next set of ``Assessment`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Assessment`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Assessment) - an array of
                ``Assessment`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AssessmentList, number=n)


class AssessmentOffered(abc_assessment_objects.AssessmentOffered, osid_objects.OsidObject, osid_markers.Subjugateable):
    """An ``AssessmentOffered`` represents a sequence of assessment items.

    Like all OSID objects, an ``AssessmentOffered`` is identified by its
    ``Id`` and any persisted references should use the ``Id``.

    """
    _namespace = 'assessment.AssessmentOffered'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ASSESSMENT_OFFERED', **kwargs)
        self._catalog_name = 'Bank'

    def get_assessment_id(self):
        """Gets the assessment ``Id`` corresponding to this assessment offering.

        return: (osid.id.Id) - the assessment id
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        if not bool(self._my_map['assessmentId']):
            raise errors.IllegalState('assessment empty')
        return Id(self._my_map['assessmentId'])

    assessment_id = property(fget=get_assessment_id)

    def get_assessment(self):
        """Gets the assessment corresponding to this assessment offereng.

        return: (osid.assessment.Assessment) - the assessment
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        if not bool(self._my_map['assessmentId']):
            raise errors.IllegalState('assessment empty')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_lookup():
            raise errors.OperationFailed('Assessment does not support Assessment lookup')
        lookup_session = mgr.get_assessment_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment(self.get_assessment_id())

    assessment = property(fget=get_assessment)

    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        return: (osid.id.Id) - a grade id
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['levelId']):
            raise errors.IllegalState('this AssessmentOffered has no level')
        else:
            return Id(self._my_map['levelId'])

    level_id = property(fget=get_level_id)

    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        return: (osid.grading.Grade) - the level
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['levelId']):
            raise errors.IllegalState('this AssessmentOffered has no level')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_level_id())
        return osid_object

    level = property(fget=get_level)

    def are_items_sequential(self):
        """Tests if the items or parts in this assessment are taken sequentially.

        return: (boolean) - ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._my_map['itemsSequential'] is None:
            return self.get_assessment().are_items_sequential()
        return bool(self._my_map['itemsSequential'])

    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        return: (boolean) - ``true`` if the items appear in a random
                order, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._my_map['itemsShuffled'] is None:
            return self.get_assessment().are_items_shuffled()
        return bool(self._my_map['itemsShuffled'])

    def has_start_time(self):
        """Tests if there is a fixed start time for this assessment.

        return: (boolean) - ``true`` if there is a fixed start time,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetContent.has_url_template
        try:
            return bool(self._my_map['startTime'])
        except KeyError:
            return False

    def get_start_time(self):
        """Gets the start time for this assessment.

        return: (osid.calendaring.DateTime) - the designated start time
        raise:  IllegalState - ``has_start_time()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOffered.get_start_time_template
        if not bool(self._my_map['startTime']):
            raise errors.IllegalState()
        dt = self._my_map['startTime']
        return DateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    start_time = property(fget=get_start_time)

    def has_deadline(self):
        """Tests if there is a fixed end time for this assessment.

        return: (boolean) - ``true`` if there is a fixed end time,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetContent.has_url_template
        try:
            return bool(self._my_map['deadline'])
        except KeyError:
            return False

    def get_deadline(self):
        """Gets the end time for this assessment.

        return: (osid.calendaring.DateTime) - the designated end time
        raise:  IllegalState - ``has_deadline()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOffered.get_start_time_template
        if not bool(self._my_map['deadline']):
            raise errors.IllegalState()
        dt = self._my_map['deadline']
        return DateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    deadline = property(fget=get_deadline)

    def has_duration(self):
        """Tests if there is a fixed duration for this assessment.

        return: (boolean) - ``true`` if there is a fixed duration,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetContent.has_url_template
        try:
            return bool(self._my_map['duration'])
        except KeyError:
            return False

    def get_duration(self):
        """Gets the duration for this assessment.

        return: (osid.calendaring.Duration) - the duration
        raise:  IllegalState - ``has_duration()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOffered.get_duration_template
        if not bool(self._my_map['duration']):
            raise errors.IllegalState()
        return Duration(**self._my_map['duration'])

    duration = property(fget=get_duration)

    def is_scored(self):
        """Tests if this assessment will be scored.

        return: (boolean) - ``true`` if this assessment will be scored
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['scored'])

    def get_score_system_id(self):
        """Gets the grade system ``Id`` for the score.

        return: (osid.id.Id) - the grade system ``Id``
        raise:  IllegalState - ``is_scored()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['scoreSystemId']):
            raise errors.IllegalState('this AssessmentOffered has no score_system')
        else:
            return Id(self._my_map['scoreSystemId'])

    score_system_id = property(fget=get_score_system_id)

    def get_score_system(self):
        """Gets the grade system for the score.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_scored()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['scoreSystemId']):
            raise errors.IllegalState('this AssessmentOffered has no score_system')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_system_lookup():
            raise errors.OperationFailed('Grading does not support GradeSystem lookup')
        lookup_session = mgr.get_grade_system_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade_system(self.get_score_system_id())
        return osid_object

    score_system = property(fget=get_score_system)

    def is_graded(self):
        """Tests if this assessment will be graded.

        return: (boolean) - ``true`` if this assessment will be graded,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['graded'])

    def get_grade_system_id(self):
        """Gets the grade system ``Id`` for the grade.

        return: (osid.id.Id) - the grade system ``Id``
        raise:  IllegalState - ``is_graded()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['gradeSystemId']):
            raise errors.IllegalState('this AssessmentOffered has no grade_system')
        else:
            return Id(self._my_map['gradeSystemId'])

    grade_system_id = property(fget=get_grade_system_id)

    def get_grade_system(self):
        """Gets the grade system for the grade.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_graded()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['gradeSystemId']):
            raise errors.IllegalState('this AssessmentOffered has no grade_system')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_system_lookup():
            raise errors.OperationFailed('Grading does not support GradeSystem lookup')
        lookup_session = mgr.get_grade_system_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade_system(self.get_grade_system_id())
        return osid_object

    grade_system = property(fget=get_grade_system)

    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['rubricId'])

    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment offered ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this AssessmentOffered has no rubric')
        else:
            return Id(self._my_map['rubricId'])

    rubric_id = property(fget=get_rubric_id)

    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this AssessmentOffered has no rubric')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_offered_lookup():
            raise errors.OperationFailed('Assessment does not support AssessmentOffered lookup')
        lookup_session = mgr.get_assessment_offered_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        osid_object = lookup_session.get_assessment_offered(self.get_rubric_id())
        return osid_object

    rubric = property(fget=get_rubric)

    @utilities.arguments_not_none
    def get_assessment_offered_record(self, assessment_taken_record_type):
        """Gets the assessment offered record corresponding to the given ``AssessmentOffered`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_offered_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_offered_record_type)`` is ``true``
        .

        arg:    assessment_taken_record_type (osid.type.Type): an
                assessment offered record type
        return: (osid.assessment.records.AssessmentOfferedRecord) - the
                assessment offered record
        raise:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_taken_record_type)

    def get_display_name(self):
        # Overrides osid.objects.OsidObject.get_display_name to default to Assessment's
        # display_name if none has been authored for this AssessmentOffered
        from ..osid.objects import OsidObject
        if osid_objects.OsidObject.get_display_name(self).get_text():
            return osid_objects.OsidObject.get_display_name(self)
        else:
            return self.get_assessment().get_display_name()

    def get_description(self):
        # Overrides osid.objects.OsidObject.get_description to default to Assessment's
        # description if none has been authored for this AssessmentOffered
        from ..osid.objects import OsidObject
        if osid_objects.OsidObject.get_description(self).get_text():
            return osid_objects.OsidObject.get_description(self)
        else:
            return self.get_assessment().get_description()

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['startTime'] is not None:
            start_time = obj_map['startTime']
            obj_map['startTime'] = dict()
            obj_map['startTime']['year'] = start_time.year
            obj_map['startTime']['month'] = start_time.month
            obj_map['startTime']['day'] = start_time.day
            obj_map['startTime']['hour'] = start_time.hour
            obj_map['startTime']['minute'] = start_time.minute
            obj_map['startTime']['second'] = start_time.second
            obj_map['startTime']['microsecond'] = start_time.microsecond
        if obj_map['deadline'] is not None:
            deadline = obj_map['deadline']
            obj_map['deadline'] = dict()
            obj_map['deadline']['year'] = deadline.year
            obj_map['deadline']['month'] = deadline.month
            obj_map['deadline']['day'] = deadline.day
            obj_map['deadline']['hour'] = deadline.hour
            obj_map['deadline']['minute'] = deadline.minute
            obj_map['deadline']['second'] = deadline.second
            obj_map['deadline']['microsecond'] = deadline.microsecond
        obj_map = osid_objects.OsidObject.get_object_map(self, obj_map)
        if obj_map['displayName']['text'] == '':
            obj_map['displayName']['text'] = self.get_display_name().get_text()
        if obj_map['description']['text'] == '':
            obj_map['description']['text'] = self.get_description().get_text()
        return obj_map

    object_map = property(fget=get_object_map)

    def are_sections_sequential(self):
        """This method can be overwritten by a record extension."""
        return self.get_assessment().uses_simple_section_sequencing()  # Records should check this

    def are_sections_shuffled(self):
        """This method can be overwritten by a record extension."""
        return self.get_assessment().uses_shuffled_section_sequencing()  # Records should check this


class AssessmentOfferedForm(abc_assessment_objects.AssessmentOfferedForm, osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating an ``AssessmentOffered``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentOfferedAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment.AssessmentOffered'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ASSESSMENT_OFFERED', **kwargs)
        self._mdata = default_mdata.get_assessment_offered_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._level_default = self._mdata['level']['default_id_values'][0]
        self._start_time_default = self._mdata['start_time']['default_date_time_values'][0]
        self._grade_system_default = self._mdata['grade_system']['default_id_values'][0]
        self._items_shuffled_default = self._mdata['items_shuffled']['default_boolean_values'][0]
        self._score_system_default = self._mdata['score_system']['default_id_values'][0]
        self._deadline_default = self._mdata['deadline']['default_date_time_values'][0]
        self._duration_default = self._mdata['duration']['default_duration_values'][0]
        self._items_sequential_default = self._mdata['items_sequential']['default_boolean_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['levelId'] = self._level_default
        self._my_map['startTime'] = self._start_time_default
        self._my_map['gradeSystemId'] = self._grade_system_default
        self._my_map['itemsShuffled'] = self._items_shuffled_default
        self._my_map['scoreSystemId'] = self._score_system_default
        self._my_map['deadline'] = self._deadline_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['duration'] = self._duration_default
        self._my_map['assessmentId'] = str(kwargs['assessment_id'])
        self._my_map['itemsSequential'] = self._items_sequential_default

    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        return: (osid.Metadata) - metadata for the grade level
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['level'])
        metadata.update({'existing_id_values': self._my_map['levelId']})
        return Metadata(**metadata)

    level_metadata = property(fget=get_level_metadata)

    @utilities.arguments_not_none
    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        arg:    grade_id (osid.id.Id): the grade level
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_level_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_id):
            raise errors.InvalidArgument()
        self._my_map['levelId'] = str(grade_id)

    def clear_level(self):
        """Clears the level.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_level_metadata().is_read_only() or
                self.get_level_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['levelId'] = self._level_default

    level = property(fset=set_level, fdel=clear_level)

    def get_items_sequential_metadata(self):
        """Gets the metadata for sequential operation.

        return: (osid.Metadata) - metadata for the sequential flag
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['items_sequential'])
        metadata.update({'existing_boolean_values': self._my_map['itemsSequential']})
        return Metadata(**metadata)

    items_sequential_metadata = property(fget=get_items_sequential_metadata)

    @utilities.arguments_not_none
    def set_items_sequential(self, sequential):
        """Sets the items sequential flag.

        arg:    sequential (boolean): ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        raise:  InvalidArgument - ``sequential`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_group_template
        if self.get_items_sequential_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_boolean(sequential):
            raise errors.InvalidArgument()
        self._my_map['itemsSequential'] = sequential

    def clear_items_sequential(self):
        """Clears the items sequential flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_group_template
        if (self.get_items_sequential_metadata().is_read_only() or
                self.get_items_sequential_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['itemsSequential'] = self._items_sequential_default

    items_sequential = property(fset=set_items_sequential, fdel=clear_items_sequential)

    def get_items_shuffled_metadata(self):
        """Gets the metadata for shuffling items.

        return: (osid.Metadata) - metadata for the shuffled flag
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['items_shuffled'])
        metadata.update({'existing_boolean_values': self._my_map['itemsShuffled']})
        return Metadata(**metadata)

    items_shuffled_metadata = property(fget=get_items_shuffled_metadata)

    @utilities.arguments_not_none
    def set_items_shuffled(self, shuffle):
        """Sets the shuffle flag.

        The shuffle flag may be overidden by other assessment sequencing
        rules.

        arg:    shuffle (boolean): ``true`` if the items are shuffled,
                ``false`` if the items appear in the designated order
        raise:  InvalidArgument - ``shuffle`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_group_template
        if self.get_items_shuffled_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_boolean(shuffle):
            raise errors.InvalidArgument()
        self._my_map['itemsShuffled'] = shuffle

    def clear_items_shuffled(self):
        """Clears the shuffle flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_group_template
        if (self.get_items_shuffled_metadata().is_read_only() or
                self.get_items_shuffled_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['itemsShuffled'] = self._items_shuffled_default

    items_shuffled = property(fset=set_items_shuffled, fdel=clear_items_shuffled)

    def get_start_time_metadata(self):
        """Gets the metadata for the assessment start time.

        return: (osid.Metadata) - metadata for the start time
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['start_time'])
        metadata.update({'existing_date_time_values': self._my_map['startTime']})
        return Metadata(**metadata)

    start_time_metadata = property(fget=get_start_time_metadata)

    @utilities.arguments_not_none
    def set_start_time(self, start):
        """Sets the assessment start time.

        arg:    start (osid.calendaring.DateTime): assessment start time
        raise:  InvalidArgument - ``start`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.set_start_time_template
        if self.get_start_time_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_date_time(
                start,
                self.get_start_time_metadata()):
            raise errors.InvalidArgument()
        self._my_map['startTime'] = start

    def clear_start_time(self):
        """Clears the start time.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.clear_start_time_template
        if (self.get_start_time_metadata().is_read_only() or
                self.get_start_time_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['startTime'] = self._start_time_default

    start_time = property(fset=set_start_time, fdel=clear_start_time)

    def get_deadline_metadata(self):
        """Gets the metadata for the assessment deadline.

        return: (osid.Metadata) - metadata for the end time
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['deadline'])
        metadata.update({'existing_date_time_values': self._my_map['deadline']})
        return Metadata(**metadata)

    deadline_metadata = property(fget=get_deadline_metadata)

    @utilities.arguments_not_none
    def set_deadline(self, end):
        """Sets the assessment end time.

        arg:    end (timestamp): assessment end time
        raise:  InvalidArgument - ``end`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.set_start_time_template
        if self.get_deadline_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_timestamp(
                end,
                self.get_deadline_metadata()):
            raise errors.InvalidArgument()
        self._my_map['deadline'] = end

    def clear_deadline(self):
        """Clears the deadline.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.clear_start_time_template
        if (self.get_deadline_metadata().is_read_only() or
                self.get_deadline_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['deadline'] = self._deadline_default

    deadline = property(fset=set_deadline, fdel=clear_deadline)

    def get_duration_metadata(self):
        """Gets the metadata for the assessment duration.

        return: (osid.Metadata) - metadata for the duration
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['duration'])
        metadata.update({'existing_duration_values': self._my_map['duration']})
        return Metadata(**metadata)

    duration_metadata = property(fget=get_duration_metadata)

    @utilities.arguments_not_none
    def set_duration(self, duration):
        """Sets the assessment duration.

        arg:    duration (osid.calendaring.Duration): assessment
                duration
        raise:  InvalidArgument - ``duration`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.set_duration_template
        if self.get_duration_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_duration(
                duration,
                self.get_duration_metadata()):
            raise errors.InvalidArgument()
        map = dict()
        map['days'] = duration.days
        map['seconds'] = duration.seconds
        map['microseconds'] = duration.microseconds
        self._my_map['duration'] = map

    def clear_duration(self):
        """Clears the duration.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.clear_duration_template
        if (self.get_duration_metadata().is_read_only() or
                self.get_duration_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['duration'] = self._duration_default

    duration = property(fset=set_duration, fdel=clear_duration)

    def get_score_system_metadata(self):
        """Gets the metadata for a score system.

        return: (osid.Metadata) - metadata for the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['score_system'])
        metadata.update({'existing_id_values': self._my_map['scoreSystemId']})
        return Metadata(**metadata)

    score_system_metadata = property(fget=get_score_system_metadata)

    @utilities.arguments_not_none
    def set_score_system(self, grade_system_id):
        """Sets the scoring system.

        arg:    grade_system_id (osid.id.Id): the grade system
        raise:  InvalidArgument - ``grade_system_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_score_system_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_system_id):
            raise errors.InvalidArgument()
        self._my_map['scoreSystemId'] = str(grade_system_id)

    def clear_score_system(self):
        """Clears the score system.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_score_system_metadata().is_read_only() or
                self.get_score_system_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['scoreSystemId'] = self._score_system_default

    score_system = property(fset=set_score_system, fdel=clear_score_system)

    def get_grade_system_metadata(self):
        """Gets the metadata for a grading system.

        return: (osid.Metadata) - metadata for the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['grade_system'])
        metadata.update({'existing_id_values': self._my_map['gradeSystemId']})
        return Metadata(**metadata)

    grade_system_metadata = property(fget=get_grade_system_metadata)

    @utilities.arguments_not_none
    def set_grade_system(self, grade_system_id):
        """Sets the grading system.

        arg:    grade_system_id (osid.id.Id): the grade system
        raise:  InvalidArgument - ``grade_system_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_grade_system_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_system_id):
            raise errors.InvalidArgument()
        self._my_map['gradeSystemId'] = str(grade_system_id)

    def clear_grade_system(self):
        """Clears the grading system.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_grade_system_metadata().is_read_only() or
                self.get_grade_system_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['gradeSystemId'] = self._grade_system_default

    grade_system = property(fset=set_grade_system, fdel=clear_grade_system)

    @utilities.arguments_not_none
    def get_assessment_offered_form_record(self, assessment_offered_record_type):
        """Gets the ``AssessmentOfferedFormRecord`` corresponding to the given assessment record ``Type``.

        arg:    assessment_offered_record_type (osid.type.Type): the
                assessment offered record type
        return: (osid.assessment.records.AssessmentOfferedFormRecord) -
                the assessment offered record
        raise:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_offered_record_type)


class AssessmentOfferedList(abc_assessment_objects.AssessmentOfferedList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentOfferedList`` provides a means for accessing ``AssessmentTaken`` elements sequentially either one at a time or many at a time.

    Examples: while (aol.hasNext()) { AssessmentOffered assessment =
    aol.getNextAssessmentOffered();

    or
      while (aol.hasNext()) {
           AssessmentOffered[] assessments = aol.hetNextAssessmentsOffered(aol.available());
      }

    """

    def get_next_assessment_offered(self):
        """Gets the next ``AssessmentOffered`` in this list.

        return: (osid.assessment.AssessmentOffered) - the next
                ``AssessmentOffered`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentOffered`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(AssessmentOffered)

    __next__ = next

    next_assessment_offered = property(fget=get_next_assessment_offered)

    @utilities.arguments_not_none
    def get_next_assessments_offered(self, n):
        """Gets the next set of ``AssessmentOffered`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentOffered``
                elements requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentOffered) - an array of
                ``AssessmentOffered`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AssessmentOfferedList, number=n)


class AssessmentTaken(abc_assessment_objects.AssessmentTaken, osid_objects.OsidObject):
    """Represents a taken assessment or an assessment in progress."""
    _namespace = 'assessment.AssessmentTaken'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ASSESSMENT_TAKEN', **kwargs)
        self._catalog_name = 'Bank'
        self._assessment_sections = dict()

    def get_assessment_offered_id(self):
        """Gets the ``Id`` of the ``AssessmentOffered``.

        return: (osid.id.Id) - the assessment offered ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        if not bool(self._my_map['assessmentOfferedId']):
            raise errors.IllegalState('assessment_offered empty')
        return Id(self._my_map['assessmentOfferedId'])

    assessment_offered_id = property(fget=get_assessment_offered_id)

    def get_assessment_offered(self):
        """Gets the ``AssessmentOffered``.

        return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        if not bool(self._my_map['assessmentOfferedId']):
            raise errors.IllegalState('assessment_offered empty')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_offered_lookup():
            raise errors.OperationFailed('Assessment does not support AssessmentOffered lookup')
        lookup_session = mgr.get_assessment_offered_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment_offered(self.get_assessment_offered_id())

    assessment_offered = property(fget=get_assessment_offered)

    def get_taker_id(self):
        """Gets the ``Id`` of the resource who took or is taking this assessment.

        return: (osid.id.Id) - the resource ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._my_map['takerId']:
            return Id(self._my_map['takerId'])
        else:
            return Id(self._my_map['takingAgentId'])

    taker_id = property(fget=get_taker_id)

    def get_taker(self):
        """Gets the ``Resource`` taking this assessment.

        return: (osid.resource.Resource) - the resource
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    taker = property(fget=get_taker)

    def get_taking_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` who took or is taking the assessment.

        return: (osid.id.Id) - the agent ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return Id(self._my_map['takingAgentId'])

    taking_agent_id = property(fget=get_taking_agent_id)

    def get_taking_agent(self):
        """Gets the ``Agent``.

        return: (osid.authentication.Agent) - the agent
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    taking_agent = property(fget=get_taking_agent)

    def has_started(self):
        """Tests if this assessment has begun.

        return: (boolean) - ``true`` if the assessment has begun,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_offered = self.get_assessment_offered()
        if assessment_offered.has_start_time():
            return DateTime.utcnow() >= assessment_offered.get_start_time()
        else:
            return True

    def get_actual_start_time(self):
        """Gets the time this assessment was started.

        return: (osid.calendaring.DateTime) - the start time
        raise:  IllegalState - ``has_started()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_started():
            raise errors.IllegalState('this assessment has not yet started')
        if self._my_map['actualStartTime'] is None:
            raise errors.IllegalState('this assessment has not yet been started by the taker')
        else:
            start_time = self._my_map['actualStartTime']
            return DateTime(year=start_time.year,
                            month=start_time.month,
                            day=start_time.day,
                            hour=start_time.hour,
                            minute=start_time.minute,
                            second=start_time.second,
                            microsecond=start_time.microsecond)

    actual_start_time = property(fget=get_actual_start_time)

    def has_ended(self):
        """Tests if this assessment has ended.

        return: (boolean) - ``true`` if the assessment has ended,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        assessment_offered = self.get_assessment_offered()
        now = DateTime.utcnow()
        # There's got to be a better way to do this:
        if self._my_map['completionTime'] is not None:
            return True
        elif assessment_offered.has_deadline() and assessment_offered.has_duration():
            if self._my_map['actualStartTime'] is None:
                return now >= assessment_offered.get_deadline()
            else:
                return (now >= assessment_offered.get_deadline() and
                        now >= self._my_map['actualStartTime'] + assessment_offered.get_duration())
        elif assessment_offered.has_deadline():
            return now >= assessment_offered.get_deadline()
        elif assessment_offered.has_duration() and self._my_map['actualStartTime'] is not None:
            return now >= self._my_map['actualStartTime'] + assessment_offered.get_duration()
        else:
            return False

    def get_completion_time(self):
        """Gets the time of this assessment was completed.

        return: (osid.calendaring.DateTime) - the end time
        raise:  IllegalState - ``has_ended()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_ended():
            raise errors.IllegalState('this assessment has not yet ended')
        if not self._my_map['completionTime']:
            raise errors.OperationFailed('someone forgot to set the completion time')
        completion_time = self._my_map['completionTime']
        return DateTime(year=completion_time.year,
                        month=completion_time.month,
                        day=completion_time.day,
                        hour=completion_time.hour,
                        minute=completion_time.minute,
                        second=completion_time.second,
                        microsecond=completion_time.microsecond)

    completion_time = property(fget=get_completion_time)

    def get_time_spent(self):
        """Gets the total time spent taking this assessment.

        return: (osid.calendaring.Duration) - the total time spent
        *compliance: mandatory -- This method must be implemented.*

        """
        # Take another look at this. Not sure it's correct:
        if not self.has_started or not self.has_ended():
            raise errors.IllegalState()
        if self._my_map['completionTime'] is not None:
            return self.get_completion_time() - self.get_actual_start_time()
        else:
            raise errors.IllegalState()

    time_spent = property(fget=get_time_spent)

    def get_completion(self):
        """Gets a completion percentage of the assessment.

        return: (cardinal) - the percent complete (0-100)
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentTaken.get_completion_template
        return int(self._my_map['completion'])

    completion = property(fget=get_completion)

    def is_scored(self):
        """Tests if a score is available for this assessment.

        return: (boolean) - ``true`` if a score is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['scored'])

    def get_score_system_id(self):
        """Gets a score system ``Id`` for the assessment.

        return: (osid.id.Id) - the grade system
        raise:  IllegalState - ``is_score()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['scoreSystemId']):
            raise errors.IllegalState('this AssessmentTaken has no score_system')
        mgr = self._get_provider_manager('ID')
        if not mgr.supports_id_lookup():
            raise errors.OperationFailed('Id does not support Id lookup')
        lookup_session = mgr.get_id_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_no_catalog_view()
        osid_object = lookup_session.get_id(self.get_score_system_id())
        return osid_object

    score_system_id = property(fget=get_score_system_id)

    def get_score_system(self):
        """Gets a grade system for the score.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_scored()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['scoreSystemId']):
            raise errors.IllegalState('this AssessmentTaken has no score_system')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_system_lookup():
            raise errors.OperationFailed('Grading does not support GradeSystem lookup')
        lookup_session = mgr.get_grade_system_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade_system(self.get_score_system_id())
        return osid_object

    score_system = property(fget=get_score_system)

    def get_score(self):
        """Gets a score for the assessment.

        return: (decimal) - the score
        raise:  IllegalState - ``is_scored()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentTaken.get_score_template
        return Decimal(self._my_map['score'])

    score = property(fget=get_score)

    def is_graded(self):
        """Tests if a grade is available for this assessment.

        return: (boolean) - ``true`` if a grade is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['graded'])

    def get_grade_id(self):
        """Gets a grade ``Id`` for the assessment.

        return: (osid.id.Id) - the grade
        raise:  IllegalState - ``is_graded()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['gradeId']):
            raise errors.IllegalState('this AssessmentTaken has no grade')
        else:
            return Id(self._my_map['gradeId'])

    grade_id = property(fget=get_grade_id)

    def get_grade(self):
        """Gets a grade for the assessment.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``is_graded()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['gradeId']):
            raise errors.IllegalState('this AssessmentTaken has no grade')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_grade_id())
        return osid_object

    grade = property(fget=get_grade)

    def get_feedback(self):
        """Gets any overall comments available for this assessment by the grader.

        return: (osid.locale.DisplayText) - comments
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.Asset.get_title_template
        return DisplayText(self._my_map['feedback'])

    feedback = property(fget=get_feedback)

    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['rubricId'])

    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment taken ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this AssessmentTaken has no rubric')
        else:
            return Id(self._my_map['rubricId'])

    rubric_id = property(fget=get_rubric_id)

    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.AssessmentTaken) - the assessment taken
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['rubricId']):
            raise errors.IllegalState('this AssessmentTaken has no rubric')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_taken_lookup():
            raise errors.OperationFailed('Assessment does not support AssessmentTaken lookup')
        lookup_session = mgr.get_assessment_taken_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        osid_object = lookup_session.get_assessment_taken(self.get_rubric_id())
        return osid_object

    rubric = property(fget=get_rubric)

    @utilities.arguments_not_none
    def get_assessment_taken_record(self, assessment_taken_record_type):
        """Gets the assessment taken record corresponding to the given ``AssessmentTaken`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_taken_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_taken_record_type)`` is ``true`` .

        arg:    assessment_taken_record_type (osid.type.Type): an
                assessment taken record type
        return: (osid.assessment.records.AssessmentTakenRecord) - the
                assessment taken record
        raise:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_taken_record_type)

    def get_display_name(self):
        # Overrides osid.objects.OsidObject.get_display_name to default to AssessmentOffered's
        # display_name if none has been authored for this AssessmentTaken
        from ..osid.objects import OsidObject
        if OsidObject.get_display_name(self).get_text():
            return OsidObject.get_display_name(self)
        else:
            return self.get_assessment_offered().get_display_name()

    def get_description(self):
        # Overrides osid.objects.OsidObject.get_description to default to AssessmentOffered's
        # description if none has been authored for this AssessmentTaken
        from ..osid.objects import OsidObject
        if OsidObject.get_description(self).get_text():
            return OsidObject.get_description(self)
        else:
            return self.get_assessment_offered().get_description()

    def _update_available_sections(self):
        # THIS IS NOT RIGHT. LOOPS WITH _get_first_assessment_section
        if ('sections' not in self._my_map or not self._my_map['sections']):
            section_id = self._get_first_assessment_section().get_id()
        else:
            section_id = Id(self._my_map['sections'][0])
        finished = False
        while not finished:
            try:
                section_id = self._get_next_assessment_section(section_id).get_id()
            except errors.IllegalState:
                finished = True

    def _create_section(self, part_id):
        from .mixins import LoadedSection
        init_map = {'assessmentPartId': str(part_id),
                    'assessmentTakenId': str(self.get_id()),
                    'recordTypeIds': []}
        return LoadedSection(osid_object_map=init_map, runtime=self._runtime, proxy=self._proxy)

    def _get_first_assessment_section(self):
        """Gets the first section for this Taken's Assessment."""
        if ('sections' not in self._my_map or not self._my_map['sections']):
            # This is the first time for this Taken, so start assessment
            # SHOULD THIS USE self._update_available_sections????
            assessment_id = self.get_assessment_offered().get_assessment().get_id()
            first_part_id = get_first_part_id_for_assessment(assessment_id, runtime=self._runtime, proxy=self._proxy)
            first_section = self._create_section(first_part_id)
            self._my_map['sections'] = [str(first_section.get_id())]
            self._my_map['actualStartTime'] = DateTime.utcnow()
            self._save()
            return first_section
        else:
            return self._get_assessment_section(Id(self._my_map['sections'][0]))

    def _get_next_assessment_section(self, assessment_section_id):
        """Gets the next section following section_id.

        Assumes that section list exists in taken and section_id is in section list.
        Assumes that Section parts only exist as children of Assessments

        """
        if self._my_map['sections'][-1] == str(assessment_section_id):
            # section_id represents the last seen section
            section = self._get_assessment_section(assessment_section_id)
            next_part_id, level = get_next_part_id(section._assessment_part_id,
                                                   runtime=self._runtime,
                                                   proxy=self._proxy,
                                                   sequestered=True)  # Raises IllegalState
            next_section = self._create_section(next_part_id)
            self._my_map['sections'].append(str(next_section.get_id()))
            self._save()
            return next_section
        else:
            return self._get_assessment_section(
                Id(self._my_map['sections'][self._my_map['sections'].index(str(assessment_section_id)) + 1]))

    def _get_previous_assessment_section(self, assessment_section_id):
        """Gets the previous section before section_id.

        Assumes that section list exists in taken and section_id is in section list.
        Assumes that Section parts only exist as children of Assessments

        """
        if self._my_map['sections'][0] == str(assessment_section_id):
            raise errors.IllegalState('already at the first section')
        else:
            return self._get_assessment_section(
                Id(self._my_map['sections'][self._my_map['sections'].index(str(assessment_section_id)) - 1]))

    def _get_assessment_section(self, assessment_section_id):
        if assessment_section_id not in self._assessment_sections:
            self._assessment_sections[assessment_section_id] = (
                get_assessment_section(assessment_section_id,
                                       runtime=self._runtime,
                                       proxy=self._proxy))
        return self._assessment_sections[assessment_section_id]

    def _get_assessment_sections(self):
        """Gets a SectionList of all Sections currently known to this AssessmentTaken"""
        section_list = []
        for section_idstr in self._my_map['sections']:
            section_list.append(self._get_assessment_section(Id(section_idstr)))
        return AssessmentSectionList(section_list, runtime=self._runtime, proxy=self._proxy)

    def _save(self):
        """Saves the current state of this AssessmentTaken.

        Should be called every time the sections map changes.

        """
        collection = JSONClientValidated('assessment',
                                         collection='AssessmentTaken',
                                         runtime=self._runtime)
        collection.save(self._my_map)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['actualStartTime'] is not None:
            actual_start_time = obj_map['actualStartTime']
            obj_map['actualStartTime'] = dict()
            obj_map['actualStartTime']['year'] = actual_start_time.year
            obj_map['actualStartTime']['month'] = actual_start_time.month
            obj_map['actualStartTime']['day'] = actual_start_time.day
            obj_map['actualStartTime']['hour'] = actual_start_time.hour
            obj_map['actualStartTime']['minute'] = actual_start_time.minute
            obj_map['actualStartTime']['second'] = actual_start_time.second
            obj_map['actualStartTime']['microsecond'] = actual_start_time.microsecond
        if obj_map['completionTime'] is not None:
            completion_time = obj_map['completionTime']
            obj_map['completionTime'] = dict()
            obj_map['completionTime']['year'] = completion_time.year
            obj_map['completionTime']['month'] = completion_time.month
            obj_map['completionTime']['day'] = completion_time.day
            obj_map['completionTime']['hour'] = completion_time.hour
            obj_map['completionTime']['minute'] = completion_time.minute
            obj_map['completionTime']['second'] = completion_time.second
            obj_map['completionTime']['microsecond'] = completion_time.microsecond
        if 'sections' in obj_map:
            del obj_map['sections']
        obj_map = osid_objects.OsidObject.get_object_map(self, obj_map)
        if obj_map['displayName']['text'] == '':
            obj_map['displayName']['text'] = self.get_display_name().get_text()
        if obj_map['description']['text'] == '':
            obj_map['description']['text'] = self.get_description().get_text()
        return obj_map

    object_map = property(fget=get_object_map)

    def _delete(self):
        if 'sections' in self._my_map:
            for section_id in self._my_map['sections']:
                section = get_assessment_section(Id(section_id), runtime=self._runtime, proxy=self._proxy)
                section._delete()


class AssessmentTakenForm(abc_assessment_objects.AssessmentTakenForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating an ``AssessmentTaken``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentTakenAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment.AssessmentTaken'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ASSESSMENT_TAKEN', **kwargs)
        self._mdata = default_mdata.get_assessment_taken_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._taker_default = self._mdata['taker']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['assessmentOfferedId'] = str(kwargs['assessment_offered_id'])
        self._my_map['takerId'] = self._taker_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['actualStartTime'] = None
        self._my_map['gradeId'] = ''
        self._my_map['completionTime'] = None
        self._my_map['score'] = 0.0

    def get_taker_metadata(self):
        """Gets the metadata for a resource to manually set which resource will be taking the assessment.

        return: (osid.Metadata) - metadata for the resource
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['taker'])
        metadata.update({'existing_id_values': self._my_map['takerId']})
        return Metadata(**metadata)

    taker_metadata = property(fget=get_taker_metadata)

    @utilities.arguments_not_none
    def set_taker(self, resource_id):
        """Sets the resource who will be taking this assessment.

        arg:    resource_id (osid.id.Id): the resource Id
        raise:  InvalidArgument - ``resource_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_taker_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(resource_id):
            raise errors.InvalidArgument()
        self._my_map['takerId'] = str(resource_id)

    def clear_taker(self):
        """Clears the resource.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_taker_metadata().is_read_only() or
                self.get_taker_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['takerId'] = self._taker_default

    taker = property(fset=set_taker, fdel=clear_taker)

    @utilities.arguments_not_none
    def get_assessment_taken_form_record(self, assessment_taken_record_type):
        """Gets the ``AssessmentTakenFormRecord`` corresponding to the given assessment taken record ``Type``.

        arg:    assessment_taken_record_type (osid.type.Type): the
                assessment taken record type
        return: (osid.assessment.records.AssessmentTakenFormRecord) -
                the assessment taken record
        raise:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_taken_record_type)


class AssessmentTakenList(abc_assessment_objects.AssessmentTakenList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentTakenList`` provides a means for accessing ``AssessmentTaken`` elements sequentially either one at a time or many at a time.

    Examples: while (atl.hasNext()) { AssessmentTaken assessment =
    atl.getNextAssessmentTaken();

    or
      while (atl.hasNext()) {
           AssessmentTaken[] assessments = atl.hetNextAssessmentsTaken(atl.available());
      }

    """

    def get_next_assessment_taken(self):
        """Gets the next ``AssessmentTaken`` in this list.

        return: (osid.assessment.AssessmentTaken) - the next
                ``AssessmentTaken`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentTaken`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(AssessmentTaken)

    __next__ = next

    next_assessment_taken = property(fget=get_next_assessment_taken)

    @utilities.arguments_not_none
    def get_next_assessments_taken(self, n):
        """Gets the next set of ``AssessmentTaken`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentTaken`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentTaken) - an array of
                ``AssessmentTaken`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AssessmentTakenList, number=n)


class AssessmentSection(abc_assessment_objects.AssessmentSection, osid_objects.OsidObject):
    """Represents an assessment section.

    An assessment section represents a cluster of questions used to
    organize the execution of an assessment. The section is the student
    aspect of an assessment part.

    """
    _namespace = 'assessment.AssessmentSection'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='AssessmentSection', **kwargs)
        self._assessment_part_id = Id(self._my_map['assessmentPartId'])
        self._assessment_taken_id = Id(self._my_map['assessmentTakenId'])

        assessment_mgr = self._get_provider_manager('ASSESSMENT', local=True)
        if self._proxy:
            taken_lookup_session = assessment_mgr.get_assessment_taken_lookup_session(proxy=self._proxy)
        else:
            taken_lookup_session = assessment_mgr.get_assessment_taken_lookup_session()
        taken_lookup_session.use_federated_bank_view()
        self._assessment_taken = taken_lookup_session.get_assessment_taken(self._assessment_taken_id)

        authoring_mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        if self._proxy:
            part_lookup_session = authoring_mgr.get_assessment_part_lookup_session(proxy=self._proxy)
        else:
            part_lookup_session = authoring_mgr.get_assessment_part_lookup_session()
        part_lookup_session.use_unsequestered_assessment_part_view()
        part_lookup_session.use_federated_bank_view()
        self._assessment_part = part_lookup_session.get_assessment_part(self._assessment_part_id)

    def get_object_map(self, obj_map=None):
        def grab_choice(choices, choice_id):
            choice_ids = [c['id'] for c in choices]

            if choice_id in choice_ids:
                return [c for c in choices if c['id'] == choice_id][0]
            return None

        def reorder_choices(choices, magic_id):
            # We may want to do this with the magic lookup session instead
            # reorder the choices list according to the order in the magic_id
            identifier = unquote(Id(magic_id).identifier)
            if '?' in identifier:
                # it is a magic ID, by our convention
                magic_params = json.loads(identifier.split('?')[1])
                try:
                    choice_ids = [c['id'] for c in choices]
                except TypeError:
                    pass
                else:
                    if (isinstance(magic_params, list) and
                            list(set(choice_ids)) == list(set(magic_params))):
                        ordered_choices = []
                        for ordered_id in magic_params:
                            ordered_choices.append(grab_choice(choices, ordered_id))
                        return ordered_choices
            return choices

        if obj_map is None:
            # obj_map = dict(self._my_map)
            obj_map = dict(self._assessment_part._my_map)
        del obj_map['_id']

        obj_map.update(
            {'type': self._namespace.split('.')[-1],
             'id': str(self.get_id())})

        # should this be here, or elsewhere?
        # Trying to make getting the section maps faster
        if 'questions' in self._my_map:
            collection = JSONClientValidated('assessment',
                                             collection='Item',
                                             runtime=self._runtime)
            questions = []
            for question in self._my_map['questions']:
                item = collection.find_one({"_id": ObjectId(Id(question['itemId']).identifier)})
                question_map = item['question']
                question_map['_id'] = str(question_map['_id'])
                question_map['learningObjectiveIds'] = item['learningObjectiveIds']

                if 'displayElements' in question:
                    question_map['displayName']['text'] = '.'.join([str(key) for key in question['displayElements']])

                # if this is a magic MC question, try reordering the choices:
                if 'choices' in question_map:
                    question_map['choices'] = reorder_choices(question_map['choices'], question['questionId'])

                response = question['responses'][0]
                responded = True
                is_correct = None
                if 'missingResponse' in response:
                    response = None
                    responded = False
                else:
                    response['confusedLearningObjectiveIds'] = []
                    if ('missingResponse' not in response and
                            'choiceIds' in response and
                            len(response['choiceIds']) > 0):
                        matching_answers = [a for a in item['answers']
                                            if 'choiceIds' in a and
                                            len(a['choiceIds']) > 0 and
                                            a['choiceIds'][0] == response['choiceIds'][0]]
                        if len(matching_answers) > 0 and 'confusedLearningObjectiveIds' in matching_answers[0]:
                            response['confusedLearningObjectiveIds'] = matching_answers[0]['confusedLearningObjectiveIds']

                    if 'solution' in item:
                        response['feedback'] = item['solution']['text']
                    if '_id' in response:
                        response['_id'] = str(response['_id'])
                    submit = response['submissionTime']
                    if submit is not None:
                        response['submissionTime'] = {
                            'year': submit.year,
                            'month': submit.month,
                            'day': submit.day,
                            'hour': submit.hour,
                            'minute': submit.minute,
                            'second': submit.second,
                            'microsecond': submit.microsecond
                        }
                    is_correct = response['isCorrect']
                question_map.update({
                    'response': response,
                    'responded': responded
                })

                question_map.update({
                    'isCorrect': is_correct
                })

                questions.append(question_map)

            obj_map.update({
                'questions': questions
            })

        # end performance tweaking of section maps

        return obj_map

    object_map = property(get_object_map)

    # Let's give the Part attributes to the Section
    def __getattribute__(self, name):
        if not name.startswith('_') and name not in ['ident', 'get_id', 'id_', 'get_object_map', 'object_map']:
            try:
                return self._assessment_part[name]
            except AttributeError:
                return object.__getattribute__(self, name)
        return object.__getattribute__(self, name)

    def get_assessment_taken_id(self):
        """Gets the ``Id`` of the ``AssessmentTaken``.

        return: (osid.id.Id) - the assessment taken ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        if not bool(self._my_map['assessmentTakenId']):
            raise errors.IllegalState('assessment_taken empty')
        return Id(self._my_map['assessmentTakenId'])

    assessment_taken_id = property(fget=get_assessment_taken_id)

    def get_assessment_taken(self):
        """Gets the ``AssessmentTakeb``.

        return: (osid.assessment.AssessmentTaken) - the assessment taken
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        if not bool(self._my_map['assessmentTakenId']):
            raise errors.IllegalState('assessment_taken empty')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_taken_lookup():
            raise errors.OperationFailed('Assessment does not support AssessmentTaken lookup')
        lookup_session = mgr.get_assessment_taken_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment_taken(self.get_assessment_taken_id())

    assessment_taken = property(fget=get_assessment_taken)

    def has_allocated_time(self):
        """Tests if this section must be completed within an allocated time.

        return: (boolean) - ``true`` if this section has an allocated
                time, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_allocated_time(self):
        """Gets the allocated time for this section.

        return: (osid.calendaring.Duration) - allocated time
        raise:  IllegalState - ``has_allocated_time()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    allocated_time = property(fget=get_allocated_time)

    def are_items_sequential(self):
        """Tests if the items or parts in this section are taken sequentially.

        return: (boolean) - ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        return: (boolean) - ``true`` if the items appear in a random
                order, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_assessment_section_record(self, assessment_section_record_type):
        """Gets the assessment section record corresponding to the given ``AssessmentSection`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_section_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_section_record_type)`` is ``true``
        .

        arg:    assessment_section_record_type (osid.type.Type): an
                assessment section record type
        return: (osid.assessment.records.AssessmentSectionRecord) - the
                assessment section record
        raise:  NullArgument - ``assessment_section_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_section_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_section_record_type)


class AssessmentSectionList(abc_assessment_objects.AssessmentSectionList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentSectionList`` provides a means for accessing ``AssessmentSection`` elements sequentially either one at a time or many at a time.

    Examples: while (asl.hasNext()) { AssessmentSection section =
    asl.getNextAssessmentSection();

    or
      while (asl.hasNext()) {
           AssessmentSection[] sections = asl.hetNextAssessmentSections(asl.available());
      }

    """

    def get_next_assessment_section(self):
        """Gets the next ``AssessmentSection`` in this list.

        return: (osid.assessment.AssessmentSection) - the next
                ``AssessmentSection`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentSection`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(AssessmentSection)

    __next__ = next

    next_assessment_section = property(fget=get_next_assessment_section)

    @utilities.arguments_not_none
    def get_next_assessment_sections(self, n):
        """Gets the next set of ``AssessmentSection`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentSection``
                elements requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentSection) - an array of
                ``AssessmentSection`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AssessmentSectionList, number=n)


class Bank(abc_assessment_objects.Bank, osid_objects.OsidCatalog):
    """A bank defines a collection of assessments and items."""
    _namespace = 'assessment.Bank'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='BANK', **kwargs)

    @utilities.arguments_not_none
    def get_bank_record(self, bank_record_type):
        """Gets the bank record corresponding to the given ``Bank`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``bank_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bank_record_type)``
        is ``true`` .

        arg:    bank_record_type (osid.type.Type): a bank record type
        return: (osid.assessment.records.BankRecord) - the bank record
        raise:  NullArgument - ``bank_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BankForm(abc_assessment_objects.BankForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating banks.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BankAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment.Bank'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='BANK', **kwargs)
        self._mdata = default_mdata.get_bank_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidCatalogForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_map(self, record_types, **kwargs)

    @utilities.arguments_not_none
    def get_bank_form_record(self, bank_record_type):
        """Gets the ``BankFormRecord`` corresponding to the given bank record ``Type``.

        arg:    bank_record_type (osid.type.Type): a bank record type
        return: (osid.assessment.records.BankFormRecord) - the bank
                record
        raise:  NullArgument - ``bank_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # this should be templated from Resource, but
        # would have to update pattern mappers
        return self._get_record(bank_record_type)


class BankList(abc_assessment_objects.BankList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BankList`` provides a means for accessing ``Bank`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Bank bank = bl.getNextBank(); }

    or
      while (bl.hasNext()) {
           Bank[] banks = bl.getNextBanks(bl.available());
      }

    """

    def get_next_bank(self):
        """Gets the next ``Bank`` in this list.

        return: (osid.assessment.Bank) - the next ``Bank`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Bank`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Bank)

    __next__ = next

    next_bank = property(fget=get_next_bank)

    @utilities.arguments_not_none
    def get_next_banks(self, n):
        """Gets the next set of ``Bank`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Bank`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.assessment.Bank) - an array of ``Bank``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(BankList, number=n)


class BankNode(abc_assessment_objects.BankNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BankHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_bank().get_object_map())
        node_map['type'] = 'BankNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for bank_node in self.get_parent_bank_nodes():
            node_map['parentNodes'].append(bank_node.get_object_node_map())
        for bank_node in self.get_child_bank_nodes():
            node_map['childNodes'].append(bank_node.get_object_node_map())
        return node_map

    def get_bank(self):
        """Gets the ``Bank`` at this node.

        return: (osid.assessment.Bank) - the bank represented by this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('ASSESSMENT', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_bank_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_bank(Id(self._my_map['id']))

    bank = property(fget=get_bank)

    def get_parent_bank_nodes(self):
        """Gets the parents of this bank.

        return: (osid.assessment.BankNodeList) - the parents of this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_bank_nodes = []
        for node in self._my_map['parentNodes']:
            parent_bank_nodes.append(BankNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BankNodeList(parent_bank_nodes)

    parent_bank_nodes = property(fget=get_parent_bank_nodes)

    def get_child_bank_nodes(self):
        """Gets the children of this bank.

        return: (osid.assessment.BankNodeList) - the children of this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_bank_nodes = []
        for node in self._my_map['childNodes']:
            parent_bank_nodes.append(BankNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BankNodeList(parent_bank_nodes)

    child_bank_nodes = property(fget=get_child_bank_nodes)


class BankNodeList(abc_assessment_objects.BankNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BankNodeList`` provides a means for accessing ``BankNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BankNode node =
    bnl.getNextBankNode(); }

    or
      while (bnl.hasNext()) {
           BankNode[] nodes = bnl.getNextBankNodes(bnl.available());
      }

    """

    def get_next_bank_node(self):
        """Gets the next ``BankNode`` in this list.

        return: (osid.assessment.BankNode) - the next ``BankNode`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``BankNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(BankNode)

    __next__ = next

    next_bank_node = property(fget=get_next_bank_node)

    @utilities.arguments_not_none
    def get_next_bank_nodes(self, n):
        """Gets the next set of ``BankNode`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``BankNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.assessment.BankNode) - an array of ``BanklNode``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(BankNodeList, number=n)


class ResponseList(abc_assessment_objects.ResponseList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResponseList`` provides a means for accessing ``Response`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Response response =
    rl.getNextResponse(); }

    or
      while (rl.hasNext()) {
           Response[] responses = rl.getNextResponses(rl.available());
      }

    """

    def get_next_response(self):
        """Gets the next ``Response`` in this list.

        return: (osid.assessment.Response) - the next ``Response`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Response`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Response)

    __next__ = next

    next_response = property(fget=get_next_response)

    @utilities.arguments_not_none
    def get_next_responses(self, n):
        """Gets the next set of ``Response`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Response`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.assessment.Response) - an array of ``Response``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ResponseList, number=n)
