"""Manager utility implementations of osid markers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .osid_errors import Unimplemented
from dlkit.abstract_osid.osid import markers as abc_osid_markers


class Sourceable(abc_osid_markers.Sourceable):
    """``Sourceble`` is used for ``OsidObjects`` where information about a provider is appropriate.

    Examples of ``Sourceables`` are catalogs, compositions, and
    services.

    """

    def get_provider_id(self):
        """Gets the ``Id`` of the provider.

        return: (osid.id.Id) - the provider ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        """Gets the ``Resource`` representing the provider.

        return: (osid.resource.Resource) - the provider
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        """Gets the branding asset ``Ids``.

        return: (osid.id.IdList) - a list of asset ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        """Gets a branding, such as an image or logo, expressed using the ``Asset`` interface.

        return: (osid.repository.AssetList) - a list of assets
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """

    branding = property(fget=get_branding)

    def get_license(self):
        """Gets the terms of usage.

        An empty license means the terms are unknown.

        return: (osid.locale.DisplayText) - the license
        *compliance: mandatory -- This method must be implemented.*

        """

    license_ = property(fget=get_license)
