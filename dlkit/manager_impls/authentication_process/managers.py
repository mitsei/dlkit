"""Manager utility implementations of authentication.process managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.authentication_process import managers as abc_authentication_process_managers


class AuthenticationProcessProfile(abc_authentication_process_managers.AuthenticationProcessProfile, osid_managers.OsidProfile):
    """The ``AuthenticationProcessProfile`` describes the interoperability among authentication process services."""

    def supports_authentication_acquisition(self):
        """Tests if authentication acquisition is supported.

        Authentication acquisition is responsible for acquiring client
        side authentication credentials.

        return: (boolean) - ``true`` if authentication acquisiiton is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_authentication_validation(self):
        """Tests if authentication validation is supported.

        Authentication validation verifies given authentication
        credentials and maps to an agent identity.

        return: (boolean) - ``true`` if authentication validation is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_trust_lookup(self):
        """Tests if a trust look up session is supported.

        return: (boolean) - ``true`` if trust lookup is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_circle_of_trust(self):
        """Tests if a session to examine agent and trust relationships is supported.

        return: (boolean) - ``true`` if a circle of trust is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_challenge(self):
        """Tests if this authentication service supports a challenge- response mechanism where credential validation service must implement a means to generate challenge data.

        return: (boolean) - ``true`` if this is a challenge-response
                system, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_authentication_record_types(self):
        """Gets the supported authentication record types.

        return: (osid.type.TypeList) - a list containing the supported
                authentication record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    authentication_record_types = property(fget=get_authentication_record_types)

    def supports_authentication_record_type(self, authentication_record_type=None):
        """Tests if the given authentication record type is supported.

        arg:    authentication_record_type (osid.type.Type): a ``Type``
                indicating an authentication record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``authentication_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if authentication_record_type is None:
            raise NullArgument()
        return False

    def get_authentication_input_record_types(self):
        """Gets the supported authentication input record types.

        return: (osid.type.TypeList) - a list containing the supported
                authentication input record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    def supports_authentication_input_record_type(self, authentication_input_record_type=None):
        """Tests if the given authentication input record type is supported.

        arg:    authentication_input_record_type (osid.type.Type): a
                ``Type`` indicating an authentication input record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``authentication_input_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if authentication_input_record_type is None:
            raise NullArgument()
        return False

    def get_challenge_record_types(self):
        """Gets the supported challenge types.

        return: (osid.type.TypeList) - a list containing the supported
                challenge types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    challenge_record_types = property(fget=get_challenge_record_types)

    def supports_challenge_record_type(self, challenge_record_type=None):
        """Tests if the given challenge data type is supported.

        arg:    challenge_record_type (osid.type.Type): a ``Type``
                indicating a challenge record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``challenge_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if challenge_record_type is None:
            raise NullArgument()
        return False

    def supports_credential_export(self):
        """Tests if ``Authentication`` objects can export serialzied credentials for transport.

        return: (boolean) - ``true`` if the given credentials export is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_credential_types(self):
        """Gets the supported credential types.

        return: (osid.type.TypeList) - a list containing the supported
                credential types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    credential_types = property(fget=get_credential_types)

    def supports_credential_type(self, credential_type=None):
        """Tests if the given credential type is supported.

        arg:    credential_type (osid.type.Type): a ``Type`` indicating
                a credential type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``credential_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if credential_type is None:
            raise NullArgument()
        return False

    def get_trust_types(self):
        """Gets the supported trust types.

        return: (osid.type.TypeList) - a list containing the supported
                trust types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    trust_types = property(fget=get_trust_types)

    def supports_trust_type(self, trust_type=None):
        """Tests if the given trust type is supported.

        arg:    trust_type (osid.type.Type): a ``Type`` indicating a
                trust type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``trust_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if trust_type is None:
            raise NullArgument()
        return False


class AuthenticationProcessManager(abc_authentication_process_managers.AuthenticationProcessManager, osid_managers.OsidManager, AuthenticationProcessProfile):
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

    def get_authentication_acquisition_session(self):
        """Gets an ``AuthenticationAcquisitionSession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        return:
                (osid.authentication.process.AuthenticationAcquisitionSe
                ssion) - an acquisition session for this service
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authentication_acquisition()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_acquisition()`` is ``true``.*

        """
        raise Unimplemented()

    authentication_acquisition_session = property(fget=get_authentication_acquisition_session)

    def get_authentication_validation_session(self):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service.

        return:
                (osid.authentication.process.AuthenticationValidationSes
                sion) - an ``AuthenticationValidationSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_validation()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_validation()`` is ``true``.*

        """
        raise Unimplemented()

    authentication_validation_session = property(fget=get_authentication_validation_session)

    def get_trust_lookup_session(self):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        return: (osid.authentication.process.TrustLookupSession) - a
                ``TrustLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_trust_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    trust_lookup_session = property(fget=get_trust_lookup_session)

    def get_trust_lookup_session_for_agency(self, agency_id=None):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        return: (osid.authentication.process.TrustLookupSession) - a
                ``TrustLookupSession``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_trust_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if agency_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_circle_of_trust_session(self):
        """Gets the ``OsidSession`` associated with the trust circle service.

        return: (osid.authentication.process.CircleOfTrustSession) - a
                ``CircleOfTrustSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_circle_of_trust()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` is ``true``.*

        """
        raise Unimplemented()

    circle_of_trust_session = property(fget=get_circle_of_trust_session)

    def get_circle_of_trust_session_for_agency(self, agency_id=None):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        return: (osid.authentication.process.CircleOfTrustSession) - a
                ``CircleOfTrustSession``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_ciirle_of_trust()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if agency_id is None:
            raise NullArgument
        raise Unimplemented()


class AuthenticationProcessProxyManager(abc_authentication_process_managers.AuthenticationProcessProxyManager, osid_managers.OsidProxyManager, AuthenticationProcessProfile):
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

    def get_authentication_acquisition_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the ``AuthenticationAcquisitionSession`` using the supplied ``Authentication``.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return:
                (osid.authentication.process.AuthenticationAcquisitionSe
                ssion) - an ``AuthenticationAcquisitionSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_authentication_acquisition()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_acquisition()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_authentication_validation_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service using the supplied ``Authentication``.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return:
                (osid.authentication.process.AuthenticationValidationSes
                sion) - an ``AuthenticationValidationSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_authentication_validation()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_validation()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_trust_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.process.TrustLookupSession) - a
                ``TrustLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_trust_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_trust_lookup_session_for_agency(self, agency_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.process.TrustLookupSession) - a
                ``TrustLookupSession``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_trust_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if agency_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_circle_of_trust_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the trust circle service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.process.CircleOfTrustSession) - a
                ``CircleOfTrustSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_circle_of_trust()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_circle_of_trust_session_for_agency(self, agency_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        arg:    agency_id (osid.id.Id): the ``Id`` of the agency
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.authentication.process.CircleOfTrustSession) - a
                ``CircleOfTrustSession``
        raise:  NotFound - ``agency_id`` not found
        raise:  NullArgument - ``agency_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_ciirle_of_trust()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        if agency_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()
