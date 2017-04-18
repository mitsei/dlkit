"""Implementations of grading abstract base class search_orders."""
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


class GradeSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_grade_system(self, style):
        """Specified a preference for ordering results by the grade system.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grade_system_search_order(self):
        """Tests if a ``GradeSystemSearchOrder`` interface is available for grade systems.

        :return: ``true`` if a grade system search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_search_order(self):
        """Gets the search order for a grade system.

        :return: the grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchOrder

    grade_system_search_order = property(fget=get_grade_system_search_order)

    @abc.abstractmethod
    def order_by_input_score_start_range(self, style):
        """Specified a preference for ordering results by start of the input score range.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_input_score_end_range(self, style):
        """Specified a preference for ordering results by end of the input score range.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_output_score(self, style):
        """Specified a preference for ordering results by the output score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_grade_search_order_record(self, grade_record_type):
        """Gets the grade search order record corresponding to the given grade record ``Type``.

        Multiple retrievals return the same underlying object.

        :param grade_record_type: a grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade search order record
        :rtype: ``osid.grading.records.GradeSearchOrderRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSearchOrderRecord


class GradeSystemSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_based_on_grades(self, style):
        """Orders the results by systems based on grades.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_lowest_numeric_score(self, style):
        """Orders the results by lowest score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_numeric_score_increment(self, style):
        """Orders the results by score increment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_highest_numeric_score(self, style):
        """Orders the results by highest score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_grade_system_search_order_record(self, grade_system_record_type):
        """Gets the grade system search order record corresponding to the given grade entry record ``Type``.

        Multiple retrievals return the same underlying object.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system search order record
        :rtype: ``osid.grading.records.GradeSystemSearchOrderRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemSearchOrderRecord


class GradeEntrySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_gradebook_column(self, style):
        """Specified a preference for ordering results by the gradebook column.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_gradebook_column_search_order(self):
        """Tests if a ``GradebookColumnSearchOrder`` is available.

        :return: ``true`` if a gradebook column search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_search_order(self):
        """Gets the search order for a gradebook column.

        :return: the gradebook column search order
        :rtype: ``osid.grading.GradebookColumnSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSearchOrder

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    @abc.abstractmethod
    def order_by_key_resource(self, style):
        """Specified a preference for ordering results by the key resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_key_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a key resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_key_resource_search_order(self):
        """Gets the search order for a resource.

        :return: the key resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_key_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_key_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    key_resource_search_order = property(fget=get_key_resource_search_order)

    @abc.abstractmethod
    def order_by_derived(self, style):
        """Specified a preference for ordering results by the derived entries.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_ignored_for_calculations(self, style):
        """Specified a preference for ordering results by the ignore for calculations flag.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_grade(self, style):
        """Specified a preference for ordering results by the grade or score.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grade_search_order(self):
        """Tests if a ``GradeSearchOrder`` is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_search_order(self):
        """Gets the search order for a grade.

        :return: the grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grade_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSearchOrder

    grade_search_order = property(fget=get_grade_search_order)

    @abc.abstractmethod
    def order_by_time_graded(self, style):
        """Specified a preference for ordering results by the time graded.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_grader(self, style):
        """Specified a preference for ordering results by the grader.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grader_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available for grader resources.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grader_search_order(self):
        """Gets the search order for a grader.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grader_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grader_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    grader_search_order = property(fget=get_grader_search_order)

    @abc.abstractmethod
    def order_by_grading_agent(self, style):
        """Specified a preference for ordering results by the grading agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grading_agent_search_order(self):
        """Tests if an ``AgentSearchOrder`` is available fo grading agents.

        :return: ``true`` if an agent search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grading_agent_search_order(self):
        """Gets the search order for a grading agent.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grading_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    grading_agent_search_order = property(fget=get_grading_agent_search_order)

    @abc.abstractmethod
    def get_grade_entry_search_order_record(self, grade_entry_record_type):
        """Gets the grade entry search order record corresponding to the given grade entry record ``Type``.

        Multiple retrievals return the same underlying object.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the grade entry search order record
        :rtype: ``osid.grading.records.GradeEntrySearchOrderRecord``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntrySearchOrderRecord


class GradebookColumnSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_grade_system(self, style):
        """Specified a preference for ordering results by the grade system.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_grade_system_search_order(self):
        """Tests if a ``GradeSystemSearchOrder`` is available for grade systems.

        :return: ``true`` if a grade system search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_summary_search_order(self):
        """Gets the search order for a grade system.

        :return: the grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemSearchOrder

    gradebook_column_summary_search_order = property(fget=get_gradebook_column_summary_search_order)

    @abc.abstractmethod
    def supports_gradebook_column_summary_search_order(self):
        """Tests if a ``GradebookColumnSummarySearchOrder`` is available for gradebook column summaries.

        :return: ``true`` if a gradebook column summary search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_search_order(self):
        """Gets the search order for a gradebook column summary search order.

        :return: the gradebook column summary search order
        :rtype: ``osid.grading.GradebookColumnSummarySearchOrder``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_summary_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_summary_search_order()`` is
        ``true``.*

        """
        return  # osid.grading.GradebookColumnSummarySearchOrder

    grade_system_search_order = property(fget=get_grade_system_search_order)

    @abc.abstractmethod
    def get_gradebook_column_search_order_record(self, gradebook_column_record_type):
        """Gets the gradebook column search order record corresponding to the given gradebook column record ``Type``.

        Multiple retrievals return the same underlying object.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the gradebook column search order record
        :rtype: ``osid.grading.records.GradebookColumnSearchOrderRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSearchOrderRecord


class GradebookColumnSummarySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_mean(self, style):
        """Specified a preference for ordering results by the mean.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_median(self, style):
        """Specified a preference for ordering results by the median.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_mode(self, style):
        """Specified a preference for ordering results by the mode.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_rms(self, style):
        """Specified a preference for ordering results by the root mean square.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_standard_deviation(self, style):
        """Specified a preference for ordering results by the standard deviation.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_sum(self, style):
        """Specified a preference for ordering results by the sum.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_gradebook_column_summary_search_order_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary search order record corresponding to the given gradebook column summary record ``Type``.

        Multiple retrievals return the same underlying object.

        :param gradebook_column_summary_record_type: a gradebook column summary record type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: the gradebook column summary search order record
        :rtype: ``osid.grading.records.GradebookColumnSummarySearchOrderRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_summary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_summary_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSummarySearchOrderRecord


class GradebookSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_search_order_record(self, gradebook_record_type):
        """Gets the gradebook search order record corresponding to the given gradebook record ``Type``.

        Multiple retrievals return the same underlying object.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook search order record
        :rtype: ``osid.grading.records.GradebookSearchOrderRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookSearchOrderRecord
