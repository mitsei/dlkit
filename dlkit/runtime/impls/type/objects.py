from dlkit.abstract_osid.type import objects as abc_type_objects
from ..osid import objects as osid_objects


class TypeList(abc_type_objects.TypeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``TypeList`` provides a means for accessing ``Type`` elements sequentially either one at a time or many at a time.

    Examples: while (tl.hasNext()) { Type type = tl.getNextType(); }

    or
      while (tl.hasNext()) {
           Type[] types = tl.getNextTypes(tl.available());
      }

    """

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        return: (osid.type.Type) - the next ``Type`` in this list. The
                ``has_next()`` method should be used to test that a next
                ``Type`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        import sys
        from ..osid.osid_errors import IllegalState, OperationFailed
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except:  # Need to specify exceptions here
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        from ..osid.objects import OsidList
        from .primitives import Type
        try:
            next_item = OsidList.next(self)
        except:
            raise
        if isinstance(next_item, dict):
            next_item = Type(next_item)
        return next_item

    next_type = property(fget=get_next_type)

    next_type = property(fget=get_next_type)

    def get_next_types(self, n=None):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Type`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.type.Type) - an array of ``Type`` elements.The
                length of the array is less than or equal to the number
                specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        import sys
        from ..osid.osid_errors import IllegalState, OperationFailed
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(self.next())
                except:  # Need to specify exceptions here
                    raise OperationFailed()
                x = x + 1
            return next_list
