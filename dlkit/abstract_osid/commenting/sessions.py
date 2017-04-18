"""Implementations of commenting abstract base class sessions."""
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


class CommentLookupSession:
    """This session defines methods for retrieving comments."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_lookup_comments(self):
        """Tests if this user can examine this book.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if book reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_comment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_comment_view(self):
        """A complete view of the ``Comment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_effective_comment_view(self):
        """Only comments whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_effective_comment_view(self):
        """All comments of any effective dates are returned by all methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_comment(self, comment_id):
        """Gets the ``Comment`` specified by its ``Id``.

        :param comment_id: the ``Id`` of the ``Comment`` to retrieve
        :type comment_id: ``osid.id.Id``
        :return: the returned ``Comment``
        :rtype: ``osid.commenting.Comment``
        :raise: ``NotFound`` -- no ``Comment`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Comment

    @abc.abstractmethod
    def get_comments_by_ids(self, comment_ids):
        """Gets a ``CommentList`` corresponding to the given ``IdList``.

        :param comment_ids: the list of ``Ids`` to retrieve
        :type comment_ids: ``osid.id.IdList``
        :return: the returned ``Comment list``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``comment_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` which does not include comments of genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_parent_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` and include any additional comments with genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_record_type(self, comment_record_type):
        """Gets a ``CommentList`` containing the given comment record ``Type``.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_on_date(self, from_, to):
        """Gets a ``CommentList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_on_date(self, comment_genus_type, from_, to):
        """Gets a ``CommentList`` of a given genus type and effective during the entire given date range inclusive but not confined to the date range.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_commentor(self, resource_id):
        """Gets a list of comments corresponding to a resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_commentor_on_date(self, resource_id, from_, to):
        """Gets a list of all comments corresponding to a resource ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_commentor(self, resource_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_commentor_on_date(self, resource_id, comment_genus_type, from_, to):
        """Gets a list of all comments of the given genus type corresponding to a resource ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_reference(self, reference_id):
        """Gets a list of comments corresponding to a reference ``Id``.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_reference_on_date(self, reference_id, from_, to):
        """Gets a list of all comments corresponding to a reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``reference_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_reference(self, reference_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a reference ``Id``.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``reference_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_reference_on_date(self, reference_id, comment_genus_type, from_, to):
        """Gets a list of all comments of the given genus type corresponding to a reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``reference_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_commentor_and_reference(self, resource_id, reference_id):
        """Gets a list of comments corresponding to a resource and reference ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_for_commentor_and_reference_on_date(self, resource_id, reference_id, from_, to):
        """Gets a list of all comments corresponding to a resource and reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, reference_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_commentor_and_reference(self, resource_id, reference_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a resource and reference ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id, reference_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments_by_genus_type_for_commentor_and_reference_on_date(self, resource_id, reference_id, comment_genus_type, from_, to):
        """Gets a list of all comments corresponding to a resource and reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, reference_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comments(self):
        """Gets all comments.

        :return: a list of comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    comments = property(fget=get_comments)


class RatingLookupSession:
    """This session defines methods for retrieving comments."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_lookup_ratings(self):
        """Tests if this user can examine this book.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if book reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_comment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_comment_view(self):
        """A complete view of the ``Comment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include ratings in books which are
        children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_cumulative_rating(self):
        """Gets the cumulative rating for all the references in this book.

        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    cumulative_rating = property(fget=get_cumulative_rating)

    @abc.abstractmethod
    def get_cumulative_rating_for_reference(self, reference_id):
        """Gets the cumulative rating for a reference.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no reference found with the given ``Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    @abc.abstractmethod
    def get_cumulative_rating_for_commentor(self, resource_id):
        """Gets the cumulative rating for a commentor.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no resource found with the given ``Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    @abc.abstractmethod
    def get_top_references(self, max_):
        """Gets the top rated references in this book.

        :param max: the maximum number to return
        :type max: ``cardinal``
        :return: the top references
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_references(self, grade_id):
        """Gets the references with ratings equal to or higher than the given grade.

        :param grade_id: the ``Id`` of the grade
        :type grade_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no reference found with the given ``Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade


class CommentQuerySession:
    """This session provides methods for searching ``Comment`` objects.

    The search query is constructed using the ``CommentQuery``. The book
    record ``Type`` also specifies the record for the book query.

    Comments may have a query record indicated by their respective
    record types. The query record is accessed via the ``CommentQuery``.
    The returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_search_comments(self):
        """Tests if this user can perform comment searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_comment_query(self):
        """Gets a comment query.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQuery

    comment_query = property(fget=get_comment_query)

    @abc.abstractmethod
    def get_comments_by_query(self, comment_query):
        """Gets a list of comments matching the given search.

        :param comment_query: the search query array
        :type comment_query: ``osid.commenting.CommentQuery``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList


class CommentSearchSession:
    """This session provides methods for searching ``Comment`` objects.

    The search query is constructed using the ``CommentQuery``. The
    comment record ``Type`` also specifies the record for the comment
    query.

    ``get_comments_by_query()`` is the basic search method and returns a
    list of ``Comment`` elements. A more advanced search may be
    performed with ``getCommentsBySearch()``. It accepts a
    ``CommentSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_comments_by_search()`` returns a
    ``CommentSearchResults`` that can be used to access the resulting
    ``CommentList`` or be used to perform a search within the result set
    through ``CommentSearch``.

    Comments may have a query record indicated by their respective
    record types. The query record is accessed via the ``CommentQuery``.
    The returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_comment_search(self):
        """Gets a comment search.

        :return: the comment search
        :rtype: ``osid.commenting.CommentSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentSearch

    comment_search = property(fget=get_comment_search)

    @abc.abstractmethod
    def get_comment_search_order(self):
        """Gets a comment search order.

        The ``CommentSearchOrder`` is supplied to a ``CommentSearch`` to
        specify the ordering of results.

        :return: the comment search order
        :rtype: ``osid.commenting.CommentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentSearchOrder

    comment_search_order = property(fget=get_comment_search_order)

    @abc.abstractmethod
    def get_comments_by_search(self, comment_query, comment_search):
        """Gets the search results matching the given search.

        :param comment_query: the comment query
        :type comment_query: ``osid.commenting.CommentQuery``
        :param comment_search: the comment search
        :type comment_search: ``osid.commenting.CommentSearch``
        :return: the search results
        :rtype: ``osid.commenting.CommentSearchResults``
        :raise: ``NullArgument`` -- ``comment_query`` or ``comment_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_query`` or ``comment_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentSearchResults

    @abc.abstractmethod
    def get_comment_query_from_inspector(self, comment_query_inspector):
        """Gets an entry query from an inspector.

        The inspector is available from an ``CommentSearchResults``.

        :param comment_query_inspector: a comment query inspector
        :type comment_query_inspector: ``osid.commenting.CommentQueryInspector``
        :return: the entry query
        :rtype: ``osid.commenting.CommentQuery``
        :raise: ``NullArgument`` -- ``comment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``comment_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQuery


class CommentAdminSession:
    """This session creates, updates, and deletes ``Comments``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Comment,`` a ``CommentForm`` is requested using
    ``get_comment_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``CommentForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``CommentForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``CommentForm`` corresponds to an attempted
    transaction.

    For updates, ``CommentForms`` are requested to the ``Comment``
    ``Id`` that is to be updated using ``getCommentFormForUpdate()``.
    Similarly, the ``CommentForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``CommentForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Comments``. To unmap a ``Comment``
    from the current ``Book,`` the ``CommentBookAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Comment`` itself thus removing it from all known ``Book``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_create_comments(self):
        """Tests if this user can create comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Comment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_comment_with_record_types(self, comment_record_types):
        """Tests if this user can create a single ``Comment`` using the desired record types.

        While ``CommentingManager.getCommentRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Comment``.
        Providing an empty array tests if a ``Comment`` can be created
        with no records.

        :param comment_record_types: array of comment record types
        :type comment_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Comment`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_form_for_create(self, reference_id, comment_record_types):
        """Gets the comment form for creating new comments.

        A new form should be requested for each create transaction.

        :param reference_id: the ``Id`` for the reference object
        :type reference_id: ``osid.id.Id``
        :param comment_record_types: array of comment record types
        :type comment_record_types: ``osid.type.Type[]``
        :return: the comment form
        :rtype: ``osid.commenting.CommentForm``
        :raise: ``NullArgument`` -- ``reference_id or comment_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentForm

    @abc.abstractmethod
    def create_comment(self, comment_form):
        """Creates a new ``Comment``.

        :param comment_form: the form for this ``Comment``
        :type comment_form: ``osid.commenting.CommentForm``
        :return: the new ``Comment``
        :rtype: ``osid.commenting.Comment``
        :raise: ``IllegalState`` -- ``comment_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``comment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_form`` did not originate from ``get_comment_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Comment

    @abc.abstractmethod
    def can_update_comments(self):
        """Tests if this user can update comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Comment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_form_for_update(self, comment_id):
        """Gets the comment form for updating an existing comment.

        A new comment form should be requested for each update
        transaction.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: the comment form
        :rtype: ``osid.commenting.CommentForm``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentForm

    @abc.abstractmethod
    def update_comment(self, comment_form):
        """Updates an existing comment.

        :param comment_form: the form containing the elements to be updated
        :type comment_form: ``osid.commenting.CommentForm``
        :raise: ``IllegalState`` -- ``comment_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``comment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_form`` did not originate from ``get_comment_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_comments(self):
        """Tests if this user can delete comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Comment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_comment(self, comment_id):
        """Deletes a ``Comment``.

        :param comment_id: the ``Id`` of the ``Comment`` to remove
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_comment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Comnents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Comment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_comment(self, comment_id, alias_id):
        """Adds an ``Id`` to a ``Comment`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Comment`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another comment, it is
        reassigned to the given comment ``Id``.

        :param comment_id: the ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``comment_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CommentNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Comment`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_register_for_comment_notifications(self):
        """Tests if this user can register for ``Comment`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for commentss in
        books which are children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_comment_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_comment_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_comment_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_comment_notification(self, notification_id):
        """Acknowledge a comment notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_comments(self):
        """Register for notifications of new comments.

        ``CommentReceiver.newComments()`` is invoked when a new
        ``Comment`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_comments_for_commentor(self, resource_id):
        """Register for notifications of new comments by the given resource ``Id``.

        ``CommentReceiver.newComments()`` is invoked when a new
        ``Comment`` is created.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_comments_for_reference(self, reference_id):
        """Register for notifications of new comments for the given reference ``Id``.

        ``CommentReceiver.newComments()`` is invoked when a new
        ``Comment`` is created.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_comments(self):
        """Registers for notification of updated comments.

        ``CommentReceiver.changedComments()`` is invoked when a comment
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_comments_for_commentor(self, resource_id):
        """Register for notifications of changed comments by the given resource ``Id``.

        ``CommentReceiver.changedComments()`` is invoked when a
        ``Comment`` by the resource is changed.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_comments_for_reference(self, reference_id):
        """Register for notifications of changed comments for the given reference ``Id``.

        ``CommentReceiver.changedComments()`` is invoked when a
        ``Comment`` for the reference is changed.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_comment(self, comment_id):
        """Registers for notification of an updated comment.

        ``CommentReceiver.changedComments()`` is invoked when the
        specified comment is changed.

        :param comment_id: the ``Id`` of the ``Comment`` to monitor
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a comment was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_comments(self):
        """Registers for notification of deleted comments.

        ``CommentReceiver.deletedComments()`` is invoked when a comment
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_comments_for_commentor(self, resource_id):
        """Register for notifications of deleted comments by the given resource ``Id``.

        ``CommentReceiver.deletedComments()`` is invoked when a
        ``Comment`` by the resource is deleted.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_comments_for_reference(self, reference_id):
        """Register for notifications of deleted comments for the given reference ``Id``.

        ``CommentReceiver.deletedComments()`` is invoked when a
        ``Comment`` for the reference is deleted.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_comment(self, comment_id):
        """Registers for notification of a deleted comment.

        ``CommentReceiver.deletedComments()`` is invoked when the
        specified comment is deleted.

        :param comment_id: the ``Id`` of the ``Comment`` to monitor
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a comment was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_comment_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_comment_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_comment_notification(self, notification_id):
        """Acknowledge an comment notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CommentBookSession:
    """This session provides methods to retrieve ``Comment`` to ``Book`` mappings.

    A ``Comment`` may appear in multiple ``Books``. Each ``Book`` may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_comment_book_mappings(self):
        """Tests if this user can perform lookups of comment/book mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intendedas a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_book_view(self):
        """A complete view of the ``Comment`` and ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_comment_ids_by_book(self, book_id):
        """Gets the list of Comment Ids associated with a ``Book``.

        :param book_id: ``Id`` of a ``Book``.
        :type book_id: ``osid.id.Id``
        :return: list of related comment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_comments_by_book(self, book_id):
        """Gets the list of ``Comments`` associated with a ``Book``.

        :param book_id: ``Id`` of a ``Book``
        :type book_id: ``osid.id.Id``
        :return: list of related comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_comment_ids_by_books(self, book_ids):
        """Gets the list of ``Comment Ids`` corresponding to a list of ``Book`` objects.

        :param book_ids: list of book ``Ids``
        :type book_ids: ``osid.id.IdList``
        :return: list of comment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_comments_by_books(self, book_ids):
        """Gets the list of ``Comments`` corresponding to a list of ``Books``.

        :param book_ids: list of book ``Ids``
        :type book_ids: ``osid.id.IdList``
        :return: list of comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentList

    @abc.abstractmethod
    def get_book_ids_by_comment(self, comment_id):
        """Gets the list of ``Book``  ``Ids`` mapped to a ``Comment``.

        :param comment_id: ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_books_by_comment(self, comment_id):
        """Gets the list of ``Book`` objects mapped to a ``Comment``.

        :param comment_id: ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of books
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList


class CommentBookAssignmentSession:
    """This session provides methods to re-assign ``Comments`` to ``Books``.

    A ``Comment`` may map to multiple ``Books`` and removing the last
    reference to a ``Comment`` is the equivalent of deleting it. Each
    ``Book`` may have its own authorizations governing who is allowed to
    operate on it.

    Adding a reference of a ``Comment`` to another ``Book`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_comments(self):
        """Tests if this user can alter comment/book mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_comments_to_book(self, book_id):
        """Tests if this user can alter comment/book mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_book_ids(self, book_id):
        """Gets a list of books including and under the given book node in which any comment can be assigned.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: list of assignable book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_book_ids_for_comment(self, book_id, comment_id):
        """Gets a list of books including and under the given book node in which a specific comment can be assigned.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of assignable book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_id`` or ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_comment_to_book(self, comment_id, book_id):
        """Adds an existing ``Comment`` to a ``Book``.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``comment_id`` is already assigned to ``book_id``
        :raise: ``NotFound`` -- ``comment_id`` or ``book_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_comment_from_book(self, comment_id, book_id):
        """Removes a ``Comment`` from a ``Book``.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id`` or ``book_id`` not found or ``comment_id`` not assigned to ``book_id``
        :raise: ``NullArgument`` -- ``comment_id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_comment_to_book(self, comment_id, from_book_id, to_book_id):
        """Moves a ``Credit`` from one ``Book`` to another.

        Mappings to other ``Books`` are unaffected.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :param from_book_id: the ``Id`` of the current ``Book``
        :type from_book_id: ``osid.id.Id``
        :param to_book_id: the ``Id`` of the destination ``Book``
        :type to_book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id, from_book_id,`` or ``to_book_id`` not found or ``comment`` not mapped to ``from_book_id``
        :raise: ``NullArgument`` -- ``comment_id, book_id_id,`` or ``to_book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class CommentSmartBookSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``CommentQuery`` can be retrieved from this session and mapped to
    this ``Book`` to create a virtual collection of ``Comments``. The
    comments may be sequenced using the ``CommentSearchOrder`` from this
    session.

    This ``Book`` has a default query that matches any comment and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``CommentQueryInspector``. The query may be
    modified by converting the inspector back to a ``CommentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_id = property(fget=get_book_id)

    @abc.abstractmethod
    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the ``Book`` associated with this session
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    book = property(fget=get_book)

    @abc.abstractmethod
    def can_manage_smart_books(self):
        """Tests if this user can manage smart books.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart book management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_comment_query(self):
        """Gets a comment query.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQuery

    comment_query = property(fget=get_comment_query)

    @abc.abstractmethod
    def get_comment_search_order(self):
        """Gets a comment search order.

        :return: the comment search order
        :rtype: ``osid.commenting.CommentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentSearchOrder

    comment_search_order = property(fget=get_comment_search_order)

    @abc.abstractmethod
    def apply_comment_query(self, comment_query):
        """Applies a comment query to this book.

        :param comment_query: the comment query
        :type comment_query: ``osid.commenting.CommentQuery``
        :raise: ``NullArgument`` -- ``comment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``comment_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_comment_query(self):
        """Gets a comment query inspector for this book.

        :return: the comment query inspector
        :rtype: ``osid.commenting.CommentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQueryInspector

    @abc.abstractmethod
    def apply_comment_sequencing(self, comment_search_order):
        """Applies a comment search order to this book.

        :param comment_search_order: the comment search order
        :type comment_search_order: ``osid.commenting.CommentSearchOrder``
        :raise: ``NullArgument`` -- ``comment_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``comment_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_comment_query_from_inspector(self, comment_query_inspector):
        """Gets a comment query from an inspector.

        :param comment_query_inspector: a query inspector
        :type comment_query_inspector: ``osid.commenting.CommentQueryInspector``
        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``
        :raise: ``NullArgument`` -- ``comment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``comment_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.CommentQuery


class BookLookupSession:
    """This session provides methods for retrieving ``Book`` objects.

    The ``Book`` represents a collection of comments.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_books(self):
        """Tests if this user can perform ``Book`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_book(self, book_id):
        """Gets the ``Book`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Book`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Book`` and retained for compatibility.

        :param book_id: ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.commenting.Book

    @abc.abstractmethod
    def get_books_by_ids(self, book_ids):
        """Gets a ``BookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the books
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Books`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param book_ids: the list of ``Ids`` to retrieve
        :type book_ids: ``osid.id.IdList``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def get_books_by_genus_type(self, book_genus_type):
        """Gets a ``BookList`` corresponding to the given book genus ``Type`` which does not include books of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_genus_type: a book genus type
        :type book_genus_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def get_books_by_parent_genus_type(self, book_genus_type):
        """Gets a ``BookList`` corresponding to the given book genus ``Type`` and include any additional books with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_genus_type: a book genus type
        :type book_genus_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def get_books_by_record_type(self, book_record_type):
        """Gets a ``BookList`` containing the given book record ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_record_type: a book record type
        :type book_record_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def get_books_by_provider(self, resource_id):
        """Gets a ``BookList`` from the given provider ````.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def get_books(self):
        """Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: a list of ``Books``
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    books = property(fget=get_books)


class BookQuerySession:
    """This session provides methods for searching ``Book`` objects.

    The search query is constructed using the ``BookQuery``. The book
    record ``Type`` also specifies the record for the book query.

    Books may have a query record indicated by their respective record
    types. The query record is accessed via the ``BookQuery``. The
    returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_books(self):
        """Tests if this user can perform ``Book`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_query(self):
        """Gets a book query.

        :return: the book query
        :rtype: ``osid.commenting.BookQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookQuery

    book_query = property(fget=get_book_query)

    @abc.abstractmethod
    def get_books_by_query(self, book_query):
        """Gets a list of ``Books`` matching the given search.

        :param book_query: the book query
        :type book_query: ``osid.commenting.BookQuery``
        :return: the returned ``BookList``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList


class BookSearchSession:
    """This session provides methods for searching ``Book`` objects.

    The search query is constructed using the ``BookQuery``. The book
    record ``Type`` also specifies the record for the book query.

    ``get_books_by_query()`` is the basic search method and returns a
    list of ``Book`` elements. A more advanced search may be performed
    with ``getBooksBySearch()``. It accepts a ``BookSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_books_by_search()`` returns a ``BookSearchResults`` that can
    be used to access the resulting ``BookList`` or be used to perform a
    search within the result set through ``BookSearch``.

    Books may have a query record indicated by their respective record
    types. The query record is accessed via the ``BookQuery``. The
    returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_search(self):
        """Gets a book search.

        :return: the book search
        :rtype: ``osid.commenting.BookSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookSearch

    book_search = property(fget=get_book_search)

    @abc.abstractmethod
    def get_book_search_order(self):
        """Gets a book search order.

        The ``BookSearchOrder`` is supplied to a ``BookSearch`` to
        specify the ordering of results.

        :return: the book search order
        :rtype: ``osid.commenting.BookSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookSearchOrder

    book_search_order = property(fget=get_book_search_order)

    @abc.abstractmethod
    def get_books_by_search(self, book_query, book_search):
        """Gets the search results matching the given search.

        :param book_query: the book query
        :type book_query: ``osid.commenting.BookQuery``
        :param book_search: the book search
        :type book_search: ``osid.commenting.BookSearch``
        :return: the search results
        :rtype: ``osid.commenting.BookSearchResults``
        :raise: ``NullArgument`` -- ``book_query`` or ``book_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_query`` or ``book_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookSearchResults

    @abc.abstractmethod
    def get_book_query_from_inspector(self, book_query_inspector):
        """Gets an entry query from an inspector.

        The inspector is available from an ``BookSearchResults``.

        :param book_query_inspector: a book query inspector
        :type book_query_inspector: ``osid.commenting.BookQueryInspector``
        :return: the book query
        :rtype: ``osid.commenting.BookQuery``
        :raise: ``NullArgument`` -- ``book_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``book_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookQuery


class BookAdminSession:
    """This session creates, updates, and deletes ``Books``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Book,`` a ``BookForm`` is requested using
    ``get_book_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BookForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BookForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BookForm`` corresponds
    to an attempted transaction.

    For updates, ``BookForms`` are requested to the ``Book``  ``Id``
    that is to be updated using ``getBookFormForUpdate()``. Similarly,
    the ``BookForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``BookForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Books``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_books(self):
        """Tests if this user can create ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Book`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_book_with_record_types(self, book_record_types):
        """Tests if this user can create a single ``Book`` using the desired record types.

        While ``CommentingManager.getBookRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Book``.
        Providing an empty array tests if a ``Book`` can be created with
        no records.

        :param book_record_types: array of book record types
        :type book_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Book`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_form_for_create(self, book_record_types):
        """Gets the book form for creating new books.

        A new form should be requested for each create transaction.

        :param book_record_types: array of book record types
        :type book_record_types: ``osid.type.Type[]``
        :return: the book form
        :rtype: ``osid.commenting.BookForm``
        :raise: ``NullArgument`` -- ``book_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookForm

    @abc.abstractmethod
    def create_book(self, book_form):
        """Creates a new ``Book``.

        :param book_form: the form for this ``Book``
        :type book_form: ``osid.commenting.BookForm``
        :return: the new ``Book``
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- ``book_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``book_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_form`` did not originte from ``get_book_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.Book

    @abc.abstractmethod
    def can_update_books(self):
        """Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Book`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_form_for_update(self, book_id):
        """Gets the book form for updating an existing book.

        A new book form should be requested for each update transaction.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: the book form
        :rtype: ``osid.commenting.BookForm``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookForm

    @abc.abstractmethod
    def update_book(self, book_form):
        """Updates an existing book.

        :param book_form: the form containing the elements to be updated
        :type book_form: ``osid.commenting.BookForm``
        :raise: ``IllegalState`` -- ``book_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``book_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_form`` did not originte from ``get_book_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_books(self):
        """Tests if this user can delete ``Books`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Book`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_book(self, book_id):
        """Deletes a ``Book``.

        :param book_id: the ``Id`` of the ``Book`` to remove
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_book_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Book`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_book(self, book_id, alias_id):
        """Adds an ``Id`` to a ``Book`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Book`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another book, it is
        reassigned to the given book ``Id``.

        :param book_id: the ``Id`` of a ``Book``
        :type book_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BookNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Book`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to the ``Book`` object
    itself. Adding and removing comments result in notifications
    available from the notification session for comments.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_book_notifications(self):
        """Tests if this user can register for ``Book`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def reliable_book_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_book_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_book_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_book_notification(self, notification_id):
        """Acknowledge a book notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_books(self):
        """Register for notifications of new books.

        ``BookReceiver.newBooks()`` is invoked when a new ``Book`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_books(self):
        """Registers for notification of updated books.

        ``BookReceiver.changedBooks()`` is invoked when a book is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_book(self, book_id):
        """Registers for notification of an updated book.

        ``BookReceiver.changedBooks()`` is invoked when the specified
        book is changed.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_books(self):
        """Registers for notification of deleted books.

        ``BookReceiver.deletedBooks()`` is invoked when a book is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_book(self, book_id):
        """Registers for notification of a deleted book.

        ``BookReceiver.deletedBooks()`` is invoked when the specified
        book is deleted.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_book_hierarchy(self):
        """Registers for notification of an updated book hierarchy structure.

        ``BookReceiver.changedChildOfBookss()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_book_hierarchy_for_ancestors(self, book_id):
        """Registers for notification of an updated book hierarchy structure.

        ``BookReceiver.changedChildOfBooks()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param book_id: the ``Id`` of the ``Book`` node to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_book_hierarchy_for_descendants(self, book_id):
        """Registers for notification of an updated book hierarchy structure.

        ``BookReceiver.changedChildOfBooks()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param book_id: the ``Id`` of the ``Book`` node to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_book_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_book_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_book_notification(self, notification_id):
        """Acknowledge an book notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BookHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Book`` objects.

    Each node in the hierarchy is a unique ``Book``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_books()`` and ``getChildBooks()``. To relate these
    ``Ids`` to another OSID, ``get_book_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Book`` available in the Commenting OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_books()`` or ``get_child_books()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: book elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    @abc.abstractmethod
    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    book_hierarchy = property(fget=get_book_hierarchy)

    @abc.abstractmethod
    def can_access_book_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_book_view(self):
        """The returns from the book methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_book_ids(self):
        """Gets the root book ``Ids`` in this hierarchy.

        :return: the root book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_book_ids = property(fget=get_root_book_ids)

    @abc.abstractmethod
    def get_root_books(self):
        """Gets the root books in the book hierarchy.

        A node with no parents is an orphan. While all book ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root books
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.commenting.BookList

    root_books = property(fget=get_root_books)

    @abc.abstractmethod
    def has_parent_books(self, book_id):
        """Tests if the ``Book`` has any parents.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the book has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_book(self, id_, book_id):
        """Tests if an ``Id`` is a direct parent of book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``book_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_book_ids(self, book_id):
        """Gets the parent ``Ids`` of the given book.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the book
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_books(self, book_id):
        """Gets the parent books of the given ``id``.

        :param book_id: the ``Id`` of the ``Book`` to query
        :type book_id: ``osid.id.Id``
        :return: the parent books of the ``id``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- a ``Book`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def is_ancestor_of_book(self, id_, book_id):
        """Tests if an ``Id`` is an ancestor of a book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_books(self, book_id):
        """Tests if a book has any children.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``book_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_book(self, id_, book_id):
        """Tests if a book is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_book_ids(self, book_id):
        """Gets the child ``Ids`` of the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :return: the children of the book
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_books(self, book_id):
        """Gets the child books of the given ``id``.

        :param book_id: the ``Id`` of the ``Book`` to query
        :type book_id: ``osid.id.Id``
        :return: the child books of the ``id``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- a ``Book`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookList

    @abc.abstractmethod
    def is_descendant_of_book(self, id_, book_id):
        """Tests if an ``Id`` is a descendant of a book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_book_node_ids(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a book node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_book_nodes(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a book node
        :rtype: ``osid.commenting.BookNode``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.commenting.BookNode


class BookHierarchyDesignSession:
    """This session manages a hierarchy of books.

    Books may be organized into a hierarchy for organizing or
    federating. A parent ``Book`` includes all of the comments of its
    children such that a single root node contains all of the comments
    of the federation.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    @abc.abstractmethod
    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    book_hierarchy = property(fget=get_book_hierarchy)

    @abc.abstractmethod
    def can_modify_book_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_book(self, book_id):
        """Adds a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_book(self, book_id):
        """Removes a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` is not a root
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_book(self, book_id, child_id):
        """Adds a child to a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``book_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_book(self, book_id, child_id):
        """Removes a child from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``book_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_books(self, book_id):
        """Removes all children from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
