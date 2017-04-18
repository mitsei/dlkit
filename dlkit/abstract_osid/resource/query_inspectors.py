"""Implementations of resource abstract base class query_inspectors."""
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


class ResourceQueryInspector:
    """This is the query inspector for examining resource queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_group_terms(self):
        """Gets the group query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    group_terms = property(fget=get_group_terms)

    @abc.abstractmethod
    def get_demographic_terms(self):
        """Gets the demographic query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    demographic_terms = property(fget=get_demographic_terms)

    @abc.abstractmethod
    def get_containing_group_id_terms(self):
        """Gets the containing group ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    containing_group_id_terms = property(fget=get_containing_group_id_terms)

    @abc.abstractmethod
    def get_containing_group_terms(self):
        """Gets the containing group query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    containing_group_terms = property(fget=get_containing_group_terms)

    @abc.abstractmethod
    def get_avatar_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    avatar_id_terms = property(fget=get_avatar_id_terms)

    @abc.abstractmethod
    def get_avatar_terms(self):
        """Gets the asset query terms.

        :return: the query terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.repository.AssetQueryInspector

    avatar_terms = property(fget=get_avatar_terms)

    @abc.abstractmethod
    def get_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    @abc.abstractmethod
    def get_agent_terms(self):
        """Gets the agent query terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    @abc.abstractmethod
    def get_resource_relationship_id_terms(self):
        """Gets the resource relationship ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    resource_relationship_id_terms = property(fget=get_resource_relationship_id_terms)

    @abc.abstractmethod
    def get_resource_relationship_terms(self):
        """Gets the resource relationship query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceRelationshipQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceRelationshipQueryInspector

    resource_relationship_terms = property(fget=get_resource_relationship_terms)

    @abc.abstractmethod
    def get_bin_id_terms(self):
        """Gets the bin ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bin_id_terms = property(fget=get_bin_id_terms)

    @abc.abstractmethod
    def get_bin_terms(self):
        """Gets the bin query terms.

        :return: the query terms
        :rtype: ``osid.resource.BinQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinQueryInspector

    bin_terms = property(fget=get_bin_terms)

    @abc.abstractmethod
    def get_resource_query_inspector_record(self, resource_record_type):
        """Gets the record query inspector record corresponding to the given ``Resource`` record ``Type``.

        :param resource_record_type: a resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the resource query inspector record
        :rtype: ``osid.resource.records.ResourceQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceQueryInspectorRecord


class ResourceRelationshipQueryInspector:
    """This is the query inspector for examining resource relationship queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_resource_id_terms(self):
        """Gets the source resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    source_resource_id_terms = property(fget=get_source_resource_id_terms)

    @abc.abstractmethod
    def get_source_resource_terms(self):
        """Gets the source resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    source_resource_terms = property(fget=get_source_resource_terms)

    @abc.abstractmethod
    def get_destination_resource_id_terms(self):
        """Gets the Destination resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    destination_resource_id_terms = property(fget=get_destination_resource_id_terms)

    @abc.abstractmethod
    def get_destination_resource_terms(self):
        """Gets the Destination resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    destination_resource_terms = property(fget=get_destination_resource_terms)

    @abc.abstractmethod
    def get_same_resource_terms(self):
        """Gets the same resource query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    same_resource_terms = property(fget=get_same_resource_terms)

    @abc.abstractmethod
    def get_bin_id_terms(self):
        """Gets the bin ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    bin_id_terms = property(fget=get_bin_id_terms)

    @abc.abstractmethod
    def get_bin_terms(self):
        """Gets the bin query terms.

        :return: the query terms
        :rtype: ``osid.resource.BinQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinQueryInspector

    bin_terms = property(fget=get_bin_terms)

    @abc.abstractmethod
    def get_resource_relationship_query_inspector_record(self, resource_relationship_record_type):
        """Gets the resource relationship query inspector record corresponding to the given ``ResourceRelationship`` record ``Type``.

        :param resource_relationship_record_type: a resource relationship record type
        :type resource_relationship_record_type: ``osid.type.Type``
        :return: the resource relationship query inspector record
        :rtype: ``osid.resource.records.ResourceRelationshipQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``resource_relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceRelationshipQueryInspectorRecord


class BinQueryInspector:
    """This is the query inspector for examining bin queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    @abc.abstractmethod
    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    @abc.abstractmethod
    def get_ancestor_bin_id_terms(self):
        """Gets the ancestor bin ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_bin_id_terms = property(fget=get_ancestor_bin_id_terms)

    @abc.abstractmethod
    def get_ancestor_bin_terms(self):
        """Gets the ancestor bin query terms.

        :return: the query terms
        :rtype: ``osid.resource.BinQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinQueryInspector

    ancestor_bin_terms = property(fget=get_ancestor_bin_terms)

    @abc.abstractmethod
    def get_descendant_bin_id_terms(self):
        """Gets the descendant bin ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_bin_id_terms = property(fget=get_descendant_bin_id_terms)

    @abc.abstractmethod
    def get_descendant_bin_terms(self):
        """Gets the descendant bin query terms.

        :return: the query terms
        :rtype: ``osid.resource.BinQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.BinQueryInspector

    descendant_bin_terms = property(fget=get_descendant_bin_terms)

    @abc.abstractmethod
    def get_bin_query_inspector_record(self, bin_record_type):
        """Gets the bin query inspector record corresponding to the given ``Bin`` record ``Type``.

        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin query inspector record
        :rtype: ``osid.resource.records.BinQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.BinQueryInspectorRecord
