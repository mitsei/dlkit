"""JSON implementations of relationship objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import importlib


from . import default_mdata
from .. import utilities
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.relationship import objects as abc_relationship_objects
from dlkit.primordium.id.primitives import Id


class Relationship(abc_relationship_objects.Relationship, osid_objects.OsidRelationship):
    """A ``Relationship`` is an object between two peers.

    The genus type indicates the relationship between the peer and the
    related peer.

    """
    _namespace = 'relationship.Relationship'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='RELATIONSHIP', **kwargs)
        self._catalog_name = 'Family'

    def get_source_id(self):
        """Gets the from peer ``Id`` in this relationship.

        return: (osid.id.Id) - the peer
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['sourceId'])

    source_id = property(fget=get_source_id)

    def get_destination_id(self):
        """Gets the to peer ``Id`` in this relationship.

        return: (osid.id.Id) - the related peer
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['destinationId'])

    destination_id = property(fget=get_destination_id)

    @utilities.arguments_not_none
    def get_relationship_record(self, relationship_record_type):
        """Gets the relationshop record corresponding to the given ``Relationship`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``relationship_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(relationship_record_type)`` is ``true`` .

        arg:    relationship_record_type (osid.type.Type): the type of
                relationship record to retrieve
        return: (osid.relationship.records.RelationshipRecord) - the
                relationship record
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(relationship_record_type)


class RelationshipForm(abc_relationship_objects.RelationshipForm, osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Relationships``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RelationshipAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'relationship.Relationship'

    def __init__(self, **kwargs):
        osid_objects.OsidRelationshipForm.__init__(self, object_name='RELATIONSHIP', **kwargs)
        self._mdata = default_mdata.get_relationship_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidRelationshipForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidRelationshipForm._init_map(self, record_types=record_types)
        self._my_map['sourceId'] = str(kwargs['source_id'])
        self._my_map['destinationId'] = str(kwargs['destination_id'])
        self._my_map['assignedFamilyIds'] = [str(kwargs['family_id'])]

    @utilities.arguments_not_none
    def get_relationship_form_record(self, relationship_record_type):
        """Gets the ``RelationshipFormRecord`` corresponding to the given relationship record ``Type``.

        arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        return: (osid.relationship.records.RelationshipFormRecord) - the
                relationship form record
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(relationship_record_type)


class RelationshipList(abc_relationship_objects.RelationshipList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``Relationship`` provides a means for accessing ``Relationship`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Relationship relationship =
    rl.getNextRelationship(); }

    or
      while (rl.hasNext()) {
           Relationship[] relationships = rl.getNextRelationships(rl.available());
      }

    """

    def get_next_relationship(self):
        """Gets the next ``Relationship`` in this list.

        return: (osid.relationship.Relationship) - the next
                ``Relationship`` in this list. The ``has_next()`` method
                should be used to test that a next ``Relationship`` is
                available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Relationship)

    __next__ = next

    next_relationship = property(fget=get_next_relationship)

    @utilities.arguments_not_none
    def get_next_relationships(self, n):
        """Gets the next set of ``Relationships`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Relationship`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.relationship.Relationship) - an array of
                ``Relationship`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(RelationshipList, number=n)


class Family(abc_relationship_objects.Family, osid_objects.OsidCatalog):
    """A ``Family`` represents a collection of relationships.

    Like all OSID objects, a ``Family`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    _namespace = 'relationship.Family'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='FAMILY', **kwargs)

    @utilities.arguments_not_none
    def get_family_record(self, family_record_type):
        """Gets the famly record corresponding to the given ``Family`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``family_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(family_record_type)``
        is ``true`` .

        arg:    family_record_type (osid.type.Type): the type of family
                record to retrieve
        return: (osid.relationship.records.FamilyRecord) - the family
                record
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``has_record_type(family_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class FamilyForm(abc_relationship_objects.FamilyForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Family`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FamilyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'relationship.Family'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='FAMILY', **kwargs)
        self._mdata = default_mdata.get_family_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidCatalogForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_map(self, record_types, **kwargs)

    @utilities.arguments_not_none
    def get_family_form_record(self, family_record_type):
        """Gets the ``FamilyFormRecord`` corresponding to the given family record ``Type``.

        arg:    family_record_type (osid.type.Type): the family record
                type
        return: (osid.relationship.records.FamilyFormRecord) - the
                family form record
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``has_record_type(family_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class FamilyList(abc_relationship_objects.FamilyList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``FamilyList`` provides a means for accessing ``Family`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Family family = fl.getNextFamily();
    }

    or
      while (fl.hasNext()) {
           Family[] families = fl.getNextFamilies(fl.available());
      }

    """

    def get_next_family(self):
        """Gets the next ``Family`` in this list.

        return: (osid.relationship.Family) - the next ``Family`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Family`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Family)

    __next__ = next

    next_family = property(fget=get_next_family)

    @utilities.arguments_not_none
    def get_next_families(self, n):
        """Gets the next set of ``Family elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Family`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.relationship.Family) - an array of ``Family``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(FamilyList, number=n)


class FamilyNode(abc_relationship_objects.FamilyNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``FamilyHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_family().get_object_map())
        node_map['type'] = 'FamilyNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for family_node in self.get_parent_family_nodes():
            node_map['parentNodes'].append(family_node.get_object_node_map())
        for family_node in self.get_child_family_nodes():
            node_map['childNodes'].append(family_node.get_object_node_map())
        return node_map

    def get_family(self):
        """Gets the ``Family`` at this node.

        return: (osid.relationship.Family) - the family represented by
                this node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('RELATIONSHIP', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_family_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_family(Id(self._my_map['id']))

    family = property(fget=get_family)

    def get_parent_family_nodes(self):
        """Gets the parents of this family.

        return: (osid.relationship.FamilyNodeList) - the parents of the
                ``id``
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_family_nodes = []
        for node in self._my_map['parentNodes']:
            parent_family_nodes.append(FamilyNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return FamilyNodeList(parent_family_nodes)

    parent_family_nodes = property(fget=get_parent_family_nodes)

    def get_child_family_nodes(self):
        """Gets the children of this family.

        return: (osid.relationship.FamilyNodeList) - the children of
                this family
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_family_nodes = []
        for node in self._my_map['childNodes']:
            parent_family_nodes.append(FamilyNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return FamilyNodeList(parent_family_nodes)

    child_family_nodes = property(fget=get_child_family_nodes)


class FamilyNodeList(abc_relationship_objects.FamilyNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``FamilyNodeList`` provides a means for accessing ``FamilyNode`` elements sequentially either one at a time or many at a time.

    Examples: while (fnl.hasNext()) { FamilyNode node =
    fnl.getNextFamilyNode(); }

    or
      while (fnl.hasNext()) {
           FamilyNode[] nodes = fnl.getNextFamilyNodes(fnl.available());
      }

    """

    def get_next_family_node(self):
        """Gets the next ``FamilyNode`` in this list.

        return: (osid.relationship.FamilyNode) - the next ``FamilyNode``
                in this list. The ``has_next()`` method should be used
                to test that a next ``FamilyNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(FamilyNode)

    __next__ = next

    next_family_node = property(fget=get_next_family_node)

    @utilities.arguments_not_none
    def get_next_family_nodes(self, n):
        """Gets the next set of ``FamilyNode elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``FamilyNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.relationship.FamilyNode) - an array of
                ``FamilyNode`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(FamilyNodeList, number=n)
