"""JSON implementations of logging records."""

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
from dlkit.abstract_osid.logging_ import records as abc_logging_records


class LogEntryRecord(abc_logging_records.LogEntryRecord, osid_records.OsidRecord):
    """A record for a ``LogEntry``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogEntryQueryRecord(abc_logging_records.LogEntryQueryRecord, osid_records.OsidRecord):
    """A record for a ``LoglEntryQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogEntryFormRecord(abc_logging_records.LogEntryFormRecord, osid_records.OsidRecord):
    """A record for a ``LogEntryForm``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogEntrySearchRecord(abc_logging_records.LogEntrySearchRecord, osid_records.OsidRecord):
    """A record for a ``LogEntrySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogRecord(abc_logging_records.LogRecord, osid_records.OsidRecord):
    """A record for a ``Log``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogQueryRecord(abc_logging_records.LogQueryRecord, osid_records.OsidRecord):
    """A record for a ``LogQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogFormRecord(abc_logging_records.LogFormRecord, osid_records.OsidRecord):
    """A record for a ``LogForm``.

    The methods specified by the record type are available through the
    underlying object.

    """


class LogSearchRecord(abc_logging_records.LogSearchRecord, osid_records.OsidRecord):
    """A record for a ``LogSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
