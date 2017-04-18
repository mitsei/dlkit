"""Implementations of transport abstract base class managers."""
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


class TransportProfile:
    """The ``TransportProfile`` defines the interoperability of the transport OSID."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if any transport endpoint federation is exposed.

        Federation is exposed when a specific endpoint may be used.
        Federation is not exposed when a set of endpoints appears as a
        single endpoint.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_outbound_stream(self):
        """Tests if outbound stream transport is supported.

        :return: ``true`` if outbound stream transport is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_inbound_stream(self):
        """Tests if inbound stream transport is supported.

        :return: ``true`` if incoming stream transport is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_outbound_message(self):
        """Tests if outbound message transport is supported.

        :return: ``true`` if outbound message transport is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_inbound_message(self):
        """Tests if inbound message transport is supported.

        :return: ``true`` if incoming message transport is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_endpoint_lookup(self):
        """Tests if endpoint lookup is supported.

        :return: ``true`` if endpoint lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_endpoint_record_types(self):
        """Gets a list of supported endpoint record types.

        :return: a list of supported endpoint record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    endpoint_record_types = property(fget=get_endpoint_record_types)

    @abc.abstractmethod
    def supports_endpoint_record_type(self, endpoint_record_type):
        """Tests if an endpoint record type is supported.

        :param endpoint_record_type: an endpoint record type
        :type endpoint_record_type: ``osid.type.Type``
        :return: ``true`` if the endpoint record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_request_record_types(self):
        """Gets a list of supported request record types.

        :return: a list of supported request record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    request_record_types = property(fget=get_request_record_types)

    @abc.abstractmethod
    def supports_request_record_type(self, request_record_type):
        """Tests if a request record type is supported.

        :param request_record_type: a request record type
        :type request_record_type: ``osid.type.Type``
        :return: ``true`` if the request record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``request_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_response_record_types(self):
        """Gets a list of supported response record types.

        :return: a list of supported response record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    response_record_types = property(fget=get_response_record_types)

    @abc.abstractmethod
    def supports_response_record_type(self, response_record_type):
        """Tests if a response record type is supported.

        :param response_record_type: a response record type
        :type response_record_type: ``osid.type.Type``
        :return: ``true`` if the response record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``response_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class TransportManager:
    """This manager provides access to the sessions defined in this service.

    The outbound sessions are used to connect to a remote endpoint and
    the inbound sessions are used to receive incoming connections.

    The two flavors of transport are stream and message oriented.
    Messages offer more structured requests and responses although their
    structure may include embedded streams.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_outbound_stream_session(self):
        """Gets a service for outbound stream transport.

        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_stream()`` is ``true``.*

        """
        return  # osid.transport.OutboundStreamSession

    outbound_stream_session = property(fget=get_outbound_stream_session)

    @abc.abstractmethod
    def get_outbound_stream_session_for_endpoint(self, endpoint_id):
        """Gets a service for outbound stream transport using a specified ``Endpoint``.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_stream()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.OutboundStreamSession

    @abc.abstractmethod
    def get_inbound_stream_session(self, stream_receiver):
        """Gets a service for inbound stream transport.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NullArgument`` -- ``stream_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_stream()`` is ``true``.*

        """
        return  # osid.transport.InboundStreamSession

    @abc.abstractmethod
    def get_inbound_stream_session_for_endpoint(self, stream_receiver, endpoint_id):
        """Gets a service for inbound stream transport using a specified ``Endpoint``.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``stream_receiver`` or ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_stream()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.InboundStreamSession

    @abc.abstractmethod
    def get_outbound_message_session(self):
        """Gets a service for outbound message transport.

        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_message() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_message()`` is ``true``.*

        """
        return  # osid.transport.OutboundMessageSession

    outbound_message_session = property(fget=get_outbound_message_session)

    @abc.abstractmethod
    def get_outbound_message_session_for_endpoint(self, endpoint_id):
        """Gets a service for outbound message transport using a specified Endpoint.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_message() or supports_visible_federation_i() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_message()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.OutboundMessageSession

    @abc.abstractmethod
    def get_inbound_message_session(self, message_receiver):
        """Gets a service for inbound message transport.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NullArgument`` -- ``message_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_message() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_message()`` is ``true``.*

        """
        return  # osid.transport.InboundMessageSession

    @abc.abstractmethod
    def get_inbound_message_session_for_endpoint(self, message_receiver, endpoint_id):
        """Gets a service for inbound message transport using a specified Endpoint.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``message_receiver`` or ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_message() or supports_visible_federation_i() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_message()`` and
        ``supports_visible_federation()`` are true.*

        """
        return  # osid.transport.InboundMessageSession

    @abc.abstractmethod
    def get_endpoint_lookup_session(self):
        """Gets the endpoint lookup service.

        :return: an ``EndpointLookupSesson``
        :rtype: ``osid.transport.EndpointLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound()`` is ``true``.*

        """
        return  # osid.transport.EndpointLookupSession

    endpoint_lookup_session = property(fget=get_endpoint_lookup_session)


class TransportProxyManager:
    """This manager provides access to the sessions defined in this service.

    The outbound sessions are used to connect to a remote endpoint and
    the inbound sessions are used to receive incoming connections.

    The two flavors of transport are stream and message oriented.
    Messages offer more structured requests and responses although their
    structure may include embedded streams.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_outbound_stream_session(self, proxy):
        """Gets a service for outbound stream transport.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_stream()`` is ``true``.*

        """
        return  # osid.transport.OutboundStreamSession

    @abc.abstractmethod
    def get_outbound_stream_session_for_endpoint(self, endpoint_id, proxy):
        """Gets a service for outbound stream transport using a specified ``Endpoint``.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` or ``proxy`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_stream()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.OutboundStreamSession

    @abc.abstractmethod
    def get_inbound_stream_session(self, stream_receiver, proxy):
        """Gets a service for inbound stream transport.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NullArgument`` -- ``stream_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_stream()`` is ``true``.*

        """
        return  # osid.transport.InboundStreamSession

    @abc.abstractmethod
    def get_inbound_stream_session_for_endpoint(self, stream_receiver, endpoint_id, proxy):
        """Gets a service for inbound stream transport using a specified ``Endpoint``.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``stream_receiver, endpoint_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_stream()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.InboundStreamSession

    @abc.abstractmethod
    def get_outbound_message_session(self, proxy):
        """Gets a service for outbound message transport.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_message() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_message()`` is ``true``.*

        """
        return  # osid.transport.OutboundMessageSession

    @abc.abstractmethod
    def get_outbound_message_session_for_endpoint(self, endpoint_id, proxy):
        """Gets a service for outbound message transport using a specified Endpoint.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_message() or supports_visible_federation_i() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_outbound_message()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return  # osid.transport.OutboundMessageSession

    @abc.abstractmethod
    def get_inbound_message_session(self, message_receiver, proxy):
        """Gets a service for inbound message transport.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NullArgument`` -- ``message_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_message() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_message()`` is ``true``.*

        """
        return  # osid.transport.InboundMessageSession

    @abc.abstractmethod
    def get_inbound_message_session_for_endpoint(self, message_receiver, endpoint_id, proxy):
        """Gets a service for inbound message transport using a specified Endpoint.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``message_receiver, endpoint_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_message() or supports_visible_federation_i() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound_message()`` and
        ``supports_visible_federation()`` are true.*

        """
        return  # osid.transport.InboundMessageSession

    @abc.abstractmethod
    def get_endpoint_lookup_session(self, proxy):
        """Gets the endpoint lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EndpointLookupSesson``
        :rtype: ``osid.transport.EndpointLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_inbound()`` is ``true``.*

        """
        return  # osid.transport.EndpointLookupSession
