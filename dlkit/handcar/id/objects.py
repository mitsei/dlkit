# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Id Service.

from ...abstract_osid.id import objects as abc_id_objects
from ..osid import objects as osid_objects
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import NullArgument, InvalidArgument, NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported

INVALID = 0
VALID = 1


class IdList(abc_id_objects.IdList, osid_objects.OsidList):
    """Like all OsidLists,  IdList provides a means for accessing Id
    elements sequentially either one at a time or many at a time.

    Examples: while (il.hasNext()) { Id id = il.getNextId(); }

    or
      while (il.hasNext()) {
           Id[] ids = il.getNextIds(il.available());
      }

    """

    def get_next_id(self):
        """Gets the next Id in this list.

        return: (osid.id.Id) - the next Id in this list. The has_next()
                method should be used to test that a next Id is
                available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        try:
            next_item = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        try:
            next_item = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_item, dict):
            next_item = Id(next_item)
        return next_item

    __next__ = next

    def get_next_ids(self, n=None):
        """Gets the next set of Ids in this list.

        The specified amount must be less than or equal to the return
        from available().

        arg:    n (cardinal): the number of Id elements requested which
                must be less than or equal to available()
        return: (osid.id.Id) - an array of Id elements.  The length of
                the array is less than or equal to the number specified.
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

    next_id = property(get_next_id)
