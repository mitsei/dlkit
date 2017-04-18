"""Implementations of hierarchy abstract base class objects."""
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


class Hierarchy:
    """A ``Hierarchy`` represents an authenticatable identity.

    Like all OSID objects, a ``Hierarchy`` is identified by its Id and
    any persisted references should use the Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_hierarchy_record(self, hierarchy_record_type):
        """Gets the hierarchy record corresponding to the given ``Hierarchy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``hierarchy_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(hierarchy_record_type)`` is ``true`` .

        :param hierarchy_record_type: the type of the record to retrieve
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy record
        :rtype: ``osid.hierarchy.records.HierarchyRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchyrecord_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.records.HierarchyRecord


class HierarchyForm:
    """This is the form for creating and updating ``Hierarchy`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``HierarchyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_hierarchy_form_record(self, hierarchy_record_type):
        """Gets the ``HierarchyFormRecord`` corresponding to the given hierarchy record ``Type``.

        :param hierarchy_record_type: the hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy form record
        :rtype: ``osid.hierarchy.records.HierarchyFormRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.records.HierarchyFormRecord


class HierarchyList:
    """Like all ``OsidLists,``  ``HierarchyList`` provides a means for accessing ``Id`` elements sequentially either one at a time or many at a time.

    Examples: while (hl.hasNext()) { Hierarchy hierarchy =
    hl.getNextHierarchy(); }

    or
      while (hl.hasNext()) {
           Hierarchy[] hierarchies = hl.getNextHierarchies(hl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_hierarchy(self):
        """Gets the next ``Hierarchy`` in this list.

        :return: the next ``Hierarchy`` in this list. The ``has_next()`` method should be used to test that a next ``Hierarchy`` is available before calling this method.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    next_hierarchy = property(fget=get_next_hierarchy)

    @abc.abstractmethod
    def get_next_hierarchies(self, n):
        """Gets the next set of ``Hierarchy`` objects in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Hierarchy`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Hierarchy`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy


class Node:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the hierarchy traversal
    session.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_parents(self):
        """Gets the parents of this node.

        :return: the parents of this node
        :rtype: ``osid.hierarchy.NodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.NodeList

    parents = property(fget=get_parents)

    @abc.abstractmethod
    def get_children(self):
        """Gets the children of this node.

        :return: the children of this node
        :rtype: ``osid.hierarchy.NodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.NodeList

    children = property(fget=get_children)


class NodeList:
    """Like all ``OsidLists,``  ``NodeList`` provides a means for accessing ``Id`` elements sequentially either one at a time or many at a time.

    Examples: while (nl.hasNext()) { Node node = nl.getNextNode(); }

    or
      while (nl.hasNext()) {
           Node[] nodes = nl.getNextNodes(nl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_node(self):
        """Gets the next ``Node`` in this list.

        :return: the next ``Node`` in this list. The ``has_next()`` method should be used to test that a next ``Node`` is available before calling this method.
        :rtype: ``osid.hierarchy.Node``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    next_node = property(fget=get_next_node)

    @abc.abstractmethod
    def get_next_nodes(self, n):
        """Gets the next set of ``Node`` objects in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Node`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Node`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.hierarchy.Node``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node
