"""Implementations of osid abstract base class records."""
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


class OsidRecord:
    """``OsidRecord`` is a top-level interface for all record objects.

    A record is an auxiliary interface that can be retrieved from an
    OSID object, query, form or search order that contains method
    definitions outside the core OSID specification. An OSID record
    interface specification is identified with a ``Type``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def implements_record_type(self, record_type):
        """Tests if the given type is implemented by this record.

        Other types than that directly indicated by ``get_type()`` may
        be supported through an inheritance scheme where the given type
        specifies a record that is a parent interface of the interface
        specified by ``getType()``.

        :param record_type: a type
        :type record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is implemented by this record, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean
