"""Implementations of authorization abstract base class objects."""
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


class Authorization:
    """An Authorization is a mapping among an actor, a ``Function`` and a ``Qualifier``.

    This interface is not required for performing authorization checks
    but is used for examining and managing authorizations.

    The actor of an authorization may be specified in a variety of
    forms.

      * ``Agent``
      * ``Resource:`` the authorization provider uses all the ``Agents``
        associated with a ``Resource`` for matching authorizations
      * ``Resource`` and ``Trust:`` the authorization provider uses the
        associated ``Agents`` within a cicle of ``Trust``


    An explicit ``Authorization`` represents the mappings as they are
    specified in the authorization provdier. Implicit authorizations may
    be retrieved which are authorizations inferred through the
    ``Function`` or ``Qualifier`` hierarchies. An implicit
    ``Authorization`` is one where ``is_implicit()`` is true and should
    not be used for modification as it is only available for auditing
    purposes.

    An ``Authorization`` containing a ``Resource`` may also provide the
    associated Agent in a request for implicit authorizations or for all
    the authorizations, both explicit and implicit, for a given
    ``Agent``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_implicit(self):
        """Tests if this authorization is implicit.

        :return: ``true`` if this authorization is implicit, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def has_resource(self):
        """Tests if this authorization has a ``Resource``.

        :return: ``true`` if this authorization has a ``Resource,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_id(self):
        """Gets the ``resource _id`` for this authorization.

        :return: the ``Resource Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_resource()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    resource_id = property(fget=get_resource_id)

    @abc.abstractmethod
    def get_resource(self):
        """Gets the ``Resource`` for this authorization.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- ``has_resource()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    resource = property(fget=get_resource)

    @abc.abstractmethod
    def has_trust(self):
        """Tests if this authorization has a ``Trust``.

        :return: ``true`` if this authorization has a ``Trust,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_trust_id(self):
        """Gets the ``Trust``  ``Id`` for this authorization.

        :return: the trust ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_trust()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    trust_id = property(fget=get_trust_id)

    @abc.abstractmethod
    def get_trust(self):
        """Gets the ``Trust`` for this authorization.

        :return: the ``Trust``
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``IllegalState`` -- ``has_trust()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.Trust

    trust = property(fget=get_trust)

    @abc.abstractmethod
    def has_agent(self):
        """Tests if this authorization has an ``Agent``.

        An implied authorization may have an ``Agent`` in addition to a
        specified ``Resource``.

        :return: ``true`` if this authorization has an ``Agent,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_id(self):
        """Gets the ``Agent Id`` for this authorization.

        :return: the ``Agent Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_agent()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agent_id = property(fget=get_agent_id)

    @abc.abstractmethod
    def get_agent(self):
        """Gets the ``Agent`` for this authorization.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``has_agent()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    agent = property(fget=get_agent)

    @abc.abstractmethod
    def get_function_id(self):
        """Gets the ``Function Id`` for this authorization.

        :return: the function ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    function_id = property(fget=get_function_id)

    @abc.abstractmethod
    def get_function(self):
        """Gets the ``Function`` for this authorization.

        :return: the function
        :rtype: ``osid.authorization.Function``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Function

    function = property(fget=get_function)

    @abc.abstractmethod
    def get_qualifier_id(self):
        """Gets the ``Qualifier Id`` for this authorization.

        :return: the qualifier ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    qualifier_id = property(fget=get_qualifier_id)

    @abc.abstractmethod
    def get_qualifier(self):
        """Gets the qualifier for this authorization.

        :return: the qualifier
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Qualifier

    qualifier = property(fget=get_qualifier)

    @abc.abstractmethod
    def get_authorization_record(self, authorization_record_type):
        """Gets the authorization record corresponding to the given ``Authorization`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authorization_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authorization_record_type)`` is ``true`` .

        :param authorization_record_type: the type of the record to retrieve
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization record
        :rtype: ``osid.authorization.records.AuthorizationRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationRecord


class AuthorizationForm:
    """This is the form for creating and updating ``Authorizations``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AuthorizationAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorization_form_record(self, authorization_record_type):
        """Gets the ``AuthorizationFormRecord`` corresponding to the given authorization record ``Type``.

        :param authorization_record_type: the authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization form record
        :rtype: ``osid.authorization.records.AuthorizationFormRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationFormRecord


class AuthorizationList:
    """Like all ``OsidLists,``  ``AuthorizationList`` provides a means for accessing ``Authorization`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Authorization authorization =
    al.getNextAuthorization(); }

    or
      while (al.hasNext()) {
           Authorization[] authorizations = al.getNextAuthorizations(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_authorization(self):
        """Gets the next ``Authorization`` in this list.

        :return: the next ``Authorization`` in this list. The ``has_next()`` method should be used to test that a next ``Authorization`` is available before calling this method.
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Authorization

    next_authorization = property(fget=get_next_authorization)

    @abc.abstractmethod
    def get_next_authorizations(self, n):
        """Gets the next set of ``Authorization`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Authorization`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Authorization`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Authorization


class Function:
    """A ``Function`` represents an authenticatable identity.

    Like all OSID objects, a ``Function`` is identified by its ``Id``
    and any persisted references should use the ``Id``. A rule
    associated with the ``Function`` specifies conditions that can be
    supplied to authorization checks.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_hierarchy_id(self):
        """Gets the qualifier hierarchy ``Id`` for this function.

        :return: the qualifier hierarchy ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    @abc.abstractmethod
    def get_qualifier_hierarchy(self):
        """Gets the qualifier hierarchy for this function.

        :return: the qualifier hierarchy
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    @abc.abstractmethod
    def get_function_record(self, function_record_type):
        """Gets the function record corresponding to the given ``Function`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``function_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(function_record_type)`` is ``true`` .

        :param function_record_type: the type of the record to retrieve
        :type function_record_type: ``osid.type.Type``
        :return: the function record
        :rtype: ``osid.authorization.records.FunctionRecord``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.FunctionRecord


class FunctionForm:
    """This is the form for creating and updating ``Functions``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FunctionAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_hierarchy_metadata(self):
        """Gets the metadata for a qualifier hierarchy.

        :return: metadata for the qualifier hierarchy
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    qualifier_hierarchy_metadata = property(fget=get_qualifier_hierarchy_metadata)

    @abc.abstractmethod
    def set_qualifier_hierarchy(self, qualifier_hierarchy_id):
        """Sets the qualifier hierarchy.

        :param qualifier_hierarchy_id: the new qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``qualifier_hierarchy_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_qualifier_hierarchy(self):
        """Clears the qualifier hierarchy.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    qualifier_hierarchy = property(fset=set_qualifier_hierarchy, fdel=clear_qualifier_hierarchy)

    @abc.abstractmethod
    def get_function_form_record(self, function_record_type):
        """Gets the ``FunctionFormRecord`` corresponding to the given function record ``Type``.

        :param function_record_type: the function record type
        :type function_record_type: ``osid.type.Type``
        :return: the function form record
        :rtype: ``osid.authorization.records.FunctionFormRecord``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.FunctionFormRecord


class FunctionList:
    """Like all ``OsidLists,``  ``FunctionList`` provides a means for accessing ``Function`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Function function =
    fl.getNextFunction(); }

    or
      while (fl.hasNext()) {
           Function[] functions = fl.getNextFunctions(fl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_function(self):
        """Gets the next ``Function`` in this list.

        :return: the next ``Function`` in this list. The ``has_next()`` method should be used to test that a next ``Function`` is available before calling this method.
        :rtype: ``osid.authorization.Function``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Function

    next_function = property(fget=get_next_function)

    @abc.abstractmethod
    def get_next_functions(self, n):
        """Gets the next set of ``Function`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Function`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Function`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Function``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Function


class Qualifier:
    """A ``Qualifier`` represents an authenticatable identity.

    Like all OSID objects, a ``Qualifier`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_record(self, qualifier_record_type):
        """Gets the qualifier record corresponding to the given ``Qualifier`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``qualifier_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(qualifier_record_type)`` is ``true`` .

        :param qualifier_record_type: the type of the record to retrieve
        :type qualifier_record_type: ``osid.type.Type``
        :return: the qualifier record
        :rtype: ``osid.authorization.records.QualifierRecord``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.QualifierRecord


class QualifierForm:
    """This is the form for creating and updating ``Qualifiers``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``QualifierAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_form_record(self, qualifier_record_type):
        """Gets the ``QualifierFormRecord`` corresponding to the given qualifier record ``Type``.

        :param qualifier_record_type: the qualifier record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the qualifier form record
        :rtype: ``osid.authorization.records.QualifierFormRecord``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.QualifierFormRecord


class QualifierList:
    """Like all ``OsidLists,``  ``QualifierList`` provides a means for accessing ``Qualifier`` elements sequentially either one at a time or many at a time.

    Examples: while (ql.hasNext()) { Qualifier qualifier =
    ql.getNextQualifier(); }

    or
      while (ql.hasNext()) {
           Qualifier[] qualifiers = ql.hetNextQualifiers(ql.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_qualifier(self):
        """Gets the next ``Qualifier`` in this list.

        :return: the next ``Qualifier`` in this list. The ``has_next()`` method should be used to test that a next ``Qualifier`` is available before calling this method.
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Qualifier

    next_qualifier = property(fget=get_next_qualifier)

    @abc.abstractmethod
    def get_next_qualifiers(self, n):
        """Gets the next set of ``Qualifier`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Qualifier`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Qualifier`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Qualifier


class QualifierNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``QualifierHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier(self):
        """Gets the ``Qualifier`` at this node.

        :return: the qualifier represented by this node
        :rtype: ``osid.authorization.Qualifier``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Qualifier

    qualifier = property(fget=get_qualifier)

    @abc.abstractmethod
    def get_parent_qualifier_nodes(self):
        """Gets the parents of this qualifier.

        :return: the parents of this qualifier
        :rtype: ``osid.authorization.QualifierNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierNodeList

    parent_qualifier_nodes = property(fget=get_parent_qualifier_nodes)

    @abc.abstractmethod
    def get_child_qualifier_nodes(self):
        """Gets the children of this qualifier.

        :return: the children of this qualifier
        :rtype: ``osid.authorization.QualifierNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierNodeList

    child_qualifier_nodes = property(fget=get_child_qualifier_nodes)


class QualifierNodeList:
    """Like all ``OsidLists,``  ``QualifierNodeList`` provides a means for accessing ``QualifierNode`` elements sequentially either one at a time or many at a time.

    Examples: while (qnl.hasNext()) { QualifierNode node =
    qnl.getNextQualifierNode(); }

    or
      while (qnl.hasNext()) {
           QualifierNode[] nodes = qnl.hetNextQualifierNodes(qnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_qualifier_node(self):
        """Gets the next ``QualifierNode`` in this list.

        :return: the next ``QualifierNode`` in this list. The ``has_next()`` method should be used to test that a next ``QualifierNode`` is available before calling this method.
        :rtype: ``osid.authorization.QualifierNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierNode

    next_qualifier_node = property(fget=get_next_qualifier_node)

    @abc.abstractmethod
    def get_next_qualifier_nodes(self, n):
        """Gets the next set of ``QualifierNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``QualifierNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``QualifierNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.QualifierNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierNode


class Vault:
    """A vault defines a collection of authorizations and functions."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_record(self, vault_record_type):
        """Gets the vault record corresponding to the given ``Vault`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``vault_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(vault_record_type)``
        is ``true`` .

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault record
        :rtype: ``osid.authorization.records.VaultRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.VaultRecord


class VaultForm:
    """This is the form for creating and updating vaults.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``VaultAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_form_record(self, vault_record_type):
        """Gets the ``VaultFormRecord`` corresponding to the given vault record ``Type``.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault form record
        :rtype: ``osid.authorization.records.VaultFormRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.VaultFormRecord


class VaultList:
    """Like all ``OsidLists,``  ``VaultList`` provides a means for accessing ``Vault`` elements sequentially either one at a time or many at a time.

    Examples: while (vl.hasNext()) { Vault vault = vl.getNextVault(); }

    or
      while (vl.hasNext()) {
           Vault[] vaults = vl.getNextVaults(vl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_vault(self):
        """Gets the next ``Vault`` in this list.

        :return: the next ``Vault`` in this list. The ``has_next()`` method should be used to test that a next ``Vault`` is available before calling this method.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    next_vault = property(fget=get_next_vault)

    @abc.abstractmethod
    def get_next_vaults(self, n):
        """Gets the next set of ``Vault`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Vault`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Vault`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault


class VaultNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``VaultHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` at this node.

        :return: the vault represented by this node
        :rtype: ``osid.authorization.Vault``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def get_parent_vault_nodes(self):
        """Gets the parents of this vault.

        :return: the parents of this vault
        :rtype: ``osid.authorization.VaultNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultNodeList

    parent_vault_nodes = property(fget=get_parent_vault_nodes)

    @abc.abstractmethod
    def get_child_vault_nodes(self):
        """Gets the children of this vault.

        :return: the children of this vault
        :rtype: ``osid.authorization.VaultNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultNodeList

    child_vault_nodes = property(fget=get_child_vault_nodes)


class VaultNodeList:
    """Like all ``OsidLists,``  ``VaultNodeList`` provides a means for accessing ``VaultNode`` elements sequentially either one at a time or many at a time.

    Examples: while (vnl.hasNext()) { VaultNode node =
    vnl.getNextVaultNode(); }

    or
      while (vnl.hasNext()) {
           VaultNode[] nodes = vnl.getNextVaultNodes(vnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_vault_node(self):
        """Gets the next ``VaultNode`` in this list.

        :return: the next ``VaultNode`` in this list. The ``has_next()`` method should be used to test that a next ``VaultNode`` is available before calling this method.
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultNode

    next_vault_node = property(fget=get_next_vault_node)

    @abc.abstractmethod
    def get_next_vault_nodes(self, n):
        """Gets the next set of ``VaultNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``VaultNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``VaultNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultNode
