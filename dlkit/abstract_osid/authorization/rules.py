"""Implementations of authorization abstract base class rules."""
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


class AuthorizationCondition:
    """An authorization condition interface."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorization_condition_record(self, authorization_condition_record_type):
        """Gets the authorization condition record corresponding to the given ``AuthorizationCondition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authorization_condition_record_type``
        may be the ``Type`` returned in ``get_condition_record_types()``
        or any of its parents in a ``Type`` hierarchy where
        ``has_condition_record_typ
        e(authorization_condition_record_type)`` is ``true`` .

        :param authorization_condition_record_type: an authorization condition record type
        :type authorization_condition_record_type: ``osid.type.Type``
        :return: the authorization condition record
        :rtype: ``osid.authorization.records.AuthorizationConditionRecord``
        :raise: ``NullArgument`` -- ``authorization_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_condition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationConditionRecord
