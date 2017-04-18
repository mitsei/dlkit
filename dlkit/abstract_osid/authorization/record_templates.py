"""Implementations of authorization abstract base class records."""
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


class AuthorizationRecord:
    """A record for an ``Authorization`` The methods specified by the record type are available through the underlying object."""
    __metaclass__ = abc.ABCMeta


class AuthorizationQueryRecord:
    """A record for an ``AuthorizationQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationQueryInspectorRecord:
    """A record for an ``AuthorizationQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationFormRecord:
    """A record for an ``AuthorizationForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationSearchOrderRecord:
    """A record for an ``AuthorizationSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationSearchRecord:
    """A record for an ``AuthorizationSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationSearchResultsRecord:
    """A record for an ``AuthorizationSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class AuthorizationConditionRecord:
    """A record for an ``AuthorizationCondition``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionRecord:
    """A record for a ``Function``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionQueryRecord:
    """A record for a ``FunctionQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionQueryInspectorRecord:
    """A record for a ``FunctionQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionFormRecord:
    """A record for a ``FunctionForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionSearchOrderRecord:
    """A record for a ``FunctionSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionSearchRecord:
    """A record for a ``FunctionSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class FunctionSearchResultsRecord:
    """A record for a ``FunctionSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierRecord:
    """A record for a ``Qualifier``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierQueryRecord:
    """A record for a ``QualifierQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierQueryInspectorRecord:
    """A record for a ``QualifierQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierFormRecord:
    """A record for a ``QualifierForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierSearchOrderRecord:
    """A record for a ``QualifierSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierSearchRecord:
    """A record for a ``QualifierSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class QualifierSearchResultsRecord:
    """A record for a ``QualifierSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultRecord:
    """A record for a ``Vault``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultQueryRecord:
    """A record for a ``VaultQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultQueryInspectorRecord:
    """A record for a ``VaultQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultFormRecord:
    """A record for a ``VaultForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultSearchOrderRecord:
    """A record for a ``VaultSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultSearchRecord:
    """A record for a ``VaultSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class VaultSearchResultsRecord:
    """A record for a ``VaultSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
