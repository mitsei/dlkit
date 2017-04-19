"""AuthZ Adapter implementations of osid markers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid.osid_errors import Unimplemented
from ..utilities import raise_null_argument
from dlkit.abstract_osid.osid import markers as abc_osid_markers


class Sourceable(abc_osid_markers.Sourceable):
    """Adapts underlying Sourceable methodswith authorization checks."""

    def get_provider_id(self):
        raise Unimplemented()

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        raise Unimplemented()

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        raise Unimplemented()

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        raise Unimplemented()

    branding = property(fget=get_branding)

    def get_license(self):
        raise Unimplemented()

    license_ = property(fget=get_license)
