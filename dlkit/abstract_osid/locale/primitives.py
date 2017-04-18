"""Implementations of locale abstract base class primitives."""
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


class DisplayText:
    """Text to be displayed."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_language_type(self):
        """Gets the language ``Type``.

        :return: the language type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    language_type = property(fget=get_language_type)

    @abc.abstractmethod
    def get_script_type(self):
        """Gets the script ``Type``.

        :return: the script type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    script_type = property(fget=get_script_type)

    @abc.abstractmethod
    def get_format_type(self):
        """Gets the format ``Type`` of the text string.

        :return: the format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    format_type = property(fget=get_format_type)

    @abc.abstractmethod
    def get_text(self):
        """Gets the text string.

        :return: the string
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    text = property(fget=get_text)
