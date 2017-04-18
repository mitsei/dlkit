"""Implementations of authentication.process abstract base class rules."""
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


class AuthenticationInput:
    """An authorization condition interface."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authentication_input_record(self, authentication_input_record_type):
        """Gets the record corresponding to the given ``AuthenticationInput`` record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces. The ``authentication_input_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authentication_input_record_type)`` is
        ``true`` .

        :param authentication_input_record_type: an authentication input record type
        :type authentication_input_record_type: ``osid.type.Type``
        :return: the authentication input record
        :rtype: ``osid.authentication.process.records.AuthenticationInputRecord``
        :raise: ``NullArgument`` -- ``authentication_input_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(authentication_input_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.records.AuthenticationInputRecord
