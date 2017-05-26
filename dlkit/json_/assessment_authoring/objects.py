"""JSON implementations of assessment.authoring objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import importlib


from . import default_mdata
from .. import utilities
from ..assessment.objects import Bank, ItemList
from ..id.objects import IdList
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..primitives import Type
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.assessment_authoring import objects as abc_assessment_authoring_objects
from dlkit.abstract_osid.osid import errors
from dlkit.json_.assessment.assessment_utilities import get_assessment_part_lookup_session, get_item_lookup_session


SIMPLE_SEQUENCE_RECORD_TYPE = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'osid-object',
    'identifier': 'simple-child-sequencing'})


class AssessmentPart(abc_assessment_authoring_objects.AssessmentPart, osid_objects.OsidObject, osid_markers.Containable, osid_markers.Operable):
    """An ``AssessmentPart`` represents a section of an assessment.

    ``AssessmentParts`` may be visible as sections of an assessment or
    just used to clump together a set of items on which to hang sequence
    rules.

    """
    _namespace = 'assessment_authoring.AssessmentPart'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ASSESSMENT_PART', **kwargs)
        self._catalog_name = 'Bank'

    def get_assessment_id(self):
        """Gets the assessment ``Id`` to which this rule belongs.

        return: (osid.id.Id) - ``Id`` of an assessment
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return Id(self._my_map['assessmentId'])

    assessment_id = property(fget=get_assessment_id)

    def get_assessment(self):
        """Gets the assessment to which this rule belongs.

        return: (osid.assessment.Assessment) - an assessment
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_lookup():
            raise errors.OperationFailed('Assessment does not support Assessment lookup')
        lookup_session = mgr.get_assessment_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment(self.get_assessment_id())

    assessment = property(fget=get_assessment)

    def has_parent_part(self):
        """Tests if this assessment part belongs to a parent assessment part.

        return: (boolean) - ``true`` if this part has a parent,
                ``false`` if a root
        *compliance: mandatory -- This method must be implemented.*

        """
        return bool('assessmentPartId' in self._my_map and self._my_map['assessmentPartId'])

    def get_assessment_part_id(self):
        """Gets the parent assessment ``Id``.

        return: (osid.id.Id) - ``Id`` of an assessment
        raise:  IllegalState - ``has_parent_part()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return Id(self._my_map['assessmentPartId'])

    assessment_part_id = property(fget=get_assessment_part_id)

    def get_assessment_part(self):
        """Gets the parent assessment.

        return: (osid.assessment.authoring.AssessmentPart) - the parent
                assessment part
        raise:  IllegalState - ``has_parent_part()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        lookup_session = self._get_assessment_part_lookup_session()
        return lookup_session.get_assessment_part(self.get_assessment_part_id())

    assessment_part = property(fget=get_assessment_part)

    def is_section(self):
        """Tests if this part should be visible as a section in an assessment.

        If visible, this part will appear to the user as a separate
        section of the assessment. Typically, a section may not be under
        a non-sectioned part.

        return: (boolean) - ``true`` if this part is a section,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return not self.is_sequestered()

    def get_weight(self):
        """Gets an integral weight factor for this assessment part used for scoring.

        The percentage weight for this part is this weight divided by
        the sum total of all the weights in the assessment.

        return: (cardinal) - the weight
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    weight = property(fget=get_weight)

    def get_allocated_time(self):
        """Gets the allocated time for this part.

        The allocated time may be used to assign fixed time limits to
        each item or can be used to estimate the total assessment time.

        return: (osid.calendaring.Duration) - allocated time
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    allocated_time = property(fget=get_allocated_time)

    def get_child_assessment_part_ids(self):
        """Gets any child assessment part ``Ids``.

        return: (osid.id.IdList) - ``Ids`` of the child assessment parts
        *compliance: mandatory -- This method must be implemented.*

        """
        return IdList(self._my_map['childIds'])

    child_assessment_part_ids = property(fget=get_child_assessment_part_ids)

    def get_child_assessment_parts(self):
        """Gets any child assessment parts.

        return: (osid.assessment.authoring.AssessmentPartList) - the
                child assessment parts
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # only returned unsequestered children?
        lookup_session = self._get_assessment_part_lookup_session()
        lookup_session.use_sequestered_assessment_part_view()
        return lookup_session.get_assessment_parts_by_ids(self.get_child_ids())

    child_assessment_parts = property(fget=get_child_assessment_parts)

    @utilities.arguments_not_none
    def get_assessment_part_record(self, assessment_part_record_type):
        """Gets the assessment part record corresponding to the given ``AssessmentPart`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_part_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_part_record_type)`` is ``true`` .

        arg:    assessment_part_record_type (osid.type.Type): the type
                of the record to retrieve
        return: (osid.assessment.authoring.records.AssessmentPartRecord)
                - the assessment part record
        raise:  NullArgument - ``assessment_part_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_part_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_part_record_type)

    def get_child_ids(self):
        """Gets the child ``Ids`` of this assessment part."""
        return IdList(self._my_map['childIds'])

    def supports_item_ordering(self):
        """This method can be overridden by a record extension. Must be immutable"""
        return False

    def supports_simple_item_sequencing(self):
        """This method can be overridden by a record extension. Must be immutable"""
        return False

    def has_children(self):
        """This method can be overwritten by a record extension."""
        return bool(self._supports_simple_sequencing() and self._my_map['childIds'])

    def are_items_sequential(self):
        """This can be overridden by a record extension"""
        return False

    def are_items_shuffled(self):
        """This can be overridden by a record extension"""
        return False

    def are_children_sequential(self):
        """This can be overridden by a record extension"""
        return False

    def are_children_shuffled(self):
        """This can be overridden by a record extension"""
        return False

    # This method is probably not required
    def has_items(self):
        """This is out of spec, but required for adaptive assessment parts?"""
        if 'itemIds' in self._my_map and self._my_map['itemIds']:
            return True
        return False

    def get_items(self):
        """This is out of spec, but required for adaptive assessment parts?"""
        ils = get_item_lookup_session(runtime=self._runtime, proxy=self._proxy)
        ils.use_federated_bank_view()
        items = []
        if self.has_items():
            for idstr in self._my_map['itemIds']:
                items.append(ils.get_item(Id(idstr)))
        return ItemList(items, runtime=self._runtime, proxy=self._proxy)

    def get_item_ids(self):
        """This is out of spec, but required for adaptive assessment parts?"""
        item_ids = []
        if self.has_items():
            for idstr in self._my_map['itemIds']:
                item_ids.append(idstr)
        return IdList(item_ids)

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])

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

    def get_next_assessment_part_id(self, assessment_part_id):
        """This supports the basic simple sequence case. Can be overriden in a record for other cases"""
        if self.has_next_assessment_part(assessment_part_id):
            return Id(self._my_map['childIds'][self._my_map['childIds'].index(str(assessment_part_id)) + 1])

    def get_next_assessment_part(self, assessment_part_id):
        next_part_id = self.get_next_assessment_part_id(assessment_part_id)
        lookup_session = self._get_assessment_part_lookup_session()
        return lookup_session.get_assessment_part(next_part_id)

    def _get_assessment_part_lookup_session(self):
        """need to account for magic parts"""
        section = getattr(self, '_assessment_section', None)
        session = get_assessment_part_lookup_session(self._runtime,
                                                     self._proxy,
                                                     section)
        session.use_unsequestered_assessment_part_view()
        session.use_federated_bank_view()
        return session


class AssessmentPartForm(abc_assessment_authoring_objects.AssessmentPartForm, osid_objects.OsidObjectForm, osid_objects.OsidContainableForm, osid_objects.OsidOperableForm):
    """This is the form for creating and updating ``AssessmentParts``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAuthoringSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'assessment_authoring.AssessmentPart'

    def __init__(self, **kwargs):
        osid_objects.OsidContainableForm.__init__(self)
        osid_objects.OsidOperableForm.__init__(self)
        osid_objects.OsidObjectForm.__init__(self, object_name='ASSESSMENT_PART', **kwargs)
        self._mdata = default_mdata.get_assessment_part_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidContainableForm._init_metadata(self)
        osid_objects.OsidOperableForm._init_metadata(self)
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        if 'assessment_part_id' not in kwargs:
            # Only "Section" Parts are allowed directly under Assessments
            self._mdata['sequestered']['is_read_only'] = True
            self._mdata['sequestered']['is_required'] = True
            self._mdata['sequestered']['default_boolean_values'] = [False]
        else:
            if 'mdata' in kwargs:
                self._mdata['sequestered'] = kwargs['mdata']['sequestered']
        self._assessment_part_default = self._mdata['assessment_part']['default_id_values'][0]
        self._assessment_default = self._mdata['assessment']['default_id_values'][0]
        self._weight_default = self._mdata['weight']['default_integer_values'][0]
        self._allocated_time_default = self._mdata['allocated_time']['default_duration_values'][0]
        self._items_sequential_default = None
        self._items_shuffled_default = None
        self._mdata['children'] = {
            'element_label': 'Children',
            'instructions': 'accepts an IdList',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidContainableForm._init_map(self)
        osid_objects.OsidOperableForm._init_map(self)
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        if 'assessment_part_id' in kwargs:
            self._my_map['assessmentPartId'] = str(kwargs['assessment_part_id'])
            if 'mdata' in kwargs:
                self._my_map['sequestered'] = kwargs['mdata']['sequestered']['default_boolean_values'][0]
        else:
            self._my_map['assessmentPartId'] = self._assessment_part_default
            self._my_map['sequestered'] = False  # Parts under Assessments must be "Sections"
        if 'assessment_id' in kwargs:
            self._my_map['assessmentId'] = str(kwargs['assessment_id'])
        else:
            self._my_map['assessmentId'] = self._assessment_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['allocatedTime'] = self._allocated_time_default
        self._my_map['itemsSequential'] = self._items_sequential_default
        self._my_map['itemsShuffled'] = self._items_shuffled_default
        self._my_map['weight'] = self._weight_default
        if self._supports_simple_sequencing():
            self._my_map['childIds'] = []

    def get_weight_metadata(self):
        """Gets the metadata for the weight.

        return: (osid.Metadata) - metadata for the weight
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['weight'])
        metadata.update({'existing_cardinal_values': self._my_map['weight']})
        return Metadata(**metadata)

    weight_metadata = property(fget=get_weight_metadata)

    @utilities.arguments_not_none
    def set_weight(self, weight):
        """Sets the weight on a scale from 0-100.

        arg:    weight (cardinal): the new weight
        raise:  InvalidArgument - ``weight`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def clear_weight(self):
        """Clears the weight.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    weight = property(fset=set_weight, fdel=clear_weight)

    def get_allocated_time_metadata(self):
        """Gets the metadata for the allocated time.

        return: (osid.Metadata) - metadata for the allocated time
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['allocated_time'])
        metadata.update({'existing_duration_values': self._my_map['allocatedTime']})
        return Metadata(**metadata)

    allocated_time_metadata = property(fget=get_allocated_time_metadata)

    @utilities.arguments_not_none
    def set_allocated_time(self, time):
        """Sets the allocated time.

        arg:    time (osid.calendaring.Duration): the allocated time
        raise:  InvalidArgument - ``time`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.set_duration_template
        if self.get_allocated_time_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_duration(
                time,
                self.get_allocated_time_metadata()):
            raise errors.InvalidArgument()
        map = dict()
        map['days'] = time.days
        map['seconds'] = time.seconds
        map['microseconds'] = time.microseconds
        self._my_map['allocatedTime'] = map

    def clear_allocated_time(self):
        """Clears the allocated time.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.assessment.AssessmentOfferedForm.clear_duration_template
        if (self.get_allocated_time_metadata().is_read_only() or
                self.get_allocated_time_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['allocatedTime'] = self._allocated_time_default

    allocated_time = property(fset=set_allocated_time, fdel=clear_allocated_time)

    @utilities.arguments_not_none
    def get_assessment_part_form_record(self, assessment_part_record_type):
        """Gets the ``AssessmentPartFormRecord`` corresponding to the given assessment record ``Type``.

        arg:    assessment_part_record_type (osid.type.Type): the
                assessment part record type
        return:
                (osid.assessment.authoring.records.AssessmentPartFormRec
                ord) - the assessment part record
        raise:  NullArgument - ``assessment_part_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_part_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(assessment_part_record_type)

    def set_items_sequential(self, sequential):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['itemsSequential'] = sequential

    def set_items_shuffled(self, shuffled):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['itemsShuffled'] = shuffled

    def set_children_sequential(self, sequential):  # This should be set in a record
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['childrenSequential'] = sequential

    def set_children_shuffled(self, shuffled):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['childrenShuffled'] = shuffled

    def get_children_metadata(self):
        """Gets the metadata for children.

        return: (osid.Metadata) - metadata for the children
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        metadata = dict(self._mdata['children'])
        metadata.update({'existing_children_values': self._my_map['childIds']})
        return Metadata(**metadata)

    children_metadata = property(fget=get_children_metadata)

    @utilities.arguments_not_none
    def set_children(self, child_ids):
        """Sets the children.

        arg:    child_ids (osid.id.Id[]): the children``Ids``
        raise:  InvalidArgument - ``child_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self._supports_simple_sequencing():
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        if not isinstance(child_ids, list):
            raise errors.InvalidArgument()
        if self.get_children_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in child_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            if str(object_id) not in idstr_list:
                idstr_list.append(str(object_id))
        self._my_map['childIds'] = idstr_list

    def clear_children(self):
        """Clears the children.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self._supports_simple_sequencing():
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        if (self.get_children_metadata().is_read_only() or
                self.get_children_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['childIds'] = self._children_default

    children = property(fset=set_children, fdel=clear_children)

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])


class AssessmentPartList(abc_assessment_authoring_objects.AssessmentPartList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentPartList`` provides a means for accessing ``AssessmentPart`` elements sequentially either one at a time or many at a time.

    Examples: while (apl.hasNext()) { AssessmentPart assessmentPart =
    apl.getNextAssessmentPart(); }

    or
      while (apl.hasNext()) {
           AssessmentPart[] assessmentParts = apl.hetNextAssessmentParts(apl.available());
      }

    """

    def get_next_assessment_part(self):
        """Gets the next ``AssessmentPart`` in this list.

        return: (osid.assessment.authoring.AssessmentPart) - the next
                ``AssessmentPart`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentPart`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(AssessmentPart)

    __next__ = next

    next_assessment_part = property(fget=get_next_assessment_part)

    @utilities.arguments_not_none
    def get_next_assessment_parts(self, n):
        """Gets the next set of ``AssessmentPart`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentPart`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.authoring.AssessmentPart) - an array of
                ``AssessmentPart`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AssessmentPartList, number=n)


class SequenceRule(abc_assessment_authoring_objects.SequenceRule, osid_objects.OsidRule):
    """A ``SequenceRule`` defines the ordering of ``AssessmentParts``."""
    _namespace = 'assessment_authoring.SequenceRule'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='SEQUENCE_RULE', **kwargs)
        self._catalog_name = 'Bank'

    def get_assessment_part_id(self):
        """Gets the assessment part ``Id`` to which this rule belongs.

        return: (osid.id.Id) - ``Id`` of an assessment part
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return Id(self._my_map['assessmentPartId'])

    assessment_part_id = property(fget=get_assessment_part_id)

    def get_assessment_part(self):
        """Gets the assessment part to which this rule belongs.

        return: (osid.assessment.authoring.AssessmentPart) - an
                assessment part
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING')
        if not mgr.supports_assessment_part_lookup():
            raise errors.OperationFailed('Assessment_Authoring does not support AssessmentPart lookup')
        lookup_session = mgr.get_assessment_part_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessment_part(self.get_assessment_part_id())

    assessment_part = property(fget=get_assessment_part)

    def get_next_assessment_part_id(self):
        """Gets the next assessment part ``Id`` for success of this rule.

        return: (osid.id.Id) - ``Id`` of an assessment part
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['nextAssessmentPartId'])

    next_assessment_part_id = property(fget=get_next_assessment_part_id)

    def get_next_assessment_part(self):
        """Gets the next assessment part for success of this rule.

        return: (osid.assessment.authoring.AssessmentPart) - an
                assessment part
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    next_assessment_part = property(fget=get_next_assessment_part)

    def get_minimum_score(self):
        """Gets the minimum score expressed as an integer (0-100) for this rule.

        return: (cardinal) - minimum score
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    minimum_score = property(fget=get_minimum_score)

    def get_maximum_score(self):
        """Gets the maximum score expressed as an integer (0-100) for this rule.

        return: (cardinal) - maximum score
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    maximum_score = property(fget=get_maximum_score)

    def is_cumulative(self):
        """Tests if the score is applied to all previous assessment parts.

        return: (boolean) - ``true`` if the score is applied to all
                previous assessment parts, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['cumulative'])

    def get_applied_assessment_part_ids(self):
        """Qualifies ``is_cumulative()`` to apply to a specific list of assessment parts.

        If ``is_cumulative()`` is ``true,`` this method may return an
        empty list to mean all previous assessment parts.

        return: (osid.id.IdList) - list of assessment parts
        raise:  IllegalState - ``is_cumulative()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_asset_ids_template
        return IdList(self._my_map['appliedAssessmentPartIds'])

    applied_assessment_part_ids = property(fget=get_applied_assessment_part_ids)

    def get_applied_assessment_parts(self):
        """Qualifies ``is_cumulative()`` to apply to a specific list of assessment parts.

        If ``is_cumulative()`` is ``true,`` this method may return an
        empty list to mean all previous assessment parts.

        return: (osid.assessment.authoring.AssessmentPartList) - list of
                assessment parts
        raise:  IllegalState - ``is_cumulative()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    applied_assessment_parts = property(fget=get_applied_assessment_parts)

    @utilities.arguments_not_none
    def get_sequence_rule_record(self, sequence_rule_record_type):
        """Gets the assessment sequence rule record corresponding to the given ``SequenceRule`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``sequence_rule_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(sequence_rule_record_type)`` is ``true`` .

        arg:    sequence_rule_record_type (osid.type.Type): the type of
                the record to retrieve
        return: (osid.assessment.authoring.records.SequenceRuleRecord) -
                the assessment sequence rule record
        raise:  NullArgument - ``sequence_rule_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(sequence_rule_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(sequence_rule_record_type)


class SequenceRuleForm(abc_assessment_authoring_objects.SequenceRuleForm, osid_objects.OsidRuleForm):
    """This is the form for creating and updating sequence rules.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``SequenceSession``
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='SEQUENCE_RULE', **kwargs)
        self._mdata = default_mdata.get_sequence_rule_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._cumulative_default = self._mdata['cumulative']['default_boolean_values'][0]
        self._minimum_score_default = self._mdata['minimum_score']['default_integer_values'][0]
        self._maximum_score_default = self._mdata['maximum_score']['default_integer_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['nextAssessmentPartId'] = str(kwargs['next_assessment_part_id'])
        self._my_map['cumulative'] = self._cumulative_default
        self._my_map['minimumScore'] = self._minimum_score_default
        self._my_map['maximumScore'] = self._maximum_score_default
        self._my_map['assessmentPartId'] = str(kwargs['assessment_part_id'])
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]

    def get_minimum_score_metadata(self):
        """Gets the metadata for the minimum score.

        return: (osid.Metadata) - metadata for the minimum score
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['minimum_score'])
        metadata.update({'existing_cardinal_values': self._my_map['minimumScore']})
        return Metadata(**metadata)

    minimum_score_metadata = property(fget=get_minimum_score_metadata)

    @utilities.arguments_not_none
    def set_minimum_score(self, score):
        """Sets the minimum score for this rule.

        arg:    score (cardinal): minimum score
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    minimum_score = property(fset=set_minimum_score)

    def get_maximum_score_metadata(self):
        """Gets the metadata for the maximum score.

        return: (osid.Metadata) - metadata for the maximum score
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['maximum_score'])
        metadata.update({'existing_cardinal_values': self._my_map['maximumScore']})
        return Metadata(**metadata)

    maximum_score_metadata = property(fget=get_maximum_score_metadata)

    @utilities.arguments_not_none
    def set_maximum_score(self, score):
        """Sets the maximum score for this rule.

        arg:    score (cardinal): maximum score
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    maximum_score = property(fset=set_maximum_score)

    def get_cumulative_metadata(self):
        """Gets the metadata for the cumulative flag.

        return: (osid.Metadata) - metadata for the cumulative flag
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['cumulative'])
        metadata.update({'existing_boolean_values': self._my_map['cumulative']})
        return Metadata(**metadata)

    cumulative_metadata = property(fget=get_cumulative_metadata)

    @utilities.arguments_not_none
    def set_cumulative(self, cumulative):
        """Applies this rule to all previous assessment parts.

        arg:    cumulative (boolean): ``true`` to apply to all previous
                assessment parts. ``false`` to apply to the immediate
                previous assessment part
        raise:  InvalidArgument - ``cumulative`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_group_template
        if self.get_cumulative_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_boolean(cumulative):
            raise errors.InvalidArgument()
        self._my_map['cumulative'] = cumulative

    cumulative = property(fset=set_cumulative)

    def get_applied_assessment_parts_metadata(self):
        """Gets the metadata for the applied assessment parts.

        return: (osid.Metadata) - metadata for the applied assessment
                parts
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['applied_assessment_parts'])
        metadata.update({'existing_none_values': self._my_map['appliedAssessmentParts']})
        return Metadata(**metadata)

    applied_assessment_parts_metadata = property(fget=get_applied_assessment_parts_metadata)

    @utilities.arguments_not_none
    def apply_assessment_parts(self, assessment_part_ids):
        """Designates assessment parts to which the rule applies.

        arg:    assessment_part_ids (osid.id.Id[]): the parts to which
                this rule should apply
        raise:  InvalidArgument - ``assessment_part_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``assessment_part_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_sequence_rule_form_record(self, sequence_rule_record):
        """Gets the ``SequenceRuleFormRecord`` corresponding to the given sequence rule record ``Type``.

        arg:    sequence_rule_record (osid.type.Type): a sequence rule
                record type
        return:
                (osid.assessment.authoring.records.SequenceRuleFormRecor
                d) - the sequence rule record
        raise:  NullArgument - ``sequence_rule_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(asequence_rule_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(sequence_rule_record)


class SequenceRuleList(abc_assessment_authoring_objects.SequenceRuleList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``SequenceRuleList`` provides a means for accessing ``SequenceRule`` elements sequentially either one at a time or many at a time.

    Examples: while (srl.hasNext()) { AssessmentSequenceRule rule =
    srl.getNextAssessmentSequenceRule(); }

    or
      while (srl.hasNext()) {
           AssessmentSequenceRule[] rules = srl.getNextAssessmentSequenceRules(srl.available());
      }

    """

    def get_next_sequence_rule(self):
        """Gets the next ``SequenceRule`` in this list.

        return: (osid.assessment.authoring.SequenceRule) - the next
                ``SequenceRule`` in this list. The ``has_next()`` method
                should be used to test that a next ``SequenceRule`` is
                available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(SequenceRule)

    __next__ = next

    next_sequence_rule = property(fget=get_next_sequence_rule)

    @utilities.arguments_not_none
    def get_next_sequence_rules(self, n):
        """Gets the next set of ``SequenceRule`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``SequenceRule`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.authoring.SequenceRule) - an array of
                ``SequenceRule`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(SequenceRuleList, number=n)
