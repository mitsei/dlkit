"""Implementations of resource abstract base class queries."""
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


class ResourceQuery:
    """This is the query for searching resources.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_group(self, match):
        """Matches resources that are also groups.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_group_terms(self):
        """Clears the group terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    group_terms = property(fdel=clear_group_terms)

    @abc.abstractmethod
    def match_demographic(self, match):
        """Matches resources that are also demographics.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_demographic_terms(self):
        """Clears the demographic terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    demographic_terms = property(fdel=clear_demographic_terms)

    @abc.abstractmethod
    def match_containing_group_id(self, resource_id, match):
        """Sets the group ``Id`` for this query to match resources within the given group.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_group_id_terms(self):
        """Clears the group ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_group_id_terms = property(fdel=clear_containing_group_id_terms)

    @abc.abstractmethod
    def supports_containing_group_query(self):
        """Tests if a ``ResourceQuery`` is available for querying containing groups.

        :return: ``true`` if a group resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_containing_group_query(self):
        """Gets the query for a a containing group.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_containing_group_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    containing_group_query = property(fget=get_containing_group_query)

    @abc.abstractmethod
    def match_any_containing_group(self, match):
        """Matches resources inside any group.

        :param match: ``true`` to match any containing group, ``false`` to match resources part of no groups
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_group_terms(self):
        """Clears the containing group terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_group_terms = property(fdel=clear_containing_group_terms)

    @abc.abstractmethod
    def match_avatar_id(self, asset_id, match):
        """Sets the asset ``Id`` for this query.

        :param asset_id: the asset ``Id``
        :type asset_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_avatar_id_terms(self):
        """Clears the asset ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    avatar_id_terms = property(fdel=clear_avatar_id_terms)

    @abc.abstractmethod
    def supports_avatar_query(self):
        """Tests if an ``AssetQuery`` is available.

        :return: ``true`` if an asset query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_avatar_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``Unimplemented`` -- ``supports_avatar_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_avatar_query()`` is ``true``.*

        """
        return  # osid.repository.AssetQuery

    avatar_query = property(fget=get_avatar_query)

    @abc.abstractmethod
    def match_any_avatar(self, match):
        """Matches resources with any asset.

        :param match: ``true`` to match any asset, ``false`` to match resources with no asset
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_avatar_terms(self):
        """Clears the asset terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    avatar_terms = property(fdel=clear_avatar_terms)

    @abc.abstractmethod
    def match_agent_id(self, agent_id, match):
        """Sets the agent ``Id`` for this query.

        :param agent_id: the agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)

    @abc.abstractmethod
    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def match_any_agent(self, match):
        """Matches resources with any agent.

        :param match: ``true`` to match any agent, ``false`` to match resources with no agent
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_agent_terms(self):
        """Clears the agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_terms = property(fdel=clear_agent_terms)

    @abc.abstractmethod
    def match_resource_relationship_id(self, resource_relationship_id, match):
        """Sets the resource relationship ``Id`` for this query.

        :param resource_relationship_id: the resource relationship ``Id``
        :type resource_relationship_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_relationship_id_terms(self):
        """Clears the resource relationship ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_relationship_id_terms = property(fdel=clear_resource_relationship_id_terms)

    @abc.abstractmethod
    def supports_resource_relationship_query(self):
        """Tests if a ``ResourceRelationshipQuery`` is available.

        :return: ``true`` if a resource relationship query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_relationship_query(self):
        """Gets the query for aa resource relationship.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource relationship query
        :rtype: ``osid.resource.ResourceRelationshipQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceRelationshipQuery

    resource_relationship_query = property(fget=get_resource_relationship_query)

    @abc.abstractmethod
    def match_any_resource_relationship(self, match):
        """Matches resources with any resource relationship.

        :param match: ``true`` to match any resource relationship, ``false`` to match resources with no relationship
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_relationship_terms(self):
        """Clears the resource relationship terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_relationship_terms = property(fdel=clear_resource_relationship_terms)

    @abc.abstractmethod
    def match_bin_id(self, bin_id, match):
        """Sets the bin ``Id`` for this query.

        :param bin_id: the bin ``Id``
        :type bin_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bin_id_terms(self):
        """Clears the bin ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_id_terms = property(fdel=clear_bin_id_terms)

    @abc.abstractmethod
    def supports_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        :return: ``true`` if a bin query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuery

    bin_query = property(fget=get_bin_query)

    @abc.abstractmethod
    def clear_bin_terms(self):
        """Clears the bin terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_terms = property(fdel=clear_bin_terms)

    @abc.abstractmethod
    def get_resource_query_record(self, resource_record_type):
        """Gets the resource query record corresponding to the given ``Resource`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param resource_record_type: a resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the resource query record
        :rtype: ``osid.resource.records.ResourceQueryRecord``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceQueryRecord


class ResourceRelationshipQuery:
    """This is the query for searching resource relationships.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_source_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_source_resource_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_resource_id_terms = property(fdel=clear_source_resource_id_terms)

    @abc.abstractmethod
    def supports_source_resource_query(self):
        """Tests if a ``ResourceQuery`` is available for querying resources.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_source_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_source_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_source_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    source_resource_query = property(fget=get_source_resource_query)

    @abc.abstractmethod
    def clear_source_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_resource_terms = property(fdel=clear_source_resource_terms)

    @abc.abstractmethod
    def match_destination_resource_id(self, peer_resource_id, match):
        """Sets the peer resource ``Id`` for this query.

        :param peer_resource_id: a peer resource ``Id``
        :type peer_resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``peer_resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_destination_resource_id_terms(self):
        """Clears the peer resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    destination_resource_id_terms = property(fdel=clear_destination_resource_id_terms)

    @abc.abstractmethod
    def supports_destination_resource_query(self):
        """Tests if a ``ResourceQuery`` is available for querying resources.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_destination_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_destination_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_destination_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    destination_resource_query = property(fget=get_destination_resource_query)

    @abc.abstractmethod
    def clear_destination_resource_terms(self):
        """Clears the peer resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    destination_resource_terms = property(fdel=clear_destination_resource_terms)

    @abc.abstractmethod
    def match_same_resource(self, match):
        """Matches relationships where the peer resources are the same.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_same_resource_terms(self):
        """Clears the same resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    same_resource_terms = property(fdel=clear_same_resource_terms)

    @abc.abstractmethod
    def match_bin_id(self, bin_id, match):
        """Sets the bin ``Id`` for this query to match terms assigned to bins.

        :param bin_id: the bin ``Id``
        :type bin_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bin_id_terms(self):
        """Clears the bin ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_id_terms = property(fdel=clear_bin_id_terms)

    @abc.abstractmethod
    def supports_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        :return: ``true`` if a bin query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuery

    bin_query = property(fget=get_bin_query)

    @abc.abstractmethod
    def clear_bin_terms(self):
        """Clears the bin terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_terms = property(fdel=clear_bin_terms)

    @abc.abstractmethod
    def get_resource_relationship_query_record(self, resource_relationship_record_type):
        """Gets the resource relationship query record corresponding to the given ``ResourceRelationship`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param resource_relationship_record_type: a resource relationship query record type
        :type resource_relationship_record_type: ``osid.type.Type``
        :return: the resource relationship query record
        :rtype: ``osid.resource.records.ResourceRelationshipQueryRecord``
        :raise: ``NullArgument`` -- ``resource_relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.ResourceRelationshipQueryRecord


class BinQuery:
    """This is the query for searching bins.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    @abc.abstractmethod
    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    @abc.abstractmethod
    def match_any_resource(self, match):
        """Matches bins with any resource.

        :param match: ``true`` to match bins with any resource, ``false`` to match bins with no resources
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)

    @abc.abstractmethod
    def match_ancestor_bin_id(self, binid, match):
        """Sets the bin ``Id`` for this query to match bins that have the specified bin as an ancestor.

        :param binid: a bin ``Id``
        :type binid: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_bin_id_terms(self):
        """Clears the ancestor bin ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bin_id_terms = property(fdel=clear_ancestor_bin_id_terms)

    @abc.abstractmethod
    def supports_ancestor_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        :return: ``true`` if a bin query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuery

    ancestor_bin_query = property(fget=get_ancestor_bin_query)

    @abc.abstractmethod
    def match_any_ancestor_bin(self, match):
        """Matches bins with any ancestor.

        :param match: ``true`` to match bins with any ancestor, ``false`` to match root bins
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_bin_terms(self):
        """Clears the ancestor bin terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bin_terms = property(fdel=clear_ancestor_bin_terms)

    @abc.abstractmethod
    def match_descendant_bin_id(self, binid, match):
        """Sets the bin ``Id`` for this query to match bins that have the specified bin as a descendant.

        :param binid: a bin ``Id``
        :type binid: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_bin_id_terms(self):
        """Clears the descendant bin ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bin_id_terms = property(fdel=clear_descendant_bin_id_terms)

    @abc.abstractmethod
    def supports_descendant_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        :return: ``true`` if a bin query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_bin_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_bin_query()`` is ``true``.*

        """
        return  # osid.resource.BinQuery

    descendant_bin_query = property(fget=get_descendant_bin_query)

    @abc.abstractmethod
    def match_any_descendant_bin(self, match):
        """Matches bins with any descendant.

        :param match: ``true`` to match bins with any descendant, ``false`` to match leaf bins
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_bin_terms(self):
        """Clears the descendant bin terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bin_terms = property(fdel=clear_descendant_bin_terms)

    @abc.abstractmethod
    def get_bin_query_record(self, bin_record_type):
        """Gets the bin query record corresponding to the given ``Bin`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin query record
        :rtype: ``osid.resource.records.BinQueryRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.records.BinQueryRecord
