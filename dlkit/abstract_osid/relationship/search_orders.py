"""Implementations of relationship abstract base class search_orders."""
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


class RelationshipSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_source(self, style):
        """Specifies a preference for ordering the result set by the source peer.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_destination(self, style):
        """Specifies a preference for ordering the result set by the destination peer.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_relationship_search_order_record(self, relationship_record_type):
        """Gets the relationship search order record corresponding to the given relationship record ``Type``.

        Multiple retrievals return the same underlying object.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship search order record
        :rtype: ``osid.relationship.records.RelationshipSearchOrderRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.RelationshipSearchOrderRecord


class FamilySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_family_search_order_record(self, family_record_type):
        """Gets the family search record order corresponding to the given family record Type.

        Multiple retrievals return the same underlying object.

        :param family_record_type: a family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family search order record
        :rtype: ``osid.relationship.records.FamilySearchOrderRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.relationship.records.FamilySearchOrderRecord
