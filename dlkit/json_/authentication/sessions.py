"""JSON implementations of authentication sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from bson.objectid import ObjectId


from . import objects
from .. import utilities
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import Id
from ..utilities import JSONClientValidated
from dlkit.abstract_osid.authentication import sessions as abc_authentication_sessions
from dlkit.abstract_osid.osid import errors


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True


class AgentLookupSession(abc_authentication_sessions.AgentLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Agent`` objects.

    The ``Agent`` represents the authenticated entity. Agents generally
    map to resources although this isn't always the case.

    This session defines two sets of views which offer differing
    behaviors when retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition
      * isolated agency view: All agent methods in this session operate,
        retrieve and pertain to agents defined explicitly in the current
        agency. Using an isolated view is useful for managing agents
        with the AgentAdminSession.
      * federated agency view: All agent methods in this session
        operate, retrieve and pertain to all agents defined in this
        agency and any other agents implicitly available in this agency
        through agency inheritence.


    Generally, the comparative view should be used for most applications
    as it permits operation even if there a particular element is
    inaccessible. For example, a hierarchy output can be plugged into a
    lookup method to retrieve all objects known to a hierarchy, but it
    may not be necessary to break execution if a node from the hierarchy
    no longer exists. However, some administrative applications may need
    to know whether it had retrieved an entire set of objects and may
    sacrifice some interoperability for the sake of precision.

    Agents may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Agent``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Agency
        self._catalog_name = 'Agency'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='authentication',
            cat_name='Agency',
            cat_class=objects.Agency)
        self._kwargs = kwargs

    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Agency Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        return: (osid.authentication.Agency) - the ``Agency`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    agency = property(fget=get_agency)

    def can_lookup_agents(self):
        """Tests if this user can perform ``Agent`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this agency only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_agent(self, agent_id):
        """Gets the ``Agent`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agent`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agent`` and retained for compatibility.

        arg:    agent_id (osid.id.Id): the ``Id`` of an ``Agent``
        return: (osid.authentication.Agent) - the returned ``Agent``
        raise:  NotFound - no ``Agent`` found with the given ``Id``
        raise:  NullArgument - ``agent_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('authentication',
                                         collection='Agent',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(agent_id, 'authentication').get_identifier())},
                 **self._view_filter()))
        return objects.Agent(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_agents_by_ids(self, agent_ids):
        """Gets an ``AgentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the agents
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agents`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    agent_ids (osid.id.IdList): a list of agent ``Ids``
        return: (osid.authentication.AgentList) - the returned ``Agent
                list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``agent_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('authentication',
                                         collection='Agent',
                                         runtime=self._runtime)
        object_id_list = []
        for i in agent_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'authentication').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.AgentList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_agents_by_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` which does not include agents of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        arg:    agent_genus_type (osid.type.Type): an agent genus type
        return: (osid.authentication.AgentList) - the returned ``Agent``
                list
        raise:  NullArgument - ``agent_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('authentication',
                                         collection='Agent',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(agent_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AgentList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_agents_by_parent_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` and include any additional agents with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        arg:    agent_genus_type (osid.type.Type): an agent genus type
        return: (osid.authentication.AgentList) - the returned ``Agent``
                list
        raise:  NullArgument - ``agent_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AgentList([])

    @utilities.arguments_not_none
    def get_agents_by_record_type(self, agent_record_type):
        """Gets an ``AgentList`` containing the given agent record ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        arg:    agent_record_type (osid.type.Type): an agent record type
        return: (osid.authentication.AgentList) - the returned ``Agent``
                list
        raise:  NullArgument - ``agent_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AgentList([])

    def get_agents(self):
        """Gets all ``Agents``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        return: (osid.authentication.AgentList) - a list of ``Agents``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('authentication',
                                         collection='Agent',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AgentList(result, runtime=self._runtime, proxy=self._proxy)

    agents = property(fget=get_agents)
