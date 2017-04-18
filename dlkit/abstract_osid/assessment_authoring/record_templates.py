"""Implementations of assessment.authoring abstract base class records."""
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


class AssessmentPartRecord:
    """A record for an ``AssessmentPart``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartQueryRecord:
    """A record for an ``AssessmentPartQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartQueryInspectorRecord:
    """A record for an ``AssessmentPartQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartFormRecord:
    """A record for an ``AssessmentPartForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartSearchOrderRecord:
    """A record for an ``AssessmentPartSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartSearchRecord:
    """A record for an ``AssessmentPartSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AssessmentPartSearchResultsRecord:
    """A record for an ``AssessmentPartSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleRecord:
    """A record for a ``SequenceRule``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleQueryRecord:
    """A record for a ``SequenceRuleQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleQueryInspectorRecord:
    """A record for a ``SequenceRuleQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleFormRecord:
    """A record for a ``SequenceRuleForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleSearchOrderRecord:
    """A record for a ``SequenceRuleSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleSearchRecord:
    """A record for a ``SequenceRuleSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleSearchResultsRecord:
    """A record for a ``SequenceRuleSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerRecord:
    """A record for a ``SequenceRuleEnabler``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerQueryRecord:
    """A record for a ``SequenceRuleEnablerQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerQueryInspectorRecord:
    """A record for a ``SequenceRuleEnablerQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerSearchOrderRecord:
    """A record for a ``SequenceRuleEnablerSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerSearchRecord:
    """A record for a ``SequenceRuleEnablerSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SequenceRuleEnablerSearchResultsRecord:
    """A record for a ``SequenceRuleEnablerSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
