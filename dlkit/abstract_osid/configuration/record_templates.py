"""Implementations of configuration abstract base class records."""
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


class ParameterRecord:
    """A record for a ``Parameter``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterQueryRecord:
    """A record for a ``ParameterQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterQueryInspectorRecord:
    """A record for a ``ParameterQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterFormRecord:
    """A record for a ``ParameterForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterSearchOrderRecord:
    """A record for a ``ParameterSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterSearchRecord:
    """A record for a ``ParameterSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ParameterSearchResultsRecord:
    """A record for a ``ParameterSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueRecord:
    """A record for a ``Value``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueQueryRecord:
    """A record for a ``ValueQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueQueryInspectorRecord:
    """A record for a ``ValueQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueFormRecord:
    """A record for a ``ValuerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueSearchOrderRecord:
    """A record for a ``ValueSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueSearchRecord:
    """A record for a ``ValueSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueSearchResultsRecord:
    """A record for a ``ValueSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ValueConditionRecord:
    """A record for a ``ValueCondition``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationRecord:
    """A record for a ``Configuration``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationQueryRecord:
    """A record for a ``ConfigurationQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationQueryInspectorRecord:
    """A record for a ``ConfigurationQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationFormRecord:
    """A record for a ``ConfigurationForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationSearchOrderRecord:
    """A record for a ``ConfigurationSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationSearchRecord:
    """A record for a ``ConfigurationSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ConfigurationSearchResultsRecord:
    """A record for a ``ConfigurationSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
