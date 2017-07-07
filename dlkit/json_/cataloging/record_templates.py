"""JSON implementations of cataloging records."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import records as osid_records
from dlkit.abstract_osid.cataloging import records as abc_cataloging_records


class CatalogRecord(abc_cataloging_records.CatalogRecord, osid_records.OsidRecord):
    """A record for a ``Catalog``.

    The methods specified by the record type are available through the
    underlying object.

    """


class CatalogQueryRecord(abc_cataloging_records.CatalogQueryRecord, osid_records.OsidRecord):
    """A record for a ``CatalogQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """


class CatalogFormRecord(abc_cataloging_records.CatalogFormRecord, osid_records.OsidRecord):
    """A record for a ``CatalogForm``.

    The methods specified by the record type are available through the
    underlying object.

    """


class CatalogSearchRecord(abc_cataloging_records.CatalogSearchRecord, osid_records.OsidRecord):
    """A record for a ``CatalogSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
