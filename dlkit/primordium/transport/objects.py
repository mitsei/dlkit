"""
Generic implementions of osid.transport primitive objects.

Can be used by implementations and consumer applications alike.

"""
# pylint: disable=invalid-name
#    method argument 'n' defined in spec

from dlkit.abstract_osid.transport import objects as abc_transport_objects
from dlkit.abstract_osid.osid.errors import NullArgument, IllegalState


class DataInputStream(abc_transport_objects.DataInputStream):
    """The data input stream provides a means for reading data from a stream."""

    def __init__(self, input_data):
        self._my_data = input_data

    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, name):
        if not name.startswith('__'):
            try:
                return getattr(self._my_data, name)
            except:
                raise

    def at_end_of_stream(self):
        """Tests if the end of this stream has been reached.

        This may not be a permanent condition as more data may be
        available at a later time as in the case of tailing a file.

        return: (boolean) - ``true`` if the end of this stream has been
                reached, ``false`` otherwise
        raise:  IllegalState - this stream has been closed
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def available(self):
        """Gets the number of ``bytes`` available for retrieval.

        The number returned by this method may be less than or equal to
        the total number of ``bytes`` in this stream.

        return: (cardinal) - the number of ``bytes`` available for
                retrieval
        raise:  IllegalState - this stream has been closed
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def skip(self, n):
        """Skips a specified number of ``bytes`` in the stream.

        arg:    n (cardinal): the number of ``bytes`` to skip
        return: (cardinal) - the actual number of ``bytes`` skipped
        raise:  IllegalState - this stream has been closed or
                ``at_end_of_stream()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._my_data.closed or self.at_end_of_stream():
            raise IllegalState()
        if n is not None:
            self._my_data.seek(n)

    ##
    # The following two methods stray from the spec:

    def read_to_buffer(self, buf, n):
        """Reads a specified number of ``bytes`` from this stream.

        arg:    buf (byte[]): the buffer in which the data is read
        arg:    n (cardinal): the number of ``bytes`` to read
        return: (integer) - the actual number of ``bytes`` read
        raise:  IllegalState - this stream has been closed or
                ``at_end_of_stream()`` is ``true``
        raise:  InvalidArgument - the size of ``buf`` is less than ``n``
        raise:  NullArgument - ``buf`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if buf is None:
            raise NullArgument()
        if self._my_data.closed or self.at_end_of_stream():
            raise IllegalState()
        initial_buf_len = len(buf)
        buf.append(self._my_data.read(size=n))
        return len(buf) - initial_buf_len

    def read(self, buf=None, n=None):
        """Reads a specified number of ``bytes`` from this stream.

        arg:    n (cardinal): the number of ``bytes`` to read
        return: (integer) - the ``bytes`` read
        raise:  IllegalState - this stream has been closed or
                ``at_end_of_stream()`` is ``true``
        raise:  InvalidArgument - the size of ``buf`` is less than ``n``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if n is not None:
            return self._my_data.read(n)
        else:
            return self._my_data.read()

    def close(self):
        """Closes this stream and frees up any allocated resources.

        Methods in this object may not be invoked after this method is
        called.

        raise:  IllegalState - this stream has been closed
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._my_data.closed:
            raise IllegalState()
        self._my_data.close()
