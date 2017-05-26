"""Manager utility implementations of osid objects."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from dlkit.abstract_osid.osid import objects as abc_osid_objects


class OsidList(abc_osid_objects.OsidList):
    """``OsidList`` is the top-level interface for all OSID lists.

    An OSID list provides sequential access, one at a time or many at a
    time, access to a set of elements. These elements are not required
    to be OsidObjects but generally are. The element retrieval methods
    are defined in the sub-interface of ``OsidList`` where the
    appropriate return type is defined.

    Osid lists are a once pass through iteration of elements. The size
    of the object set and the means in which the element set is
    generated or stored is not known. Assumptions based on the length of
    the element set by copying the entire contents of the list into a
    fixed buffer should be done with caution a awareness that an
    implementation may return a number of elements ranging from zero to
    infinity.

    Lists are returned by methods when multiple return values are
    possible. There is no guarantee that successive calls to the same
    method will return the same set of elements in a list. Unless an
    order is specified in an interface definition, the order of the
    elements is not known.

    """
    def __init__(self, iter_object=None, count=None, db_prefix='', runtime=None):
        if iter_object is None:
            iter_object = []
        if count is not None:
            self._count = count
        elif isinstance(iter_object, dict) or isinstance(iter_object, list):
            self._count = len(iter_object)
        else:
            self._count = None
        self._runtime = runtime
        self._db_prefix = db_prefix
        self._iter_object = iter(iter_object)

    def __iter__(self):
        return self

    def next(self):
        """Iterator 'next' method"""
        try:
            next_object = next(self._iter_object)
        except:
            raise
        if self._count is not None:
            self._count -= 1
        return next_object

    __next__ = next

    def len(self):
        return self.available()

    def has_next(self):
        """Tests if there are more elements in this list.

        return: (boolean) - ``true`` if more elements are available in
                this list, ``false`` if the end of the list has been
                reached
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return ``true`` for this method.

        """
        if self._count is not None:
            # If count is available, use it
            return bool(self._count)
        else:
            # otherwise we have no idea
            return True

    def available(self):
        """Gets the number of elements available for retrieval.

        The number returned by this method may be less than or equal to
        the total number of elements in this list. To determine if the
        end of the list has been reached, the method ``has_next()``
        should be used. This method conveys what is known about the
        number of remaining elements at a point in time and can be used
        to determine a minimum size of the remaining elements, if known.
        A valid return is zero even if ``has_next()`` is true.

        This method does not imply asynchronous usage. All OSID methods
        may block.

        return: (cardinal) - the number of elements available for
                retrieval
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return a positive integer for this method so the consumer can
        continue execution to receive the error. In all other
        circumstances, the provider must not return a number greater
        than the number of elements known since this number will be fed
        as a parameter to the bulk retrieval method.

        """
        if self._count is not None:
            # If count is available, use it
            return self._count
        else:
            # We have no idea.
            return 0  # Don't know what to do here

    def skip(self, n=None):
        """Skip the specified number of elements in the list.

        If the number skipped is greater than the number of elements in
        the list, hasNext() becomes false and available() returns zero
        as there are no more elements to retrieve.

        arg:    n (cardinal): the number of elements to skip
        *compliance: mandatory -- This method must be implemented.*

        """
        # STILL NEED TO IMPLEMENT THIS ###
        pass
