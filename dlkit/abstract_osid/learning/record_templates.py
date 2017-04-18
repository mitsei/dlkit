"""Implementations of learning abstract base class records."""
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


class ObjectiveRecord:
    """A record for an ``Objective``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveQueryRecord:
    """A record for an ``ObjectiveQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveQueryInspectorRecord:
    """A record for an ``ObjectiveQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveFormRecord:
    """A record for an ``ObjectiveForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveSearchOrderRecord:
    """A record for an ``ObjectiveSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveSearchRecord:
    """A record for an ``ObjectiveSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveSearchResultsRecord:
    """A record for an ``ObjectiveSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivityRecord:
    """A record for a ``Activity``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivityQueryRecord:
    """A record for an ``ActivityQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivityQueryInspectorRecord:
    """A record for an ``ActivityQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivityFormRecord:
    """A record for a ``ActivityForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivitySearchOrderRecord:
    """A record for an ``ActivitySearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivitySearchRecord:
    """A record for an ``ActivitySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ActivitySearchResultsRecord:
    """A record for an ``ActivitySearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencyRecord:
    """A record for a ``Proficiency``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencyQueryRecord:
    """A record for a ``ProficiencyQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencyQueryInspectorRecord:
    """A record for a ``ProficiencyQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencyFormRecord:
    """A record for a ``ProficiencyForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencySearchOrderRecord:
    """A record for a ``ProficiencySearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencySearchRecord:
    """A record for a ``ProficiencySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ProficiencySearchResultsRecord:
    """A record for a ``ProficiencySearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankRecord:
    """A record for a ``ObjectiveBank``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankQueryRecord:
    """A record for an ``ObjectiveBankQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankQueryInspectorRecord:
    """A record for an ``ObjectiveBankQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankFormRecord:
    """A record for a ``ObjectiveBankForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankSearchOrderRecord:
    """A record for a ``ObjectiveBankSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankSearchRecord:
    """A record for a ``ObjectiveBankSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ObjectiveBankSearchResultsRecord:
    """A record for a ``ObjectiveBankSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
