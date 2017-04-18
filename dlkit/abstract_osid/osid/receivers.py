"""Implementations of osid abstract base class receivers."""
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


class OsidReceiver:
    """An ``OsidReceiver`` is used to receive asynchronous notifications from a service.

    The receiver defines the interface to be implemented by the
    consumer.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def up(self):
        """The callback for notifications that the notification bus is operational.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def down(self):
        """The callback for notifications that the notification bus is not operating.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass
