"""Implementations of authentication abstract base class records."""
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


class AgentRecord:
    """A record for an ``Agent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentQueryRecord:
    """A record for an ``AgentQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentQueryInspectorRecord:
    """A record for an ``AgentQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentFormRecord:
    """A record for an ``AgentForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentSearchOrderRecord:
    """A record for an ``AgentSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentSearchRecord:
    """A record for an ``AgentSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgentSearchResultsRecord:
    """A record for an ``AgentSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencyRecord:
    """A record for an ``Agency``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencyQueryRecord:
    """A record for an ``AgencyQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencyQueryInspectorRecord:
    """A record for an ``AgencyQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencyFormRecord:
    """A record for an ``AgencyForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencySearchOrderRecord:
    """A record for an ``AgencySearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencySearchRecord:
    """A record for an ``AgencySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AgencySearchResultsRecord:
    """A record for an ``AgencySearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
