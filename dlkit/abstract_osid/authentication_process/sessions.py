"""Implementations of authentication.process abstract base class sessions."""
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


class AuthenticationAcquisitionSession:
    """This session acquires authentication credentials.

    The basic method, ``get_authentication(),`` gets authentication
    credentials for use with authenticating to a remote peer. These
    credentials may be generated from direct user input or retrieved via
    a file, for example.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authentication(self):
        """Gets the authentication credential for the current user.

        The input data may represent the identity of the remote peer or
        data from a challenge-response transaction necessary for
        generating the credantial.

        :return: the acquired authentication credential
        :rtype: ``osid.authentication.process.Authentication``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authentication.process.Authentication

    authentication = property(fget=get_authentication)


class AuthenticationValidationSession:
    """This session is the remote end of a transport link from the acquisition session and validates authentication credentials sent to it.

    The basic method, ``authenticate()`` accepts a credential, validates
    it and returns an ``Authentication`` containing the identity of the
    authenticated user.

    This OSID does not define any root interface for credentials and
    challenge data. The object representing these are completely defined
    within their ``Type,`` providing flexibility in adapting to a
    variety of application environments.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authentication_input(self):
        """Gets an interface for authentication input.

        :return: authentication input
        :rtype: ``osid.authentication.process.AuthenticationInput``


        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authentication.process.AuthenticationInput

    authentication_input = property(fget=get_authentication_input)

    @abc.abstractmethod
    def authenticate(self, input_):
        """Validates and returns the authentication credential from the given data.

        :param input: the authentication input to be validated
        :type input: ``osid.authentication.process.AuthenticationInput``
        :return: the resulting authentication
        :rtype: ``osid.authentication.process.Authentication``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authentication.process.Authentication

    @abc.abstractmethod
    def get_challenge_data(self, input_):
        """Gets data that can be used for a challenge to the peer attempting authentication.

        :param input: authentication input
        :type input: ``osid.authentication.process.AuthenticationInput``
        :return: the acquired challenge data
        :rtype: ``osid.authentication.process.Challenge``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- challenge response not available
        :raise: ``Unsupported`` -- ``input`` is not of this service

        *compliance: optional -- This method must be implemented if
        ``AuthenticationProcessManager.supportsChallenge()`` is
        ``true``.*

        """
        return  # osid.authentication.process.Challenge


class TrustLookupSession:
    """This session provides methods for retrieving ``Trusts``.

    The ``Trust`` represents the trust level of an agent. The
    relationship among ``Agents`` and ``Trust`` is not explicity managed
    but understood by an Authentication OSID Provider when orchestration
    to an Authorization OSID Provider is desired.

    This session defines two sets of views which offer differing
    behaviors when retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition
      * isolated agency view: All agent methods in this session operate,
        retrieve and pertain to trusts defined explicitly in the current
        agency.
      * federated agency view: All trust methods in this session
        operate, retrieve and pertain to all trusts defined in this
        agency and any other trusts implicitly available in this agency
        through agency inheritence.


    Generally, the comparative view should be used for most applications
    as it permits operation even if there a particular element is
    inaccessible. For example, a hierarchy output can be plugged into a
    lookup method to retrieve all objects known to a hierarchy, but it
    may not be necessary to break execution if a node from the hierarchy
    no longer exists. However, some administrative applications may need
    to know whether it had retrieved an entire set of objects and may
    sacrifice some interoperability for the sake of precision.

    Trusts may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Trust``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_lookup_trusts(self):
        """Tests if this user can perform ``Trust`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_trust_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_trust_view(self):
        """A complete view of the ``Trust`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include trusts in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_trust(self, trust_id):
        """Gets the ``Trust`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Trust`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Trust`` and retained for compatibility.

        :param trust_id: the ``Id`` of the ``Trust`` to retrieve
        :type trust_id: ``osid.id.Id``
        :return: the returned ``Trust``
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``NotFound`` -- no ``Trust`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``trust_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.Trust

    @abc.abstractmethod
    def get_trusts_by_ids(self, trust_ids):
        """Gets a ``TrustList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the trusts
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Trusts`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param trust_ids: a list of trust ``Ids``
        :type trust_ids: ``osid.id.IdList``
        :return: the returned ``Trust list``
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``trust_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    @abc.abstractmethod
    def get_trusts_by_genus_type(self, trust_genus_type):
        """Gets a ``TrustList`` corresponding to the given trust genus ``Type`` which does not include trusts of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known trusts or
        an error results. Otherwise, the returned list may contain only
        those trusts that are accessible through this session.

        :param trust_genus_type: a trust genus type
        :type trust_genus_type: ``osid.type.Type``
        :return: the returned ``Trust`` list
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``NullArgument`` -- ``trust_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    @abc.abstractmethod
    def get_trusts_by_parent_genus_type(self, trust_genus_type):
        """Gets a ``TrustList`` corresponding to the given trust genus ``Type`` and include any additional trusts with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known trusts or
        an error results. Otherwise, the returned list may contain only
        those trusts that are accessible through this session.

        :param trust_genus_type: a trust genus type
        :type trust_genus_type: ``osid.type.Type``
        :return: the returned ``Trust`` list
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``NullArgument`` -- ``trust_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    @abc.abstractmethod
    def get_trusts_by_record_type(self, trust_record_type):
        """Gets a ``TrustList`` containing the given trust record ``Type``.

        In plenary mode, the returned list contains all known trusts or
        an error results. Otherwise, the returned list may contain only
        those trusts that are accessible through this session.

        :param trust_record_type: a trust record type
        :type trust_record_type: ``osid.type.Type``
        :return: the returned ``Trust`` list
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``NullArgument`` -- ``trust_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    @abc.abstractmethod
    def get_circle_of_trust(self, trust_id):
        """Gets a ``TrustList`` in the same circle, or the same level of confidence, as the given trust.

        In plenary mode, the returned list contains all known trusts or
        an error results. Otherwise, the returned list may contain only
        those trusts that are accessible through this session.

        :param trust_id: a trust ``Id``
        :type trust_id: ``osid.id.Id``
        :return: the returned ``Trust`` list
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``NotFound`` -- ``trust_id`` is not found
        :raise: ``NullArgument`` -- ``trust_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    @abc.abstractmethod
    def get_trusts(self):
        """Gets all ``Trusts``.

        In plenary mode, the returned list contains all known trusts or
        an error results. Otherwise, the returned list may contain only
        those trusts that are accessible through this session.

        :return: a list of ``Trusts``
        :rtype: ``osid.authentication.process.TrustList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.TrustList

    trusts = property(fget=get_trusts)


class CircleOfTrustSession:
    """This session examines the relationship between ``Agents`` and ``Trusts``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_lookup_trust_circles(self):
        """Tests if this user can look up trusts for agents.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known these methods will
        result in a ``PermissionDenied``. This is intended as a hint to
        an application that may opt not to offer create operations to
        users outside the circle.

        :return: ``false`` if trust methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include trusts in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_trust(self, agent_id):
        """Gets a trust level for the given agent.

        An ``Agent`` may be in one circle of trust that, in turn, is
        inside another circle of trust. To test whether an agent is
        inside a specific circle, use ``IsInCircle()``.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :return: the trust
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.Trust

    @abc.abstractmethod
    def is_in_circle(self, agent_id):
        """Tests if the given agent is inside the given circle of trust.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :return: ``true`` if the agent is in the given trust, ``false`` if agent not found or is outside the circle
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean
