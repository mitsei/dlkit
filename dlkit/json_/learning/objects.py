"""JSON implementations of learning objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import importlib


from decimal import Decimal


from . import default_mdata
from .. import utilities
from ..id.objects import IdList
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.learning import objects as abc_learning_objects
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


class Objective(abc_learning_objects.Objective, osid_objects.OsidObject, osid_markers.Federateable):
    """An ``Objective`` is a statable learning objective."""
    _namespace = 'learning.Objective'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='OBJECTIVE', **kwargs)
        self._catalog_name = 'ObjectiveBank'

    def has_assessment(self):
        """Tests if an assessment is associated with this objective.

        return: (boolean) - ``true`` if an assessment exists, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['assessmentId'])

    def get_assessment_id(self):
        """Gets the assessment ``Id`` associated with this learning objective.

        return: (osid.id.Id) - the assessment ``Id``
        raise:  IllegalState - ``has_assessment()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['assessmentId']):
            raise errors.IllegalState('this Objective has no assessment')
        else:
            return Id(self._my_map['assessmentId'])

    assessment_id = property(fget=get_assessment_id)

    def get_assessment(self):
        """Gets the assessment associated with this learning objective.

        return: (osid.assessment.Assessment) - the assessment
        raise:  IllegalState - ``has_assessment()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['assessmentId']):
            raise errors.IllegalState('this Objective has no assessment')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_lookup():
            raise errors.OperationFailed('Assessment does not support Assessment lookup')
        lookup_session = mgr.get_assessment_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        osid_object = lookup_session.get_assessment(self.get_assessment_id())
        return osid_object

    assessment = property(fget=get_assessment)

    def has_knowledge_category(self):
        """Tests if this objective has a knowledge dimension.

        return: (boolean) - ``true`` if a knowledge category exists,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['knowledgeCategoryId'])

    def get_knowledge_category_id(self):
        """Gets the grade ``Id`` associated with the knowledge dimension.

        return: (osid.id.Id) - the grade ``Id``
        raise:  IllegalState - ``has_knowledge_category()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['knowledgeCategoryId']):
            raise errors.IllegalState('this Objective has no knowledge_category')
        else:
            return Id(self._my_map['knowledgeCategoryId'])

    knowledge_category_id = property(fget=get_knowledge_category_id)

    def get_knowledge_category(self):
        """Gets the grade associated with the knowledge dimension.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``has_knowledge_category()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['knowledgeCategoryId']):
            raise errors.IllegalState('this Objective has no knowledge_category')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_knowledge_category_id())
        return osid_object

    knowledge_category = property(fget=get_knowledge_category)

    def has_cognitive_process(self):
        """Tests if this objective has a cognitive process type.

        return: (boolean) - ``true`` if a cognitive process exists,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['cognitiveProcessId'])

    def get_cognitive_process_id(self):
        """Gets the grade ``Id`` associated with the cognitive process.

        return: (osid.id.Id) - the grade ``Id``
        raise:  IllegalState - ``has_cognitive_process()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['cognitiveProcessId']):
            raise errors.IllegalState('this Objective has no cognitive_process')
        else:
            return Id(self._my_map['cognitiveProcessId'])

    cognitive_process_id = property(fget=get_cognitive_process_id)

    def get_cognitive_process(self):
        """Gets the grade associated with the cognitive process.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``has_cognitive_process()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['cognitiveProcessId']):
            raise errors.IllegalState('this Objective has no cognitive_process')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_cognitive_process_id())
        return osid_object

    cognitive_process = property(fget=get_cognitive_process)

    @utilities.arguments_not_none
    def get_objective_record(self, objective_record_type):
        """Gets the objective bank record corresponding to the given ``Objective`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``objective_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_record_type)`` is ``true`` .

        arg:    objective_record_type (osid.type.Type): an objective
                record type
        return: (osid.learning.records.ObjectiveRecord) - the objective
                record
        raise:  NullArgument - ``objective_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(objective_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(objective_record_type)


class ObjectiveForm(abc_learning_objects.ObjectiveForm, osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm):
    """This is the form for creating and updating ``Objectives``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'learning.Objective'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='OBJECTIVE', **kwargs)
        self._mdata = default_mdata.get_objective_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._cognitive_process_default = self._mdata['cognitive_process']['default_id_values'][0]
        self._assessment_default = self._mdata['assessment']['default_id_values'][0]
        self._knowledge_category_default = self._mdata['knowledge_category']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['assignedObjectiveBankIds'] = [str(kwargs['objective_bank_id'])]
        self._my_map['cognitiveProcessId'] = self._cognitive_process_default
        self._my_map['assessmentId'] = self._assessment_default
        self._my_map['knowledgeCategoryId'] = self._knowledge_category_default

    def get_assessment_metadata(self):
        """Gets the metadata for an assessment.

        return: (osid.Metadata) - metadata for the assessment
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['assessment'])
        metadata.update({'existing_id_values': self._my_map['assessmentId']})
        return Metadata(**metadata)

    assessment_metadata = property(fget=get_assessment_metadata)

    @utilities.arguments_not_none
    def set_assessment(self, assessment_id):
        """Sets the assessment.

        arg:    assessment_id (osid.id.Id): the new assessment
        raise:  InvalidArgument - ``assessment_id`` is invalid
        raise:  NoAccess - ``assessment_id`` cannot be modified
        raise:  NullArgument - ``assessment_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_assessment_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(assessment_id):
            raise errors.InvalidArgument()
        self._my_map['assessmentId'] = str(assessment_id)

    def clear_assessment(self):
        """Clears the assessment.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_assessment_metadata().is_read_only() or
                self.get_assessment_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['assessmentId'] = self._assessment_default

    assessment = property(fset=set_assessment, fdel=clear_assessment)

    def get_knowledge_category_metadata(self):
        """Gets the metadata for a knowledge category.

        return: (osid.Metadata) - metadata for the knowledge category
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['knowledge_category'])
        metadata.update({'existing_id_values': self._my_map['knowledgeCategoryId']})
        return Metadata(**metadata)

    knowledge_category_metadata = property(fget=get_knowledge_category_metadata)

    @utilities.arguments_not_none
    def set_knowledge_category(self, grade_id):
        """Sets the knowledge category.

        arg:    grade_id (osid.id.Id): the new knowledge category
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``grade_id`` cannot be modified
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_knowledge_category_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_id):
            raise errors.InvalidArgument()
        self._my_map['knowledgeCategoryId'] = str(grade_id)

    def clear_knowledge_category(self):
        """Clears the knowledge category.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_knowledge_category_metadata().is_read_only() or
                self.get_knowledge_category_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['knowledgeCategoryId'] = self._knowledge_category_default

    knowledge_category = property(fset=set_knowledge_category, fdel=clear_knowledge_category)

    def get_cognitive_process_metadata(self):
        """Gets the metadata for a cognitive process.

        return: (osid.Metadata) - metadata for the cognitive process
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['cognitive_process'])
        metadata.update({'existing_id_values': self._my_map['cognitiveProcessId']})
        return Metadata(**metadata)

    cognitive_process_metadata = property(fget=get_cognitive_process_metadata)

    @utilities.arguments_not_none
    def set_cognitive_process(self, grade_id):
        """Sets the cognitive process.

        arg:    grade_id (osid.id.Id): the new cognitive process
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``grade_id`` cannot be modified
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_cognitive_process_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_id):
            raise errors.InvalidArgument()
        self._my_map['cognitiveProcessId'] = str(grade_id)

    def clear_cognitive_process(self):
        """Clears the cognitive process.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_cognitive_process_metadata().is_read_only() or
                self.get_cognitive_process_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['cognitiveProcessId'] = self._cognitive_process_default

    cognitive_process = property(fset=set_cognitive_process, fdel=clear_cognitive_process)

    @utilities.arguments_not_none
    def get_objective_form_record(self, objective_record_type):
        """Gets the ``ObjectiveFormRecord`` corresponding to the given objective record ``Type``.

        arg:    objective_record_type (osid.type.Type): the objective
                record type
        return: (osid.learning.records.ObjectiveFormRecord) - the
                objective form record
        raise:  NullArgument - ``objective_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(objective_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(objective_record_type)


class ObjectiveList(abc_learning_objects.ObjectiveList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveList`` provides a means for accessing ``Objective`` elements sequentially either one at a time or many at a time.

    Examples: while (ol.hasNext()) { Objective objective =
    ol.getNextObjective(); }

    or
      while (ol.hasNext()) {
           Objective[] objectives = ol.getNextObjectives(ol.available());
      }

    """

    def get_next_objective(self):
        """Gets the next ``Objective`` in this list.

        return: (osid.learning.Objective) - the next ``Objective`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Objective`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Objective)

    __next__ = next

    next_objective = property(fget=get_next_objective)

    @utilities.arguments_not_none
    def get_next_objectives(self, n):
        """Gets the next set of ``Objective`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Objective`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.learning.Objective) - an array of ``Objective``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ObjectiveList, number=n)


class ObjectiveNode(abc_learning_objects.ObjectiveNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveHierarchySession``.

    """

    def get_objective(self):
        """Gets the ``Objective`` at this node.

        return: (osid.learning.Objective) - the objective represented by
                this node
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective = property(fget=get_objective)

    def get_parent_objective_nodes(self):
        """Gets the parents of this objective.

        return: (osid.learning.ObjectiveNodeList) - the parents of the
                ``id``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    parent_objective_nodes = property(fget=get_parent_objective_nodes)

    def get_child_objective_nodes(self):
        """Gets the children of this objective.

        return: (osid.learning.ObjectiveNodeList) - the children of this
                objective
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    child_objective_nodes = property(fget=get_child_objective_nodes)


class ObjectiveNodeList(abc_learning_objects.ObjectiveNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveNodeList`` provides a means for accessing ``ObjectiveNode`` elements sequentially either one at a time or many at a time.

    Examples: while (onl.hasNext()) { ObjectiveNode node =
    onl.getNextObjectiveNode(); }

    or
      while (onl.hasNext()) {
           ObjectiveNode[] nodes = onl.getNextObjectiveNodes(onl.available());
      }

    """

    def get_next_objective_node(self):
        """Gets the next ``ObjectiveNode`` in this list.

        return: (osid.learning.ObjectiveNode) - the next
                ``ObjectiveNode`` in this list. The ``has_next()``
                method should be used to test that a next
                ``ObjectiveNode`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(ObjectiveNode)

    __next__ = next

    next_objective_node = property(fget=get_next_objective_node)

    @utilities.arguments_not_none
    def get_next_objective_nodes(self, n):
        """Gets the next set of ``ObjectiveNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``ObjectiveNode`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.learning.ObjectiveNode) - an array of
                ``ObjectiveNode`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ObjectiveNodeList, number=n)


class Activity(abc_learning_objects.Activity, osid_objects.OsidObject, osid_markers.Subjugateable):
    """An ``Activity`` represents learning material or other learning activities to meet an objective.

    An Activity has may relate to a set of ``Asssts`` for self learning,
    recommended ``Courses`` to take, or a learning ``Assessment``. The
    learning ``Assessment`` differs from the ``Objective``
    ``Assessment`` in that the latter used to test for proficiency in
    the ``Objective``.

    Generally, an ``Activity`` should focus on one of assets, courses,
    assessments, or some other specific activity related to the
    objective described or related in the ``ActivityRecord``.

    """
    _namespace = 'learning.Activity'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='ACTIVITY', **kwargs)
        self._catalog_name = 'ObjectiveBank'

    def get_objective_id(self):
        """Gets the ``Id`` of the related objective.

        return: (osid.id.Id) - the objective ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        if not bool(self._my_map['objectiveId']):
            raise errors.IllegalState('objective empty')
        return Id(self._my_map['objectiveId'])

    objective_id = property(fget=get_objective_id)

    def get_objective(self):
        """Gets the related objective.

        return: (osid.learning.Objective) - the related objective
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        if not bool(self._my_map['objectiveId']):
            raise errors.IllegalState('objective empty')
        mgr = self._get_provider_manager('LEARNING')
        if not mgr.supports_objective_lookup():
            raise errors.OperationFailed('Learning does not support Objective lookup')
        lookup_session = mgr.get_objective_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_objective_bank_view()
        return lookup_session.get_objective(self.get_objective_id())

    objective = property(fget=get_objective)

    def is_asset_based_activity(self):
        """Tests if this is an asset based activity.

        return: (boolean) - ``true`` if this activity is based on
                assets, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return bool(self._my_map['assetIds'])

    def get_asset_ids(self):
        """Gets the ``Ids`` of any assets associated with this activity.

        return: (osid.id.IdList) - list of asset ``Ids``
        raise:  IllegalState - ``is_asset_based_activity()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_asset_ids_template
        return IdList(self._my_map['assetIds'])

    asset_ids = property(fget=get_asset_ids)

    def get_assets(self):
        """Gets any assets associated with this activity.

        return: (osid.repository.AssetList) - list of assets
        raise:  IllegalState - ``is_asset_based_activity()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_assets_template
        if not bool(self._my_map['assetIds']):
            raise errors.IllegalState('no assetIds')
        mgr = self._get_provider_manager('REPOSITORY')
        if not mgr.supports_asset_lookup():
            raise errors.OperationFailed('Repository does not support Asset lookup')

        # What about the Proxy?
        lookup_session = mgr.get_asset_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_repository_view()
        return lookup_session.get_assets_by_ids(self.get_asset_ids())

    assets = property(fget=get_assets)

    def is_course_based_activity(self):
        """Tests if this is a course based activity.

        return: (boolean) - ``true`` if this activity is based on
                courses, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return bool(self._my_map['courseIds'])

    def get_course_ids(self):
        """Gets the ``Ids`` of any courses associated with this activity.

        return: (osid.id.IdList) - list of course ``Ids``
        raise:  IllegalState - ``is_course_based_activity()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_asset_ids_template
        return IdList(self._my_map['courseIds'])

    course_ids = property(fget=get_course_ids)

    def get_courses(self):
        """Gets any courses associated with this activity.

        return: (osid.course.CourseList) - list of courses
        raise:  IllegalState - ``is_course_based_activity()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_assets_template
        if not bool(self._my_map['courseIds']):
            raise errors.IllegalState('no courseIds')
        mgr = self._get_provider_manager('COURSE')
        if not mgr.supports_course_lookup():
            raise errors.OperationFailed('Course does not support Course lookup')

        # What about the Proxy?
        lookup_session = mgr.get_course_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_no_catalog_view()
        return lookup_session.get_courses_by_ids(self.get_course_ids())

    courses = property(fget=get_courses)

    def is_assessment_based_activity(self):
        """Tests if this is an assessment based activity.

        These assessments are for learning the objective and not for
        assessing prodiciency in the objective.

        return: (boolean) - ``true`` if this activity is based on
                assessments, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return bool(self._my_map['assessmentIds'])

    def get_assessment_ids(self):
        """Gets the ``Ids`` of any assessments associated with this activity.

        return: (osid.id.IdList) - list of assessment ``Ids``
        raise:  IllegalState - ``is_assessment_based_activity()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_asset_ids_template
        return IdList(self._my_map['assessmentIds'])

    assessment_ids = property(fget=get_assessment_ids)

    def get_assessments(self):
        """Gets any assessments associated with this activity.

        return: (osid.assessment.AssessmentList) - list of assessments
        raise:  IllegalState - ``is_assessment_based_activity()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_assets_template
        if not bool(self._my_map['assessmentIds']):
            raise errors.IllegalState('no assessmentIds')
        mgr = self._get_provider_manager('ASSESSMENT')
        if not mgr.supports_assessment_lookup():
            raise errors.OperationFailed('Assessment does not support Assessment lookup')

        # What about the Proxy?
        lookup_session = mgr.get_assessment_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bank_view()
        return lookup_session.get_assessments_by_ids(self.get_assessment_ids())

    assessments = property(fget=get_assessments)

    @utilities.arguments_not_none
    def get_activity_record(self, activity_record_type):
        """Gets the activity record corresponding to the given ``Activity`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``activity_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(activity_record_type)`` is ``true`` .

        arg:    activity_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.learning.records.ActivityRecord) - the activity
                record
        raise:  NullArgument - ``activity_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(activity_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(activity_record_type)


class ActivityForm(abc_learning_objects.ActivityForm, osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``Activities``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ActivityAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'learning.Activity'

    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='ACTIVITY', **kwargs)
        self._mdata = default_mdata.get_activity_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._courses_default = self._mdata['courses']['default_id_values']
        self._assessments_default = self._mdata['assessments']['default_id_values']
        self._assets_default = self._mdata['assets']['default_id_values']

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['assignedObjectiveBankIds'] = [str(kwargs['objective_bank_id'])]
        self._my_map['courseIds'] = self._courses_default
        self._my_map['assessmentIds'] = self._assessments_default
        self._my_map['objectiveId'] = str(kwargs['objective_id'])
        self._my_map['assetIds'] = self._assets_default

    def get_assets_metadata(self):
        """Gets the metadata for the assets.

        return: (osid.Metadata) - metadata for the assets
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.get_assets_metadata_template
        metadata = dict(self._mdata['assets'])
        metadata.update({'existing_assets_values': self._my_map['assetIds']})
        return Metadata(**metadata)

    assets_metadata = property(fget=get_assets_metadata)

    @utilities.arguments_not_none
    def set_assets(self, asset_ids):
        """Sets the assets.

        arg:    asset_ids (osid.id.Id[]): the asset ``Ids``
        raise:  InvalidArgument - ``asset_ids`` is invalid
        raise:  NullArgument - ``asset_ids`` is ``null``
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.set_assets_template
        if not isinstance(asset_ids, list):
            raise errors.InvalidArgument()
        if self.get_assets_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in asset_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            idstr_list.append(str(object_id))
        self._my_map['assetIds'] = idstr_list

    def clear_assets(self):
        """Clears the assets.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.clear_assets_template
        if (self.get_assets_metadata().is_read_only() or
                self.get_assets_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['assetIds'] = self._assets_default

    assets = property(fset=set_assets, fdel=clear_assets)

    def get_courses_metadata(self):
        """Gets the metadata for the courses.

        return: (osid.Metadata) - metadata for the courses
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.get_assets_metadata_template
        metadata = dict(self._mdata['courses'])
        metadata.update({'existing_courses_values': self._my_map['courseIds']})
        return Metadata(**metadata)

    courses_metadata = property(fget=get_courses_metadata)

    @utilities.arguments_not_none
    def set_courses(self, course_ids):
        """Sets the courses.

        arg:    course_ids (osid.id.Id[]): the course ``Ids``
        raise:  InvalidArgument - ``course_ids`` is invalid
        raise:  NullArgument - ``course_ids`` is ``null``
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.set_assets_template
        if not isinstance(course_ids, list):
            raise errors.InvalidArgument()
        if self.get_courses_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in course_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            idstr_list.append(str(object_id))
        self._my_map['courseIds'] = idstr_list

    def clear_courses(self):
        """Clears the courses.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.clear_assets_template
        if (self.get_courses_metadata().is_read_only() or
                self.get_courses_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['courseIds'] = self._courses_default

    courses = property(fset=set_courses, fdel=clear_courses)

    def get_assessments_metadata(self):
        """Gets the metadata for the assessments.

        return: (osid.Metadata) - metadata for the assessments
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.get_assets_metadata_template
        metadata = dict(self._mdata['assessments'])
        metadata.update({'existing_assessments_values': self._my_map['assessmentIds']})
        return Metadata(**metadata)

    assessments_metadata = property(fget=get_assessments_metadata)

    @utilities.arguments_not_none
    def set_assessments(self, assessment_ids):
        """Sets the assessments.

        arg:    assessment_ids (osid.id.Id[]): the assessment ``Ids``
        raise:  InvalidArgument - ``assessment_ids`` is invalid
        raise:  NullArgument - ``assessment_ids`` is ``null``
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.set_assets_template
        if not isinstance(assessment_ids, list):
            raise errors.InvalidArgument()
        if self.get_assessments_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in assessment_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            idstr_list.append(str(object_id))
        self._my_map['assessmentIds'] = idstr_list

    def clear_assessments(self):
        """Clears the assessments.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.ActivityForm.clear_assets_template
        if (self.get_assessments_metadata().is_read_only() or
                self.get_assessments_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['assessmentIds'] = self._assessments_default

    assessments = property(fset=set_assessments, fdel=clear_assessments)

    @utilities.arguments_not_none
    def get_activity_form_record(self, activity_record_type):
        """Gets the ``ActivityFormRecord`` corresponding to the given activity record ``Type``.

        arg:    activity_record_type (osid.type.Type): the activity
                record type
        return: (osid.learning.records.ActivityFormRecord) - the
                activity form record
        raise:  NullArgument - ``activity_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(activity_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(activity_record_type)


class ActivityList(abc_learning_objects.ActivityList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ActivityList`` provides a means for accessing ``Activity`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Activity activity =
    al.getNextActivity(); }

    or
      while (al.hasNext()) {
           Activity[] activities = al.getNextActivities(al.available());
      }

    """

    def get_next_activity(self):
        """Gets the next ``Activity`` in this list.

        return: (osid.learning.Activity) - the next ``Activity`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Activity`` is available before calling
                this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Activity)

    __next__ = next

    next_activity = property(fget=get_next_activity)

    @utilities.arguments_not_none
    def get_next_activities(self, n):
        """Gets the next set of ``Activity`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Activity`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.learning.Activity) - an array of ``Activity``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ActivityList, number=n)


class Proficiency(abc_learning_objects.Proficiency, osid_objects.OsidRelationship):
    """A ``Proficiency`` represents a competency of a leraning objective."""
    _namespace = 'learning.Proficiency'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='PROFICIENCY', **kwargs)
        self._catalog_name = 'ObjectiveBank'

    def get_resource_id(self):
        """Gets the resource ``Id`` to whom this proficiency applies.

        return: (osid.id.Id) - the resource ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['resourceId'])

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the resource to whom this proficiency applies.

        return: (osid.resource.Resource) - the resource
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource = property(fget=get_resource)

    def get_objective_id(self):
        """Gets the objective ``Id`` to whom this proficiency applies.

        return: (osid.id.Id) - the objective ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['objectiveId'])

    objective_id = property(fget=get_objective_id)

    def get_objective(self):
        """Gets the objective to whom this proficiency applies.

        return: (osid.learning.Objective) - the objective
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        if not bool(self._my_map['objectiveId']):
            raise errors.IllegalState('objective empty')
        mgr = self._get_provider_manager('LEARNING')
        if not mgr.supports_objective_lookup():
            raise errors.OperationFailed('Learning does not support Objective lookup')
        lookup_session = mgr.get_objective_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_objective_bank_view()
        return lookup_session.get_objective(self.get_objective_id())

    objective = property(fget=get_objective)

    def get_completion(self):
        """Gets the completion of this objective as a percentage 0-100.

        return: (decimal) - the completion
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.grading.GradeSystem.get_lowest_numeric_score_template
        if self._my_map['completion'] is None:
            return None
        else:
            return Decimal(str(self._my_map['completion']))

    completion = property(fget=get_completion)

    def has_level(self):
        """Tests if a proficiency level is available.

        return: (boolean) - ``true`` if a level is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_level_id(self):
        """Gets the proficiency level expressed as a grade.

        return: (osid.id.Id) - the grade ``Id``
        raise:  IllegalState - ``has_level()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    level_id = property(fget=get_level_id)

    def get_level(self):
        """Gets the proficiency level expressed as a grade.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``has_level()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    level = property(fget=get_level)

    @utilities.arguments_not_none
    def get_proficiency_record(self, proficiency_record_type):
        """Gets the proficiency record corresponding to the given ``Proficiency`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proficiency_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(proficiency_record_type)`` is ``true`` .

        arg:    proficiency_record_type (osid.type.Type): the type of
                proficiency record to retrieve
        return: (osid.learning.records.ProficiencyRecord) - the
                proficiency record
        raise:  NullArgument - ``proficiency_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(proficiency_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(proficiency_record_type)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['startDate'] is not None:
            actual_start_date = obj_map['startDate']
            obj_map['startDate'] = dict()
            obj_map['startDate']['year'] = actual_start_date.year
            obj_map['startDate']['month'] = actual_start_date.month
            obj_map['startDate']['day'] = actual_start_date.day
            obj_map['startDate']['hour'] = actual_start_date.hour
            obj_map['startDate']['minute'] = actual_start_date.minute
            obj_map['startDate']['second'] = actual_start_date.second
            obj_map['startDate']['microsecond'] = actual_start_date.microsecond
        if obj_map['endDate'] is not None:
            actual_end_date = obj_map['endDate']
            obj_map['endDate'] = dict()
            obj_map['endDate']['year'] = actual_end_date.year
            obj_map['endDate']['month'] = actual_end_date.month
            obj_map['endDate']['day'] = actual_end_date.day
            obj_map['endDate']['hour'] = actual_end_date.hour
            obj_map['endDate']['minute'] = actual_end_date.minute
            obj_map['endDate']['second'] = actual_end_date.second
            obj_map['endDate']['microsecond'] = actual_end_date.microsecond

        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class ProficiencyForm(abc_learning_objects.ProficiencyForm, osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Proficiencies``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ProficiencyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'learning.Proficiency'

    def __init__(self, **kwargs):
        osid_objects.OsidRelationshipForm.__init__(self, object_name='PROFICIENCY', **kwargs)
        self._mdata = default_mdata.get_proficiency_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidRelationshipForm._init_metadata(self, **kwargs)
        self._completion_default = self._mdata['completion']['default_decimal_values'][0]
        self._level_default = self._mdata['level']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidRelationshipForm._init_map(self, record_types=record_types)
        self._my_map['assignedObjectiveBankIds'] = [str(kwargs['objective_bank_id'])]
        self._my_map['completion'] = self._completion_default
        self._my_map['objectiveId'] = str(kwargs['objective_id'])
        self._my_map['resourceId'] = str(kwargs['resource_id'])
        self._my_map['levelId'] = self._level_default

    def get_completion_metadata(self):
        """Gets the metadata for completion percentage.

        return: (osid.Metadata) - metadata for the completion percentage
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['completion'])
        metadata.update({'existing_decimal_values': self._my_map['completion']})
        return Metadata(**metadata)

    completion_metadata = property(fget=get_completion_metadata)

    @utilities.arguments_not_none
    def set_completion(self, completion):
        """Sets the completion percentage.

        arg:    completion (decimal): the completion percentage
        raise:  InvalidArgument - ``completion`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.grading.GradeSystemForm.set_lowest_numeric_score
        if self.get_completion_metadata().is_read_only():
            raise errors.NoAccess()
        try:
            completion = float(completion)
        except ValueError:
            raise errors.InvalidArgument()
        if not self._is_valid_decimal(completion, self.get_completion_metadata()):
            raise errors.InvalidArgument()
        self._my_map['completion'] = completion

    def clear_completion(self):
        """Clears the completion.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.grading.GradeSystemForm.clear_lowest_numeric_score
        if (self.get_completion_metadata().is_read_only() or
                self.get_completion_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['completion'] = self._completion_default

    completion = property(fset=set_completion, fdel=clear_completion)

    def get_level_metadata(self):
        """Gets the metadata for a level.

        return: (osid.Metadata) - metadata for the grade level
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['level'])
        metadata.update({'existing_id_values': self._my_map['levelId']})
        return Metadata(**metadata)

    level_metadata = property(fget=get_level_metadata)

    @utilities.arguments_not_none
    def set_level(self, grade):
        """Sets the level expressed as a ``Grade``.

        arg:    grade (osid.grading.Grade): the level
        raise:  InvalidArgument - ``grade`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``grade`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_level_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade):
            raise errors.InvalidArgument()
        self._my_map['level'] = str(grade)

    def set_level_id(self, grade_id):
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
        if (self.get_level_metadata().is_read_only() or
                self.get_level_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['levelId'] = self._level_default
        self._my_map['level'] = self._level_default

    level = property(fset=set_level, fdel=clear_level)

    @utilities.arguments_not_none
    def get_proficiency_form_record(self, proficiency_record_type):
        """Gets the ``ProficiencyFormRecord`` corresponding to the given proficiency record ``Type``.

        arg:    proficiency_record_type (osid.type.Type): a proficiency
                record type
        return: (osid.learning.records.ProficiencyFormRecord) - the
                proficiency form record
        raise:  NullArgument - ``proficiency_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(proficiency_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(proficiency_record_type)


class ProficiencyList(abc_learning_objects.ProficiencyList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ProficiencyList`` provides a means for accessing ``Proficiency`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Proficiency proficiency =
    pl.getNextProficiency(); }

    or
      while (pl.hasNext()) {
           Proficiency[] proficiencies = pl.getNextProficiencies(pl.available());
      }

    """

    def get_next_proficiency(self):
        """Gets the next ``Proficiency`` in this list.

        return: (osid.learning.Proficiency) - the next ``Proficiency``
                in this list. The ``has_next()`` method should be used
                to test that a next ``Proficiency`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Proficiency)

    __next__ = next

    next_proficiency = property(fget=get_next_proficiency)

    @utilities.arguments_not_none
    def get_next_proficiencies(self, n):
        """Gets the next set of ``Proficiency`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Proficiency`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.learning.Proficiency) - an array of
                ``Proficiency`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ProficiencyList, number=n)


class ObjectiveBank(abc_learning_objects.ObjectiveBank, osid_objects.OsidCatalog):
    """an objective bank defines a collection of objectives."""
    _namespace = 'learning.ObjectiveBank'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='OBJECTIVE_BANK', **kwargs)

    @utilities.arguments_not_none
    def get_objective_bank_record(self, objective_bank_record_type):
        """Gets the objective bank record corresponding to the given ``ObjectiveBank`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``objective_bank_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_bank_record_type)`` is ``true`` .

        arg:    objective_bank_record_type (osid.type.Type): an
                objective bank record type
        return: (osid.learning.records.ObjectiveBankRecord) - the
                objective bank record
        raise:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(objective_bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ObjectiveBankForm(abc_learning_objects.ObjectiveBankForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating objective banks.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveBankAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'learning.ObjectiveBank'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='OBJECTIVE_BANK', **kwargs)
        self._mdata = default_mdata.get_objective_bank_mdata()
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
    def get_objective_bank_form_record(self, objective_bank_record_type):
        """Gets the ``ObjectiveBankFormRecord`` corresponding to the given objective bank record ``Type``.

        arg:    objective_bank_record_type (osid.type.Type): an
                objective bank record type
        return: (osid.learning.records.ObjectiveBankFormRecord) - the
                objective bank form record
        raise:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(objective_bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ObjectiveBankList(abc_learning_objects.ObjectiveBankList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveBankList`` provides a means for accessing ``ObjectiveBank`` elements sequentially either one at a time or many at a time.

    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }

    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }

    """

    def get_next_objective_bank(self):
        """Gets the next ``ObjectiveBank`` in this list.

        return: (osid.learning.ObjectiveBank) - the next
                ``ObjectiveBank`` in this list. The ``has_next()``
                method should be used to test that a next
                ``ObjectiveBank`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(ObjectiveBank)

    __next__ = next

    next_objective_bank = property(fget=get_next_objective_bank)

    @utilities.arguments_not_none
    def get_next_objective_banks(self, n):
        """Gets the next set of ``ObjectiveBank`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``ObjectiveBank`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.learning.ObjectiveBank) - an array of
                ``ObjectiveBank`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ObjectiveBankList, number=n)


class ObjectiveBankNode(abc_learning_objects.ObjectiveBankNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveBankHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_objective_bank().get_object_map())
        node_map['type'] = 'ObjectiveBankNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for objective_bank_node in self.get_parent_objective_bank_nodes():
            node_map['parentNodes'].append(objective_bank_node.get_object_node_map())
        for objective_bank_node in self.get_child_objective_bank_nodes():
            node_map['childNodes'].append(objective_bank_node.get_object_node_map())
        return node_map

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` at this node.

        return: (osid.learning.ObjectiveBank) - the objective bank
                represented by this node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('LEARNING', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_objective_bank_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_objective_bank(Id(self._my_map['id']))

    objective_bank = property(fget=get_objective_bank)

    def get_parent_objective_bank_nodes(self):
        """Gets the parents of this objective bank.

        return: (osid.learning.ObjectiveBankNodeList) - the parents of
                the ``id``
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_objective_bank_nodes = []
        for node in self._my_map['parentNodes']:
            parent_objective_bank_nodes.append(ObjectiveBankNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return ObjectiveBankNodeList(parent_objective_bank_nodes)

    parent_objective_bank_nodes = property(fget=get_parent_objective_bank_nodes)

    def get_child_objective_bank_nodes(self):
        """Gets the children of this objective bank.

        return: (osid.learning.ObjectiveBankNodeList) - the children of
                this objective bank
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_objective_bank_nodes = []
        for node in self._my_map['childNodes']:
            parent_objective_bank_nodes.append(ObjectiveBankNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return ObjectiveBankNodeList(parent_objective_bank_nodes)

    child_objective_bank_nodes = property(fget=get_child_objective_bank_nodes)


class ObjectiveBankNodeList(abc_learning_objects.ObjectiveBankNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveBankNodeList`` provides a means for accessing ``ObjectiveBankNode`` elements sequentially either one at a time or many at a time.

    Examples: while (obnl.hasNext()) { ObjectiveBankNode node bank =
    obnl.getNextObjectiveBankNode(); }

    or
      while (obnl.hasNext()) {
           ObjectiveBankNode[] nodes = obnl.getNextObjectiveBankNodes(obnl.available());
      }

    """

    def get_next_objective_bank_node(self):
        """Gets the next ``ObjectiveBankNode`` in this list.

        return: (osid.learning.ObjectiveBankNode) - the next
                ``ObjectiveBankNode`` in this list. The ``has_next()``
                method should be used to test that a next
                ``ObjectiveBankNode`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(ObjectiveBankNode)

    __next__ = next

    next_objective_bank_node = property(fget=get_next_objective_bank_node)

    @utilities.arguments_not_none
    def get_next_objective_bank_nodes(self, n):
        """Gets the next set of ``ObjectiveBankNode`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``ObjectiveBankNode``
                elements requested which must be less than or equal to
                ``available()``
        return: (osid.learning.ObjectiveBankNode) - an array of
                ``ObjectiveBankNode`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(ObjectiveBankNodeList, number=n)
