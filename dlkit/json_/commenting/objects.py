"""JSON implementations of commenting objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


import importlib


from . import default_mdata
from .. import utilities
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import DisplayText
from ..primitives import Id
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.commenting import objects as abc_commenting_objects
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


class Comment(abc_commenting_objects.Comment, osid_objects.OsidRelationship):
    """A ``Comment`` represents a comment and/or rating related to a reference object in a book."""
    _namespace = 'commenting.Comment'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='COMMENT', **kwargs)
        self._catalog_name = 'Book'

    def get_reference_id(self):
        """Gets the ``Id`` of the referenced object to which this comment pertains.

        return: (osid.id.Id) - the reference ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['referenceId'])

    reference_id = property(fget=get_reference_id)

    def get_commentor_id(self):
        """Gets the ``Id`` of the resource who created this comment.

        return: (osid.id.Id) - the ``Resource``  ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.relationship.Relationship.get_source_id
        return Id(self._my_map['commentorId'])

    commentor_id = property(fget=get_commentor_id)

    def get_commentor(self):
        """Gets the resource who created this comment.

        return: (osid.resource.Resource) - the ``Resource``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    commentor = property(fget=get_commentor)

    def get_commenting_agent_id(self):
        """Gets the ``Id`` of the agent who created this comment.

        return: (osid.id.Id) - the ``Agent``  ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_commentor_id()

    commenting_agent_id = property(fget=get_commenting_agent_id)

    def get_commenting_agent(self):
        """Gets the agent who created this comment.

        return: (osid.authentication.Agent) - the ``Agent``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if not self.has_commentor():
            raise errors.IllegalState('this Comment has no commenting_agent')
        try:
            from ..authentication import managers
        except ImportError:
            raise errors.OperationFailed('failed to import authentication.managers')
        try:
            mgr = managers.AuthenticationManager()
        except:
            raise errors.OperationFailed('failed to instantiate AuthenticationManager')
        if not mgr.supports_agent_lookup():
            raise errors.OperationFailed('Authentication does not support Agent lookup')
        try:
            osid_object = mgr.get_agent_lookup_session().get_agent(self.get_commenting_agent_id())
        except:
            raise errors.OperationFailed()
        else:
            return osid_object

    commenting_agent = property(fget=get_commenting_agent)

    def get_text(self):
        """Gets the comment text.

        return: (osid.locale.DisplayText) - the comment text
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.Asset.get_title_template
        return DisplayText(self._my_map['text'])

    text = property(fget=get_text)

    def has_rating(self):
        """Tests if this comment includes a rating.

        return: (boolean) - ``true`` if this comment includes a rating,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['ratingId'])

    def get_rating_id(self):
        """Gets the ``Id`` of the ``Grade``.

        return: (osid.id.Id) - the ``Agent``  ``Id``
        raise:  IllegalState - ``has_rating()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not bool(self._my_map['ratingId']):
            raise errors.IllegalState('this Comment has no rating')
        else:
            return Id(self._my_map['ratingId'])

    rating_id = property(fget=get_rating_id)

    def get_rating(self):
        """Gets the ``Grade``.

        return: (osid.grading.Grade) - the ``Grade``
        raise:  IllegalState - ``has_rating()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not bool(self._my_map['ratingId']):
            raise errors.IllegalState('this Comment has no rating')
        mgr = self._get_provider_manager('GRADING')
        if not mgr.supports_grade_lookup():
            raise errors.OperationFailed('Grading does not support Grade lookup')
        lookup_session = mgr.get_grade_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_gradebook_view()
        osid_object = lookup_session.get_grade(self.get_rating_id())
        return osid_object

    rating = property(fget=get_rating)

    @utilities.arguments_not_none
    def get_comment_record(self, comment_record_type):
        """Gets the comment record corresponding to the given ``Comment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``comment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(comment_record_type)`` is ``true`` .

        arg:    comment_record_type (osid.type.Type): the type of
                comment record to retrieve
        return: (osid.commenting.records.CommentRecord) - the comment
                record
        raise:  NullArgument - ``comment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(comment_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(comment_record_type)

    def has_commentor(self):
        return bool(self._my_map['commentorId'])

    def get_object_map(self):
        obj_map = dict(self._my_map)
        obj_map['commentingAgentId'] = str(self.get_commenting_agent_id())
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class CommentForm(abc_commenting_objects.CommentForm, osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Comment`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CommentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'commenting.Comment'

    def __init__(self, **kwargs):
        osid_objects.OsidRelationshipForm.__init__(self, object_name='COMMENT', **kwargs)
        self._mdata = default_mdata.get_comment_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidRelationshipForm._init_metadata(self, **kwargs)
        update_display_text_defaults(self._mdata['text'], self._locale_map)
        self._text_default = dict(self._mdata['text']['default_string_values'][0])
        self._rating_default = self._mdata['rating']['default_id_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidRelationshipForm._init_map(self, record_types=record_types)
        self._my_map['text'] = self._text_default
        self._my_map['assignedBookIds'] = [str(kwargs['book_id'])]
        self._my_map['commentorId'] = str(kwargs['effective_agent_id'])
        self._my_map['referenceId'] = str(kwargs['reference_id'])
        self._my_map['ratingId'] = self._rating_default

    def get_text_metadata(self):
        """Gets the metadata for the text.

        return: (osid.Metadata) - metadata for the text
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['text'])
        metadata.update({'existing_string_values': self._my_map['text']})
        return Metadata(**metadata)

    text_metadata = property(fget=get_text_metadata)

    @utilities.arguments_not_none
    def set_text(self, text):
        """Sets the text.

        arg:    text (string): the new text
        raise:  InvalidArgument - ``text`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``text`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetForm.set_title_template
        self._my_map['text'] = self._get_display_text(text, self.get_text_metadata())

    def clear_text(self):
        """Clears the text.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.repository.AssetForm.clear_title_template
        if (self.get_text_metadata().is_read_only() or
                self.get_text_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['text'] = dict(self._text_default)

    text = property(fset=set_text, fdel=clear_text)

    def get_rating_metadata(self):
        """Gets the metadata for a rating.

        return: (osid.Metadata) - metadata for the rating
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._mdata['rating'])
        metadata.update({'existing_id_values': self._my_map['ratingId']})
        return Metadata(**metadata)

    rating_metadata = property(fget=get_rating_metadata)

    @utilities.arguments_not_none
    def set_rating(self, grade_id):
        """Sets the rating.

        arg:    grade_id (osid.id.Id): the new rating
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_rating_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(grade_id):
            raise errors.InvalidArgument()
        self._my_map['ratingId'] = str(grade_id)

    def clear_rating(self):
        """Clears the rating.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_rating_metadata().is_read_only() or
                self.get_rating_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['ratingId'] = self._rating_default

    rating = property(fset=set_rating, fdel=clear_rating)

    @utilities.arguments_not_none
    def get_comment_form_record(self, comment_record_type):
        """Gets the ``CommentFormRecord`` corresponding to the given comment record ``Type``.

        arg:    comment_record_type (osid.type.Type): the comment record
                type
        return: (osid.commenting.records.CommentFormRecord) - the
                comment form record
        raise:  NullArgument - ``comment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(comment_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(comment_record_type)


class CommentList(abc_commenting_objects.CommentList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CommentList`` provides a means for accessing ``Comment`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Comment comment =
    cl.getNextComment(); }

    or
      while (cl.hasNext()) {
           Comment[] comments = cl.getNextComments(cl.available());
      }

    """

    def get_next_comment(self):
        """Gets the next ``Comment`` in this list.

        return: (osid.commenting.Comment) - the next ``Comment`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Comment`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Comment)

    __next__ = next

    next_comment = property(fget=get_next_comment)

    @utilities.arguments_not_none
    def get_next_comments(self, n):
        """Gets the next set of ``Comment`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Comment`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.commenting.Comment) - an array of ``Comment``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(CommentList, number=n)


class Book(abc_commenting_objects.Book, osid_objects.OsidCatalog):
    """A ``Book`` represents a collection of comments.

    Like all OSID objects, a ``Book`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    _namespace = 'commenting.Book'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='BOOK', **kwargs)

    @utilities.arguments_not_none
    def get_book_record(self, book_record_type):
        """Gets the book record corresponding to the given ``Book`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``book_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(book_record_type)``
        is ``true`` .

        arg:    book_record_type (osid.type.Type): the type of book
                record to retrieve
        return: (osid.commenting.records.BookRecord) - the book record
        raise:  NullArgument - ``book_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(book_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BookForm(abc_commenting_objects.BookForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Books``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'commenting.Book'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='BOOK', **kwargs)
        self._mdata = default_mdata.get_book_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidCatalogForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_map(self, record_types, **kwargs)

    @utilities.arguments_not_none
    def get_book_form_record(self, book_record_type):
        """Gets the ``BookFormRecord`` corresponding to the given book record ``Type``.

        arg:    book_record_type (osid.type.Type): the book record type
        return: (osid.commenting.records.BookFormRecord) - the book form
                record
        raise:  NullArgument - ``book_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(book_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class BookList(abc_commenting_objects.BookList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BookList`` provides a means for accessing ``Book`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Book book = bl.getNextBook(); }

    or
      while (bl.hasNext()) {
           Book[] books = bl.getNextBooks(bl.available());
      }

    """

    def get_next_book(self):
        """Gets the next ``Book`` in this list.

        return: (osid.commenting.Book) - the next ``Book`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Book`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Book)

    __next__ = next

    next_book = property(fget=get_next_book)

    @utilities.arguments_not_none
    def get_next_books(self, n):
        """Gets the next set of ``Book`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Book`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.commenting.Book) - an array of ``Book``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(BookList, number=n)


class BookNode(abc_commenting_objects.BookNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BookHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_book().get_object_map())
        node_map['type'] = 'BookNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for book_node in self.get_parent_book_nodes():
            node_map['parentNodes'].append(book_node.get_object_node_map())
        for book_node in self.get_child_book_nodes():
            node_map['childNodes'].append(book_node.get_object_node_map())
        return node_map

    def get_book(self):
        """Gets the ``Book`` at this node.

        return: (osid.commenting.Book) - the book represented by this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('COMMENTING', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_book_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_book(Id(self._my_map['id']))

    book = property(fget=get_book)

    def get_parent_book_nodes(self):
        """Gets the parents of this book.

        return: (osid.commenting.BookNodeList) - the parents of this
                book
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_book_nodes = []
        for node in self._my_map['parentNodes']:
            parent_book_nodes.append(BookNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BookNodeList(parent_book_nodes)

    parent_book_nodes = property(fget=get_parent_book_nodes)

    def get_child_book_nodes(self):
        """Gets the children of this book.

        return: (osid.commenting.BookNodeList) - the children of this
                book
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_book_nodes = []
        for node in self._my_map['childNodes']:
            parent_book_nodes.append(BookNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BookNodeList(parent_book_nodes)

    child_book_nodes = property(fget=get_child_book_nodes)


class BookNodeList(abc_commenting_objects.BookNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BookNodeList`` provides a means for accessing ``BookNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BookNode node =
    bnl.getNextBookNode(); }

    or
      while (bnl.hasNext()) {
           BookNode[] nodes = bnl.getNextBookNodes(bnl.available());
      }

    """

    def get_next_book_node(self):
        """Gets the next ``BookNode`` in this list.

        return: (osid.commenting.BookNode) - the next ``BookNode`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``BookNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(BookNode)

    __next__ = next

    next_book_node = property(fget=get_next_book_node)

    @utilities.arguments_not_none
    def get_next_book_nodes(self, n):
        """Gets the next set of ``BookNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``BookNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.commenting.BookNode) - an array of ``BookNode``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(BookNodeList, number=n)
