"""Implementations of cataloging abstract base class objects."""
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


class Catalog:
    """A ``Catalog`` represents a collection of entries.

    Like all OSID objects, a ``Catalog`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    ``get_catalog_record()`` should be used to retrieve any record
    corresponding to arecord ``Type``. The existence of the record must
    not be assumed until requested at which point it is safe to cast
    into the record indicated by the type.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_record(self, catalog_record_type):
        """Gets the catalog record corresponding to the given ``Catalog`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``catalog_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(catalog_record_type)`` is ``true`` .

        :param catalog_record_type: a type of the record to retrieve
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog record
        :rtype: ``osid.cataloging.records.CatalogRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogRecord


class CatalogForm:
    """This is the form for creating and updating ``Catalogs``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CatalogAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog_form_record(self, catalog_record_type):
        """Gets the ``CatalogFormRecord`` corresponding to the given catalog record ``Type``.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog form record
        :rtype: ``osid.cataloging.records.CatalogFormRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogFormRecord


class CatalogList:
    """Like all ``OsidLists,``  ``CatalogList`` provides a means for accessing ``Catalog`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Catalog catalog =
    cl.getNextCatalog(); }

    or
      while (cl.hasNext()) {
           Catalog[] catalogs = cl.getNextCatalogs(cl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_catalog(self):
        """Gets the next ``Catalog`` in this list.

        :return: the next ``Catalog`` in this list. The ``has_next()`` method should be used to test that a next ``Catalog`` is available before calling this method.
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog

    next_catalog = property(fget=get_next_catalog)

    @abc.abstractmethod
    def get_next_catalogs(self, n):
        """Gets the next set of ``Catalog`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Catalog`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Catalog`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog


class CatalogNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``CatalogHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_catalog(self):
        """Gets the ``Catalog`` at this node.

        :return: the catalog represented by this node
        :rtype: ``osid.cataloging.Catalog``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog

    catalog = property(fget=get_catalog)

    @abc.abstractmethod
    def get_parent_catalog_nodes(self):
        """Gets the parents of this catalog.

        :return: the parents of the ``id``
        :rtype: ``osid.cataloging.CatalogNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNodeList

    parent_catalog_nodes = property(fget=get_parent_catalog_nodes)

    @abc.abstractmethod
    def get_child_catalog_nodes(self):
        """Gets the children of this catalog.

        :return: the children of this catalog
        :rtype: ``osid.cataloging.CatalogNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNodeList

    child_catalog_nodes = property(fget=get_child_catalog_nodes)


class CatalogNodeList:
    """Like all ``OsidLists,``  ``CatalogNodeList`` provides a means for accessing ``CatalogNode`` elements sequentially either one at a time or many at a time.

    Examples: while (cnl.hasNext()) { CatalogNode node =
    cnl.getNextCatalogNode(); }

    or
      while (cnl.hasNext()) {
           CatalogNode[] nodes = cnl.getNextCatalogNodes(cnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_catalog_node(self):
        """Gets the next ``CatalogNode`` in this list.

        :return: the next ``CatalogNode`` in this list. The ``has_next()`` method should be used to test that a next ``CatalogNode`` is available before calling this method.
        :rtype: ``osid.cataloging.CatalogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNode

    next_catalog_node = property(fget=get_next_catalog_node)

    @abc.abstractmethod
    def get_next_catalog_nodes(self, n):
        """Gets the next set of ``CatalogNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``CatalogNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``CatalogNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.cataloging.CatalogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNode
