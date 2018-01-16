"""JSON implementations of relationship searches."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import objects
from . import queries
from .. import utilities
from ..osid import searches as osid_searches
from ..primitives import Id
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.relationship import searches as abc_relationship_searches


class RelationshipSearch(abc_relationship_searches.RelationshipSearch, osid_searches.OsidSearch):
    """The search interface for governing relationship searches."""
    def __init__(self, runtime):
        self._namespace = 'relationship.Relationship'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_relationships(self, relationship_ids):
        """Execute this search among the given list of relationships.

        arg:    relationship_ids (osid.id.IdList): list of relationships
        raise:  NullArgument - ``relationship_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = relationship_ids

    @utilities.arguments_not_none
    def order_relationship_results(self, relationship_search_order):
        """Specify an ordering to the search results.

        arg:    relationship_search_order
                (osid.relationship.RelationshipSearchOrder):
                relationship search order
        raise:  NullArgument - ``relationship_search_order`` is ``null``
        raise:  Unsupported - ``relationship_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_relationship_search_record(self, relationship_search_record_type):
        """Gets the relationship search record corresponding to the given relationship search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    relationship_search_record_type (osid.type.Type): a
                relationship search record type
        return: (osid.relationship.records.RelationshipSearchRecord) -
                the relationship search record
        raise:  NullArgument - ``relationship_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class RelationshipSearchResults(abc_relationship_searches.RelationshipSearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'relationship.Relationship'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_relationships(self):
        """Gets the relationship list resulting from a search.

        return: (osid.relationship.RelationshipList) - the relationship
                list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.RelationshipList(self._results, runtime=self._runtime)

    relationships = property(fget=get_relationships)

    def get_relationship_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.relationship.RelationshipQueryInspector) - the
                relationship query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.RelationshipQueryInspector(self._query_terms, runtime=self._runtime)

    relationship_query_inspector = property(fget=get_relationship_query_inspector)

    @utilities.arguments_not_none
    def get_relationship_search_results_record(self, relationship_search_record_type):
        """Gets the relationship search results record corresponding to the given relationship search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces.

        arg:    relationship_search_record_type (osid.type.Type): a
                relationship search record type
        return:
                (osid.relationship.records.RelationshipSearchResultsReco
                rd) - the relationship search results record
        raise:  NullArgument - ``relationship_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class FamilySearch(abc_relationship_searches.FamilySearch, osid_searches.OsidSearch):
    """The search interface for governing family searches."""
    def __init__(self, runtime):
        self._namespace = 'relationship.Family'
        self._runtime = runtime
        record_type_data_sets = get_registry('RESOURCE_RECORD_TYPES', runtime)
        self._record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        self._id_list = None
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_searches.OsidSearch.__init__(self, runtime)

    @utilities.arguments_not_none
    def search_among_families(self, family_ids):
        """Execute this search among the given list of families.

        arg:    family_ids (osid.id.IdList): list of families
        raise:  NullArgument - ``family_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        self._id_list = family_ids

    @utilities.arguments_not_none
    def order_family_results(self, family_search_order):
        """Specify an ordering to the search results.

        arg:    family_search_order
                (osid.relationship.FamilySearchOrder): family search
                order
        raise:  NullArgument - ``family_search_order`` is ``null``
        raise:  Unsupported - ``family_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_family_search_record(self, family_search_record_type):
        """Gets the family search record corresponding to the given family search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    family_search_record_type (osid.type.Type): a family
                search record type
        return: (osid.relationship.records.FamilySearchRecord) - the
                family search record
        raise:  NullArgument - ``family_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(family_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class FamilySearchResults(abc_relationship_searches.FamilySearchResults, osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search and is used as a vehicle to perform a search within a previous result set."""
    def __init__(self, results, query_terms, runtime):
        # if you don't iterate, then .count() on the cursor is an inaccurate representation of limit / skip
        # self._results = [r for r in results]
        self._namespace = 'relationship.Family'
        self._results = results
        self._query_terms = query_terms
        self._runtime = runtime
        self.retrieved = False

    def get_families(self):
        """Gets the family list resulting from a search.

        return: (osid.relationship.FamilyList) - the family list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.retrieved:
            raise errors.IllegalState('List has already been retrieved.')
        self.retrieved = True
        return objects.FamilyList(self._results, runtime=self._runtime)

    families = property(fget=get_families)

    def get_family_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.relationship.FamilyQueryInspector) - the family
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return queries.FamilyQueryInspector(self._query_terms, runtime=self._runtime)

    family_query_inspector = property(fget=get_family_query_inspector)

    @utilities.arguments_not_none
    def get_family_search_results_record(self, family_search_record_type):
        """Gets the family search results record corresponding to the given family search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    family_search_record_type (osid.type.Type): a family
                search record type
        return: (osid.relationship.records.FamilySearchResultsRecord) -
                the family search results record
        raise:  NullArgument - ``FamilySearchRecordType`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(family_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
