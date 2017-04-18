"""Implementations of configuration abstract base class rules."""
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


class ValueCondition:
    """A value condition interface."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_condition_record(self, value_condition_record_type):
        """Gets the record corresponding to the given ``ValueCondition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``value_condition_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(value_condition_record_type)`` is ``true`` .

        :param value_condition_record_type: a value condition record type
        :type value_condition_record_type: ``osid.type.Type``
        :return: the value condition record
        :rtype: ``osid.configuration.records.ValueConditionRecord``
        :raise: ``NullArgument`` -- ``value_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_condition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueConditionRecord
