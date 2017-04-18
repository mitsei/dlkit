"""Implementations of hierarchy abstract base class query_inspectors."""
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


class HierarchyQueryInspector:
    """This is the query inspector for examining hierarchy queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_node_id_terms(self):
        """Gets the node ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    node_id_terms = property(fget=get_node_id_terms)

    @abc.abstractmethod
    def get_hierarchy_query_inspector_record(self, hierarchy_record_type):
        """Gets the hierarchy query inspector record corresponding to the given ``Hierarchy`` record ``Type``.

        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy query inspector record
        :rtype: ``osid.hierarchy.records.HierarchyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.records.HierarchyQueryInspectorRecord
