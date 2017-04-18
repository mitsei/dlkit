"""Implementations of transport abstract base class receivers."""
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


class StreamReceiver:
    """The ``StreamReceiver`` is used to receive incoming connections.

    The receiver is provided to the service via the
    ``InboundStreamSession`` and invoked by the transport provider when
    a new association is created.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def dispatch(self, session):
        """Invoked by the transport provider when a new connection request or datagram is received.

        :param session: a session to send and receive data
        :type session: ``osid.transport.OutboundStreamSession``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class MessageReceiver:
    """The ``MessageReceiver`` is used to receive incoming connections.

    The receiver is provided to the service via the
    ``InboundMessageSession`` and invoked by the transport provider when
    a new association is created.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def dispatch(self, session):
        """Invoked by the transport provider when a new connection request or datagram is received.

        :param session: a session to send and receive messages
        :type session: ``osid.transport.OutboundMessageSession``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
