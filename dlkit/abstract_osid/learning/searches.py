"""Implementations of learning abstract base class searches."""
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


class ObjectiveSearch:
    """``ObjectiveSearch`` defines the interface for specifying objective search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_objectives(self, objective_ids):
        """Execute this search among the given list of objectives.

        :param objective_ids: list of objectives
        :type objective_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_objective_results(self, objective_search_order):
        """Specify an ordering to the search results.

        :param objective_search_order: objective search order
        :type objective_search_order: ``osid.learning.ObjectiveSearchOrder``
        :raise: ``NullArgument`` -- ``objective_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``objective_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_search_record(self, objective_search_record_type):
        """Gets the objective search record corresponding to the given objective search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param objective_search_record_type: an objective search record type
        :type objective_search_record_type: ``osid.type.Type``
        :return: the objective search record
        :rtype: ``osid.learning.records.ObjectiveSearchRecord``
        :raise: ``NullArgument`` -- ``objective_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(objective_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveSearchRecord


class ObjectiveSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objectives(self):
        """Gets the objective list resulting from the search.

        :return: the objective list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    objectives = property(fget=get_objectives)

    @abc.abstractmethod
    def get_objective_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.learning.ObjectiveQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    objective_query_inspector = property(fget=get_objective_query_inspector)

    @abc.abstractmethod
    def get_objective_search_results_record(self, objective_search_record_type):
        """Gets the objective search results record corresponding to the given objective search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param objective_search_record_type: an objective search record type
        :type objective_search_record_type: ``osid.type.Type``
        :return: the objective search results record
        :rtype: ``osid.learning.records.ObjectiveSearchResultsRecord``
        :raise: ``NullArgument`` -- ``objective_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(objective_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveSearchResultsRecord


class ActivitySearch:
    """``ActivitySearch`` defines the interface for specifying activity search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_activities(self, activity_ids):
        """Execute this search among the given list of activities.

        :param activity_ids: list of activities
        :type activity_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``activity_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_activity_results(self, activitiesearch_order):
        """Specify an ordering to the search results.

        :param activitiesearch_order: activity search order
        :type activitiesearch_order: ``osid.learning.ActivitySearchOrder``
        :raise: ``NullArgument`` -- ``activitiesearch_order`` is ``null``
        :raise: ``Unsupported`` -- ``activitiesearch_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_activity_search_record(self, activitiesearch_record_type):
        """Gets the activity record corresponding to the given activity search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param activitiesearch_record_type: an activity search record type
        :type activitiesearch_record_type: ``osid.type.Type``
        :return: the activity search record
        :rtype: ``osid.learning.records.ActivitySearchRecord``
        :raise: ``NullArgument`` -- ``activitiesearch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(activitiesearch_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivitySearchRecord


class ActivitySearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_activities(self):
        """Gets the activity list resulting from the search.

        :return: the activity list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    activities = property(fget=get_activities)

    @abc.abstractmethod
    def get_activity_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.learning.ActivityQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQueryInspector

    activity_query_inspector = property(fget=get_activity_query_inspector)

    @abc.abstractmethod
    def get_activity_search_results_record(self, activitiesearch_record_type):
        """Gets the activity search results record corresponding to the given activity search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param activitiesearch_record_type: an activity search record type
        :type activitiesearch_record_type: ``osid.type.Type``
        :return: the activity search results record
        :rtype: ``osid.learning.records.ActivitySearchResultsRecord``
        :raise: ``NullArgument`` -- ``activitiesearch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(activitiesearch_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ActivitySearchResultsRecord


class ProficiencySearch:
    """The search interface for governing proficiency searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_proficiencies(self, proficiency_ids):
        """Execute this search among the given list of proficiencies.

        :param proficiency_ids: list of proficiencies
        :type proficiency_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``proficiency_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_proficiency_results(self, proficiency_search_order):
        """Specify an ordering to the search results.

        :param proficiency_search_order: proficiency search order
        :type proficiency_search_order: ``osid.learning.ProficiencySearchOrder``
        :raise: ``NullArgument`` -- ``proficiency_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``proficiency_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_proficiency_search_record(self, proficiency_search_record_type):
        """Gets the proficiency search record corresponding to the given proficiency search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param proficiency_search_record_type: a proficiency search record type
        :type proficiency_search_record_type: ``osid.type.Type``
        :return: the proficiency search record
        :rtype: ``osid.learning.records.ProficiencySearchRecord``
        :raise: ``NullArgument`` -- ``proficiency_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencySearchRecord


class ProficiencySearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_proficiencies(self):
        """Gets the proficiency list resulting from a search.

        :return: the proficiency list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    proficiencies = property(fget=get_proficiencies)

    @abc.abstractmethod
    def get_proficiency_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the proficiency query inspector
        :rtype: ``osid.learning.ProficiencyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQueryInspector

    proficiency_query_inspector = property(fget=get_proficiency_query_inspector)

    @abc.abstractmethod
    def get_proficiency_search_results_record(self, proficiency_search_record_type):
        """Gets the proficiency search results record corresponding to the given proficiency search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param proficiency_search_record_type: a proficiency search record type
        :type proficiency_search_record_type: ``osid.type.Type``
        :return: the proficiency search results record
        :rtype: ``osid.learning.records.ProficiencySearchResultsRecord``
        :raise: ``NullArgument`` -- ``proficiency_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ProficiencySearchResultsRecord


class ObjectiveBankSearch:
    """The interface for governing objective bank searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_objective_banks(self, objective_bank_ids):
        """Execute this search among the given list of objective banks.

        :param objective_bank_ids: list of objective banks
        :type objective_bank_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective bank_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_objective_bank_results(self, objective_bank_search_order):
        """Specify an ordering to the search results.

        :param objective_bank_search_order: objective bank search order
        :type objective_bank_search_order: ``osid.learning.ObjectiveBankSearchOrder``
        :raise: ``NullArgument`` -- ``objective_bank_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``objective_bank_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_bank_search_record(self, objective_bank_search_record_type):
        """Gets the objective bank search record corresponding to the given objective bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param objective_bank_search_record_type: an objective bank search record type
        :type objective_bank_search_record_type: ``osid.type.Type``
        :return: the objective bank search record
        :rtype: ``osid.learning.records.ObjectiveBankSearchRecord``
        :raise: ``NullArgument`` -- ``objective_bank_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(objective bank_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankSearchRecord


class ObjectiveBankSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_banks(self):
        """Gets the objective bank list resulting from the search.

        :return: the objective bank list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)

    @abc.abstractmethod
    def get_objective_bank_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.learning.ObjectiveBankQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQueryInspector

    objective_bank_query_inspector = property(fget=get_objective_bank_query_inspector)

    @abc.abstractmethod
    def get_objective_bank_search_results_record(self, objective_bank_search_record_type):
        """Gets the objective bank search results record corresponding to the given objective bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param objective_bank_search_record_type: an objective bank search record type
        :type objective_bank_search_record_type: ``osid.type.Type``
        :return: the objective bank search results record
        :rtype: ``osid.learning.records.ObjectiveBankSearchResultsRecord``
        :raise: ``NullArgument`` -- ``objective_bank_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_search_record_type(objective bank_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.records.ObjectiveBankSearchResultsRecord
