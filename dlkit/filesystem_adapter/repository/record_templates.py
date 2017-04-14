"""repository.record_templates"""
# pylint: disable=too-few-public-methods

from ...abstract_osid.repository import records as abc_repository_records
from ..osid import records as osid_records


class AssetRecord(abc_repository_records.AssetRecord, osid_records.OsidRecord):
    """A record for an ``Asset``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetRecord, self).__init__()


class AssetQueryRecord(abc_repository_records.AssetQueryRecord, osid_records.OsidRecord):
    """A record for an ``AssetQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetQueryRecord, self).__init__()


class AssetFormRecord(abc_repository_records.AssetFormRecord, osid_records.OsidRecord):
    """A record for an ``AssetForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetFormRecord, self).__init__()


class AssetContentRecord(abc_repository_records.AssetContentRecord, osid_records.OsidRecord):
    """A record for an ``AssetContent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetContentRecord, self).__init__()


class AssetContentQueryRecord(abc_repository_records.AssetContentQueryRecord,
                              osid_records.OsidRecord):
    """A record for an ``AssetContentQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetContentQueryRecord, self).__init__()


class AssetContentFormRecord(abc_repository_records.AssetContentFormRecord,
                             osid_records.OsidRecord):
    """A record for an ``AssetForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(AssetContentFormRecord, self).__init__()


class RepositoryRecord(abc_repository_records.RepositoryRecord,
                       osid_records.OsidRecord):
    """A record for a ``Repository``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(RepositoryRecord, self).__init__()


class RepositoryQueryRecord(abc_repository_records.RepositoryQueryRecord,
                            osid_records.OsidRecord):
    """A record for a ``RepositoryQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(RepositoryQueryRecord, self).__init__()


class RepositoryFormRecord(abc_repository_records.RepositoryFormRecord,
                           osid_records.OsidRecord):
    """A record for a ``RepositoryForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    def __init__(self):
        super(RepositoryFormRecord, self).__init__()
