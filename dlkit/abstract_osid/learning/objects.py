"""Implementations of learning abstract base class objects."""
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


class Objective:
    """An ``Objective`` is a statable learning objective."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def has_assessment(self):
        """Tests if an assessment is associated with this objective.

        :return: ``true`` if an assessment exists, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_id(self):
        """Gets the assessment ``Id`` associated with this learning objective.

        :return: the assessment ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    assessment_id = property(fget=get_assessment_id)

    @abc.abstractmethod
    def get_assessment(self):
        """Gets the assessment associated with this learning objective.

        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- ``has_assessment()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Assessment

    assessment = property(fget=get_assessment)

    @abc.abstractmethod
    def has_knowledge_category(self):
        """Tests if this objective has a knowledge dimension.

        :return: ``true`` if a knowledge category exists, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_knowledge_category_id(self):
        """Gets the grade ``Id`` associated with the knowledge dimension.

        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_knowledge_category()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    knowledge_category_id = property(fget=get_knowledge_category_id)

    @abc.abstractmethod
    def get_knowledge_category(self):
        """Gets the grade associated with the knowledge dimension.

        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_knowledge_category()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    knowledge_category = property(fget=get_knowledge_category)

    @abc.abstractmethod
    def has_cognitive_process(self):
        """Tests if this objective has a cognitive process type.

        :return: ``true`` if a cognitive process exists, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_cognitive_process_id(self):
        """Gets the grade ``Id`` associated with the cognitive process.

        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_cognitive_process()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    cognitive_process_id = property(fget=get_cognitive_process_id)

    @abc.abstractmethod
    def get_cognitive_process(self):
        """Gets the grade associated with the cognitive process.

        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_cognitive_process()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    cognitive_process = property(fget=get_cognitive_process)

    @abc.abstractmethod
    def get_objective_record(self, objective_record_type):
        """Gets the objective bank record corresponding to the given ``Objective`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``objective_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_record_type)`` is ``true`` .

        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective record
        :rtype: ``osid.learning.records.ObjectiveRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveRecord


class ObjectiveForm:
    """This is the form for creating and updating ``Objectives``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_metadata(self):
        """Gets the metadata for an assessment.

        :return: metadata for the assessment
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    assessment_metadata = property(fget=get_assessment_metadata)

    @abc.abstractmethod
    def set_assessment(self, assessment_id):
        """Sets the assessment.

        :param assessment_id: the new assessment
        :type assessment_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``assessment_id`` is invalid
        :raise: ``NoAccess`` -- ``assessment_id`` cannot be modified
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment(self):
        """Clears the assessment.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment = property(fset=set_assessment, fdel=clear_assessment)

    @abc.abstractmethod
    def get_knowledge_category_metadata(self):
        """Gets the metadata for a knowledge category.

        :return: metadata for the knowledge category
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    knowledge_category_metadata = property(fget=get_knowledge_category_metadata)

    @abc.abstractmethod
    def set_knowledge_category(self, grade_id):
        """Sets the knowledge category.

        :param grade_id: the new knowledge category
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``grade_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_knowledge_category(self):
        """Clears the knowledge category.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    knowledge_category = property(fset=set_knowledge_category, fdel=clear_knowledge_category)

    @abc.abstractmethod
    def get_cognitive_process_metadata(self):
        """Gets the metadata for a cognitive process.

        :return: metadata for the cognitive process
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    cognitive_process_metadata = property(fget=get_cognitive_process_metadata)

    @abc.abstractmethod
    def set_cognitive_process(self, grade_id):
        """Sets the cognitive process.

        :param grade_id: the new cognitive process
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``grade_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cognitive_process(self):
        """Clears the cognitive process.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cognitive_process = property(fset=set_cognitive_process, fdel=clear_cognitive_process)

    @abc.abstractmethod
    def get_objective_form_record(self, objective_record_type):
        """Gets the ``ObjectiveFormRecord`` corresponding to the given objective record ``Type``.

        :param objective_record_type: the objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective form record
        :rtype: ``osid.learning.records.ObjectiveFormRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveFormRecord


class ObjectiveList:
    """Like all ``OsidLists,``  ``ObjectiveList`` provides a means for accessing ``Objective`` elements sequentially either one at a time or many at a time.

    Examples: while (ol.hasNext()) { Objective objective =
    ol.getNextObjective(); }

    or
      while (ol.hasNext()) {
           Objective[] objectives = ol.getNextObjectives(ol.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_objective(self):
        """Gets the next ``Objective`` in this list.

        :return: the next ``Objective`` in this list. The ``has_next()`` method should be used to test that a next ``Objective`` is available before calling this method.
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective

    next_objective = property(fget=get_next_objective)

    @abc.abstractmethod
    def get_next_objectives(self, n):
        """Gets the next set of ``Objective`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Objective`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Objective`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective


class ObjectiveNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective(self):
        """Gets the ``Objective`` at this node.

        :return: the objective represented by this node
        :rtype: ``osid.learning.Objective``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective

    objective = property(fget=get_objective)

    @abc.abstractmethod
    def get_parent_objective_nodes(self):
        """Gets the parents of this objective.

        :return: the parents of the ``id``
        :rtype: ``osid.learning.ObjectiveNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveNodeList

    parent_objective_nodes = property(fget=get_parent_objective_nodes)

    @abc.abstractmethod
    def get_child_objective_nodes(self):
        """Gets the children of this objective.

        :return: the children of this objective
        :rtype: ``osid.learning.ObjectiveNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveNodeList

    child_objective_nodes = property(fget=get_child_objective_nodes)


class ObjectiveNodeList:
    """Like all ``OsidLists,``  ``ObjectiveNodeList`` provides a means for accessing ``ObjectiveNode`` elements sequentially either one at a time or many at a time.

    Examples: while (onl.hasNext()) { ObjectiveNode node =
    onl.getNextObjectiveNode(); }

    or
      while (onl.hasNext()) {
           ObjectiveNode[] nodes = onl.getNextObjectiveNodes(onl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_objective_node(self):
        """Gets the next ``ObjectiveNode`` in this list.

        :return: the next ``ObjectiveNode`` in this list. The ``has_next()`` method should be used to test that a next ``ObjectiveNode`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveNode

    next_objective_node = property(fget=get_next_objective_node)

    @abc.abstractmethod
    def get_next_objective_nodes(self, n):
        """Gets the next set of ``ObjectiveNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``ObjectiveNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveNode


class Activity:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_id(self):
        """Gets the ``Id`` of the related objective.

        :return: the objective ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_id = property(fget=get_objective_id)

    @abc.abstractmethod
    def get_objective(self):
        """Gets the related objective.

        :return: the related objective
        :rtype: ``osid.learning.Objective``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective

    objective = property(fget=get_objective)

    @abc.abstractmethod
    def is_asset_based_activity(self):
        """Tests if this is an asset based activity.

        :return: ``true`` if this activity is based on assets, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_ids(self):
        """Gets the ``Ids`` of any assets associated with this activity.

        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_asset_based_activity()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    asset_ids = property(fget=get_asset_ids)

    @abc.abstractmethod
    def get_assets(self):
        """Gets any assets associated with this activity.

        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``IllegalState`` -- ``is_asset_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetList

    assets = property(fget=get_assets)

    @abc.abstractmethod
    def is_course_based_activity(self):
        """Tests if this is a course based activity.

        :return: ``true`` if this activity is based on courses, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_course_ids(self):
        """Gets the ``Ids`` of any courses associated with this activity.

        :return: list of course ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_course_based_activity()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    course_ids = property(fget=get_course_ids)

    @abc.abstractmethod
    def get_courses(self):
        """Gets any courses associated with this activity.

        :return: list of courses
        :rtype: ``osid.course.CourseList``
        :raise: ``IllegalState`` -- ``is_course_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.course.CourseList

    courses = property(fget=get_courses)

    @abc.abstractmethod
    def is_assessment_based_activity(self):
        """Tests if this is an assessment based activity.

        These assessments are for learning the objective and not for
        assessing prodiciency in the objective.

        :return: ``true`` if this activity is based on assessments, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_ids(self):
        """Gets the ``Ids`` of any assessments associated with this activity.

        :return: list of assessment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_assessment_based_activity()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    assessment_ids = property(fget=get_assessment_ids)

    @abc.abstractmethod
    def get_assessments(self):
        """Gets any assessments associated with this activity.

        :return: list of assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``IllegalState`` -- ``is_assessment_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    assessments = property(fget=get_assessments)

    @abc.abstractmethod
    def get_activity_record(self, activity_record_type):
        """Gets the activity record corresponding to the given ``Activity`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``activity_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(activity_record_type)`` is ``true`` .

        :param activity_record_type: the type of the record to retrieve
        :type activity_record_type: ``osid.type.Type``
        :return: the activity record
        :rtype: ``osid.learning.records.ActivityRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivityRecord


class ActivityForm:
    """This is the form for creating and updating ``Activities``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ActivityAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assets_metadata(self):
        """Gets the metadata for the assets.

        :return: metadata for the assets
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    assets_metadata = property(fget=get_assets_metadata)

    @abc.abstractmethod
    def set_assets(self, asset_ids):
        """Sets the assets.

        :param asset_ids: the asset ``Ids``
        :type asset_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``asset_ids`` is invalid
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assets(self):
        """Clears the assets.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assets = property(fset=set_assets, fdel=clear_assets)

    @abc.abstractmethod
    def get_courses_metadata(self):
        """Gets the metadata for the courses.

        :return: metadata for the courses
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    courses_metadata = property(fget=get_courses_metadata)

    @abc.abstractmethod
    def set_courses(self, course_ids):
        """Sets the courses.

        :param course_ids: the course ``Ids``
        :type course_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``course_ids`` is invalid
        :raise: ``NullArgument`` -- ``course_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_courses(self):
        """Clears the courses.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    courses = property(fset=set_courses, fdel=clear_courses)

    @abc.abstractmethod
    def get_assessments_metadata(self):
        """Gets the metadata for the assessments.

        :return: metadata for the assessments
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    assessments_metadata = property(fget=get_assessments_metadata)

    @abc.abstractmethod
    def set_assessments(self, assessment_ids):
        """Sets the assessments.

        :param assessment_ids: the assessment ``Ids``
        :type assessment_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``assessment_ids`` is invalid
        :raise: ``NullArgument`` -- ``assessment_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessments(self):
        """Clears the assessments.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessments = property(fset=set_assessments, fdel=clear_assessments)

    @abc.abstractmethod
    def get_activity_form_record(self, activity_record_type):
        """Gets the ``ActivityFormRecord`` corresponding to the given activity record ``Type``.

        :param activity_record_type: the activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the activity form record
        :rtype: ``osid.learning.records.ActivityFormRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivityFormRecord


class ActivityList:
    """Like all ``OsidLists,``  ``ActivityList`` provides a means for accessing ``Activity`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Activity activity =
    al.getNextActivity(); }

    or
      while (al.hasNext()) {
           Activity[] activities = al.getNextActivities(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_activity(self):
        """Gets the next ``Activity`` in this list.

        :return: the next ``Activity`` in this list. The ``has_next()`` method should be used to test that a next ``Activity`` is available before calling this method.
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Activity

    next_activity = property(fget=get_next_activity)

    @abc.abstractmethod
    def get_next_activities(self, n):
        """Gets the next set of ``Activity`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Activity`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Activity`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Activity


class Proficiency:
    """A ``Proficiency`` represents a competency of a leraning objective."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_id(self):
        """Gets the resource ``Id`` to whom this proficiency applies.

        :return: the resource ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    resource_id = property(fget=get_resource_id)

    @abc.abstractmethod
    def get_resource(self):
        """Gets the resource to whom this proficiency applies.

        :return: the resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    resource = property(fget=get_resource)

    @abc.abstractmethod
    def get_objective_id(self):
        """Gets the objective ``Id`` to whom this proficiency applies.

        :return: the objective ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_id = property(fget=get_objective_id)

    @abc.abstractmethod
    def get_objective(self):
        """Gets the objective to whom this proficiency applies.

        :return: the objective
        :rtype: ``osid.learning.Objective``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective

    objective = property(fget=get_objective)

    @abc.abstractmethod
    def get_completion(self):
        """Gets the completion of this objective as a percentage 0-100.

        :return: the completion
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    completion = property(fget=get_completion)

    @abc.abstractmethod
    def has_level(self):
        """Tests if a proficiency level is available.

        :return: ``true`` if a level is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_id(self):
        """Gets the proficiency level expressed as a grade.

        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_level()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    level_id = property(fget=get_level_id)

    @abc.abstractmethod
    def get_level(self):
        """Gets the proficiency level expressed as a grade.

        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_level()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    level = property(fget=get_level)

    @abc.abstractmethod
    def get_proficiency_record(self, proficiency_record_type):
        """Gets the proficiency record corresponding to the given ``Proficiency`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proficiency_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(proficiency_record_type)`` is ``true`` .

        :param proficiency_record_type: the type of proficiency record to retrieve
        :type proficiency_record_type: ``osid.type.Type``
        :return: the proficiency record
        :rtype: ``osid.learning.records.ProficiencyRecord``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencyRecord


class ProficiencyForm:
    """This is the form for creating and updating ``Proficiencies``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ProficiencyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_completion_metadata(self):
        """Gets the metadata for completion percentage.

        :return: metadata for the completion percentage
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    completion_metadata = property(fget=get_completion_metadata)

    @abc.abstractmethod
    def set_completion(self, completion):
        """Sets the completion percentage.

        :param completion: the completion percentage
        :type completion: ``decimal``
        :raise: ``InvalidArgument`` -- ``completion`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_completion(self):
        """Clears the completion.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    completion = property(fset=set_completion, fdel=clear_completion)

    @abc.abstractmethod
    def get_level_metadata(self):
        """Gets the metadata for a level.

        :return: metadata for the grade level
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    level_metadata = property(fget=get_level_metadata)

    @abc.abstractmethod
    def set_level(self, grade):
        """Sets the level expressed as a ``Grade``.

        :param grade: the level
        :type grade: ``osid.grading.Grade``
        :raise: ``InvalidArgument`` -- ``grade`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``grade`` is ``null``

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
    def get_proficiency_form_record(self, proficiency_record_type):
        """Gets the ``ProficiencyFormRecord`` corresponding to the given proficiency record ``Type``.

        :param proficiency_record_type: a proficiency record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: the proficiency form record
        :rtype: ``osid.learning.records.ProficiencyFormRecord``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencyFormRecord


class ProficiencyList:
    """Like all ``OsidLists,``  ``ProficiencyList`` provides a means for accessing ``Proficiency`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Proficiency proficiency =
    pl.getNextProficiency(); }

    or
      while (pl.hasNext()) {
           Proficiency[] proficiencies = pl.getNextProficiencies(pl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_proficiency(self):
        """Gets the next ``Proficiency`` in this list.

        :return: the next ``Proficiency`` in this list. The ``has_next()`` method should be used to test that a next ``Proficiency`` is available before calling this method.
        :rtype: ``osid.learning.Proficiency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Proficiency

    next_proficiency = property(fget=get_next_proficiency)

    @abc.abstractmethod
    def get_next_proficiencies(self, n):
        """Gets the next set of ``Proficiency`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Proficiency`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Proficiency`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.Proficiency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Proficiency


class ObjectiveBank:
    """an objective bank defines a collection of objectives."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_record(self, objective_bank_record_type):
        """Gets the objective bank record corresponding to the given ``ObjectiveBank`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``objective_bank_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_bank_record_type)`` is ``true`` .

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank record
        :rtype: ``osid.learning.records.ObjectiveBankRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankRecord


class ObjectiveBankForm:
    """This is the form for creating and updating objective banks.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveBankAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_form_record(self, objective_bank_record_type):
        """Gets the ``ObjectiveBankFormRecord`` corresponding to the given objective bank record ``Type``.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank form record
        :rtype: ``osid.learning.records.ObjectiveBankFormRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankFormRecord


class ObjectiveBankList:
    """Like all ``OsidLists,``  ``ObjectiveBankList`` provides a means for accessing ``ObjectiveBank`` elements sequentially either one at a time or many at a time.

    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }

    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_objective_bank(self):
        """Gets the next ``ObjectiveBank`` in this list.

        :return: the next ``ObjectiveBank`` in this list. The ``has_next()`` method should be used to test that a next ``ObjectiveBank`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    next_objective_bank = property(fget=get_next_objective_bank)

    @abc.abstractmethod
    def get_next_objective_banks(self, n):
        """Gets the next set of ``ObjectiveBank`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``ObjectiveBank`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveBank`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank


class ObjectiveBankNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveBankHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` at this node.

        :return: the objective bank represented by this node
        :rtype: ``osid.learning.ObjectiveBank``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def get_parent_objective_bank_nodes(self):
        """Gets the parents of this objective bank.

        :return: the parents of the ``id``
        :rtype: ``osid.learning.ObjectiveBankNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankNodeList

    parent_objective_bank_nodes = property(fget=get_parent_objective_bank_nodes)

    @abc.abstractmethod
    def get_child_objective_bank_nodes(self):
        """Gets the children of this objective bank.

        :return: the children of this objective bank
        :rtype: ``osid.learning.ObjectiveBankNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankNodeList

    child_objective_bank_nodes = property(fget=get_child_objective_bank_nodes)


class ObjectiveBankNodeList:
    """Like all ``OsidLists,``  ``ObjectiveBankNodeList`` provides a means for accessing ``ObjectiveBankNode`` elements sequentially either one at a time or many at a time.

    Examples: while (obnl.hasNext()) { ObjectiveBankNode node bank =
    obnl.getNextObjectiveBankNode(); }

    or
      while (obnl.hasNext()) {
           ObjectiveBankNode[] nodes = obnl.getNextObjectiveBankNodes(obnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_objective_bank_node(self):
        """Gets the next ``ObjectiveBankNode`` in this list.

        :return: the next ``ObjectiveBankNode`` in this list. The ``has_next()`` method should be used to test that a next ``ObjectiveBankNode`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankNode

    next_objective_bank_node = property(fget=get_next_objective_bank_node)

    @abc.abstractmethod
    def get_next_objective_bank_nodes(self, n):
        """Gets the next set of ``ObjectiveBankNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``ObjectiveBankNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveBankNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankNode
