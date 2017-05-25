# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Type Service.

from ...abstract_osid.type import objects as abc_type_objects
from ..osid import objects as osid_objects
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import NullArgument, InvalidArgument, NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported

INVALID = 0
VALID = 1


class TypeList(abc_type_objects.TypeList, osid_objects.OsidList):
    """Like all OsidLists,  TypeList provides a means for accessing Type
    elements sequentially either one at a time or many at a time.

    Examples: while (tl.hasNext()) { Type type = tl.getNextType(); }

    or
      while (tl.hasNext()) {
           Type[] types = tl.getNextTypes(tl.available());
      }

    """

    def get_next_type(self):
        """Gets the next Type in this list.

        return: (osid.type.Type) - the next Type in this list. The
                has_next() method should be used to test that a next
                Type is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_object = next(self)
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
            next_object = Type(next_object)
        return next_object

    __next__ = next
    next_type = property(fget=get_next_type)

    def get_next_types(self, n=None):
        """Gets the next set of Types in this list.

        The specified amount must be less than or equal to the return
        from available().

        arg:    n (cardinal): the number of Type elements requested
                which must be less than or equal to available()
        return: (osid.type.Type) - an array of Type elements.  The
                length of the array is less than or equal to the number
                specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x = x + 1
            return next_list
