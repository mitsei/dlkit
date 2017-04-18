"""Implementations of learning abstract base class query_inspectors."""
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


class ObjectiveQueryInspector:
    """This is the query inspector for examining objective queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the asset ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    @abc.abstractmethod
    def get_assessment_terms(self):
        """Gets the asset query terms.

        :return: the asset terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    @abc.abstractmethod
    def get_knowledge_category_id_terms(self):
        """Gets the knowledge category ``Id`` query terms.

        :return: the knowledge category ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    knowledge_category_id_terms = property(fget=get_knowledge_category_id_terms)

    @abc.abstractmethod
    def get_knowledge_category_terms(self):
        """Gets the knowledge category query terms.

        :return: the knowledge category terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    knowledge_category_terms = property(fget=get_knowledge_category_terms)

    @abc.abstractmethod
    def get_cognitive_process_id_terms(self):
        """Gets the cognitive process ``Id`` query terms.

        :return: the cognitive process ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    cognitive_process_id_terms = property(fget=get_cognitive_process_id_terms)

    @abc.abstractmethod
    def get_cognitive_process_terms(self):
        """Gets the cognitive process query terms.

        :return: the cognitive process terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    cognitive_process_terms = property(fget=get_cognitive_process_terms)

    @abc.abstractmethod
    def get_requisite_objective_id_terms(self):
        """Gets the requisite objective ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    requisite_objective_id_terms = property(fget=get_requisite_objective_id_terms)

    @abc.abstractmethod
    def get_requisite_objective_terms(self):
        """Gets the requisite objective query terms.

        :return: the query terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    requisite_objective_terms = property(fget=get_requisite_objective_terms)

    @abc.abstractmethod
    def get_dependent_objective_id_terms(self):
        """Gets the requisite objective ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    dependent_objective_id_terms = property(fget=get_dependent_objective_id_terms)

    @abc.abstractmethod
    def get_dependent_objective_terms(self):
        """Gets the requisite objective query terms.

        :return: the query terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    dependent_objective_terms = property(fget=get_dependent_objective_terms)

    @abc.abstractmethod
    def get_equivalent_objective_id_terms(self):
        """Gets the equivalent objective ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    equivalent_objective_id_terms = property(fget=get_equivalent_objective_id_terms)

    @abc.abstractmethod
    def get_equivalent_objective_terms(self):
        """Gets the equivalent objective query terms.

        :return: the query terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    equivalent_objective_terms = property(fget=get_equivalent_objective_terms)

    @abc.abstractmethod
    def get_ancestor_objective_id_terms(self):
        """Gets the ancestor objective ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_objective_id_terms = property(fget=get_ancestor_objective_id_terms)

    @abc.abstractmethod
    def get_ancestor_objective_terms(self):
        """Gets the ancestor objective query terms.

        :return: the query terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    ancestor_objective_terms = property(fget=get_ancestor_objective_terms)

    @abc.abstractmethod
    def get_descendant_objective_id_terms(self):
        """Gets the descendant objective ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_objective_id_terms = property(fget=get_descendant_objective_id_terms)

    @abc.abstractmethod
    def get_descendant_objective_terms(self):
        """Gets the descendant objective query terms.

        :return: the query terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    descendant_objective_terms = property(fget=get_descendant_objective_terms)

    @abc.abstractmethod
    def get_activity_id_terms(self):
        """Gets the activity ``Id`` query terms.

        :return: the activity ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    activity_id_terms = property(fget=get_activity_id_terms)

    @abc.abstractmethod
    def get_activity_terms(self):
        """Gets the activity query terms.

        :return: the activity terms
        :rtype: ``osid.learning.ActivityQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQueryInspector

    activity_terms = property(fget=get_activity_terms)

    @abc.abstractmethod
    def get_objective_bank_id_terms(self):
        """Gets the objective bank ``Id`` query terms.

        :return: the objective bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_bank_id_terms = property(fget=get_objective_bank_id_terms)

    @abc.abstractmethod
    def get_objective_bank_terms(self):
        """Gets the objective bank query terms.

        :return: the objective bank terms
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    objective_bank_terms = property(fget=get_objective_bank_terms)

    @abc.abstractmethod
    def get_objective_query_inspector_record(self, objective_record_type):
        """Gets the objective query inspector record corresponding to the given ``Objective`` record ``Type``.

        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective query inspector record
        :rtype: ``osid.learning.records.ObjectiveQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveQueryInspectorRecord


class ActivityQueryInspector:
    """This is the query inspector for examining activity queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_id_terms(self):
        """Gets the objective ``Id`` query terms.

        :return: the objective ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_id_terms = property(fget=get_objective_id_terms)

    @abc.abstractmethod
    def get_objective_terms(self):
        """Gets the objective query terms.

        :return: the objective terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    objective_terms = property(fget=get_objective_terms)

    @abc.abstractmethod
    def get_asset_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the asset ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    asset_id_terms = property(fget=get_asset_id_terms)

    @abc.abstractmethod
    def get_asset_terms(self):
        """Gets the asset query terms.

        :return: the asset terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    asset_terms = property(fget=get_asset_terms)

    @abc.abstractmethod
    def get_course_id_terms(self):
        """Gets the course ``Id`` query terms.

        :return: the course ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    course_id_terms = property(fget=get_course_id_terms)

    @abc.abstractmethod
    def get_course_terms(self):
        """Gets the course query terms.

        :return: the course terms
        :rtype: ``osid.course.CourseQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.course.CourseQueryInspector

    course_terms = property(fget=get_course_terms)

    @abc.abstractmethod
    def get_assessment_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    @abc.abstractmethod
    def get_assessment_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    @abc.abstractmethod
    def get_objective_bank_id_terms(self):
        """Gets the objective bank ``Id`` query terms.

        :return: the objective bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_bank_id_terms = property(fget=get_objective_bank_id_terms)

    @abc.abstractmethod
    def get_objective_bank_terms(self):
        """Gets the objective bank query terms.

        :return: the objective bank terms
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    objective_bank_terms = property(fget=get_objective_bank_terms)

    @abc.abstractmethod
    def get_activity_query_inspector_record(self, activity_record_type):
        """Gets the activity query inspector record corresponding to the given ``Activity`` record ``Type``.

        :param activity_record_type: an activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the activity query inspector record
        :rtype: ``osid.learning.records.ActivityQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivityQueryInspectorRecord


class ProficiencyQueryInspector:
    """This is the query inspector for examining proficiency queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_id_terms(self):
        """Gets the resource ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    @abc.abstractmethod
    def get_resource_terms(self):
        """Gets the resource terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    @abc.abstractmethod
    def get_objective_id_terms(self):
        """Gets the objective ``Id`` terms.

        :return: the objective ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_id_terms = property(fget=get_objective_id_terms)

    @abc.abstractmethod
    def get_objective_terms(self):
        """Gets the objective terms.

        :return: the objective terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    objective_terms = property(fget=get_objective_terms)

    @abc.abstractmethod
    def get_completion_terms(self):
        """Gets the completion terms.

        :return: the completion terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    completion_terms = property(fget=get_completion_terms)

    @abc.abstractmethod
    def get_minimum_completion_terms(self):
        """Gets the minimum completion terms.

        :return: the minimum completion terms
        :rtype: ``osid.search.terms.DecimalTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalTerm

    minimum_completion_terms = property(fget=get_minimum_completion_terms)

    @abc.abstractmethod
    def get_level_id_terms(self):
        """Gets the level ``Id`` query terms.

        :return: the level ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    level_id_terms = property(fget=get_level_id_terms)

    @abc.abstractmethod
    def get_level_terms(self):
        """Gets the level query terms.

        :return: the level terms
        :rtype: ``osid.grading.GradeQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeQueryInspector

    level_terms = property(fget=get_level_terms)

    @abc.abstractmethod
    def get_objective_bank_id_terms(self):
        """Gets the objective bank ``Id`` query terms.

        :return: the objective bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_bank_id_terms = property(fget=get_objective_bank_id_terms)

    @abc.abstractmethod
    def get_objective_bank_terms(self):
        """Gets the objective bank query terms.

        :return: the objective bank terms
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    objective_bank_terms = property(fget=get_objective_bank_terms)

    @abc.abstractmethod
    def get_proficiency_query_inspector_record(self, proficiency_record_type):
        """Gets the proficiency query inspector record corresponding to the given ``Proficiency`` record ``Type``.

        :param proficiency_record_type: a proficiency record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: the proficiency query inspector record
        :rtype: ``osid.learning.records.ProficiencyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencyQueryInspectorRecord


class ObjectiveBankQueryInspector:
    """This is the query inspector for examining objective bank queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_id_terms(self):
        """Gets the objective ``Id`` query terms.

        :return: the objective ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    objective_id_terms = property(fget=get_objective_id_terms)

    @abc.abstractmethod
    def get_objective_terms(self):
        """Gets the objective query terms.

        :return: the objective terms
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    objective_terms = property(fget=get_objective_terms)

    @abc.abstractmethod
    def get_activity_id_terms(self):
        """Gets the activity ``Id`` query terms.

        :return: the activity ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    activity_id_terms = property(fget=get_activity_id_terms)

    @abc.abstractmethod
    def get_activity_terms(self):
        """Gets the activity query terms.

        :return: the activity terms
        :rtype: ``osid.learning.ActivityQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQueryInspector

    activity_terms = property(fget=get_activity_terms)

    @abc.abstractmethod
    def get_ancestor_objective_bank_id_terms(self):
        """Gets the ancestor objective bank ``Id`` query terms.

        :return: the ancestor objective bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_objective_bank_id_terms = property(fget=get_ancestor_objective_bank_id_terms)

    @abc.abstractmethod
    def get_ancestor_objective_bank_terms(self):
        """Gets the ancestor objective bank query terms.

        :return: the ancestor objective bank terms
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    ancestor_objective_bank_terms = property(fget=get_ancestor_objective_bank_terms)

    @abc.abstractmethod
    def get_descendant_objective_bank_id_terms(self):
        """Gets the descendant objective bank ``Id`` query terms.

        :return: the descendant objective bank ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_objective_bank_id_terms = property(fget=get_descendant_objective_bank_id_terms)

    @abc.abstractmethod
    def get_descendant_objective_bank_terms(self):
        """Gets the descendant objective bank query terms.

        :return: the descendant objective bank terms
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    descendant_objective_bank_terms = property(fget=get_descendant_objective_bank_terms)

    @abc.abstractmethod
    def get_objective_bank_query_inspector_record(self, objective_bank_record_type):
        """Gets the objective bank query inspector record corresponding to the given ``ObjectiveBank`` record ``Type``.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank query inspector record
        :rtype: ``osid.learning.records.ObjectiveBankQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankQueryInspectorRecord
