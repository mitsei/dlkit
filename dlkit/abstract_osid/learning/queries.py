"""Implementations of learning abstract base class queries."""
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


class ObjectiveQuery:
    """This is the query for searching objectives.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_id_terms(self):
        """Clears the assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available for querying activities.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def match_any_assessment(self, match):
        """Matches an objective that has any assessment assigned.

        :param match: ``true`` to match objectives with any assessment, ``false`` to match objectives with no assessment
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_terms(self):
        """Clears the assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    @abc.abstractmethod
    def match_knowledge_category_id(self, grade_id, match):
        """Sets the knowledge category ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_knowledge_category_id_terms(self):
        """Clears the knowledge category ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    knowledge_category_id_terms = property(fdel=clear_knowledge_category_id_terms)

    @abc.abstractmethod
    def supports_knowledge_category_query(self):
        """Tests if a ``GradeQuery`` is available for querying knowledge categories.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_knowledge_category_query(self):
        """Gets the query for a knowledge category.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_knowledge_category_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_knowledge_category_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    knowledge_category_query = property(fget=get_knowledge_category_query)

    @abc.abstractmethod
    def match_any_knowledge_category(self, match):
        """Matches an objective that has any knowledge category.

        :param match: ``true`` to match objectives with any knowledge category, ``false`` to match objectives with no knowledge category
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_knowledge_category_terms(self):
        """Clears the knowledge category terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    knowledge_category_terms = property(fdel=clear_knowledge_category_terms)

    @abc.abstractmethod
    def match_cognitive_process_id(self, grade_id, match):
        """Sets the cognitive process ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cognitive_process_id_terms(self):
        """Clears the cognitive process ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cognitive_process_id_terms = property(fdel=clear_cognitive_process_id_terms)

    @abc.abstractmethod
    def supports_cognitive_process_query(self):
        """Tests if a ``GradeQuery`` is available for querying cognitive processes.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_cognitive_process_query(self):
        """Gets the query for a cognitive process.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_cognitive_process_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_cognitive_process_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    cognitive_process_query = property(fget=get_cognitive_process_query)

    @abc.abstractmethod
    def match_any_cognitive_process(self, match):
        """Matches an objective that has any cognitive process.

        :param match: ``true`` to match objectives with any cognitive process, ``false`` to match objectives with no cognitive process
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cognitive_process_terms(self):
        """Clears the cognitive process terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cognitive_process_terms = property(fdel=clear_cognitive_process_terms)

    @abc.abstractmethod
    def match_activity_id(self, activity_id, match):
        """Sets the activity ``Id`` for this query.

        :param activity_id: an activity ``Id``
        :type activity_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_activity_id_terms(self):
        """Clears the activity ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    activity_id_terms = property(fdel=clear_activity_id_terms)

    @abc.abstractmethod
    def supports_activity_query(self):
        """Tests if an ``ActivityQuery`` is available for querying activities.

        :return: ``true`` if an activity query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_activity_query(self):
        """Gets the query for an activity.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        return  # osid.learning.ActivityQuery

    activity_query = property(fget=get_activity_query)

    @abc.abstractmethod
    def match_any_activity(self, match):
        """Matches an objective that has any related activity.

        :param match: ``true`` to match objectives with any activity, ``false`` to match objectives with no activity
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_activity_terms(self):
        """Clears the activity terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    activity_terms = property(fdel=clear_activity_terms)

    @abc.abstractmethod
    def match_requisite_objective_id(self, requisite_objective_id, match):
        """Sets the requisite objective ``Id`` for this query.

        :param requisite_objective_id: a requisite objective ``Id``
        :type requisite_objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``requisite_objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_requisite_objective_id_terms(self):
        """Clears the requisite objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    requisite_objective_id_terms = property(fdel=clear_requisite_objective_id_terms)

    @abc.abstractmethod
    def supports_requisite_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available for querying requisite objectives.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_requisite_objective_query(self):
        """Gets the query for a requisite objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_requisite_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_requisite_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    requisite_objective_query = property(fget=get_requisite_objective_query)

    @abc.abstractmethod
    def match_any_requisite_objective(self, match):
        """Matches an objective that has any related requisite.

        :param match: ``true`` to match objectives with any requisite, ``false`` to match objectives with no requisite
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_requisite_objective_terms(self):
        """Clears the requisite objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    requisite_objective_terms = property(fdel=clear_requisite_objective_terms)

    @abc.abstractmethod
    def match_dependent_objective_id(self, dependent_objective_id, match):
        """Sets the dependent objective ``Id`` to query objectives dependent on the given objective.

        :param dependent_objective_id: a dependent objective ``Id``
        :type dependent_objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``dependent_objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependent_objective_id_terms(self):
        """Clears the dependent objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependent_objective_id_terms = property(fdel=clear_dependent_objective_id_terms)

    @abc.abstractmethod
    def supports_depndent_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available for querying dependent objectives.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_dependent_objective_query(self):
        """Gets the query for a dependent objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_dependent_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_dependent_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    dependent_objective_query = property(fget=get_dependent_objective_query)

    @abc.abstractmethod
    def match_any_dependent_objective(self, match):
        """Matches an objective that has any related dependents.

        :param match: ``true`` to match objectives with any dependent, ``false`` to match objectives with no dependents
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_dependent_objective_terms(self):
        """Clears the dependent objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    dependent_objective_terms = property(fdel=clear_dependent_objective_terms)

    @abc.abstractmethod
    def match_equivalent_objective_id(self, equivalent_objective_id, match):
        """Sets the equivalent objective ``Id`` to query equivalents.

        :param equivalent_objective_id: an equivalent objective ``Id``
        :type equivalent_objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``equivalent_objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_equivalent_objective_id_terms(self):
        """Clears the equivalent objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    equivalent_objective_id_terms = property(fdel=clear_equivalent_objective_id_terms)

    @abc.abstractmethod
    def supports_equivalent_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available for querying equivalent objectives.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_equivalent_objective_query(self):
        """Gets the query for an equivalent objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_equivalent_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_equivalent_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    equivalent_objective_query = property(fget=get_equivalent_objective_query)

    @abc.abstractmethod
    def match_any_equivalent_objective(self, match):
        """Matches an objective that has any related equivalents.

        :param match: ``true`` to match objectives with any equivalent, ``false`` to match objectives with no equivalents
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_equivalent_objective_terms(self):
        """Clears the equivalent objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    equivalent_objective_terms = property(fdel=clear_equivalent_objective_terms)

    @abc.abstractmethod
    def match_ancestor_objective_id(self, objective_id, match):
        """Sets the objective ``Id`` for this query to match objectives that have the specified objective as an ancestor.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_objective_id_terms(self):
        """Clears the ancestor objective ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_objective_id_terms = property(fdel=clear_ancestor_objective_id_terms)

    @abc.abstractmethod
    def supports_ancestor_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_objective_query(self):
        """Gets the query for an objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    ancestor_objective_query = property(fget=get_ancestor_objective_query)

    @abc.abstractmethod
    def match_any_ancestor_objective(self, match):
        """Matches objectives that have any ancestor.

        :param match: ``true`` to match objective with any ancestor, ``false`` to match root objectives
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_objective_terms(self):
        """Clears the ancestor objective query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_objective_terms = property(fdel=clear_ancestor_objective_terms)

    @abc.abstractmethod
    def match_descendant_objective_id(self, objective_id, match):
        """Sets the objective ``Id`` for this query to match objectives that have the specified objective as a descendant.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_objective_id_terms(self):
        """Clears the descendant objective ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_objective_id_terms = property(fdel=clear_descendant_objective_id_terms)

    @abc.abstractmethod
    def supports_descendant_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_objective_query(self):
        """Gets the query for an objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    descendant_objective_query = property(fget=get_descendant_objective_query)

    @abc.abstractmethod
    def match_any_descendant_objective(self, match):
        """Matches objectives that have any ancestor.

        :param match: ``true`` to match objectives with any ancestor, ``false`` to match leaf objectives
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_objective_terms(self):
        """Clears the descendant objective query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_objective_terms = property(fdel=clear_descendant_objective_terms)

    @abc.abstractmethod
    def match_objective_bank_id(self, objective_bank_id, match):
        """Sets the objective bank ``Id`` for this query.

        :param objective_bank_id: an objective bank ``Id``
        :type objective_bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_bank_id_terms(self):
        """Clears the objective bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_id_terms = property(fdel=clear_objective_bank_id_terms)

    @abc.abstractmethod
    def supports_objective_bank_query(self):
        """Tests if a ``ObjectiveBankQuery`` is available for querying objective banks.

        :return: ``true`` if an objective bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_query(self):
        """Gets the query for an objective bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveBankQuery

    objective_bank_query = property(fget=get_objective_bank_query)

    @abc.abstractmethod
    def clear_objective_bank_terms(self):
        """Clears the objective bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_terms = property(fdel=clear_objective_bank_terms)

    @abc.abstractmethod
    def get_objective_query_record(self, objective_record_type):
        """Gets the objective query record corresponding to the given ``Objective`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param objective_record_type: an objective query record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective query record
        :rtype: ``osid.learning.records.ObjectiveQueryRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveQueryRecord


class ActivityQuery:
    """This is the query for searching activities.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_objective_id(self, objective_id, match):
        """Sets the objective ``Id`` for this query.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_id_terms(self):
        """Clears the objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_id_terms = property(fdel=clear_objective_id_terms)

    @abc.abstractmethod
    def supports_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available for querying objectives.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_query(self):
        """Gets the query for an objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    @abc.abstractmethod
    def clear_objective_terms(self):
        """Clears the objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_terms = property(fdel=clear_objective_terms)

    @abc.abstractmethod
    def match_asset_id(self, asset_id, match):
        """Sets the asset ``Id`` for this query.

        :param asset_id: an asset ``Id``
        :type asset_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_id_terms(self):
        """Clears the asset ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_id_terms = property(fdel=clear_asset_id_terms)

    @abc.abstractmethod
    def supports_asset_query(self):
        """Tests if an ``AssetQuery`` is available for querying objectives.

        :return: ``true`` if an robjective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_asset_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuery

    asset_query = property(fget=get_asset_query)

    @abc.abstractmethod
    def match_any_asset(self, match):
        """Matches an activity that has any objective assigned.

        :param match: ``true`` to match activities with any asset, ``false`` to match activities with no asset
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_asset_terms(self):
        """Clears the asset terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    asset_terms = property(fdel=clear_asset_terms)

    @abc.abstractmethod
    def match_course_id(self, course_id, match):
        """Sets the course ``Id`` for this query.

        :param course_id: a course ``Id``
        :type course_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``course_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_course_id_terms(self):
        """Clears the course ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    course_id_terms = property(fdel=clear_course_id_terms)

    @abc.abstractmethod
    def supports_course_query(self):
        """Tests if a ``CourseQuery`` is available for querying courses.

        :return: ``true`` if a course query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_course_query(self):
        """Gets the query for a course.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the course query
        :rtype: ``osid.course.CourseQuery``
        :raise: ``Unimplemented`` -- ``supports_course_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_course_query()`` is ``true``.*

        """
        return  # osid.course.CourseQuery

    course_query = property(fget=get_course_query)

    @abc.abstractmethod
    def match_any_course(self, match):
        """Matches an activity that has any course assigned.

        :param match: ``true`` to match activities with any courses, ``false`` to match activities with no courses
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_course_terms(self):
        """Clears the course terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    course_terms = property(fdel=clear_course_terms)

    @abc.abstractmethod
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_id_terms(self):
        """Clears the assessment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    @abc.abstractmethod
    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available for querying assessments.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_query(self):
        """Gets the query for a assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_query()`` is ``true``.*

        """
        return  # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    @abc.abstractmethod
    def match_any_assessment(self, match):
        """Matches an activity that has any assessment assigned.

        :param match: ``true`` to match activities with any assessments, ``false`` to match activities with no assessments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_assessment_terms(self):
        """Clears the assessment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    @abc.abstractmethod
    def match_objective_bank_id(self, objective_bank_id, match):
        """Sets the objective bank ``Id`` for this query.

        :param objective_bank_id: an objective bank ``Id``
        :type objective_bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_bank_id_terms(self):
        """Clears the objective bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_id_terms = property(fdel=clear_objective_bank_id_terms)

    @abc.abstractmethod
    def supports_objective_bank_query(self):
        """Tests if a ``ObjectiveBankQuery`` is available for querying resources.

        :return: ``true`` if an objective bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_query(self):
        """Gets the query for an objective bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveBankQuery

    objective_bank_query = property(fget=get_objective_bank_query)

    @abc.abstractmethod
    def clear_objective_bank_terms(self):
        """Clears the objective bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_terms = property(fdel=clear_objective_bank_terms)

    @abc.abstractmethod
    def get_activity_query_record(self, activity_record_type):
        """Gets the activity query record corresponding to the given ``Activity`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param activity_record_type: an activity query record type
        :type activity_record_type: ``osid.type.Type``
        :return: the activity query record
        :rtype: ``osid.learning.records.ActivityQueryRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivityQueryRecord


class ProficiencyQuery:
    """This is the query for searching proficiencies.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    @abc.abstractmethod
    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    @abc.abstractmethod
    def clear_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)

    @abc.abstractmethod
    def match_objective_id(self, objective_id, match):
        """Sets the objective ``Id`` for this query.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_id_terms(self):
        """Clears the objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_id_terms = property(fdel=clear_objective_id_terms)

    @abc.abstractmethod
    def supports_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available for querying objectives.

        :return: ``true`` if an robjective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_query(self):
        """Gets the query for an objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    @abc.abstractmethod
    def match_any_objective(self, match):
        """Matches an activity that has any objective assigned.

        :param match: ``true`` to match activities with any objective, ``false`` to match activities with no objective
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_terms(self):
        """Clears the objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_terms = property(fdel=clear_objective_terms)

    @abc.abstractmethod
    def match_completion(self, start, end, match):
        """Sets the completion for this query to match completion percentages between the given range inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_completion_terms(self):
        """Clears the completion terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    completion_terms = property(fdel=clear_completion_terms)

    @abc.abstractmethod
    def match_minimum_completion(self, completion, match):
        """Sets the minimum completion for this query.

        :param completion: completion percentage
        :type completion: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_completion_terms(self):
        """Clears the minimum completion terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_completion_terms = property(fdel=clear_minimum_completion_terms)

    @abc.abstractmethod
    def match_level_id(self, grade_id, match):
        """Sets the level grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_id_terms(self):
        """Clears all level ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_id_terms = property(fdel=clear_level_id_terms)

    @abc.abstractmethod
    def supports_level_query(self):
        """Tests if a ``GradeQuery`` is available.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_level_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_level_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    level_query = property(fget=get_level_query)

    @abc.abstractmethod
    def match_any_level(self, match):
        """Matches an assessment offered that has any level assigned.

        :param match: ``true`` to match offerings with any level, ``false`` to match offerings with no levsls
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_level_terms(self):
        """Clears all level terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level_terms = property(fdel=clear_level_terms)

    @abc.abstractmethod
    def match_objective_bank_id(self, objective_bank_id, match):
        """Sets the objective bank ``Id`` for this query.

        :param objective_bank_id: an objective bank ``Id``
        :type objective_bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_bank_id_terms(self):
        """Clears the objective bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_id_terms = property(fdel=clear_objective_bank_id_terms)

    @abc.abstractmethod
    def supports_objective_bank_query(self):
        """Tests if a ``ObjectiveBankQuery`` is available for querying resources.

        :return: ``true`` if an objective bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_query(self):
        """Gets the query for an objective bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveBankQuery

    objective_bank_query = property(fget=get_objective_bank_query)

    @abc.abstractmethod
    def clear_objective_bank_terms(self):
        """Clears the objective bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_bank_terms = property(fdel=clear_objective_bank_terms)

    @abc.abstractmethod
    def get_proficiency_query_record(self, proficiency_record_type):
        """Gets the proficiency query record corresponding to the given ``Proficiency`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param proficiency_record_type: a proficiency offered record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: the proficiency offered query record
        :rtype: ``osid.learning.records.ProficiencyQueryRecord``
        :raise: ``NullArgument`` -- ``proficiency_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_offered_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencyQueryRecord


class ObjectiveBankQuery:
    """This is the query for searching objective banks.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_objective_id(self, objective_id, match):
        """Sets the objective ``Id`` for this query.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_id_terms(self):
        """Clears the objective ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_id_terms = property(fdel=clear_objective_id_terms)

    @abc.abstractmethod
    def supports_objective_query(self):
        """Tests if an ``ObjectiveQuery`` is available.

        :return: ``true`` if an objective query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_query(self):
        """Gets the query for an objective.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    @abc.abstractmethod
    def match_any_objective(self, match):
        """Matches an objective bank that has any objective assigned.

        :param match: ``true`` to match objective banks with any objective, ``false`` to match objective banks with no objectives
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_objective_terms(self):
        """Clears the objective terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    objective_terms = property(fdel=clear_objective_terms)

    @abc.abstractmethod
    def match_activity_id(self, activity_id, match):
        """Sets the activity ``Id`` for this query.

        :param activity_id: an activity ``Id``
        :type activity_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_activity_id_terms(self):
        """Clears the activity ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    activity_id_terms = property(fdel=clear_activity_id_terms)

    @abc.abstractmethod
    def supports_activity_query(self):
        """Tests if a ``ActivityQuery`` is available for querying activities.

        :return: ``true`` if an activity query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_activity_query(self):
        """Gets the query for an activity.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        return  # osid.learning.ActivityQuery

    activity_query = property(fget=get_activity_query)

    @abc.abstractmethod
    def match_any_activity(self, match):
        """Matches an objective bank that has any activity assigned.

        :param match: ``true`` to match objective banks with any activity, ``false`` to match objective banks with no activities
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_activity_terms(self):
        """Clears the activity terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    activity_terms = property(fdel=clear_activity_terms)

    @abc.abstractmethod
    def match_ancestor_objective_bank_id(self, objective_bank_id, match):
        """Sets the objective bank ``Id`` for this query to match objective banks that have the specified objective bank as an ancestor.

        :param objective_bank_id: an objective bank ``Id``
        :type objective_bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_objective_bank_id_terms(self):
        """Clears the ancestor objective bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_objective_bank_id_terms = property(fdel=clear_ancestor_objective_bank_id_terms)

    @abc.abstractmethod
    def supports_ancestor_objective_bank_query(self):
        """Tests if a ``ObjectiveBankQuery`` is available for querying ancestor objective banks.

        :return: ``true`` if an objective bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_objective_bank_query(self):
        """Gets the query for an objective bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_objective_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_calndar_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveBankQuery

    ancestor_objective_bank_query = property(fget=get_ancestor_objective_bank_query)

    @abc.abstractmethod
    def match_any_ancestor_objective_bank(self, match):
        """Matches an objective bank that has any ancestor.

        :param match: ``true`` to match objective banks with any ancestor, ``false`` to match root objective banks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_objective_bank_terms(self):
        """Clears the ancestor objective bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_objective_bank_terms = property(fdel=clear_ancestor_objective_bank_terms)

    @abc.abstractmethod
    def match_descendant_objective_bank_id(self, objective_bank_id, match):
        """Sets the objective bank ``Id`` for this query to match objective banks that have the specified objective bank as a descendant.

        :param objective_bank_id: an objective bank ``Id``
        :type objective_bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_objective_bank_id_terms(self):
        """Clears the descendant objective bank ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_objective_bank_id_terms = property(fdel=clear_descendant_objective_bank_id_terms)

    @abc.abstractmethod
    def supports_descendant_objective_bank_query(self):
        """Tests if a ``ObjectiveBankQuery`` is available for querying descendant objective banks.

        :return: ``true`` if an objective bank query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_objective_bank_query(self):
        """Gets the query for an objective bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_objective_bank_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_calndar_query()`` is ``true``.*

        """
        return  # osid.learning.ObjectiveBankQuery

    descendant_objective_bank_query = property(fget=get_descendant_objective_bank_query)

    @abc.abstractmethod
    def match_any_descendant_objective_bank(self, match):
        """Matches an objective bank that has any descendant.

        :param match: ``true`` to match objective banks with any descendant, ``false`` to match leaf objective banks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_objective_bank_terms(self):
        """Clears the descendant objective bank terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_objective_bank_terms = property(fdel=clear_descendant_objective_bank_terms)

    @abc.abstractmethod
    def get_objective_bank_query_record(self, objective_bank_record_type):
        """Gets the objective bank query record corresponding to the given ``ObjectiveBank`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank query record
        :rtype: ``osid.learning.records.ObjectiveBankQueryRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankQueryRecord
