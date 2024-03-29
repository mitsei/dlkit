"""Implementations of transport abstract base class records."""
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


class EndpointRecord:
    """A record for an ``Endpoint``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class RequestRecord:
    """A record for a ``Request``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ResponseRecord:
    """A record for a ``Response``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
