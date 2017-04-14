import abc
from ..osid import records as osid_records


class ProxyRecord(osid_records.OsidRecord):
    """A record for a ``Proxy``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProxyConditionRecord(osid_records.OsidRecord):
    """A record for a ``ProxyCondition``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
