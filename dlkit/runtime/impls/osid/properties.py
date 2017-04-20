# -*- coding: utf-8 -*-

# This module contains the classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of  OSID properties.

from dlkit.abstract_osid.osid import properties as abc_osid_properties
from ..osid import objects as osid_objects
from .. primitives import Id, Type, DisplayText
from .osid_errors import IllegalState, OperationFailed, Unimplemented


class Property(abc_osid_properties.Property):
    """A ``Property`` is a representation of data in string form.

    Properties are exposed in OSID objects as a means of providing a
    quick gestalt of data elements whose specifics are described through
    a type specification. A view of an OSID object via Properties allows
    applications to browse the content without understanding the type
    specification in place, but any acquisition of specific data, access
    to an object or other primitive type, or changing the data requires
    the typed interfaces.

    """

    def __init__(self, property_map):
        self._my_map = property_map

    def get_display_name(self):
        """The display name for this property.

        :return: the display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return DisplayText(self._my_map['displayName'])

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """A short display label.

        :return: the display label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return DisplayText(self._my_map['displayLabel'])

    display_label = property(fget=get_display_label)

    def get_description(self):
        """A description of this property.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return DisplayText(self._my_map['description'])

    description = property(fget=get_description)

    def get_value(self):
        """The value of this property.

        :return: the value
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return self._my_map['value']

    value = property(fget=get_value)


class PropertyList(abc_osid_properties.Property, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``PropertyList`` provides a means for accessing ``Property`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Property property =
    pl.getNextProperty(); }

    or
      while (pl.hasNext()) {
           Property[] properties = pl.getNextProperties(pl.available());
      }
    """

    def get_next_property(self):
        """Gets the next ``Property`` in this list.

        :return: the next ``Property`` in this list. The ``has_next()`` method should be used to test that a next ``Property`` is available before calling this method.
        :rtype: ``osid.Property``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            next_object = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Property(next_object)
        return next_object

    next_property = property(fget=get_next_property)

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
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(self.next())
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list
