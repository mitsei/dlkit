"""Implementations of type abstract base class sessions."""
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


class TypeLookupSession:
    """This session retrieves Types.

    A single Type can be retrieved using ``get_type()`` and all types
    known to this service can be accessed via ``get_types()`` .

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_types(self):
        """Tests if this user can perform ``Type`` lookups.

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
    def get_type(self, namespace, identifier, authority):
        """Gets a ``Type`` by its string representation which is a combination of the authority and identifier.

        This method only returns the ``Type`` if it is known by the
        given identification components.

        :param namespace: the identifier namespace
        :type namespace: ``string``
        :param identifier: the identifier
        :type identifier: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``NotFound`` -- the type is not found
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    @abc.abstractmethod
    def has_type(self, type_):
        """Tests if the given ``Type`` is known.

        :param type: the ``Type`` to look for
        :type type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is known, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_types_by_domain(self, domain):
        """Gets all the known Types by domain.

        :param domain: the domain
        :type domain: ``string``
        :return: the list of ``Types`` with the given domain
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_types_by_authority(self, authority):
        """Gets all the known Types by authority.

        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- respect my authoritay

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_types_by_domain_and_authority(self, domain, authority):
        """Gets all the known Types by domain and authority.

        :param domain: the domain
        :type domain: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given domain and authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` or ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_types(self):
        """Gets all the known Types.

        :return: the list of all known ``Types``
        :rtype: ``osid.type.TypeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    types = property(fget=get_types)

    @abc.abstractmethod
    def is_equivalent(self, type_, equivalent_type):
        """Tests if the given types are equivalent.

        :param type: a type
        :type type: ``osid.type.Type``
        :param equivalent_type: another type
        :type equivalent_type: ``osid.type.Type``
        :return: ``true`` if both types are equivalent, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def implies_support(self, type_, base_type):
        """Tests if the given type is implies support of a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :param base_type: another type
        :type base_type: ``osid.type.Type``
        :return: ``true`` if ``base_type`` if supported by ``type,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def has_base_type(self, type_):
        """Tests if the given type is derived from a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: ``true`` is the given type is derived from a base type, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_base_types(self, type_):
        """Gets the immediate base types of this type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: the base types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_relation_types(self):
        """Gets all known relation ``Types``.

        A relation Types relates two ``Types``.

        :return: known relation types
        :rtype: ``osid.type.TypeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    relation_types = property(fget=get_relation_types)

    @abc.abstractmethod
    def get_source_types_by_relation_type(self, relation_type):
        """Gets all source ``Types`` related by the given type.

        :param relation_type: a relation type
        :type relation_type: ``osid.type.Type``
        :return: the source types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_destination_types_by_source(self, source_type):
        """Gets all destination Types related to the given source ``Type``.

        :param source_type: a source type
        :type source_type: ``osid.type.Type``
        :return: the related types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_destination_types_by_source_and_relation_type(self, source_type, relation_type):
        """Gets all destination Types related to the given source ``Type`` and relation ``Type``.

        :param source_type: a source type
        :type source_type: ``osid.type.Type``
        :param relation_type: a relation type
        :type relation_type: ``osid.type.Type``
        :return: the related types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_type`` or ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_destination_types_by_relation_type(self, relation_type):
        """Gets all destination ``Types`` related by the given type.

        :param relation_type: a relation type
        :type relation_type: ``osid.type.Type``
        :return: the destination types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_source_types_by_destination(self, destination_type):
        """Gets all source Types related to the given destination ``Type``.

        :param destination_type: a destination type
        :type destination_type: ``osid.type.Type``
        :return: the source types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``destination_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    @abc.abstractmethod
    def get_source_types_by_destination_and_relation_type(self, destination_type, relation_type):
        """Gets all source Types related to the given destination ``Type`` and relation ``Type``.

        :param destination_type: a destination type
        :type destination_type: ``osid.type.Type``
        :param relation_type: a relation type
        :type relation_type: ``osid.type.Type``
        :return: the related types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``destination_type`` or ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList


class TypeAdminSession:
    """This session is used to create, update and delete ``Types`` in the registry."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_types(self):
        """Tests if this user can create ``Types``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Type`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_type_form_for_create(self, type_):
        """Gets the type form for creating new types.

        A new form should be requested for each create transaction.

        :param type: the ``Type`` to be created
        :type type: ``osid.type.Type``
        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeForm

    @abc.abstractmethod
    def create_type(self, type_form):
        """Creates a new ``Type``.

        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :return: the created ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``type_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the arguments is invalid
        :raise: ``NullArgument`` -- ``type_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    @abc.abstractmethod
    def can_update_types(self):
        """Tests if this user can update types.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if type modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_type_form_for_update(self, type_):
        """Gets the type form for creating new types.

        A new form should be requested for each create transaction.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``NotFound`` -- ``type`` not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeForm

    @abc.abstractmethod
    def update_type(self, type_form):
        """Updates a type.

        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :raise: ``IllegalState`` -- ``type_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``type_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_types(self):
        """Tests if this user can delete ``Types`` from this ``ItemBank``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_delete_type(self, type_):
        """Tests if this user can delete the specified type.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleteing the
        ``Type`` will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :param type: the ``Type`` to be deleted
        :type type: ``osid.type.Type``
        :return: ``false`` if type deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_type(self, type_):
        """Removes a ``Type``.

        :param type: the ``Type`` to remove
        :type type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` is not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def make_equivalent(self, primary_type, equivalent_type):
        """Makes two ``Types`` equivalent.

        Calls to ``TypeLookupSession.getType(equivalentType)`` return
        the ``primaryType``.

        :param primary_type: the primary ``Type``
        :type primary_type: ``osid.type.Type``
        :param equivalent_type: a ``Type`` to be made equivalent
        :type equivalent_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``primary_type`` or ``equivalent_type`` is not found
        :raise: ``NullArgument`` -- ``primary_type`` or ``equivalent_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_base_type(self, type_, base_type):
        """Adds a base type to a type.

        A base type is a parent of the type where the type implies
        support of the base type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_base_type(self, type_, base_type):
        """Removes a base type from a type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found or ``base_type`` is not a base of ``type``
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_type_relation(self, source_type, destination_type, relation_type):
        """Adds a relation between two types.

        The relationship is a ``Type`` in itself.

        :param source_type: the source type
        :type source_type: ``osid.type.Type``
        :param destination_type: the destination type
        :type destination_type: ``osid.type.Type``
        :param relation_type: the relation type
        :type relation_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``source_type, destination_type,`` or ``relation_type`` is not found
        :raise: ``NullArgument`` -- ``source_type, destination_type,`` or ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_type_relation(self, source_type, destination_type, relation_type):
        """Renoves a relation between two types.

        :param source_type: the source type
        :type source_type: ``osid.type.Type``
        :param destination_type: the destination type
        :type destination_type: ``osid.type.Type``
        :param relation_type: the relation type
        :type relation_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``source_type, destination_type,`` or ``relation_type`` is not found, or the relationship does not exist
        :raise: ``NullArgument`` -- ``source_type, destination_type,`` or ``relation_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
