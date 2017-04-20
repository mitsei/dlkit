"""JSON implementations of authentication.process records."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import records as osid_records
from dlkit.abstract_osid.authentication_process import records as abc_authentication_process_records


class AuthenticationRecord(abc_authentication_process_records.AuthenticationRecord, osid_records.OsidRecord):
    """A record for an ``Authentication``.

    The methods specified by the record type are available through the
    underlying object.

    """
