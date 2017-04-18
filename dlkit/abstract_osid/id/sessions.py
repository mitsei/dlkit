"""Implementations of id abstract base class sessions."""
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


class IdLookupSession:
    """This session is for retrieving ``Id`` objects.

    ``get_ids()`` retrieves all known ``Ids``. The existence of a single
    identifier can be confirmed through the ``get_id()`` method, or it
    can be used as a means of ``Id`` translation.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_ids(self):
        """Tests if this user can perform ``Id`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_id(self, id_):
        """Gets an ``Id``.

        This method serves to get the principal ``Id`` if the given
        ``Id`` Is an alias.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: the ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    ident = property(fget=get_id)

    @abc.abstractmethod
    def get_ids_by_ids(self, ids):
        """Gets a list of ``Ids``.

        This method serves to get the principal ``Ids`` if different
        from the given ``Ids``.

        :param ids: a list of ``Ids``
        :type ids: ``osid.id.IdList``
        :return: a list of ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- an ``id`` is not found
        :raise: ``NullArgument`` -- ``ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_ids_by_authority(self, authority):
        """Gets ``Ids`` by the given authority.

        :param authority: an authority
        :type authority: ``string``
        :return: a list of ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_ids_by_authority_and_namespace(self, authority, namespace):
        """Gets ``Ids`` by the given authority and namespace.

        :param authority: an authority
        :type authority: ``string``
        :param namespace: a namespace
        :type namespace: ``string``
        :return: a list of ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``authority`` or ``namespace`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_ids(self):
        """Gets all ``Ids``.

        :return: the list of all ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    ids = property(fget=get_ids)

    @abc.abstractmethod
    def is_equivalent(self, id_, equivalent_id):
        """Tests if the two ``Ids`` are equivalent.

        Two ``Ids`` are equivalent if they identify the same object. If
        one of the ``Ids`` is not known, they are not equivalent.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param equivalent_id: an ``Id``
        :type equivalent_id: ``osid.id.Id``
        :return: ``true`` if the ``Ids`` are equivalent, false otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_id_aliases(self, id_):
        """Gets a list of ``Id`` aliases of an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: a list of alias ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_id_aliases_by_authority(self, id_, authority):
        """Gets a list of ``Id`` aliases in a authority for an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param authority: an authority
        :type authority: ``string``
        :return: a list of alias ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``id`` or ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_id_aliases_by_authority_and_namespace(self, id_, authority, namespace):
        """Gets a list of ``Id`` aliases in a namespace for an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param authority: an authority
        :type authority: ``string``
        :param namespace: a namespace
        :type namespace: ``string``
        :return: a list of alias ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``id, authority,`` or ``namespace`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList


class IdIssueSession:
    """This is a simple session used to create new ``Ids``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_issue_ids(self):
        """Tests if this user can issue ``Ids``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known create methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations.

        :return: ``false`` if create methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def issue_id(self):
        """Issues a new ``Id``.

        This method creates a new Id for a predetermined authority and
        namespace.

        :return: the new ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id


class IdAdminSession:
    """This session is used to manually create new ``Ids``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_ids(self):
        """Tests if this user can create ``Ids``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known create methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations.

        :return: ``false`` if create methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_id_form_for_create(self):
        """Gets the ``Id`` form for creating new Ids.

        A new form should be requested for each create transaction.

        :return: the ``Id`` form
        :rtype: ``osid.id.IdForm``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdForm

    id_form_for_create = property(fget=get_id_form_for_create)

    @abc.abstractmethod
    def create_id(self, id_form):
        """Creates a new ``Id``.

        A new ``IdForm`` should be requested for each create
        transaction.

        :param id_form: the ``Id`` form
        :type id_form: ``osid.id.IdForm``
        :return: the created ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- an ``Id`` for the authority, namespace, and identifier already exists
        :raise: ``IllegalState`` -- ``id_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``id_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``id_form`` did not originate from ``get_id_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    @abc.abstractmethod
    def can_alias_ids(self):
        """Tests if this user can alias ``Ids``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known add methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer alias
        operations.

        :return: ``false`` if alias methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_id(self, primary_id, equivalent_id):
        """Makes two ``Ids`` equivalent.

        The primary and equivalent ``Ids`` are already known to this
        service ````. If the external ``Id`` is already mapped to
        another ``Id,`` it is changed to map to the given primary
        ``Id``. Calls to ``IdLookupSession.getId(equivalentId)`` return
        the ``primaryId``.

        :param primary_id: the primary ``Id``
        :type primary_id: ``osid.id.Id``
        :param equivalent_id: an ``Id`` to be made equivalent
        :type equivalent_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``primary_id`` or ``equivalent_id`` is not found
        :raise: ``NullArgument`` -- ``primary_id`` or ``equivalent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_alias(self, primary_id, equivalent_id):
        """Removes equivalence from two ``Ids``.

        :param primary_id: the primary ``Id``
        :type primary_id: ``osid.id.Id``
        :param equivalent_id: the equivalent ``Id``
        :type equivalent_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``primary_id`` or ``equivalent_id`` is not found or ``equivalent_id`` not mapped to ``primary_id``
        :raise: ``NullArgument`` -- ``primary_id`` or ``equivalent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
