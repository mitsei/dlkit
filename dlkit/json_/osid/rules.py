"""JSON implementations of osid rules."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import inflection


from .. import utilities
from ..osid import markers as osid_markers
from dlkit.abstract_osid.osid import rules as abc_osid_rules
from dlkit.primordium.type.primitives import Type


class OsidCondition(abc_osid_rules.OsidCondition, osid_markers.Extensible, osid_markers.Suppliable):
    """The ``OsidCondition`` is used to input conditions into a rule for evaluation."""
    def __new__(cls, record_key, runtime=None, **kwargs):
        object_name = cls._namespace.split('.')[-1]
        record_types = [Type(data_set) for data_set in utilities.get_registry(
            inflection.underscore(object_name).upper() + '_RECORD_TYPES',
            runtime)]
        return osid_markers.Extensible.__new__(cls, object_name, record_key, record_types, runtime)


class OsidInput(abc_osid_rules.OsidInput, osid_markers.Extensible, osid_markers.Suppliable):
    """The ``OsidInput`` is used to input conditions into a rule for processing."""


class OsidResult(abc_osid_rules.OsidResult, osid_markers.Extensible, osid_markers.Browsable):
    """The ``OsidResult`` is used to retrieve the result of processing a rule."""
    def __new__(cls, record_key, runtime=None, **kwargs):
        object_name = cls._namespace.split('.')[-1]
        record_types = list()  # Need to get this from registry
        return osid_markers.Extensible.__new__(cls, object_name, record_key, record_types, runtime)

    def __init__(self, **kwargs):
        osid_markers.Extensible.__init__(self, **kwargs)
