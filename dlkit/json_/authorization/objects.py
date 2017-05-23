"""JSON implementations of authorization objects."""

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
from ..id.objects import IdList
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..utilities import get_provider_manager
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.authorization import objects as abc_authorization_objects
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


class Authorization(abc_authorization_objects.Authorization, osid_objects.OsidRelationship):
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
    _namespace = 'authorization.Authorization'

    def __init__(self, **kwargs):
        osid_objects.OsidObject.__init__(self, object_name='AUTHORIZATION', **kwargs)
        self._catalog_name = 'Vault'

    def is_implicit(self):
        """Tests if this authorization is implicit.

        return: (boolean) - ``true`` if this authorization is implicit,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return bool(self._my_map['implicit'])

    def has_resource(self):
        """Tests if this authorization has a ``Resource``.

        return: (boolean) - ``true`` if this authorization has a
                ``Resource,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['resourceId'])

    def get_resource_id(self):
        """Gets the ``resource _id`` for this authorization.

        return: (osid.id.Id) - the ``Resource Id``
        raise:  IllegalState - ``has_resource()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not self._my_map['resourceId']:
            raise errors.IllegalState('this Authorization has no resource')
        else:
            return Id(self._my_map['resourceId'])

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the ``Resource`` for this authorization.

        return: (osid.resource.Resource) - the ``Resource``
        raise:  IllegalState - ``has_resource()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not self._my_map['resourceId']:
            raise errors.IllegalState('this Authorization has no resource')
        mgr = self._get_provider_manager('RESOURCE')
        if not mgr.supports_resource_lookup():
            raise errors.OperationFailed('Resource does not support Resource lookup')
        lookup_session = mgr.get_resource_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_bin_view()
        osid_object = lookup_session.get_resource(self.get_resource_id())
        return osid_object

    resource = property(fget=get_resource)

    def has_trust(self):
        """Tests if this authorization has a ``Trust``.

        return: (boolean) - ``true`` if this authorization has a
                ``Trust,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['trustId'])

    def get_trust_id(self):
        """Gets the ``Trust``  ``Id`` for this authorization.

        return: (osid.id.Id) - the trust ``Id``
        raise:  IllegalState - ``has_trust()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not self._my_map['trustId']:
            raise errors.IllegalState('this Authorization has no trust')
        else:
            return Id(self._my_map['trustId'])

    trust_id = property(fget=get_trust_id)

    def get_trust(self):
        """Gets the ``Trust`` for this authorization.

        return: (osid.authentication.process.Trust) - the ``Trust``
        raise:  IllegalState - ``has_trust()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not self._my_map['trustId']:
            raise errors.IllegalState('this Authorization has no trust')
        mgr = self._get_provider_manager('AUTHENTICATION.PROCESS')
        if not mgr.supports_trust_lookup():
            raise errors.OperationFailed('Authentication.Process does not support Trust lookup')
        lookup_session = mgr.get_trust_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_agency_view()
        osid_object = lookup_session.get_trust(self.get_trust_id())
        return osid_object

    trust = property(fget=get_trust)

    def has_agent(self):
        """Tests if this authorization has an ``Agent``.

        An implied authorization may have an ``Agent`` in addition to a
        specified ``Resource``.

        return: (boolean) - ``true`` if this authorization has an
                ``Agent,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['agentId'])

    def get_agent_id(self):
        """Gets the ``Agent Id`` for this authorization.

        return: (osid.id.Id) - the ``Agent Id``
        raise:  IllegalState - ``has_agent()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not self._my_map['agentId']:
            raise errors.IllegalState('this Authorization has no agent')
        else:
            return Id(self._my_map['agentId'])

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` for this authorization.

        return: (osid.authentication.Agent) - the ``Agent``
        raise:  IllegalState - ``has_agent()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not self._my_map['agentId']:
            raise errors.IllegalState('this Authorization has no agent')
        mgr = self._get_provider_manager('AUTHENTICATION')
        if not mgr.supports_agent_lookup():
            raise errors.OperationFailed('Authentication does not support Agent lookup')
        lookup_session = mgr.get_agent_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_agency_view()
        osid_object = lookup_session.get_agent(self.get_agent_id())
        return osid_object

    agent = property(fget=get_agent)

    def get_function_id(self):
        """Gets the ``Function Id`` for this authorization.

        return: (osid.id.Id) - the function ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return Id(self._my_map['functionId'])

    function_id = property(fget=get_function_id)

    def get_function(self):
        """Gets the ``Function`` for this authorization.

        return: (osid.authorization.Function) - the function
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        mgr = self._get_provider_manager('AUTHORIZATION')
        if not mgr.supports_function_lookup():
            raise errors.OperationFailed('Authorization does not support Function lookup')
        lookup_session = mgr.get_function_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_vault_view()
        return lookup_session.get_function(self.get_function_id())

    function = property(fget=get_function)

    def get_qualifier_id(self):
        """Gets the ``Qualifier Id`` for this authorization.

        return: (osid.id.Id) - the qualifier ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return Id(self._my_map['qualifierId'])

    qualifier_id = property(fget=get_qualifier_id)

    def get_qualifier(self):
        """Gets the qualifier for this authorization.

        return: (osid.authorization.Qualifier) - the qualifier
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective
        mgr = self._get_provider_manager('AUTHORIZATION')
        if not mgr.supports_qualifier_lookup():
            raise errors.OperationFailed('Authorization does not support Qualifier lookup')
        lookup_session = mgr.get_qualifier_lookup_session(proxy=getattr(self, "_proxy", None))
        lookup_session.use_federated_vault_view()
        return lookup_session.get_qualifier(self.get_qualifier_id())

    qualifier = property(fget=get_qualifier)

    @utilities.arguments_not_none
    def get_authorization_record(self, authorization_record_type):
        """Gets the authorization record corresponding to the given ``Authorization`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authorization_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authorization_record_type)`` is ``true`` .

        arg:    authorization_record_type (osid.type.Type): the type of
                the record to retrieve
        return: (osid.authorization.records.AuthorizationRecord) - the
                authorization record
        raise:  NullArgument - ``authorization_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(authorization_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(authorization_record_type)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if obj_map['startDate'] is not None:
            start_date = obj_map['startDate']
            obj_map['startDate'] = dict()
            obj_map['startDate']['year'] = start_date.year
            obj_map['startDate']['month'] = start_date.month
            obj_map['startDate']['day'] = start_date.day
            obj_map['startDate']['hour'] = start_date.hour
            obj_map['startDate']['minute'] = start_date.minute
            obj_map['startDate']['second'] = start_date.second
            obj_map['startDate']['microsecond'] = start_date.microsecond
        if obj_map['endDate'] is not None:
            end_date = obj_map['endDate']
            obj_map['endDate'] = dict()
            obj_map['endDate']['year'] = end_date.year
            obj_map['endDate']['month'] = end_date.month
            obj_map['endDate']['day'] = end_date.day
            obj_map['endDate']['hour'] = end_date.hour
            obj_map['endDate']['minute'] = end_date.minute
            obj_map['endDate']['second'] = end_date.second
            obj_map['endDate']['microsecond'] = end_date.microsecond
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class AuthorizationForm(abc_authorization_objects.AuthorizationForm, osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Authorizations``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AuthorizationAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'authorization.Authorization'

    def __init__(self, **kwargs):
        osid_objects.OsidRelationshipForm.__init__(self, object_name='AUTHORIZATION', **kwargs)
        self._mdata = default_mdata.get_authorization_mdata()  # Don't know if we need default mdata for this
        self._init_metadata(**kwargs)

        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        """Initialize form metadata"""
        osid_objects.OsidRelationshipForm._init_metadata(self, **kwargs)

    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidRelationshipForm._init_map(self, record_types=record_types)
        self._my_map['assignedVaultIds'] = [str(kwargs['vault_id'])]
        self._my_map['functionId'] = str(kwargs['function_id'])
        self._my_map['qualifierId'] = str(kwargs['qualifier_id'])
        if 'agent_id' in kwargs:
            self._my_map['agentId'] = str(kwargs['agent_id'])
        if 'resource_id' in kwargs:
            self._my_map['resourceId'] = str(kwargs['resource_id'])

    @utilities.arguments_not_none
    def get_authorization_form_record(self, authorization_record_type):
        """Gets the ``AuthorizationFormRecord`` corresponding to the given authorization record ``Type``.

        arg:    authorization_record_type (osid.type.Type): the
                authorization record type
        return: (osid.authorization.records.AuthorizationFormRecord) -
                the authorization form record
        raise:  NullArgument - ``authorization_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(authorization_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_record(authorization_record_type)


class AuthorizationList(abc_authorization_objects.AuthorizationList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AuthorizationList`` provides a means for accessing ``Authorization`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Authorization authorization =
    al.getNextAuthorization(); }

    or
      while (al.hasNext()) {
           Authorization[] authorizations = al.getNextAuthorizations(al.available());
      }

    """

    def get_next_authorization(self):
        """Gets the next ``Authorization`` in this list.

        return: (osid.authorization.Authorization) - the next
                ``Authorization`` in this list. The ``has_next()``
                method should be used to test that a next
                ``Authorization`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Authorization)

    __next__ = next

    next_authorization = property(fget=get_next_authorization)

    @utilities.arguments_not_none
    def get_next_authorizations(self, n):
        """Gets the next set of ``Authorization`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``Authorization`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.authorization.Authorization) - an array of
                ``Authorization`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(AuthorizationList, number=n)


class Vault(abc_authorization_objects.Vault, osid_objects.OsidCatalog):
    """A vault defines a collection of authorizations and functions."""
    _namespace = 'authorization.Vault'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='VAULT', **kwargs)

    @utilities.arguments_not_none
    def get_vault_record(self, vault_record_type):
        """Gets the vault record corresponding to the given ``Vault`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``vault_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(vault_record_type)``
        is ``true`` .

        arg:    vault_record_type (osid.type.Type): a vault record type
        return: (osid.authorization.records.VaultRecord) - the vault
                record
        raise:  NullArgument - ``vault_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(vault_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class VaultForm(abc_authorization_objects.VaultForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating vaults.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``VaultAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    _namespace = 'authorization.Vault'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='VAULT', **kwargs)
        self._mdata = default_mdata.get_vault_mdata()
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
    def get_vault_form_record(self, vault_record_type):
        """Gets the ``VaultFormRecord`` corresponding to the given vault record ``Type``.

        arg:    vault_record_type (osid.type.Type): a vault record type
        return: (osid.authorization.records.VaultFormRecord) - the vault
                form record
        raise:  NullArgument - ``vault_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(vault_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class VaultList(abc_authorization_objects.VaultList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``VaultList`` provides a means for accessing ``Vault`` elements sequentially either one at a time or many at a time.

    Examples: while (vl.hasNext()) { Vault vault = vl.getNextVault(); }

    or
      while (vl.hasNext()) {
           Vault[] vaults = vl.getNextVaults(vl.available());
      }

    """

    def get_next_vault(self):
        """Gets the next ``Vault`` in this list.

        return: (osid.authorization.Vault) - the next ``Vault`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Vault`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(Vault)

    __next__ = next

    next_vault = property(fget=get_next_vault)

    @utilities.arguments_not_none
    def get_next_vaults(self, n):
        """Gets the next set of ``Vault`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Vault`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.authorization.Vault) - an array of ``Vault``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(VaultList, number=n)


class VaultNode(abc_authorization_objects.VaultNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``VaultHierarchySession``.

    """
    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy

    def get_object_node_map(self):
        node_map = dict(self.get_vault().get_object_map())
        node_map['type'] = 'VaultNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for vault_node in self.get_parent_vault_nodes():
            node_map['parentNodes'].append(vault_node.get_object_node_map())
        for vault_node in self.get_child_vault_nodes():
            node_map['childNodes'].append(vault_node.get_object_node_map())
        return node_map

    def get_vault(self):
        """Gets the ``Vault`` at this node.

        return: (osid.authorization.Vault) - the vault represented by
                this node
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._lookup_session is None:
            mgr = get_provider_manager('AUTHORIZATION', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_vault_lookup_session(proxy=getattr(self, "_proxy", None))
        return self._lookup_session.get_vault(Id(self._my_map['id']))

    vault = property(fget=get_vault)

    def get_parent_vault_nodes(self):
        """Gets the parents of this vault.

        return: (osid.authorization.VaultNodeList) - the parents of this
                vault
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_vault_nodes = []
        for node in self._my_map['parentNodes']:
            parent_vault_nodes.append(VaultNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return VaultNodeList(parent_vault_nodes)

    parent_vault_nodes = property(fget=get_parent_vault_nodes)

    def get_child_vault_nodes(self):
        """Gets the children of this vault.

        return: (osid.authorization.VaultNodeList) - the children of
                this vault
        *compliance: mandatory -- This method must be implemented.*

        """
        parent_vault_nodes = []
        for node in self._my_map['childNodes']:
            parent_vault_nodes.append(VaultNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return VaultNodeList(parent_vault_nodes)

    child_vault_nodes = property(fget=get_child_vault_nodes)


class VaultNodeList(abc_authorization_objects.VaultNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``VaultNodeList`` provides a means for accessing ``VaultNode`` elements sequentially either one at a time or many at a time.

    Examples: while (vnl.hasNext()) { VaultNode node =
    vnl.getNextVaultNode(); }

    or
      while (vnl.hasNext()) {
           VaultNode[] nodes = vnl.getNextVaultNodes(vnl.available());
      }

    """

    def get_next_vault_node(self):
        """Gets the next ``VaultNode`` in this list.

        return: (osid.authorization.VaultNode) - the next ``VaultNode``
                in this list. The ``has_next()`` method should be used
                to test that a next ``VaultNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return next(self)

    def next(self):
        return self._get_next_object(VaultNode)

    __next__ = next

    next_vault_node = property(fget=get_next_vault_node)

    @utilities.arguments_not_none
    def get_next_vault_nodes(self, n):
        """Gets the next set of ``VaultNode`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``VaultNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.authorization.VaultNode) - an array of
                ``VaultNode`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(VaultNodeList, number=n)
