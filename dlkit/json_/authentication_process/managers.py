"""JSON implementations of authentication.process managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import profile
from . import sessions
from .. import utilities
from ..osid import managers as osid_managers
from ..primitives import Type
from ..type.objects import TypeList
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.authentication_process import managers as authentication_process_managers


class AuthenticationProcessProfile(osid_managers.OsidProfile, authentication_process_managers.AuthenticationProcessProfile):
    """The ``AuthenticationProcessProfile`` describes the interoperability among authentication process services."""

    def get_authentication_record_types(self):
        """Gets the supported authentication record types.

        return: (osid.type.TypeList) - a list containing the supported
                authentication record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AUTHENTICATION_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    authentication_record_types = property(fget=get_authentication_record_types)

    def get_authentication_input_record_types(self):
        """Gets the supported authentication input record types.

        return: (osid.type.TypeList) - a list containing the supported
                authentication input record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('AUTHENTICATION_INPUT_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    def get_challenge_record_types(self):
        """Gets the supported challenge types.

        return: (osid.type.TypeList) - a list containing the supported
                challenge types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('CHALLENGE_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    challenge_record_types = property(fget=get_challenge_record_types)

    def get_credential_types(self):
        """Gets the supported credential types.

        return: (osid.type.TypeList) - a list containing the supported
                credential types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    credential_types = property(fget=get_credential_types)

    def get_trust_types(self):
        """Gets the supported trust types.

        return: (osid.type.TypeList) - a list containing the supported
                trust types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    trust_types = property(fget=get_trust_types)


class AuthenticationProcessManager(osid_managers.OsidManager, AuthenticationProcessProfile, authentication_process_managers.AuthenticationProcessManager):
    """The authentication process manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AuthenticationAcquisitionSession:`` a session to acquire
        credentials from a user and serialize them for transport to a
        remote peer for authentication
      * ``AuthenticationValidationSession: a`` session to receive and
        validate authentication credentials from a remote peer wishing
        to authenticate
      * ``TrustLookupSession:`` a session to look up authentication
        circles of trust
      * ``CircleOfTrustSession:`` a session to examine agent circles of
        trust

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)


class AuthenticationProcessProxyManager(osid_managers.OsidProxyManager, AuthenticationProcessProfile, authentication_process_managers.AuthenticationProcessProxyManager):
    """The authentication process proxy manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AuthenticationAcquisitionSession:`` session to acquire
        credentials from a user and serialize them for transport to a
        remote peer for authentication
      * ``AuthenticationValidationSession:`` session to receive and
        validate authentication credentials from a remote peer wishing
        to authenticate
      * ``TrustLookupSession:`` a session to look up authentication
        circles of trust
      * ``CircleOfTrustSession:`` a session to examine agent circles of
        trust

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)
