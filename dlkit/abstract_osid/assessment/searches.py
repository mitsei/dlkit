"""Implementations of assessment abstract base class searches."""
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


class ItemSearch:
    """``ItemSearch`` defines the interface for specifying item search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_items(self, item_ids):
        """Execute this search among the given list of items.

        :param item_ids: list of items
        :type item_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``item_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_item_results(self, item_search_order):
        """Specify an ordering to the search results.

        :param item_search_order: item search order
        :type item_search_order: ``osid.assessment.ItemSearchOrder``
        :raise: ``NullArgument`` -- ``item_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``item_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_item_search_record(self, item_search_record_type):
        """Gets the item search record corresponding to the given item search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param item_search_record_type: an item search record type
        :type item_search_record_type: ``osid.type.Type``
        :return: the item search record
        :rtype: ``osid.assessment.records.ItemSearchRecord``
        :raise: ``NullArgument`` -- ``item_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemSearchRecord


class ItemSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_items(self):
        """Gets the item list resulting from the search.

        :return: the item list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``IllegalState`` -- the item list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemList

    items = property(fget=get_items)

    @abc.abstractmethod
    def get_item_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.assessment.ItemQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.ItemQueryInspector

    item_query_inspector = property(fget=get_item_query_inspector)

    @abc.abstractmethod
    def get_item_search_results_record(self, item_search_record_type):
        """Gets the record corresponding to the given item search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param item_search_record_type: an item search record type
        :type item_search_record_type: ``osid.type.Type``
        :return: the item search results record
        :rtype: ``osid.assessment.records.ItemSearchResultsRecord``
        :raise: ``NullArgument`` -- ``item_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.ItemSearchResultsRecord


class AssessmentSearch:
    """``AssessmentSearch`` defines the interface for specifying assessment search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_assessments(self, assessment_ids):
        """Execute this search among the given list of assessments.

        :param assessment_ids: list of assessments
        :type assessment_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``assessment_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_assessment_results(self, assessment_search_order):
        """Specify an ordering to the search results.

        :param assessment_search_order: assessment search order
        :type assessment_search_order: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_search_record(self, assessment_search_record_type):
        """Gets the assessment search record corresponding to the given assessment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_search_record_type: an assessment search record type
        :type assessment_search_record_type: ``osid.type.Type``
        :return: the assessment search record
        :rtype: ``osid.assessment.records.AssessmentSearchRecord``
        :raise: ``NullArgument`` -- ``assessment_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentSearchRecord


class AssessmentSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessments(self):
        """Gets the assessment list resulting from the search.

        :return: the assessment list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``IllegalState`` -- the assessment list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentList

    assessments = property(fget=get_assessments)

    @abc.abstractmethod
    def get_assessment_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.assessment.AssessmentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentQueryInspector

    assessment_query_inspector = property(fget=get_assessment_query_inspector)

    @abc.abstractmethod
    def get_assessment_search_results_record(self, assessment_search_record_type):
        """Gets the assessment search order record corresponding to the given assessment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_search_record_type: an assessment search record type
        :type assessment_search_record_type: ``osid.type.Type``
        :return: the assessment search results record
        :rtype: ``osid.assessment.records.AssessmentSearchResultsRecord``
        :raise: ``NullArgument`` -- ``assessment_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentSearchResultsRecord


class AssessmentOfferedSearch:
    """``AssessmentOfferedSearch`` defines the interface for specifying assessment search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_assessments_offered(self, assessment_offrered_ids):
        """Execute this search among the given list of assessments.

        :param assessment_offrered_ids: list of assessments offered
        :type assessment_offrered_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``assessment_offered_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_assessment_offered_results(self, assessment_offered_search_order):
        """Specify an ordering to the search results.

        :param assessment_offered_search_order: assessment offered search order
        :type assessment_offered_search_order: ``osid.assessment.AssessmentOfferedSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_offered_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_offered_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_offered_search_record(self, assessment_offered_search_record_type):
        """Gets the assessment search record corresponding to the given assessment offered search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_offered_search_record_type: an assessment offered search record type
        :type assessment_offered_search_record_type: ``osid.type.Type``
        :return: the assessment offered search
        :rtype: ``osid.assessment.records.AssessmentOfferedSearchRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedSearchRecord


class AssessmentOfferedSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessments_offered(self):
        """Gets the assessment offered list resulting from the search.

        :return: the assessment offered list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``IllegalState`` -- the assessment offered list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedList

    assessments_offered = property(fget=get_assessments_offered)

    @abc.abstractmethod
    def get_assessment_offered_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentOfferedQueryInspector

    assessment_offered_query_inspector = property(fget=get_assessment_offered_query_inspector)

    @abc.abstractmethod
    def get_assessment_offered_search_results_record(self, assessment_offered_search_record_type):
        """Gets the assessment offered search results record corresponding to the given assessment offered search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_offered_search_record_type: an assessment offered search record type
        :type assessment_offered_search_record_type: ``osid.type.Type``
        :return: the assessment offered search results record
        :rtype: ``osid.assessment.records.AssessmentOfferedSearchResultsRecord``
        :raise: ``NullArgument`` -- ``assessment_offered_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_offered_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentOfferedSearchResultsRecord


class AssessmentTakenSearch:
    """``AssessmentTakenSearch`` defines the interface for specifying assessment search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_assessments_taken(self, assessment_taken_ids):
        """Execute this search among the given list of assessments.

        :param assessment_taken_ids: list of assessments taken
        :type assessment_taken_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``assessment_taken_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_assessment_taken_results(self, assessment_taken_search_order):
        """Specify an ordering to the search results.

        :param assessment_taken_search_order: assessment offered search order
        :type assessment_taken_search_order: ``osid.assessment.AssessmentTakenSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_taken_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_taken_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_taken_search_record(self, assessment_taken_search_record_type):
        """Gets the assessment taken search record corresponding to the given assessment taken search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_taken_search_record_type: an assessment taken search record type
        :type assessment_taken_search_record_type: ``osid.type.Type``
        :return: the assessment taken search record
        :rtype: ``osid.assessment.records.AssessmentTakenSearchRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenSearchRecord


class AssessmentTakenSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessments_taken(self):
        """Gets the assessment taken list resulting from the search.

        :return: the assessment taken list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``IllegalState`` -- the assessment taken list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenList

    assessments_taken = property(fget=get_assessments_taken)

    @abc.abstractmethod
    def get_assessment_taken_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.AssessmentTakenQueryInspector

    assessment_taken_query_inspector = property(fget=get_assessment_taken_query_inspector)

    @abc.abstractmethod
    def get_assessment_taken_search_results_record(self, assessment_taken_search_record_type):
        """Gets the assessment taken record corresponding to the given assessment taken search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param assessment_taken_search_record_type: an assessment taken search record type
        :type assessment_taken_search_record_type: ``osid.type.Type``
        :return: the assessment taken search results record
        :rtype: ``osid.assessment.records.AssessmentTakenSearchResultsRecord``
        :raise: ``NullArgument`` -- ``assessment_taken_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_taken_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.AssessmentTakenSearchResultsRecord


class BankSearch:
    """The interface for governing bank searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_banks(self, bank_ids):
        """Execute this search among the given list of banks.

        :param bank_ids: list of banks
        :type bank_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_bank_results(self, bank_search_order):
        """Specify an ordering to the search results.

        :param bank_search_order: bank search order
        :type bank_search_order: ``osid.assessment.BankSearchOrder``
        :raise: ``NullArgument`` -- ``bank_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``bank_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_bank_search_record(self, bank_search_record_type):
        """Gets the bank search record corresponding to the given bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param bank_search_record_type: a bank search record type
        :type bank_search_record_type: ``osid.type.Type``
        :return: the bank search record
        :rtype: ``osid.assessment.records.BankSearchRecord``
        :raise: ``NullArgument`` -- ``bank_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankSearchRecord


class BankSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_banks(self):
        """Gets the bank list resulting from a search.

        :return: the bank list
        :rtype: ``osid.assessment.BankList``
        :raise: ``IllegalState`` -- the bank list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList

    banks = property(fget=get_banks)

    @abc.abstractmethod
    def get_bank_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.assessment.BankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankQueryInspector

    bank_query_inspector = property(fget=get_bank_query_inspector)

    @abc.abstractmethod
    def get_bank_search_results_record(self, bank_search_record_type):
        """Gets the bank search results record corresponding to the given bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param bank_search_record_type: a bank search record type
        :type bank_search_record_type: ``osid.type.Type``
        :return: the bank search results record
        :rtype: ``osid.assessment.records.BankSearchResultsRecord``
        :raise: ``NullArgument`` -- ``bank_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.records.BankSearchResultsRecord
