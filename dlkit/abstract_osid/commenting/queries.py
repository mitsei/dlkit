"""Implementations of commenting abstract base class queries."""
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


class CommentQuery:
    """This is the query for searching comments.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_reference_id(self, source_id, match):
        """Sets reference ``Id``.

        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_reference_id_terms(self):
        """Clears the reference ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    reference_id_terms = property(fdel=clear_reference_id_terms)

    @abc.abstractmethod
    def match_commentor_id(self, resource_id, match):
        """Sets a resource ``Id`` to match a commentor.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_commentor_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commentor_id_terms = property(fdel=clear_commentor_id_terms)

    @abc.abstractmethod
    def supports_commentor_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commentor_query(self):
        """Gets the query for a resource query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_commentor_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commentor_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    commentor_query = property(fget=get_commentor_query)

    @abc.abstractmethod
    def clear_commentor_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commentor_terms = property(fdel=clear_commentor_terms)

    @abc.abstractmethod
    def match_commenting_agent_id(self, agent_id, match):
        """Sets an agent ``Id``.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_commenting_agent_id_terms(self):
        """Clears the agent ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commenting_agent_id_terms = property(fdel=clear_commenting_agent_id_terms)

    @abc.abstractmethod
    def supports_commenting_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commenting_agent_query(self):
        """Gets the query for an agent query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_commenting_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    commenting_agent_query = property(fget=get_commenting_agent_query)

    @abc.abstractmethod
    def clear_commenting_agent_terms(self):
        """Clears the agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commenting_agent_terms = property(fdel=clear_commenting_agent_terms)

    @abc.abstractmethod
    def match_text(self, text, string_match_type, match):
        """Matches text.

        :param text: the text
        :type text: ``string``
        :param string_match_type: a string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``text`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``text`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_text(self, match):
        """Matches a comment that has any text assigned.

        :param match: ``true`` to match comments with any text, ``false`` to match comments with no text
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_text_terms(self):
        """Clears the text terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    text_terms = property(fdel=clear_text_terms)

    @abc.abstractmethod
    def match_rating_id(self, grade_id, match):
        """Sets a grade ``Id``.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rating_id_terms(self):
        """Clears the rating ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rating_id_terms = property(fdel=clear_rating_id_terms)

    @abc.abstractmethod
    def supports_rating_query(self):
        """Tests if a ``GradeQuery`` is available.

        :return: ``true`` if a rating query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rating_query(self):
        """Gets the query for a rating query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the rating query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_rating_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    rating_query = property(fget=get_rating_query)

    @abc.abstractmethod
    def match_any_rating(self, match):
        """Matches books with any rating.

        :param match: ``true`` to match comments with any rating, ``false`` to match comments with no ratings
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rating_terms(self):
        """Clears the rating terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rating_terms = property(fdel=clear_rating_terms)

    @abc.abstractmethod
    def match_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match comments assigned to books.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_book_id_terms(self):
        """Clears the book ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    book_id_terms = property(fdel=clear_book_id_terms)

    @abc.abstractmethod
    def supports_book_query(self):
        """Tests if a ``BookQuery`` is available.

        :return: ``true`` if a book query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_query(self):
        """Gets the query for a book query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the book query
        :rtype: ``osid.commenting.BookQuery``
        :raise: ``Unimplemented`` -- ``supports_book_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        return  # osid.commenting.BookQuery

    book_query = property(fget=get_book_query)

    @abc.abstractmethod
    def clear_book_terms(self):
        """Clears the book terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    book_terms = property(fdel=clear_book_terms)

    @abc.abstractmethod
    def get_comment_query_record(self, comment_record_type):
        """Gets the comment query record corresponding to the given ``Comment`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the comment query record
        :rtype: ``osid.commenting.records.CommentQueryRecord``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentQueryRecord


class BookQuery:
    """This is the query for searching books.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_comment_id(self, comment_id, match):
        """Sets the comment ``Id`` for this query to match comments assigned to books.

        :param comment_id: a comment ``Id``
        :type comment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_comment_id_terms(self):
        """Clears the comment ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_id_terms = property(fdel=clear_comment_id_terms)

    @abc.abstractmethod
    def supports_comment_query(self):
        """Tests if a comment query is available.

        :return: ``true`` if a comment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_query(self):
        """Gets the query for a comment.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        return  # osid.commenting.CommentQuery

    comment_query = property(fget=get_comment_query)

    @abc.abstractmethod
    def match_any_comment(self, match):
        """Matches books with any comment.

        :param match: ``true`` to match books with any comment, ``false`` to match books with no comments
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_comment_terms(self):
        """Clears the comment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_terms = property(fdel=clear_comment_terms)

    @abc.abstractmethod
    def match_ancestor_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match books that have the specified book as an ancestor.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, a ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_book_id_terms(self):
        """Clears the ancestor book ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_book_id_terms = property(fdel=clear_ancestor_book_id_terms)

    @abc.abstractmethod
    def supports_ancestor_book_query(self):
        """Tests if a ``BookQuery`` is available.

        :return: ``true`` if a book query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_book_query(self):
        """Gets the query for a book.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the book query
        :rtype: ``osid.commenting.BookQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_book_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_book_query()`` is ``true``.*

        """
        return  # osid.commenting.BookQuery

    ancestor_book_query = property(fget=get_ancestor_book_query)

    @abc.abstractmethod
    def match_any_ancestor_book(self, match):
        """Matches books with any ancestor.

        :param match: ``true`` to match books with any ancestor, ``false`` to match root books
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_book_terms(self):
        """Clears the ancestor book terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_book_terms = property(fdel=clear_ancestor_book_terms)

    @abc.abstractmethod
    def match_descendant_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match books that have the specified book as a descendant.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_book_id_terms(self):
        """Clears the descendant book ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_book_id_terms = property(fdel=clear_descendant_book_id_terms)

    @abc.abstractmethod
    def supports_descendant_book_query(self):
        """Tests if a ``BookQuery`` is available.

        :return: ``true`` if a book query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_book_query(self):
        """Gets the query for a book.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the book query
        :rtype: ``osid.commenting.BookQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_book_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_book_query()`` is ``true``.*

        """
        return  # osid.commenting.BookQuery

    descendant_book_query = property(fget=get_descendant_book_query)

    @abc.abstractmethod
    def match_any_descendant_book(self, match):
        """Matches books with any descendant.

        :param match: ``true`` to match books with any descendant, ``false`` to match leaf books
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_book_terms(self):
        """Clears the descendant book terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_book_terms = property(fdel=clear_descendant_book_terms)

    @abc.abstractmethod
    def get_book_query_record(self, book_record_type):
        """Gets the book query record corresponding to the given ``Book`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param book_record_type: a book record type
        :type book_record_type: ``osid.type.Type``
        :return: the book query record
        :rtype: ``osid.commenting.records.BookQueryRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookQueryRecord
