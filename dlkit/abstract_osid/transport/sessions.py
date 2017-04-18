"""Implementations of transport abstract base class sessions."""
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


class OutboundStreamSession:
    """The outbound stream session is used to send and receive arbitrary data to and from a remote end point.

    The methods accept and return a data stream. Some protocols may send
    or receive all data within a single stream while others may use the
    streams as channels or frames of data.

    A stream may be available for reading before all the data as arrived
    and as such multiple streams may be processed simultaneously.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_endpoint_id(self):
        """Gets the ``Endpoint``  ``Id`` associated with this session.

        :return: the ``Endpoint``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    endpoint_id = property(fget=get_endpoint_id)

    @abc.abstractmethod
    def get_endpoint(self):
        """Gets the ``Endpoint`` associated with this session.

        :return: the ``Endpoint`` associated with this session
        :rtype: ``osid.transport.Endpoint``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Endpoint

    endpoint = property(fget=get_endpoint)

    @abc.abstractmethod
    def send_data(self):
        """Sends data to the remote transport endpoint.

        :return: the output stream in which to send data
        :rtype: ``osid.transport.DataOutputStream``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.DataOutputStream

    @abc.abstractmethod
    def has_data_available(self):
        """Tests to see if an input stream is available for retrieval.

        :return: ``true`` if a stream is available for reading, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def receive_data(self):
        """Receives data from the remote transport endpoint.

        :return: the input stream containing the received data
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``IllegalState`` -- ``has_data_available()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.DataInputStream


class InboundStreamSession:
    """The inbound stream session is used as a listener.

    A callback is registered using a ``StreamReceiver``. The listener is
    closed when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_endpoint_id(self):
        """Gets the ``Endpoint``  ``Id`` associated with this session.

        :return: the ``Endpoint``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    endpoint_id = property(fget=get_endpoint_id)

    @abc.abstractmethod
    def get_endpoint(self):
        """Gets the ``Endpoint`` associated with this session.

        :return: the ``Endpoint`` associated with this session
        :rtype: ``osid.transport.Endpoint``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Endpoint

    endpoint = property(fget=get_endpoint)

    @abc.abstractmethod
    def register_callback(self, receiver):
        """Registers a callback to receive incoming data.

        :param receiver: a stream receievr
        :type receiver: ``osid.transport.StreamReceiver``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OutboundMessageSession:
    """This session provides access to a request/response protocol provider.

    The data and format of the requests and responses are identified
    through their respective ``Types``. While this session is used for
    structured conversations, it doesn't preclude the use of byte
    streams as part of a ``Request`` or ``Response``.

    A ``Request`` is retrieved via ``get_request()`` and data is
    supplied to its corresponding record. The ``Request`` is then sent
    using ``send_request()`` along with an interface to be called when
    the ``Response`` arrives. The FSM of the protocol is indicated
    through the available ``Request``  ``Types`` that may change from
    one transaction to another.

    While multiple requests may be submitted before receiving a
    response, the requests may or may not be queued.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_endpoint_id(self):
        """Gets the ``Endpoint``  ``Id`` associated with this session.

        :return: the ``Endpoint``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    endpoint_id = property(fget=get_endpoint_id)

    @abc.abstractmethod
    def get_endpoint(self):
        """Gets the ``Endpoint`` associated with this session.

        :return: the ``Endpoint`` associated with this session
        :rtype: ``osid.transport.Endpoint``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Endpoint

    endpoint = property(fget=get_endpoint)

    @abc.abstractmethod
    def get_request(self):
        """Gets a ``Request`` for use with ``sendRequest()``.

        This is not a receive call.

        :return: a request
        :rtype: ``osid.transport.Request``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Request

    request = property(fget=get_request)

    @abc.abstractmethod
    def make_request(self, request, response):
        """Sends a request to the remote transport endpoint and waits for a response.

        :param request: the request
        :type request: ``osid.transport.Request``
        :param response: callback for the response
        :type response: ``osid.transport.Response``
        :raise: ``NullArgument`` -- ``request`` or ``receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``request`` is not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def send_request(self, request, callback):
        """Sends data to the remote transport endpoint and sends the response to the callback.

        :param request: the request
        :type request: ``osid.transport.Request``
        :param callback: callback for the response
        :type callback: ``osid.transport.MessageReceiver``
        :raise: ``NullArgument`` -- ``request`` or ``callback`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``request`` is not supported

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class InboundMessageSession:
    """The inbound message session is used as a listener.

    A callback is registered using a ``StreamReceiver``. The listener is
    closed when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_endpoint_id(self):
        """Gets the ``Endpoint``  ``Id`` associated with this session.

        :return: the ``Endpoint``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    endpoint_id = property(fget=get_endpoint_id)

    @abc.abstractmethod
    def get_endpoint(self):
        """Gets the ``Endpoint`` associated with this session.

        :return: the ``Endpoint`` associated with this session
        :rtype: ``osid.transport.Endpoint``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Endpoint

    endpoint = property(fget=get_endpoint)

    @abc.abstractmethod
    def register_callback(self, receiver):
        """Registers a callback to receive incoming data.

        :param receiver: a message receievr
        :type receiver: ``osid.transport.MessageReceiver``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class EndpointLookupSession:
    """This session provides methods for retrieving ``Endpoint`` objects.

    The ``Endpoint represents`` transport destination.

    This session defines two views which offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data out of sync.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_endpoints(self):
        """Tests if this user can perform ``Endpoint`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_endpoint_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_endpoint_view(self):
        """A complete view of the ``Endpoint`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_endpoint(self, endpoint_id):
        """Gets the ``Endpoint`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Endpoint`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Endpoint`` and retained for
        compatibility.

        :param endpoint_id: the ``Id`` of the ``Endpoint`` to retrieve
        :type endpoint_id: ``osid.id.Id``
        :return: the ``Endpoint``
        :rtype: ``osid.transport.Endpoint``
        :raise: ``NotFound`` -- no ``Endpoint`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``Id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.Endpoint

    @abc.abstractmethod
    def get_endpoints_by_ids(self, endpoint_ids):
        """Gets an ``EndpointList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the endpoints
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Endpoint`` elements may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param endpoint_ids: the list of ``Ids`` to retrieve
        :type endpoint_ids: ``osid.id.IdList``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``endpoint_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    @abc.abstractmethod
    def get_endpoints_by_genus_type(self, endpoint_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` which does not include endpoints
        of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoint_genus_type: an endpoint genus type
        :type endpoint_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    @abc.abstractmethod
    def get_endpoints_by_parent_genus_type(self, endpoints_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` and include any additional
        endpoints with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoints_genus_type: an endpoint genus type
        :type endpoints_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    @abc.abstractmethod
    def get_endpoints_by_record_type(self, endpoints_record_type):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.

        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoints_record_type: an endpoint record type
        :type endpoints_record_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    @abc.abstractmethod
    def get_endpoints_by_provider(self, resource_id):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.

        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    @abc.abstractmethod
    def get_endpoints(self):
        """Gets all ``Endpoint`` elements.

        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :return: a list of endpoints
        :rtype: ``osid.transport.EndpointList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.transport.EndpointList

    endpoints = property(fget=get_endpoints)
