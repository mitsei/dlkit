"""Implementations of osid abstract base class rules."""
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


class OsidCondition:
    """The ``OsidCondition`` is used to input conditions into a rule for evaluation."""
    __metaclass__ = abc.ABCMeta


class OsidInput:
    """The ``OsidInput`` is used to input conditions into a rule for processing."""
    __metaclass__ = abc.ABCMeta


class OsidResult:
    """The ``OsidResult`` is used to retrieve the result of processing a rule."""
    __metaclass__ = abc.ABCMeta
