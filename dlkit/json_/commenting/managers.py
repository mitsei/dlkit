"""JSON implementations of commenting managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import profile
from . import sessions
from .. import utilities
from ..osid import managers as osid_managers
from ..primitives import Type
from ..type.objects import TypeList
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.commenting import managers as commenting_managers


class CommentingProfile(osid_managers.OsidProfile, commenting_managers.CommentingProfile):
    """The commenting profile describes the interoperability among commenting services."""

    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        return: (boolean) - ``true`` if comment lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_comment_lookup' in profile.SUPPORTS

    def supports_comment_query(self):
        """Tests if querying comments is available.

        return: (boolean) - ``true`` if comment query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_comment_query' in profile.SUPPORTS

    def supports_comment_admin(self):
        """Tests if managing comments is available.

        return: (boolean) - ``true`` if comment admin is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_comment_admin' in profile.SUPPORTS

    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        return: (boolean) - ``true`` if book lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_book_lookup' in profile.SUPPORTS

    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        return: (boolean) - ``true`` if book administration is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_book_admin' in profile.SUPPORTS

    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        return: (boolean) - ``true`` if book hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_book_hierarchy' in profile.SUPPORTS

    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        return: (boolean) - ``true`` if book hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_book_hierarchy_design' in profile.SUPPORTS

    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                comment record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('COMMENT_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    comment_record_types = property(fget=get_comment_record_types)

    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        return: (osid.type.TypeList) - a list containing the supported
                comment search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('COMMENT_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                book record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('BOOK_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    book_record_types = property(fget=get_book_record_types)

    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        return: (osid.type.TypeList) - a list containing the supported
                book search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('BOOK_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    book_search_record_types = property(fget=get_book_search_record_types)


class CommentingManager(osid_managers.OsidManager, CommentingProfile, commenting_managers.CommentingManager):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_comment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        if not self.supports_comment_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentLookupSession(runtime=self._runtime)

    comment_lookup_session = property(fget=get_comment_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_comment_lookup_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentLookupSession(book_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_comment_query_session(self):
        """Gets the ``OsidSession`` associated with the comment query service.

        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        if not self.supports_comment_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentQuerySession(runtime=self._runtime)

    comment_query_session = property(fget=get_comment_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_comment_query_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentQuerySession(book_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_comment_admin_session(self):
        """Gets the ``OsidSession`` associated with the comment administration service.

        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        if not self.supports_comment_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentAdminSession(runtime=self._runtime)

    comment_admin_session = property(fget=get_comment_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_comment_admin_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentAdminSession(book_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        return: (osid.commenting.BookLookupSession) - a
                ``BookLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        if not self.supports_book_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookLookupSession(runtime=self._runtime)

    book_lookup_session = property(fget=get_book_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_book_admin_session(self):
        """Gets the ``OsidSession`` associated with the book administrative service.

        return: (osid.commenting.BookAdminSession) - a
                ``BookAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        if not self.supports_book_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookAdminSession(runtime=self._runtime)

    book_admin_session = property(fget=get_book_admin_session)

    @utilities.remove_null_proxy_kwarg
    def get_book_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        return: (osid.commenting.BookHierarchySession) - a
                ``BookHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        if not self.supports_book_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookHierarchySession(runtime=self._runtime)

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
    def get_book_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        return: (osid.commenting.BookHierarchyDesignSession) - a
                ``BookHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_book_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookHierarchyDesignSession(runtime=self._runtime)

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        return: (osid.commenting.batch.CommentingBatchManager) - a
                ``CommentingBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_commenting_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


class CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile, commenting_managers.CommentingProxyManager):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from a server environment. The sessions included in this manager
    are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_comment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` is ``true``.*

        """
        if not self.supports_comment_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_comment_lookup_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentLookupSession) - a
                ``CommentLookupSession``
        raise:  NotFound - no ``Book`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentLookupSession(book_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_comment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        if not self.supports_comment_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_comment_query_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentQuerySession) - a
                ``CommentQuerySession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentQuerySession(book_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_comment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` is ``true``.*

        """
        if not self.supports_comment_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.CommentAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_comment_admin_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.CommentAdminSession) - a
                ``CommentAdminSession``
        raise:  NotFound - no ``Comment`` found by the given ``Id``
        raise:  NullArgument - ``book_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_comment_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if not self.supports_comment_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.CommentAdminSession(book_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_book_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookLookupSession) - a
                ``BookLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_lookup()`` is ``true``.*

        """
        if not self.supports_book_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_book_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookAdminSession) - a
                ``BookAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_admin()`` is ``true``.*

        """
        if not self.supports_book_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_book_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookHierarchySession) - a
                ``BookHierarchySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy()`` is ``true``.*

        """
        if not self.supports_book_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_book_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.commenting.BookHierarchyDesignSession) - a
                ``BookHierarchyDesignSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_book_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_hierarchy_design()`` is ``true``.*

        """
        if not self.supports_book_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.BookHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        return: (osid.commenting.batch.CommentingBatchProxyManager) - a
                ``CommentingBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_commenting_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        raise errors.Unimplemented()

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)
