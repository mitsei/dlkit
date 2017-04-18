"""Implementations of commenting abstract base class search_orders."""
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


class CommentSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_reference(self, style):
        """Specifies a preference for ordering the result set by the reference.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_commentor(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_commentor_search_order(self):
        """Tests if a resource order interface is available.

        :return: ``true`` if a resource order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commentor_search_order(self):
        """Gets the resource order interface.

        :return: the resource search order interface
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_commentor_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commentor_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    commentor_search_order = property(fget=get_commentor_search_order)

    @abc.abstractmethod
    def order_by_commenting_agent(self, style):
        """Specifies a preference for ordering the result set by the agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_commenting_agent_search_order(self):
        """Tests if an agent order interface is available.

        :return: ``true`` if an agent order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_commenting_agent_search_order(self):
        """Gets the agent order interface.

        :return: the agent search order interface
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_commenting_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    commenting_agent_search_order = property(fget=get_commenting_agent_search_order)

    @abc.abstractmethod
    def order_by_text(self, style):
        """Specifies a preference for ordering the result set by the text.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_rating(self, style):
        """Specifies a preference for ordering the result set by the rating.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_rating_search_order(self):
        """Tests if a rating order interface is available.

        :return: ``true`` if a rating order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_rating_search_order(self):
        """Gets the rating order interface.

        :return: the rating search order interface
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_rating_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rating_search_order()`` is ``true``.*

        """
        return  # osid.grading.GradeSearchOrder

    rating_search_order = property(fget=get_rating_search_order)

    @abc.abstractmethod
    def get_comment_search_order_record(self, comment_record_type):
        """Gets the comment search order record corresponding to the given comment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the comment search order record
        :rtype: ``osid.commenting.records.CommentSearchOrderRecord``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.CommentSearchOrderRecord


class BookSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_search_order_record(self, book_record_type):
        """Gets the book search order record corresponding to the given book record Type.

        Multiple retrievals return the same underlying object.

        :param book_record_type: a book record type
        :type book_record_type: ``osid.type.Type``
        :return: the book search order record
        :rtype: ``osid.commenting.records.BookSearchOrderRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.records.BookSearchOrderRecord
