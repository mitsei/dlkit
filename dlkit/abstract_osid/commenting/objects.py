"""Implementations of commenting abstract base class objects."""
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


class Comment:
    """A ``Comment`` represents a comment and/or rating related to a reference object in a book."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_reference_id(self):
        """Gets the ``Id`` of the referenced object to which this comment pertains.

        :return: the reference ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    reference_id = property(fget=get_reference_id)

    @abc.abstractmethod
    def get_commentor_id(self):
        """Gets the ``Id`` of the resource who created this comment.

        :return: the ``Resource``  ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    commentor_id = property(fget=get_commentor_id)

    @abc.abstractmethod
    def get_commentor(self):
        """Gets the resource who created this comment.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    commentor = property(fget=get_commentor)

    @abc.abstractmethod
    def get_commenting_agent_id(self):
        """Gets the ``Id`` of the agent who created this comment.

        :return: the ``Agent``  ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    commenting_agent_id = property(fget=get_commenting_agent_id)

    @abc.abstractmethod
    def get_commenting_agent(self):
        """Gets the agent who created this comment.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    commenting_agent = property(fget=get_commenting_agent)

    @abc.abstractmethod
    def get_text(self):
        """Gets the comment text.

        :return: the comment text
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    text = property(fget=get_text)

    @abc.abstractmethod
    def has_rating(self):
        """Tests if this comment includes a rating.

        :return: ``true`` if this comment includes a rating, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rating_id(self):
        """Gets the ``Id`` of the ``Grade``.

        :return: the ``Agent``  ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_rating()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    rating_id = property(fget=get_rating_id)

    @abc.abstractmethod
    def get_rating(self):
        """Gets the ``Grade``.

        :return: the ``Grade``
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_rating()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    rating = property(fget=get_rating)

    @abc.abstractmethod
    def get_comment_record(self, comment_record_type):
        """Gets the comment record corresponding to the given ``Comment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``comment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(comment_record_type)`` is ``true`` .

        :param comment_record_type: the type of comment record to retrieve
        :type comment_record_type: ``osid.type.Type``
        :return: the comment record
        :rtype: ``osid.commenting.records.CommentRecord``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentRecord


class CommentForm:
    """This is the form for creating and updating ``Comment`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CommentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_text_metadata(self):
        """Gets the metadata for the text.

        :return: metadata for the text
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    text_metadata = property(fget=get_text_metadata)

    @abc.abstractmethod
    def set_text(self, text):
        """Sets the text.

        :param text: the new text
        :type text: ``string``
        :raise: ``InvalidArgument`` -- ``text`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``text`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_text(self):
        """Clears the text.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    text = property(fset=set_text, fdel=clear_text)

    @abc.abstractmethod
    def get_rating_metadata(self):
        """Gets the metadata for a rating.

        :return: metadata for the rating
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    rating_metadata = property(fget=get_rating_metadata)

    @abc.abstractmethod
    def set_rating(self, grade_id):
        """Sets the rating.

        :param grade_id: the new rating
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rating(self):
        """Clears the rating.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rating = property(fset=set_rating, fdel=clear_rating)

    @abc.abstractmethod
    def get_comment_form_record(self, comment_record_type):
        """Gets the ``CommentFormRecord`` corresponding to the given comment record ``Type``.

        :param comment_record_type: the comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the comment form record
        :rtype: ``osid.commenting.records.CommentFormRecord``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentFormRecord


class CommentList:
    """Like all ``OsidLists,``  ``CommentList`` provides a means for accessing ``Comment`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Comment comment =
    cl.getNextComment(); }

    or
      while (cl.hasNext()) {
           Comment[] comments = cl.getNextComments(cl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_comment(self):
        """Gets the next ``Comment`` in this list.

        :return: the next ``Comment`` in this list. The ``has_next()`` method should be used to test that a next ``Comment`` is available before calling this method.
        :rtype: ``osid.commenting.Comment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Comment

    next_comment = property(fget=get_next_comment)

    @abc.abstractmethod
    def get_next_comments(self, n):
        """Gets the next set of ``Comment`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Comment`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Comment`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.commenting.Comment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Comment


class Book:
    """A ``Book`` represents a collection of comments.

    Like all OSID objects, a ``Book`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_record(self, book_record_type):
        """Gets the book record corresponding to the given ``Book`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``book_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(book_record_type)``
        is ``true`` .

        :param book_record_type: the type of book record to retrieve
        :type book_record_type: ``osid.type.Type``
        :return: the book record
        :rtype: ``osid.commenting.records.BookRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookRecord


class BookForm:
    """This is the form for creating and updating ``Books``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_form_record(self, book_record_type):
        """Gets the ``BookFormRecord`` corresponding to the given book record ``Type``.

        :param book_record_type: the book record type
        :type book_record_type: ``osid.type.Type``
        :return: the book form record
        :rtype: ``osid.commenting.records.BookFormRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookFormRecord


class BookList:
    """Like all ``OsidLists,``  ``BookList`` provides a means for accessing ``Book`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Book book = bl.getNextBook(); }

    or
      while (bl.hasNext()) {
           Book[] books = bl.getNextBooks(bl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_book(self):
        """Gets the next ``Book`` in this list.

        :return: the next ``Book`` in this list. The ``has_next()`` method should be used to test that a next ``Book`` is available before calling this method.
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    next_book = property(fget=get_next_book)

    @abc.abstractmethod
    def get_next_books(self, n):
        """Gets the next set of ``Book`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Book`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Book`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book


class BookNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BookHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` at this node.

        :return: the book represented by this node
        :rtype: ``osid.commenting.Book``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def get_parent_book_nodes(self):
        """Gets the parents of this book.

        :return: the parents of this book
        :rtype: ``osid.commenting.BookNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookNodeList

    parent_book_nodes = property(fget=get_parent_book_nodes)

    @abc.abstractmethod
    def get_child_book_nodes(self):
        """Gets the children of this book.

        :return: the children of this book
        :rtype: ``osid.commenting.BookNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookNodeList

    child_book_nodes = property(fget=get_child_book_nodes)


class BookNodeList:
    """Like all ``OsidLists,``  ``BookNodeList`` provides a means for accessing ``BookNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BookNode node =
    bnl.getNextBookNode(); }

    or
      while (bnl.hasNext()) {
           BookNode[] nodes = bnl.getNextBookNodes(bnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_book_node(self):
        """Gets the next ``BookNode`` in this list.

        :return: the next ``BookNode`` in this list. The ``has_next()`` method should be used to test that a next ``BookNode`` is available before calling this method.
        :rtype: ``osid.commenting.BookNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookNode

    next_book_node = property(fget=get_next_book_node)

    @abc.abstractmethod
    def get_next_book_nodes(self, n):
        """Gets the next set of ``BookNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``BookNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``BookNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.commenting.BookNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookNode
