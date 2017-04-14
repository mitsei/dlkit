from dlkit.abstract_osid.authentication_process import objects as abc_authentication_process_objects
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects
from ..authentication.objects import Agent
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import *
import socket


class DjangoAuthentication(abc_authentication_process_objects.Authentication, osid_objects.OsidObject):
    """``Authentication`` represents an authentication credential which contains set of ``bytes`` and a format Type.

    Once an ``Authentication`` is created from the
    ``AuthenticationValidationSession,`` the credential data can be
    extracted and sent to the remote peer for validation. The remote
    peer gets another ``Authentication`` object as a result of
    validating the serialized credential data.

    An ``Authentication`` may or may not be valid. ``is_valid()`` should
    be checked before acting upon the ``Agent`` identity to which the
    credential is mapped.

    """
    def __init__(self):
        self._django_user = None
        self._credential = None
        self._use_user_id = None

    def get_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` identified in this authentication credential.

        :return: the ``Agent Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: The Agent should be determined at the
        time this credential is created.

        """
        if self._django_user is not None:
            if self._use_user_id:
                identifier = self._django_user.id
            else:
                identifier = self._django_user.get_username()
            return Id(identifier = identifier,
                      namespace = 'osid.agent.Agent',
                      authority = 'MIT-ODL')
        else:
            # perhaps this id should come from django settings?
            return Id(identifier = 'MC3GUE$T@MIT.EDU',
                      namespace = 'osid.agent.Agent',
                      authority = 'MIT-ODL')

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` identified in this authentication credential.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        agent_id = self.get_agent_id()
        return Agent(identifier = agent_id.identifier,
                     namespace = agent_id.namespace,
                     authority = agent_id.authority)

    agent = property(fget=get_agent)

    def is_valid(self):
        """Tests whether or not the credential represented by this ``Authentication`` is currently valid.

        A credential may be invalid because it has been destroyed,
        expired, or is somehow no longer able to be used.

        :return: ``true`` if this authentication credential is valid, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any problem in determining the validity
        of this credential should result in ``false``.

        """
        if self._django_user is not None:
            return self._django_user.is_authenticated()
        else:
            return False

    def has_expiration(self):
        """Tests if this authentication has an expiration.

        :return: ``true`` if this authentication has an expiration, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_expiration(self):
        """Gets the expiration date associated with this authentication credential.

        Consumers should check for the existence of a an expiration
        mechanism via ``hasExpiration()``.

        :return: the expiration date of this authentication credential
        :rtype: ``timestamp``
        :raise: ``IllegalState`` -- ``has_expiration()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_expiration():
            raise IllegalState()
        else:
            raise Unimplemented()

    expiration = property(fget=get_expiration)

    def has_credential(self):
        """Tests if this authentication has a credential for export.

        :return: ``true`` if this authentication has a credential, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        if self._credential is None:
            return False
        else:
            return True

    def get_credential(self, credential_type):
        """Gets the credential represented by the given ``Type`` for transport to a remote service.

        :param credential_type: the credential format ``Type``
        :type credential_type: ``osid.type.Type``
        :return: the credential
        :rtype: ``object``
        :raise: ``IllegalState`` -- ``has_credential()`` is ``false``
        :raise: ``NullArgument`` -- ``credential_type`` is ``null``
        :raise: ``Unsupported`` -- the given ``credential_type`` is not supported

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A provider may support multiple
        credential formats for a variety of applications.

        """
        if self.has_credential():
            return self._credential
        else:
            raise IllegalState()

    def get_authentication_record(self, authentication_record_type):
        """Gets the authentication record corresponding to the given authentication record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authentication_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authentication_record_type)`` is ``true`` .

        :param authentication_record_type: the type of authentication record to retrieve
        :type authentication_record_type: ``osid.type.Type``
        :return: the authentication record
        :rtype: ``osid.authentication.process.records.AuthenticationRecord``
        :raise: ``NullArgument`` -- ``authentication_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(authenticaton_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.records.AuthenticationRecord

    def set_django_user(self, django_user, use_user_id=False):
        self._django_user = django_user
        self._use_user_id = use_user_id

class XBlockAuthentication(abc_authentication_process_objects.Authentication, osid_objects.OsidObject):

    def __init__(self):
        self._xblock_user = None
        self._credential = None

    def _has_user_id(self, xblock_user):
        try:
            key = self._get_user_id_key(xblock_user)
        except KeyError:
            return False
        else:
            if xblock_user.opt_attrs[key] is not None:
                return True
            else:
                return False

    def _get_user_id_key(self, xblock_user):
        for k in xblock_user.opt_attrs:
            if '.user_id' in k:
                return k
        raise KeyError()

    def _is_authenticated(self, xblock_user):
        key = None
        for k in xblock_user.opt_attrs:
            if '.is_authenticated' in k:
                key = k
        if key is not None:
            try:
                return xblock_user.opt_attrs[key]
            except KeyError:
                return False
        return False
            

    def get_agent_id(self):
        if (self._xblock_user is not None and 
            self._xblock_user.opt_attrs != {} and
            self._has_user_id(self._xblock_user) and
            self._is_authenticated(self._xblock_user)):
            key = self._get_user_id_key(self._xblock_user)
            return Id(identifier = self._xblock_user.opt_attrs[key],
                      namespace = 'osid.agent.Agent',
                      authority = key.split('.')[0])
        else:
            return Id(identifier = 'MC3GUE$T@MIT.EDU',
                      namespace = 'osid.agent.Agent',
                      authority = 'MIT-ODL')

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        agent_id = self.get_agent_id()
        return Agent(identifier = agent_id.identifier,
                     namespace = agent_id.namespace,
                     authority = agent_id.authority)

    agent = property(fget=get_agent)

    def is_valid(self):
        if (self._xblock_user is not None and 
            self._is_authenticated(self._xblock_user)):
            return True
        else:
            return False

    def has_expiration(self):
        return False

    def get_expiration(self):
        if not self.has_expiration():
            raise IllegalState()
        else:
            raise Unimplemented()

    expiration = property(fget=get_expiration)

    def has_credential(self):
        if self._credential is None:
            return False
        else:
            return True

    def get_credential(self, credential_type):
        if self.has_credential():
            return self._credential
        else:
            raise IllegalState()

    def get_authentication_record(self, authentication_record_type):
        return # osid.authentication.process.records.AuthenticationRecord

    def set_xblock_user(self, xblock_user):
        self._xblock_user = xblock_user


class Challenge(abc_authentication_process_objects.Challenge, osid_markers.Extensible, osid_markers.Browsable):
    """The challenge data."""

    def get_challenge_record(self, challenge_record_type):
        """Gets the challenge record corresponding to the given challenge record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``challenge_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(challenge_record_type)`` is ``true`` .

        :param challenge_record_type: the type of challenge record to retrieve
        :type challenge_record_type: ``osid.type.Type``
        :return: the challenge record
        :rtype: ``osid.authentication.process.records.ChallengeRecord``
        :raise: ``NullArgument`` -- ``challenge_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(challenge_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.records.ChallengeRecord


class Trust(abc_authentication_process_objects.Trust, osid_objects.OsidObject):
    """``Trust`` represents the level of confidence in an authentication.

    An Authentication OSID Provider may issue different ``Agents`` based
    on the authentication mechanism. ``Trust`` is a grouping of
    ``Agent`` "types" that can be inferred as equivalent from an
    authorization point of view.

    The relationship among ``Agents`` and ``Trust`` is not explicity
    managed but understood by an Authentication OSID Provider when
    orchestration to an Authorization OSID Provider is desired.

    """

    def get_trust_record(self, trust_record_type):
        """Gets the trust record corresponding to the given trust record ``Type``.

        This method is used to retrieve an object implementing the
        requested. The ``trust_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(trust_record_type)``
        is ``true`` .

        :param trust_record_type: the type of trust record to retrieve
        :type trust_record_type: ``osid.type.Type``
        :return: the trust record
        :rtype: ``osid.authentication.process.records.TrustRecord``
        :raise: ``NullArgument`` -- ``trust_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(trust_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.records.TrustRecord


class TrustList(abc_authentication_process_objects.TrustList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``TrustList`` provides a means for accessing ``Trust`` elements sequentially either one at a time or many at a time.

    Examples: while (tl.hasNext()) { Trust trust = tl.getNextTrust(); }

    or
      while (tl.hasNext()) {
           Trust[] trusts = tl.getNextTrusts(tl.available());
      }
    


    """

    def get_next_trust(self):
        """Gets the next ``Trust`` in this list.

        :return: the next ``Trust`` in this list. The ``has_next()`` method should be used to test that a next ``Trust`` is available before calling this method.
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.Trust

    next_trust = property(fget=get_next_trust)

    def get_next_trusts(self, n):
        """Gets the next set of ``Trust`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Trust`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Trust`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.Trust


