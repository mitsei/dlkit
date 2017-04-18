"""Implementations of mapping abstract base class records."""
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


class LocationRecord:
    """A record for a ``Location``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationQueryRecord:
    """A record for a ``LocationQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationQueryInspectorRecord:
    """A record for a ``LocationInspectorQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationFormRecord:
    """A record for a ``LocationForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationSearchOrderRecord:
    """A record for a ``LocationSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationSearchRecord:
    """A record for a ``LocationSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class LocationSearchResultsRecord:
    """A record for a ``LocationSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapRecord:
    """A record for a ``MapRecord``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapQueryRecord:
    """A record for a ``MapQuery``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapQueryInspectorRecord:
    """A record for a ``MapQueryInspector``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapFormRecord:
    """A record for a ``MapForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapSearchOrderRecord:
    """A record for a ``MapSearchOrder``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapSearchRecord:
    """A record for a ``MapSearch``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class MapSearchResultsRecord:
    """A record for a ``MapSearchResults``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class ResourceLocationRecord:
    """A record for a ``ResourceLocationRecord``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta


class SpatialUnitRecord:
    """A record for a ``SpatialUnitRecord``.

    The methods specified by the record type are available through the
    underlying object.

    """
    __metaclass__ = abc.ABCMeta
