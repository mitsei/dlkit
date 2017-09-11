"""JSON implementations of assessment rules."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from collections import OrderedDict


from .. import utilities
from ..osid import rules as osid_rules
from ..primitives import Id
from ..utilities import get_registry
from .assessment_utilities import get_item_lookup_session
from dlkit.abstract_osid.assessment import rules as abc_assessment_rules
from dlkit.abstract_osid.osid import errors


UNANSWERED = 0
NULL_SUBMISSION = 1


class Response(abc_assessment_rules.Response, osid_rules.OsidCondition):
    """A response to an assessment item.

    This interface contains methods to set values in response to an
    assessmet item and mirrors the item record structure with the
    corresponding setters.

    """
    _namespace = 'assessment.Response'

    def __init__(self, osid_object_map, additional_attempts=None, runtime=None, proxy=None, section=None, **kwargs):
        from .objects import Answer
        self._submission_time = osid_object_map['submissionTime']
        self._runtime = runtime
        self._proxy = proxy
        if section is not None:
            self._section = section
        self._item_id = Id(osid_object_map['itemId'])
        if additional_attempts is not None:
            self._additional_attempts = additional_attempts
        else:
            self._additional_attempts = []
        if 'missingResponse' in osid_object_map:
            self._my_answer = osid_object_map['missingResponse']
        else:
            self._my_answer = Answer(osid_object_map=osid_object_map,
                                     runtime=runtime,
                                     proxy=proxy)
        self._is_correct = None
        if 'isCorrect' in osid_object_map:
            self._is_correct = osid_object_map['isCorrect']
        self._records = OrderedDict()

        # Consider that responses may want to have their own records separate
        # from the enclosed Answer records:
        self._record_type_data_sets = get_registry('RESPONSE_RECORD_TYPES', runtime)
        if 'recordTypeIds' in osid_object_map:
            record_type_ids = osid_object_map['recordTypeIds']
        else:
            record_type_ids = []
        self._load_records(record_type_ids)

    def _load_records(self, record_type_idstrs):
        for record_type_idstr in record_type_idstrs:
            self._init_record(record_type_idstr)

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, name):
        if self._my_answer == UNANSWERED:
            raise errors.IllegalState('this Item has not been attempted')
        if self._my_answer == NULL_SUBMISSION:
            raise errors.IllegalState('this Item has been skipped or cleared')
        if not name.startswith('__'):
            try:
                return getattr(self._my_answer, name)
            except:
                raise

    def get_item_id(self):
        """Gets the ``Id`` of the ``Item``.

        return: (osid.id.Id) - the assessment item ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._item_id

    item_id = property(fget=get_item_id)

    def get_item(self):
        """Gets the ``Item``.

        return: (osid.assessment.Item) - the assessment item
        *compliance: mandatory -- This method must be implemented.*

        """
        # So, for now we're assuming that what should be returned here is the question.
        # We could change this class impl to "know" if it came from a ResponseLookupSession call
        # and return the whole Item if so.
        try:
            # an un-answered response will have a magic itemId here
            item_lookup_session = get_item_lookup_session(runtime=self._runtime, proxy=self._proxy)
            item_lookup_session.use_federated_bank_view()
            item = item_lookup_session.get_item(self._item_id)
        except errors.NotFound:
            # otherwise an answered response will have an assessment-session itemId
            if self._section is not None:
                question = self._section.get_question(self._item_id)
                ils = self._section._get_item_lookup_session()
                real_item_id = Id(question._my_map['itemId'])
                item = ils.get_item(real_item_id)
            else:
                raise errors.NotFound()
        return item.get_question()

    item = property(fget=get_item)

    @utilities.arguments_not_none
    def get_response_record(self, item_record_type):
        """Gets the response record corresponding to the given ``Item`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .

        arg:    item_record_type (osid.type.Type): an item record type
        return: (osid.assessment.records.ResponseRecord) - the response
                record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_record_type(item_record_type):
            raise errors.Unsupported()
        if str(item_record_type) not in self._records:
            raise errors.Unimplemented()
        return self._records[str(item_record_type)]

    def is_answered(self):
        if self._my_answer in [UNANSWERED, NULL_SUBMISSION]:
            return False
        return True

    def is_unanswered(self):
        if self._my_answer == UNANSWERED:
            return True
        return False

    def is_null_submission(self):
        if self._my_answer == NULL_SUBMISSION:
            return True
        return False

    def get_submission_time(self):
        if self._submission_time is not None:
            return self._submission_time
        raise errors.IllegalState('Item was not attempted')

    def get_additional_attempts(self):
        from .objects import ResponseList
        return ResponseList(self._additional_attempts, self._runtime, self._proxy)

    def is_correct(self):
        if self._is_correct is not None:
            return self._is_correct
        raise errors.IllegalState('do not know if this response is correct')
