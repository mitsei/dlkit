"""Implementations of grading abstract base class records."""
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


class GradeRecord:
    """A record for a ``Grade``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeQueryRecord:
    """A record for a ``GradeQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeQueryInspectorRecord:
    """A record for a ``GradeQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeFormRecord:
    """A record for a ``GradeForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSearchOrderRecord:
    """A record for a ``GradeSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemRecord:
    """A record for a ``GradeSystem``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemQueryRecord:
    """A record for a ``GradeSystemQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemQueryInspectorRecord:
    """A record for a ``GradeSystemQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemFormRecord:
    """A record for a ``GradeSystemForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemSearchOrderRecord:
    """A record for a ``GradeSystemSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemSearchRecord:
    """A record for a ``GradeSystemSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeSystemSearchResultsRecord:
    """A record for a ``GradeSystemSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntryRecord:
    """A record for a ``GradeEntry``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntryQueryRecord:
    """A record for a ``GradeEntryQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntryQueryInspectorRecord:
    """A record for a ``GradeEntryQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntryFormRecord:
    """A record for a ``GradeEntryForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntrySearchOrderRecord:
    """A record for a ``GradeEntrySearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntrySearchRecord:
    """A record for a ``GradeEntrySearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradeEntrySearchResultsRecord:
    """A record for a ``GradeEntrySearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnRecord:
    """A record for a ``GradebookColumn``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnQueryRecord:
    """A record for a ``GradebookColumnQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnQueryInspectorRecord:
    """A record for a ``GradebookColumnQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnFormRecord:
    """A record for a ``GradebookColumnForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSearchOrderRecord:
    """A record for a ``GradebookColumnSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSearchRecord:
    """A record for a ``GradebookColumnSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSearchResultsRecord:
    """A record for a ``GradebookColumnSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSummaryRecord:
    """A record for a ``GradebookColumnSummary``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSummaryQueryRecord:
    """A record for a ``GradebookColumnSummaryQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSummaryQueryInspectorRecord:
    """A record for a ``GradebookColumnSummaryQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookColumnSummarySearchOrderRecord:
    """A record for a ``GradebookColumnSummarySearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookRecord:
    """A record for a ``Gradebook``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookQueryRecord:
    """A record for a ``GradebookQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookQueryInspectorRecord:
    """A record for a ``GradebookQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookFormRecord:
    """A record for a ``GradebookForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookSearchOrderRecord:
    """A record for a ``GradebookSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookSearchRecord:
    """A record for a ``GradebookSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class GradebookSearchResultsRecord:
    """A record for a ``GradebookSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
