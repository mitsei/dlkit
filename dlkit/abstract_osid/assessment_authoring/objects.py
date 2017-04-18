"""Implementations of assessment.authoring abstract base class objects."""
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


class AssessmentPart:
    """An ``AssessmentPart`` represents a section of an assessment.

    ``AssessmentParts`` may be visible as sections of an assessment or
    just used to clump together a set of items on which to hang sequence
    rules.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_id(self):
        """Gets the assessment ``Id`` to which this rule belongs.

        :return: ``Id`` of an assessment
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_id = property(fget=get_assessment_id)

    @abc.abstractmethod
    def get_assessment(self):
        """Gets the assessment to which this rule belongs.

        :return: an assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    assessment = property(fget=get_assessment)

    @abc.abstractmethod
    def has_parent_part(self):
        """Tests if this assessment part belongs to a parent assessment part.

        :return: ``true`` if this part has a parent, ``false`` if a root
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_part_id(self):
        """Gets the parent assessment ``Id``.

        :return: ``Id`` of an assessment
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_parent_part()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_part_id = property(fget=get_assessment_part_id)

    @abc.abstractmethod
    def get_assessment_part(self):
        """Gets the parent assessment.

        :return: the parent assessment part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- ``has_parent_part()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    assessment_part = property(fget=get_assessment_part)

    @abc.abstractmethod
    def is_section(self):
        """Tests if this part should be visible as a section in an assessment.

        If visible, this part will appear to the user as a separate
        section of the assessment. Typically, a section may not be under
        a non-sectioned part.

        :return: ``true`` if this part is a section, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_weight(self):
        """Gets an integral weight factor for this assessment part used for scoring.

        The percentage weight for this part is this weight divided by
        the sum total of all the weights in the assessment.

        :return: the weight
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    weight = property(fget=get_weight)

    @abc.abstractmethod
    def get_allocated_time(self):
        """Gets the allocated time for this part.

        The allocated time may be used to assign fixed time limits to
        each item or can be used to estimate the total assessment time.

        :return: allocated time
        :rtype: ``osid.calendaring.Duration``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    allocated_time = property(fget=get_allocated_time)

    @abc.abstractmethod
    def get_child_assessment_part_ids(self):
        """Gets any child assessment part ``Ids``.

        :return: ``Ids`` of the child assessment parts
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    child_assessment_part_ids = property(fget=get_child_assessment_part_ids)

    @abc.abstractmethod
    def get_child_assessment_parts(self):
        """Gets any child assessment parts.

        :return: the child assessment parts
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    child_assessment_parts = property(fget=get_child_assessment_parts)

    @abc.abstractmethod
    def get_assessment_part_record(self, assessment_part_record_type):
        """Gets the assessment part record corresponding to the given ``AssessmentPart`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_part_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_part_record_type)`` is ``true`` .

        :param assessment_part_record_type: the type of the record to retrieve
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the assessment part record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartRecord``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.AssessmentPartRecord


class AssessmentPartForm:
    """This is the form for creating and updating ``AssessmentParts``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAuthoringSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_weight_metadata(self):
        """Gets the metadata for the weight.

        :return: metadata for the weight
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    weight_metadata = property(fget=get_weight_metadata)

    @abc.abstractmethod
    def set_weight(self, weight):
        """Sets the weight on a scale from 0-100.

        :param weight: the new weight
        :type weight: ``cardinal``
        :raise: ``InvalidArgument`` -- ``weight`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_weight(self):
        """Clears the weight.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    weight = property(fset=set_weight, fdel=clear_weight)

    @abc.abstractmethod
    def get_allocated_time_metadata(self):
        """Gets the metadata for the allocated time.

        :return: metadata for the allocated time
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    allocated_time_metadata = property(fget=get_allocated_time_metadata)

    @abc.abstractmethod
    def set_allocated_time(self, time):
        """Sets the allocated time.

        :param time: the allocated time
        :type time: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``time`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_allocated_time(self):
        """Clears the allocated time.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    allocated_time = property(fset=set_allocated_time, fdel=clear_allocated_time)

    @abc.abstractmethod
    def get_assessment_part_form_record(self, assessment_part_record_type):
        """Gets the ``AssessmentPartFormRecord`` corresponding to the given assessment record ``Type``.

        :param assessment_part_record_type: the assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the assessment part record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartFormRecord``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.AssessmentPartFormRecord


class AssessmentPartList:
    """Like all ``OsidLists,``  ``AssessmentPartList`` provides a means for accessing ``AssessmentPart`` elements sequentially either one at a time or many at a time.

    Examples: while (apl.hasNext()) { AssessmentPart assessmentPart =
    apl.getNextAssessmentPart(); }

    or
      while (apl.hasNext()) {
           AssessmentPart[] assessmentParts = apl.hetNextAssessmentParts(apl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_assessment_part(self):
        """Gets the next ``AssessmentPart`` in this list.

        :return: the next ``AssessmentPart`` in this list. The ``has_next()`` method should be used to test that a next ``AssessmentPart`` is available before calling this method.
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    next_assessment_part = property(fget=get_next_assessment_part)

    @abc.abstractmethod
    def get_next_assessment_parts(self, n):
        """Gets the next set of ``AssessmentPart`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``AssessmentPart`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AssessmentPart`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart


class SequenceRule:
    """A ``SequenceRule`` defines the ordering of ``AssessmentParts``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_part_id(self):
        """Gets the assessment part ``Id`` to which this rule belongs.

        :return: ``Id`` of an assessment part
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_part_id = property(fget=get_assessment_part_id)

    @abc.abstractmethod
    def get_assessment_part(self):
        """Gets the assessment part to which this rule belongs.

        :return: an assessment part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    assessment_part = property(fget=get_assessment_part)

    @abc.abstractmethod
    def get_next_assessment_part_id(self):
        """Gets the next assessment part ``Id`` for success of this rule.

        :return: ``Id`` of an assessment part
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    next_assessment_part_id = property(fget=get_next_assessment_part_id)

    @abc.abstractmethod
    def get_next_assessment_part(self):
        """Gets the next assessment part for success of this rule.

        :return: an assessment part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    next_assessment_part = property(fget=get_next_assessment_part)

    @abc.abstractmethod
    def get_minimum_score(self):
        """Gets the minimum score expressed as an integer (0-100) for this rule.

        :return: minimum score
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    minimum_score = property(fget=get_minimum_score)

    @abc.abstractmethod
    def get_maximum_score(self):
        """Gets the maximum score expressed as an integer (0-100) for this rule.

        :return: maximum score
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    maximum_score = property(fget=get_maximum_score)

    @abc.abstractmethod
    def is_cumulative(self):
        """Tests if the score is applied to all previous assessment parts.

        :return: ``true`` if the score is applied to all previous assessment parts, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_applied_assessment_part_ids(self):
        """Qualifies ``is_cumulative()`` to apply to a specific list of assessment parts.

        If ``is_cumulative()`` is ``true,`` this method may return an
        empty list to mean all previous assessment parts.

        :return: list of assessment parts
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_cumulative()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    applied_assessment_part_ids = property(fget=get_applied_assessment_part_ids)

    @abc.abstractmethod
    def get_applied_assessment_parts(self):
        """Qualifies ``is_cumulative()`` to apply to a specific list of assessment parts.

        If ``is_cumulative()`` is ``true,`` this method may return an
        empty list to mean all previous assessment parts.

        :return: list of assessment parts
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``IllegalState`` -- ``is_cumulative()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    applied_assessment_parts = property(fget=get_applied_assessment_parts)

    @abc.abstractmethod
    def get_sequence_rule_record(self, sequence_rule_record_type):
        """Gets the assessment sequence rule record corresponding to the given ``SequenceRule`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``sequence_rule_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(sequence_rule_record_type)`` is ``true`` .

        :param sequence_rule_record_type: the type of the record to retrieve
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the assessment sequence rule record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleRecord


class SequenceRuleForm:
    """This is the form for creating and updating sequence rules.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``SequenceSession``
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_minimum_score_metadata(self):
        """Gets the metadata for the minimum score.

        :return: metadata for the minimum score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    minimum_score_metadata = property(fget=get_minimum_score_metadata)

    @abc.abstractmethod
    def set_minimum_score(self, score):
        """Sets the minimum score for this rule.

        :param score: minimum score
        :type score: ``cardinal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_score = property(fset=set_minimum_score)

    @abc.abstractmethod
    def get_maximum_score_metadata(self):
        """Gets the metadata for the maximum score.

        :return: metadata for the maximum score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    maximum_score_metadata = property(fget=get_maximum_score_metadata)

    @abc.abstractmethod
    def set_maximum_score(self, score):
        """Sets the maximum score for this rule.

        :param score: maximum score
        :type score: ``cardinal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    maximum_score = property(fset=set_maximum_score)

    @abc.abstractmethod
    def get_cumulative_metadata(self):
        """Gets the metadata for the cumulative flag.

        :return: metadata for the cumulative flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    cumulative_metadata = property(fget=get_cumulative_metadata)

    @abc.abstractmethod
    def set_cumulative(self, cumulative):
        """Applies this rule to all previous assessment parts.

        :param cumulative: ``true`` to apply to all previous assessment parts. ``false`` to apply to the immediate previous assessment part
        :type cumulative: ``boolean``
        :raise: ``InvalidArgument`` -- ``cumulative`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cumulative = property(fset=set_cumulative)

    @abc.abstractmethod
    def get_applied_assessment_parts_metadata(self):
        """Gets the metadata for the applied assessment parts.

        :return: metadata for the applied assessment parts
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    applied_assessment_parts_metadata = property(fget=get_applied_assessment_parts_metadata)

    @abc.abstractmethod
    def apply_assessment_parts(self, assessment_part_ids):
        """Designates assessment parts to which the rule applies.

        :param assessment_part_ids: the parts to which this rule should apply
        :type assessment_part_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``assessment_part_ids`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``assessment_part_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_form_record(self, sequence_rule_record):
        """Gets the ``SequenceRuleFormRecord`` corresponding to the given sequence rule record ``Type``.

        :param sequence_rule_record: a sequence rule record type
        :type sequence_rule_record: ``osid.type.Type``
        :return: the sequence rule record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleFormRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asequence_rule_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleFormRecord


class SequenceRuleList:
    """Like all ``OsidLists,``  ``SequenceRuleList`` provides a means for accessing ``SequenceRule`` elements sequentially either one at a time or many at a time.

    Examples: while (srl.hasNext()) { AssessmentSequenceRule rule =
    srl.getNextAssessmentSequenceRule(); }

    or
      while (srl.hasNext()) {
           AssessmentSequenceRule[] rules = srl.getNextAssessmentSequenceRules(srl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_sequence_rule(self):
        """Gets the next ``SequenceRule`` in this list.

        :return: the next ``SequenceRule`` in this list. The ``has_next()`` method should be used to test that a next ``SequenceRule`` is available before calling this method.
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRule

    next_sequence_rule = property(fget=get_next_sequence_rule)

    @abc.abstractmethod
    def get_next_sequence_rules(self, n):
        """Gets the next set of ``SequenceRule`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``SequenceRule`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``SequenceRule`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRule


class SequenceRuleEnabler:
    """A ``SequenceRuleEnabler`` describes the rules for making a ``SequenceRule`` effective."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_enabler_record(self, sequence_rule_enabler_record_type):
        """Gets the sequence rule enabler record corresponding to the given ``SequenceRuleEnabler`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``sequence_rule_enabler_record_type`` may
        be the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(sequence_rule_enabler_record_type)`` is
        ``true`` .

        :param sequence_rule_enabler_record_type: the type of sequence rule enabler record to retrieve
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the sequence rule enabler record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleEnablerRecord


class SequenceRuleEnablerForm:
    """This is the form for creating and updating ``SequenceRuleEnablers``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``SequenceRuleEnablerAdminSession``. For each data element that may
    be set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_enabler_form_record(self, sequence_rule_enabler_record_type):
        """Gets the ``SequenceRuleEnablerFormRecord`` corresponding to the given sequence rule enabler record ``Type``.

        :param sequence_rule_enabler_record_type: a sequence rule enabler record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the sequence rule enabler form record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerFormRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.records.SequenceRuleEnablerFormRecord


class SequenceRuleEnablerFormRecord:
    """A record for a ``SequenceRuleEnablerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerList:
    """Like all ``OsidLists,``  ``SequenceRuleEnablerList`` provides a means for accessing ``SequenceRuleEnabler`` elements sequentially either one at a time or many at a time.

    Examples: while (scel.hasNext()) { SequenceRuleEnabler enabler =
    scel.getNextSequenceRuleEnabler(); }

    or
      while (scel.hasNext()) {
           SequenceRuleEnabler[] enablers = scel.getNextSequenceRuleEnablers(scel.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_sequence_rule_enabler(self):
        """Gets the next ``SequenceRuleEnabler`` in this list.

        :return: the next ``SequenceRuleEnabler`` in this list. The ``has_next()`` method should be used to test that a next ``SequenceRuleEnabler`` is available before calling this method.
        :rtype: ``osid.assessment.authoring.SequenceRuleEnabler``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnabler

    next_sequence_rule_enabler = property(fget=get_next_sequence_rule_enabler)

    @abc.abstractmethod
    def get_next_sequence_rule_enablers(self, n):
        """Gets the next set of ``SequenceRuleEnabler`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``SequenceRuleEnabler`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``SequenceRuleEnabler`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.authoring.SequenceRuleEnabler``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnabler
