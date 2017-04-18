"""Implementations of relationship abstract base class objects."""
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


class Relationship:
    """A ``Relationship`` is an object between two peers.

    The genus type indicates the relationship between the peer and the
    related peer.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_id(self):
        """Gets the from peer ``Id`` in this relationship.

        :return: the peer
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    source_id = property(fget=get_source_id)

    @abc.abstractmethod
    def get_destination_id(self):
        """Gets the to peer ``Id`` in this relationship.

        :return: the related peer
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    destination_id = property(fget=get_destination_id)

    @abc.abstractmethod
    def get_relationship_record(self, relationship_record_type):
        """Gets the relationshop record corresponding to the given ``Relationship`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``relationship_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(relationship_record_type)`` is ``true`` .

        :param relationship_record_type: the type of relationship record to retrieve
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship record
        :rtype: ``osid.relationship.records.RelationshipRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.RelationshipRecord


class RelationshipForm:
    """This is the form for creating and updating ``Relationships``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RelationshipAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_relationship_form_record(self, relationship_record_type):
        """Gets the ``RelationshipFormRecord`` corresponding to the given relationship record ``Type``.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship form record
        :rtype: ``osid.relationship.records.RelationshipFormRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.RelationshipFormRecord


class RelationshipList:
    """Like all ``OsidLists,``  ``Relationship`` provides a means for accessing ``Relationship`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Relationship relationship =
    rl.getNextRelationship(); }

    or
      while (rl.hasNext()) {
           Relationship[] relationships = rl.getNextRelationships(rl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_relationship(self):
        """Gets the next ``Relationship`` in this list.

        :return: the next ``Relationship`` in this list. The ``has_next()`` method should be used to test that a next ``Relationship`` is available before calling this method.
        :rtype: ``osid.relationship.Relationship``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.Relationship

    next_relationship = property(fget=get_next_relationship)

    @abc.abstractmethod
    def get_next_relationships(self, n):
        """Gets the next set of ``Relationships`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Relationship`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Relationship`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.Relationship``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.Relationship


class Family:
    """A ``Family`` represents a collection of relationships.

    Like all OSID objects, a ``Family`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_family_record(self, family_record_type):
        """Gets the famly record corresponding to the given ``Family`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``family_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(family_record_type)``
        is ``true`` .

        :param family_record_type: the type of family record to retrieve
        :type family_record_type: ``osid.type.Type``
        :return: the family record
        :rtype: ``osid.relationship.records.FamilyRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.FamilyRecord


class FamilyForm:
    """This is the form for creating and updating ``Family`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FamilyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_family_form_record(self, family_record_type):
        """Gets the ``FamilyFormRecord`` corresponding to the given family record ``Type``.

        :param family_record_type: the family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family form record
        :rtype: ``osid.relationship.records.FamilyFormRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.FamilyFormRecord


class FamilyList:
    """Like all ``OsidLists,``  ``FamilyList`` provides a means for accessing ``Family`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Family family = fl.getNextFamily();
    }

    or
      while (fl.hasNext()) {
           Family[] families = fl.getNextFamilies(fl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_family(self):
        """Gets the next ``Family`` in this list.

        :return: the next ``Family`` in this list. The ``has_next()`` method should be used to test that a next ``Family`` is available before calling this method.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.Family

    next_family = property(fget=get_next_family)

    @abc.abstractmethod
    def get_next_families(self, n):
        """Gets the next set of ``Family elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Family`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Family`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.Family


class FamilyNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``FamilyHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_family(self):
        """Gets the ``Family`` at this node.

        :return: the family represented by this node
        :rtype: ``osid.relationship.Family``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.Family

    family = property(fget=get_family)

    @abc.abstractmethod
    def get_parent_family_nodes(self):
        """Gets the parents of this family.

        :return: the parents of the ``id``
        :rtype: ``osid.relationship.FamilyNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.FamilyNodeList

    parent_family_nodes = property(fget=get_parent_family_nodes)

    @abc.abstractmethod
    def get_child_family_nodes(self):
        """Gets the children of this family.

        :return: the children of this family
        :rtype: ``osid.relationship.FamilyNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.FamilyNodeList

    child_family_nodes = property(fget=get_child_family_nodes)


class FamilyNodeList:
    """Like all ``OsidLists,``  ``FamilyNodeList`` provides a means for accessing ``FamilyNode`` elements sequentially either one at a time or many at a time.

    Examples: while (fnl.hasNext()) { FamilyNode node =
    fnl.getNextFamilyNode(); }

    or
      while (fnl.hasNext()) {
           FamilyNode[] nodes = fnl.getNextFamilyNodes(fnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_family_node(self):
        """Gets the next ``FamilyNode`` in this list.

        :return: the next ``FamilyNode`` in this list. The ``has_next()`` method should be used to test that a next ``FamilyNode`` is available before calling this method.
        :rtype: ``osid.relationship.FamilyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.FamilyNode

    next_family_node = property(fget=get_next_family_node)

    @abc.abstractmethod
    def get_next_family_nodes(self, n):
        """Gets the next set of ``FamilyNode elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``FamilyNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``FamilyNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.FamilyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.FamilyNode
