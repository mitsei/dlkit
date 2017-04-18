"""Implementations of grading abstract base class searches."""
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


class GradeSystemSearch:
    """The interface for governing grade system searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_grade_systems(self, grade_system_ids):
        """Execute this search among the given list of grade systems.

        :param grade_system_ids: list of grade systems
        :type grade_system_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``grade_system_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_grade_system_results(self, grade_system_search_order):
        """Specify an ordering to the search results.

        :param grade_system_search_order: grade system search order
        :type grade_system_search_order: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``NullArgument`` -- ``grade_system_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``grade_system_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_grade_system_search_record(self, grade_system_search_record_type):
        """Gets the grade system search record corresponding to the given grade system search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param grade_system_search_record_type: a grade system search record type
        :type grade_system_search_record_type: ``osid.type.Type``
        :return: the grade system search record
        :rtype: ``osid.grading.records.GradeSystemSearchRecord``
        :raise: ``NullArgument`` -- ``grade_system_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemSearchRecord


class GradeSystemSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_systems(self):
        """Gets the grade system list resulting from the search.

        :return: the grade system list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemList

    grade_systems = property(fget=get_grade_systems)

    @abc.abstractmethod
    def get_grade_system_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the grade system query inspector
        :rtype: ``osid.grading.GradeSystemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystemQueryInspector

    grade_system_query_inspector = property(fget=get_grade_system_query_inspector)

    @abc.abstractmethod
    def get_grade_system_search_results_record(self, grade_system_search_record_type):
        """Gets the grade system search results record corresponding to the given grade system search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param grade_system_search_record_type: a grade system search record type
        :type grade_system_search_record_type: ``osid.type.Type``
        :return: the grade system search results record
        :rtype: ``osid.grading.records.GradeSystemSearchResultsRecord``
        :raise: ``NullArgument`` -- ``grade_system_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemSearchResultsRecord


class GradeEntrySearch:
    """``GradeEntrySearch`` defines the interface for specifying package search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_grade_entries(self, grade_entry_ids):
        """Execute this search among the given list of grade entries.

        :param grade_entry_ids: list of grade entries
        :type grade_entry_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``grade_entry_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_grade_entry_results(self, grade_entry_search_order):
        """Specify an ordering to the search results.

        :param grade_entry_search_order: package search order
        :type grade_entry_search_order: ``osid.grading.GradeEntrySearchOrder``
        :raise: ``NullArgument`` -- ``grade_entry_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``grade_entry_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_grade_entry_search_record(self, grade_entry_search_record_type):
        """Gets the grade entry search record corresponding to the given package search record ``Type``.

        This method ie used to retrieve an object implementing the
        requested record.

        :param grade_entry_search_record_type: a grade entry search record type
        :type grade_entry_search_record_type: ``osid.type.Type``
        :return: the grade entry search record
        :rtype: ``osid.grading.records.GradeEntrySearchRecord``
        :raise: ``NullArgument`` -- ``grade_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntrySearchRecord


class GradeEntrySearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_entries(self):
        """Gets the package list resulting from the search.

        :return: the grade entry list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryList

    grade_entries = property(fget=get_grade_entries)

    @abc.abstractmethod
    def get_grade_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the grade entry query inspector
        :rtype: ``osid.grading.GradeEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntryQueryInspector

    grade_entry_query_inspector = property(fget=get_grade_entry_query_inspector)

    @abc.abstractmethod
    def get_grade_entry_search_results_record(self, grade_entry_search_record_type):
        """Gets the grade entry search results record corresponding to the given grade entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param grade_entry_search_record_type: a grade entry search record type
        :type grade_entry_search_record_type: ``osid.type.Type``
        :return: the grade entry search results record
        :rtype: ``osid.grading.records.GradeEntrySearchResultsRecord``
        :raise: ``NullArgument`` -- ``grade_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntrySearchResultsRecord


class GradebookColumnSearch:
    """``GradebookColumnSearch`` defines the interface for specifying grading search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_gradebook_columns(self, gradebook_column_ids):
        """Execute this search among the given list of gradebook columns.

        :param gradebook_column_ids: list of gradebook columns
        :type gradebook_column_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_column_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_gradebook_column_results(self, gradebook_column_search_order):
        """Specify an ordering to the search results.

        :param gradebook_column_search_order: gradebook column search order
        :type gradebook_column_search_order: ``osid.grading.GradebookColumnSearchOrder``
        :raise: ``NullArgument`` -- ``gradebook_column_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_column_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_gradebook_column_search_record(self, gradebook_column_search_record_type):
        """Gets the gradebook column search record corresponding to the given gradebook column search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param gradebook_column_search_record_type: a gradebook column search record type
        :type gradebook_column_search_record_type: ``osid.type.Type``
        :return: the gradebook column search record
        :rtype: ``osid.grading.records.GradebookColumnSearchRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSearchRecord


class GradebookColumnSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_columns(self):
        """Gets the gradebook column list resulting from the search.

        :return: the gradebook column list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnList

    gradebook_columns = property(fget=get_gradebook_columns)

    @abc.abstractmethod
    def get_gradebook_column_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the gradebook column query inspector
        :rtype: ``osid.grading.GradebookColumnQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumnQueryInspector

    gradebook_column_query_inspector = property(fget=get_gradebook_column_query_inspector)

    @abc.abstractmethod
    def get_gradebook_column_search_results_record(self, gradebook_column_search_record_type):
        """Gets the gradebook column search results record corresponding to the given gradebook column search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param gradebook_column_search_record_type: a gradebook column search record type
        :type gradebook_column_search_record_type: ``osid.type.Type``
        :return: the gradebook column search results record
        :rtype: ``osid.grading.records.GradebookColumnSearchResultsRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSearchResultsRecord


class GradebookSearch:
    """The interface for governing gradebook searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_gradebooks(self, gradebook_ids):
        """Execute this search among the given list of gradebooks.

        :param gradebook_ids: list of gradebooks
        :type gradebook_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_gradebook_results(self, gradebook_search_order):
        """Specify an ordering to the search results.

        :param gradebook_search_order: gradebook search order
        :type gradebook_search_order: ``osid.grading.GradebookSearchOrder``
        :raise: ``NullArgument`` -- ``gradebook_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_gradebook_search_record(self, gradebook_search_record_type):
        """Gets the gradebook search record corresponding to the given gradebook search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param gradebook_search_record_type: a gradebook search record type
        :type gradebook_search_record_type: ``osid.type.Type``
        :return: the gradebook search record
        :rtype: ``osid.grading.records.GradebookSearchRecord``
        :raise: ``NullArgument`` -- ``gradebook_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookSearchRecord


class GradebookSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebooks(self):
        """Gets the gradebook list resulting from the search.

        :return: the gradebook list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)

    @abc.abstractmethod
    def get_gradebook_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the gradebook query inspector
        :rtype: ``osid.grading.GradebookQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookQueryInspector

    gradebook_query_inspector = property(fget=get_gradebook_query_inspector)

    @abc.abstractmethod
    def get_gradebook_search_results_record(self, gradebook_search_record_type):
        """Gets the gradebook search results record corresponding to the given gradebook search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param gradebook_search_record_type: a gradebook search record type
        :type gradebook_search_record_type: ``osid.type.Type``
        :return: the gradebook search results record
        :rtype: ``osid.grading.records.GradebookSearchResultsRecord``
        :raise: ``NullArgument`` -- ``gradebook_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookSearchResultsRecord
