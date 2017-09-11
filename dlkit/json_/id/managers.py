"""JSON implementations of id managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import managers as osid_managers
from dlkit.manager_impls.id import managers as id_managers


class IdProfile(osid_managers.OsidProfile, id_managers.IdProfile):
    """The ``IdProfile`` describes the interoperability among id services."""


class IdManager(osid_managers.OsidManager, IdProfile, id_managers.IdManager):
    """This manager provides access to the available sessions of the Id service.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier.

    The ``IdLookupSession`` can be used for mapping one ``Id`` to
    another in addition to getting a list of the assigned identifiers.

    """

    def get_id_batch_manager(self):
        """Gets an ``IdBatchManager``.

        return: (osid.id.batch.IdBatchManager) - an ``IdBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_id_batch()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    id_batch_manager = property(fget=get_id_batch_manager)


class IdProxyManager(osid_managers.OsidProxyManager, IdProfile, id_managers.IdProxyManager):
    """This manager provides access to the available sessions of the Id service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of pasisng information from a server envrionment.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier. The ``IdBrowserSession``
    can be used for mapping one ``Id`` to another in addition to getting
    a list of the assigned identifiers.

    """

    def get_id_batch_proxy_manager(self):
        """Gets an ``IdnProxyManager``.

        return: (osid.id.batch.IdBatchProxyManager) - an
                ``IdBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_id_batch()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)
