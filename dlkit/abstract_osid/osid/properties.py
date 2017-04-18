"""Implementations of osid abstract base class properties."""
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


class Property:
    """A ``Property`` is a representation of data in string form.

    Properties are exposed in OSID objects as a means of providing a
    quick gestalt of data elements whose specifics are described through
    a type specification. A view of an OSID object via Properties allows
    applications to browse the content without understanding the type
    specification in place, but any acquisition of specific data, access
    to an object or other primitive type, or changing the data requires
    the typed interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_display_name(self):
        """The display name for this property.

        :return: the display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    @abc.abstractmethod
    def get_display_label(self):
        """A short display label.

        :return: the display label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    @abc.abstractmethod
    def get_description(self):
        """A description of this property.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    description = property(fget=get_description)

    @abc.abstractmethod
    def get_value(self):
        """The value of this property.

        :return: the value
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    value = property(fget=get_value)


class PropertyList:
    """Like all ``OsidLists,``  ``PropertyList`` provides a means for accessing ``Property`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Property property =
    pl.getNextProperty(); }

    or
      while (pl.hasNext()) {
           Property[] properties = pl.getNextProperties(pl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_property(self):
        """Gets the next ``Property`` in this list.

        :return: the next ``Property`` in this list. The ``has_next()`` method should be used to test that a next ``Property`` is available before calling this method.
        :rtype: ``osid.Property``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Property

    next_property = property(fget=get_next_property)

    @abc.abstractmethod
    def get_next_properties(self, n):
        """Gets the next set of ``Property`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Property`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Property`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.Property``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Property
