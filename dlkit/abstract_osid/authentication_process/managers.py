"""Implementations of authentication.process abstract base class managers."""
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


class AuthenticationProcessProfile:
    """The ``AuthenticationProcessProfile`` describes the interoperability among authentication process services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_authentication_acquisition(self):
        """Tests if authentication acquisition is supported.

        Authentication acquisition is responsible for acquiring client
        side authentication credentials.

        :return: ``true`` if authentication acquisiiton is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_authentication_validation(self):
        """Tests if authentication validation is supported.

        Authentication validation verifies given authentication
        credentials and maps to an agent identity.

        :return: ``true`` if authentication validation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_trust_lookup(self):
        """Tests if a trust look up session is supported.

        :return: ``true`` if trust lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_circle_of_trust(self):
        """Tests if a session to examine agent and trust relationships is supported.

        :return: ``true`` if a circle of trust is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_challenge(self):
        """Tests if this authentication service supports a challenge- response mechanism where credential validation service must implement a means to generate challenge data.

        :return: ``true`` if this is a challenge-response system, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authentication_record_types(self):
        """Gets the supported authentication record types.

        :return: a list containing the supported authentication record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    authentication_record_types = property(fget=get_authentication_record_types)

    @abc.abstractmethod
    def supports_authentication_record_type(self, authentication_record_type):
        """Tests if the given authentication record type is supported.

        :param authentication_record_type: a ``Type`` indicating an authentication record type
        :type authentication_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authentication_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authentication_input_record_types(self):
        """Gets the supported authentication input record types.

        :return: a list containing the supported authentication input record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    @abc.abstractmethod
    def supports_authentication_input_record_type(self, authentication_input_record_type):
        """Tests if the given authentication input record type is supported.

        :param authentication_input_record_type: a ``Type`` indicating an authentication input record type
        :type authentication_input_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authentication_input_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_challenge_record_types(self):
        """Gets the supported challenge types.

        :return: a list containing the supported challenge types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    challenge_record_types = property(fget=get_challenge_record_types)

    @abc.abstractmethod
    def supports_challenge_record_type(self, challenge_record_type):
        """Tests if the given challenge data type is supported.

        :param challenge_record_type: a ``Type`` indicating a challenge record type
        :type challenge_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``challenge_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_credential_export(self):
        """Tests if ``Authentication`` objects can export serialzied credentials for transport.

        :return: ``true`` if the given credentials export is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_credential_types(self):
        """Gets the supported credential types.

        :return: a list containing the supported credential types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    credential_types = property(fget=get_credential_types)

    @abc.abstractmethod
    def supports_credential_type(self, credential_type):
        """Tests if the given credential type is supported.

        :param credential_type: a ``Type`` indicating a credential type
        :type credential_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credential_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_trust_types(self):
        """Gets the supported trust types.

        :return: a list containing the supported trust types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    trust_types = property(fget=get_trust_types)

    @abc.abstractmethod
    def supports_trust_type(self, trust_type):
        """Tests if the given trust type is supported.

        :param trust_type: a ``Type`` indicating a trust type
        :type trust_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``trust_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class AuthenticationProcessManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authentication_acquisition_session(self):
        """Gets an ``AuthenticationAcquisitionSession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        :return: an acquisition session for this service
        :rtype: ``osid.authentication.process.AuthenticationAcquisitionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_acquisition()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_acquisition()`` is ``true``.*

        """
        return  # osid.authentication.process.AuthenticationAcquisitionSession

    authentication_acquisition_session = property(fget=get_authentication_acquisition_session)

    @abc.abstractmethod
    def get_authentication_validation_session(self):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service.

        :return: an ``AuthenticationValidationSession``
        :rtype: ``osid.authentication.process.AuthenticationValidationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_validation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_validation()`` is ``true``.*

        """
        return  # osid.authentication.process.AuthenticationValidationSession

    authentication_validation_session = property(fget=get_authentication_validation_session)

    @abc.abstractmethod
    def get_trust_lookup_session(self):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` is ``true``.*

        """
        return  # osid.authentication.process.TrustLookupSession

    trust_lookup_session = property(fget=get_trust_lookup_session)

    @abc.abstractmethod
    def get_trust_lookup_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authentication.process.TrustLookupSession

    @abc.abstractmethod
    def get_circle_of_trust_session(self):
        """Gets the ``OsidSession`` associated with the trust circle service.

        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_circle_of_trust()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` is ``true``.*

        """
        return  # osid.authentication.process.CircleOfTrustSession

    circle_of_trust_session = property(fget=get_circle_of_trust_session)

    @abc.abstractmethod
    def get_circle_of_trust_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_ciirle_of_trust()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authentication.process.CircleOfTrustSession


class AuthenticationProcessProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authentication_acquisition_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``AuthenticationAcquisitionSession`` using the supplied ``Authentication``.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthenticationAcquisitionSession``
        :rtype: ``osid.authentication.process.AuthenticationAcquisitionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_acquisition()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_acquisition()`` is ``true``.*

        """
        return  # osid.authentication.process.AuthenticationAcquisitionSession

    @abc.abstractmethod
    def get_authentication_validation_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service using the supplied ``Authentication``.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthenticationValidationSession``
        :rtype: ``osid.authentication.process.AuthenticationValidationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_validation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_validation()`` is ``true``.*

        """
        return  # osid.authentication.process.AuthenticationValidationSession

    @abc.abstractmethod
    def get_trust_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` is ``true``.*

        """
        return  # osid.authentication.process.TrustLookupSession

    @abc.abstractmethod
    def get_trust_lookup_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_trust_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authentication.process.TrustLookupSession

    @abc.abstractmethod
    def get_circle_of_trust_session(self, proxy):
        """Gets the ``OsidSession`` associated with the trust circle service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_circle_of_trust()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` is ``true``.*

        """
        return  # osid.authentication.process.CircleOfTrustSession

    @abc.abstractmethod
    def get_circle_of_trust_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_ciirle_of_trust()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_circle_of_trust()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.authentication.process.CircleOfTrustSession
