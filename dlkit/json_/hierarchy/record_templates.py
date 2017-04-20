"""JSON implementations of hierarchy records."""

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
from dlkit.abstract_osid.hierarchy import records as abc_hierarchy_records


class HierarchyRecord(abc_hierarchy_records.HierarchyRecord, osid_records.OsidRecord):
    """A record for a ``Hierarchy``.

    The methods specified by the record type are available through the
    underlying object.

    """


class HierarchyQueryRecord(abc_hierarchy_records.HierarchyQueryRecord, osid_records.OsidRecord):
    """A record for a ``HierarchyQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """


class HierarchyFormRecord(abc_hierarchy_records.HierarchyFormRecord, osid_records.OsidRecord):
    """A record for a ``HierarchyForm``.

    The methods specified by the record type are available through the
    underlying object.

    """


class HierarchySearchRecord(abc_hierarchy_records.HierarchySearchRecord, osid_records.OsidRecord):
    """A record for a ``HierarchySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
