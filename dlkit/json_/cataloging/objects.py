"""JSON implementations of cataloging objects."""

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
from ..primitives import Id
from ..utilities import get_provider_manager
from dlkit.abstract_osid.cataloging import objects as abc_cataloging_objects
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


class Catalog(abc_cataloging_objects.Catalog, osid_objects.OsidCatalog):
    """A ``Catalog`` represents a collection of entries.

    Like all OSID objects, a ``Catalog`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    ``get_catalog_record()`` should be used to retrieve any record
    corresponding to arecord ``Type``. The existence of the record must
    not be assumed until requested at which point it is safe to cast
    into the record indicated by the type.

    """
    _namespace = 'cataloging.Catalog'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='CATALOG', **kwargs)

    @utilities.arguments_not_none
    def get_catalog_record(self, catalog_record_type):
        """Gets the catalog record corresponding to the given ``Catalog`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``catalog_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(catalog_record_type)`` is ``true`` .

        arg:    catalog_record_type (osid.type.Type): a type of the
                record to retrieve
        return: (osid.cataloging.records.CatalogRecord) - the catalog
                record
        raise:  NullArgument - ``catalog_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(catalog_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CatalogForm(abc_cataloging_objects.CatalogForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Catalogs``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CatalogAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'cataloging.Catalog'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='CATALOG', **kwargs)
        self._mdata = default_mdata.get_catalog_mdata()
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
    def get_catalog_form_record(self, catalog_record_type):
        """Gets the ``CatalogFormRecord`` corresponding to the given catalog record ``Type``.

        arg:    catalog_record_type (osid.type.Type): a catalog record
                type
        return: (osid.cataloging.records.CatalogFormRecord) - the
                catalog form record
        raise:  NullArgument - ``catalog_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(catalog_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class CatalogList(abc_cataloging_objects.CatalogList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CatalogList`` provides a means for accessing ``Catalog`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Catalog catalog =
    cl.getNextCatalog(); }

    or
      while (cl.hasNext()) {
           Catalog[] catalogs = cl.getNextCatalogs(cl.available());
      }

    """

    def get_next_catalog(self):
        """Gets the next ``Catalog`` in this list.

        return: (osid.cataloging.Catalog) - the next ``Catalog`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Catalog`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Catalog)

    __next__ = next

    next_catalog = property(fget=get_next_catalog)

    @utilities.arguments_not_none
    def get_next_catalogs(self, n):
        """Gets the next set of ``Catalog`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Catalog`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.cataloging.Catalog) - an array of ``Catalog``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(CatalogList, number=n)


class CatalogNode(abc_cataloging_objects.CatalogNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``CatalogHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_catalog().get_object_map())
        node_map['type'] = 'CatalogNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for catalog_node in self.get_parent_catalog_nodes():
            node_map['parentNodes'].append(catalog_node.get_object_node_map())
        for catalog_node in self.get_child_catalog_nodes():
            node_map['childNodes'].append(catalog_node.get_object_node_map())
        return node_map

    def get_catalog(self):
        """Gets the ``Catalog`` at this node.

        return: (osid.cataloging.Catalog) - the catalog represented by
                this node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('CATALOGING', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_catalog_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_catalog(Id(self._my_map['id']))

    catalog = property(fget=get_catalog)

    def get_parent_catalog_nodes(self):
        """Gets the parents of this catalog.

        return: (osid.cataloging.CatalogNodeList) - the parents of the
                ``id``
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_catalog_nodes = []
        for node in self._my_map['parentNodes']:
            parent_catalog_nodes.append(CatalogNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return CatalogNodeList(parent_catalog_nodes)

    parent_catalog_nodes = property(fget=get_parent_catalog_nodes)

    def get_child_catalog_nodes(self):
        """Gets the children of this catalog.

        return: (osid.cataloging.CatalogNodeList) - the children of this
                catalog
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_catalog_nodes = []
        for node in self._my_map['childNodes']:
            parent_catalog_nodes.append(CatalogNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return CatalogNodeList(parent_catalog_nodes)

    child_catalog_nodes = property(fget=get_child_catalog_nodes)


class CatalogNodeList(abc_cataloging_objects.CatalogNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CatalogNodeList`` provides a means for accessing ``CatalogNode`` elements sequentially either one at a time or many at a time.

    Examples: while (cnl.hasNext()) { CatalogNode node =
    cnl.getNextCatalogNode(); }

    or
      while (cnl.hasNext()) {
           CatalogNode[] nodes = cnl.getNextCatalogNodes(cnl.available());
      }

    """

    def get_next_catalog_node(self):
        """Gets the next ``CatalogNode`` in this list.

        return: (osid.cataloging.CatalogNode) - the next ``CatalogNode``
                in this list. The ``has_next()`` method should be used
                to test that a next ``CatalogNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(CatalogNode)

    __next__ = next

    next_catalog_node = property(fget=get_next_catalog_node)

    @utilities.arguments_not_none
    def get_next_catalog_nodes(self, n):
        """Gets the next set of ``CatalogNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``CatalogNode`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.cataloging.CatalogNode) - an array of
                ``CatalogNode`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(CatalogNodeList, number=n)
