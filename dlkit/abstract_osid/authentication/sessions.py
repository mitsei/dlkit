"""Implementations of authentication abstract base class sessions."""
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


class AgentLookupSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_lookup_agents(self):
        """Tests if this user can perform ``Agent`` lookups.

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
    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_agent(self, agent_id):
        """Gets the ``Agent`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agent`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agent`` and retained for compatibility.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: the returned ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``NotFound`` -- no ``Agent`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    @abc.abstractmethod
    def get_agents_by_ids(self, agent_ids):
        """Gets an ``AgentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the agents
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agents`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param agent_ids: a list of agent ``Ids``
        :type agent_ids: ``osid.id.IdList``
        :return: the returned ``Agent list``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``agent_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agents_by_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` which does not include agents of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agents_by_parent_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` and include any additional agents with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agents_by_record_type(self, agent_record_type):
        """Gets an ``AgentList`` containing the given agent record ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agents(self):
        """Gets all ``Agents``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :return: a list of ``Agents``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    agents = property(fget=get_agents)


class AgentQuerySession:
    """This session provides methods for searching ``Agents``.

    The search query is constructed using the ``AgentQuery``. The agent
    record ``Type`` also specifies the record for the agent query.

    This session defines views that offer differing behaviors for
    searching.

      * federated agency view: searches include agents in agencies of
        which this agency is a ancestor in the agency hierarchy
      * isolated agency view: searches are restricted to agents in this
        agency


    Agents may have an agent query record indicated by their respective
    agent record types. The agent query record is accessed via the
    ``AgentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_search_agents(self):
        """Tests if this user can perform ``Agent`` searches.

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
    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets an agent query.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def get_agents_by_query(self, agent_query):
        """Gets a list of ``Agents`` matching the given agent query.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :return: the returned ``AgentList``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList


class AgentSearchSession:
    """This session provides methods for searching ``Agents``.

    The search query is constructed using the ``AgentQuery``. The agent
    record ``Type`` also specifies the record for the agent query.

    ``get_agents_by_query()`` is the basic search method and returns a
    list of ``Agents``. A more advanced search may be performed with
    ``getAgentsBySearch()``. It accepts an ``AgentSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_agents_by_search()`` returns an ``AgentSearchResults`` that
    can be used to access the resulting ``AgentList`` or be used to
    perform a search within the result set through ``AgentSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated agency view: searches include agents in agencies of
        which this agency is a ancestor in the agency hierarchy
      * isolated agency view: searches are restricted to agents in this
        agency


    Agents may have an agent query record indicated by their respective
    record types. The agent query record is accessed via the
    ``AgentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agent_search(self):
        """Gets an agent search.

        :return: the agent search
        :rtype: ``osid.authentication.AgentSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentSearch

    agent_search = property(fget=get_agent_search)

    @abc.abstractmethod
    def get_agent_search_order(self):
        """Gets an agent search order.

        The ``AgentSearchOrder`` is supplied to an ``AgentSearch`` to
        specify the ordering of results.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    @abc.abstractmethod
    def get_agents_by_search(self, agent_query, agent_search):
        """Gets the search results matching the given search query using the given search.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :param agent_search: the agent search
        :type agent_search: ``osid.authentication.AgentSearch``
        :return: the returned search results
        :rtype: ``osid.authentication.AgentSearchResults``
        :raise: ``NullArgument`` -- ``agent_query`` or ``agent_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_search`` or ``agent_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentSearchResults

    @abc.abstractmethod
    def get_agent_query_from_inspector(self, agent_query_inspector):
        """Gets an agent query from an inspector.

        The inspector is available from an ``AgentSearchResults``.

        :param agent_query_inspector: an agent query inspector
        :type agent_query_inspector: ``osid.authentication.AgentQueryInspector``
        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``NullArgument`` -- ``agent_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``agent_query_inspector`` is not of thiss ervice

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQuery


class AgentAdminSession:
    """This session creates, updates, and deletes ``Agents``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Agent,`` an ``AgentForm`` is requested using
    ``get_agent_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AgentForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AgentForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AgentForm`` corresponds
    to an attempted transaction.

    For updates, ``AgentForms`` are requested to the ``Agent``  ``Id``
    that is to be updated using ``getAgentFormForUpdate()``. Similarly,
    the ``AgentForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``AgentForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Agents``. To unmap an ``Agent`` from
    the current ``Agency,`` the ``AgentAgencyAssignmentSession`` should
    be used. These delete operations attempt to remove the ``Agent``
    itself thus removing it from all known ``Agency`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_create_agents(self):
        """Tests if this user can create ``Agents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_agent_with_record_types(self, agent_record_types):
        """Tests if this user can create a single ``Agent`` using the desired record types.

        While ``AuthenticationManager.getAgentRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific ``Agent``.
        Providing an empty array tests if an ``Agent`` can be created
        with no records.

        :param agent_record_types: array of agent record types
        :type agent_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Agent`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_form_for_create(self, agent_record_types):
        """Gets the agent form for creating new agents.

        A new form should be requested for each create transaction.

        :param agent_record_types: array of agent record types
        :type agent_record_types: ``osid.type.Type[]``
        :return: the agent form
        :rtype: ``osid.authentication.AgentForm``
        :raise: ``NullArgument`` -- ``agent_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentForm

    @abc.abstractmethod
    def create_agent(self, agent_form):
        """Creates a new ``Agent``.

        :param agent_form: the form for this ``Agent``
        :type agent_form: ``osid.authentication.AgentForm``
        :return: the new ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``agent_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``agent_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_form`` did not originate from ``get_agent_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    @abc.abstractmethod
    def can_update_agents(self):
        """Tests if this user can update ``Agents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if agent modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_update_agent(self, agent_id):
        """Tests if this user can update a specified agent.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the agent
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer an update
        operation to an unauthorized user for this agent.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: ``false`` if agent modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``agent_id`` is not found, then
        it is acceptable to return false to indicate the lack of an
        update available.

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_form_for_update(self, agent_id):
        """Gets the agent form for updating an existing agent.

        A new agent form should be requested for each update
        transaction.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: the agent form
        :rtype: ``osid.authentication.AgentForm``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentForm

    @abc.abstractmethod
    def update_agent(self, agent_form):
        """Updates an existing agent.

        :param agent_form: the form containing the elements to be updated
        :type agent_form: ``osid.authentication.AgentForm``
        :raise: ``IllegalState`` -- ``agent_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``agent_id`` or ``agent_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_form`` did not originate from ``get_agent_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_agents(self):
        """Tests if this user can delete ``Agents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_delete_agent(self, agent_id):
        """Tests if this user can delete a specified ``Agent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Agent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer a
        delete operation to an unauthorized user for this agent.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: ``false`` if ``Agent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If the ``agent_id`` is not found, then
        it is acceptable to return false to indicate the lack of a
        delete available.

        """
        return  # boolean

    @abc.abstractmethod
    def delete_agent(self, agent_id):
        """Deletes the ``Agent`` identified by the given ``Id`` removing it from all other ``Agencies`` to which this ``Agent`` is associated.

        :param agent_id: the ``Id`` of the ``Agent`` to delete
        :type agent_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Agent`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_agent_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Agents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_agent(self, agent_id, alias_id):
        """Adds an ``Id`` to an ``Agent`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Agent`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another engine, it is
        reassigned to the given engine ``Id``.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``agent_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgentNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Agent`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``AgentLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_register_for_agent_notifications(self):
        """Tests if this user can register for ``Agent`` notifications.

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
    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_agent_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_agent_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_agent_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_agent_notification(self, notification_id):
        """Acknowledge an agent notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_agents(self):
        """Register for notifications of new agents.

        ``AgentReceiver.newAgents()`` is invoked when a new ``Agent`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agents(self):
        """Registers for notification of updated agents.

        ``AgentReceiver.changedAgents()`` is invoked when an agent is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agent(self, agent_id):
        """Registers for notification of an updated agent.

        ``AgentReceiver.changedAgents()`` is invoked when the specified
        agent is changed.

        :param agent_id: the ``Id`` of the ``Agent`` to monitor
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_agents(self):
        """Registers for notification of deleted agents.

        ``AgentReceiver.deletedAgents()`` is invoked when an agent is
        removed from this agency.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_agent(self, agent_id):
        """Registers for notification of a deleted agent.

        ``AgentReceiver.deletedAgents()`` is invoked when the specified
        agent is removed from this agency.

        :param agent_id: the ``Id`` of the ``Agent`` to monitor
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_agent_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_agent_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_agent_notification(self, notification_id):
        """Acknowledge an agent notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgentAgencySession:
    """This session provides methods to retrieve ``Agents`` to ``Agency`` mappings.

    An ``Agent`` may appear in multiple ``Agency`` objects. Each
    ``Agency`` may have its own authorizations governing who is allowed
    to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_agent_agency_mappings(self):
        """Tests if this user can perform lookups of agent/agency mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_agency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_agency_view(self):
        """A complete view of the ``Agent`` and ``Agency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_agent_ids_by_agency(self, agency_id):
        """Gets the list of ``Agent``  ``Ids`` associated with an ``Agency``.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of related agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_agents_by_agency(self, agency_id):
        """Gets the list of ``Agents`` associated with an ``Agency``.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of related agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agent_ids_by_agencies(self, agency_ids):
        """Gets the list of ``Agent Ids`` corresponding to a list of ``Agency`` objects.

        :param agency_ids: list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: list of agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_agents_by_agencies(self, agency_ids):
        """Gets the list of ``Agents`` corresponding to a list of ``Agency`` objects.

        :param agency_ids: list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: list of agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentList

    @abc.abstractmethod
    def get_agency_ids_by_agent(self, agent_id):
        """Gets the list of ``Agency``  ``Ids`` mapped to an ``Agent``.

        :param agent_id: ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_agencies_by_agent(self, agent_id):
        """Gets the list of ``Agency`` objects mapped to an ``Agent``.

        :param agent_id: ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of agencies
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList


class AgentAgencyAssignmentSession:
    """This session provides methods to re-assign ``Agents`` to ``Agencies`` An ``Agent`` may map to multiple ``Agency`` objects and removing the last reference to an ``Agent`` is the equivalent of deleting it.

    Each ``Agency`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of an ``Ageny`` to another ``Agency``
    is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_agents(self):
        """Tests if this user can alter agent/agency mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_agents_to_agency(self, agency_id):
        """Tests if this user can alter agent/agency mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_agency_ids(self, agency_id):
        """Gets a list of agencies including and under the given agency node in which any agent can be assigned.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of assignable agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_agency_ids_for_agent(self, agency_id, agent_id):
        """Gets a list of agencies including and under the given agency node in which a specific agent can be assigned.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_id`` or ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_agent_to_agency(self, agent_id, agency_id):
        """Adds an existing ``Agent`` to an ``Agency``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agent_id`` is already assigned to ``agency_id``
        :raise: ``NotFound`` -- ``agent_id`` or ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_agent_from_agency(self, agent_id, agency_id):
        """Removes an ``Agent`` from an ``Agency``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` or ``agency_id`` not found or ``agent_id`` not assigned to ``agency_id``
        :raise: ``NullArgument`` -- ``agent_id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_agent_to_agency(self, agent_id, from_agency_id, to_agency_id):
        """Moves an ``Agent`` from one ``Agency`` to another.

        Mappings to other ``Agencies`` are unaffected.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param from_agency_id: the ``Id`` of the current ``Agency``
        :type from_agency_id: ``osid.id.Id``
        :param to_agency_id: the ``Id`` of the destination ``Agency``
        :type to_agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id, from_agency_id,`` or ``to_agency_id`` not found or ``agent_id`` not mapped to ``from_agency_id``
        :raise: ``NullArgument`` -- ``agent_id, from_agency_id,`` or ``to_agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgentSmartAgencySession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``AgentQuery`` can be retrieved from this session and mapped to
    this ``Agency`` to create a virtual collection of ``Agents``. The
    agents may be sequenced using the ``AgentSearchOrder`` from this
    session.

    This ``Agency`` has a default query that matches any agent and a
    default search order that specifies no sequencing. The queries may
    be examined using an ``AgentQueryInspector``. The query may be
    modified by converting the inspector back to an ``AgentQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_id = property(fget=get_agency_id)

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def can_manage_smart_agencies(self):
        """Tests if this user can manage smart agencies.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart agency management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_query(self):
        """Gets an agent query.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    @abc.abstractmethod
    def get_agent_search_order(self):
        """Gets an agent search order.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    @abc.abstractmethod
    def apply_agent_query(self, agent_query):
        """Applies an agent query to this agency.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :raise: ``NullArgument`` -- ``agent_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``agent_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_agent_query(self):
        """Gets an agent query inspector for this agency.

        :return: the agent query inspector
        :rtype: ``osid.authentication.AgentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQueryInspector

    @abc.abstractmethod
    def apply_agent_sequencing(self, agent_search_order):
        """Applies an agent search order to this agency.

        :param agent_search_order: the agent search order
        :type agent_search_order: ``osid.authentication.AgentSearchOrder``
        :raise: ``NullArgument`` -- ``agent_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``agent_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_agent_query_from_inspector(self, agent_query_inspector):
        """Gets an agent query from an inspector.

        :param agent_query_inspector: a query inspector
        :type agent_query_inspector: ``osid.authentication.AgentQueryInspector``
        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``NullArgument`` -- ``agent_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``agent_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgentQuery


class AgencyLookupSession:
    """This session provides methods for retrieving ``Agency`` objects.

    The ``Agency`` represents a collection of ``Agents``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Agencies`` it can access, without breaking execution.
    However, an administrative application may require all ``Agency``
    elements to be available.

    Agencies may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Agency``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_agencies(self):
        """Tests if this user can perform ``Agency`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_agency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_agency_view(self):
        """A complete view of the ``Agency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_agency(self, agency_id):
        """Gets the ``Agency`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agency`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agency`` and retained for compatibility.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: the agency
        :rtype: ``osid.authentication.Agency``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authentication.Agency

    @abc.abstractmethod
    def get_agencies_by_ids(self, agency_ids):
        """Gets an ``AgencyList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the agencies
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agency`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param agency_ids: a list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def get_agencies_by_genus_type(self, agency_genus_type):
        """Gets an ``AgencyList`` corresponding to the given agency genus ``Type`` which does not include agencies of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_genus_type: an agency genus type
        :type agency_genus_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def get_agencies_by_parent_genus_type(self, agency_genus_type):
        """Gets an ``AgencyList`` corresponding to the given agency genus ``Type`` and include any additional agencies with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_genus_type: an agency genus type
        :type agency_genus_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def get_agencies_by_record_type(self, agency_record_type):
        """Gets an ``AgencyList`` containing the given agency record ``Type``.

        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def get_agencies_by_provider(self, resource_id):
        """Gets an ``AgencyList`` from the given provider.

        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def get_agencies(self):
        """Gets all ``Agencies``.

        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :return: an ``AgencyList``
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    agencies = property(fget=get_agencies)


class AgencyQuerySession:
    """This session provides methods for searching among ``Agency`` objects.

    The search query is constructed using the ``AgencyQuery``.

    Agencies may have a query record indicated by their respective
    record types. The query record is accessed via the ``AgencyQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_agencies(self):
        """Tests if this user can perform ``Agency`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an app

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agency_query(self):
        """Gets an agency query.

        :return: an agency query
        :rtype: ``osid.authentication.AgencyQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyQuery

    agency_query = property(fget=get_agency_query)

    @abc.abstractmethod
    def get_agencies_by_query(self, agency_query):
        """Gets a list of ``Agency`` objects matching the given agency query.

        :param agency_query: the agency query
        :type agency_query: ``osid.authentication.AgencyQuery``
        :return: the returned ``AgencyList``
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList


class AgencySearchSession:
    """This session provides methods for searching among ``Agency`` objects.

    The search query is constructed using the ``AgencyQuery``.

    ``get_agencies_by_query()`` is the basic search method and returns a
    list of ``Agency`` objects.A more advanced search may be performed
    with ``getAgenciesBySearch()``. It accepts a ``AgencySearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_agencies_by_search()`` returns a ``AgencySearchResults`` that
    can be used to access the resulting ``AgencyList`` or be used to
    perform a search within the result set through ``AgencySearch``.

    Agencies may have a query record indicated by their respective
    record types. The query record is accessed via the ``AgencyQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_search(self):
        """Gets an agency search.

        :return: an agency search
        :rtype: ``osid.authentication.AgencySearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencySearch

    agency_search = property(fget=get_agency_search)

    @abc.abstractmethod
    def get_agency_search_order(self):
        """Gets an agency search order.

        The ``AgencySearchOrder`` is supplied to a ``AgencySearch`` to
        specify the ordering of results.

        :return: the agency search order
        :rtype: ``osid.authentication.AgencySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencySearchOrder

    agency_search_order = property(fget=get_agency_search_order)

    @abc.abstractmethod
    def get_agencies_by_search(self, agency_query, agency_search):
        """Gets the search results matching the given search query using the given search.

        :param agency_query: the agency query
        :type agency_query: ``osid.authentication.AgencyQuery``
        :param agency_search: the agency search
        :type agency_search: ``osid.authentication.AgencySearch``
        :return: the search results
        :rtype: ``osid.authentication.AgencySearchResults``
        :raise: ``NullArgument`` -- ``agency_query`` or ``agency_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_query`` or ``agency_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencySearchResults

    @abc.abstractmethod
    def get_agency_query_from_inspector(self, agency_query_inspector):
        """Gets an agency query from an inspector.

        The inspector is available from an ``AgencySearchResults``.

        :param agency_query_inspector: an agency query inspector
        :type agency_query_inspector: ``osid.authentication.AgencyQueryInspector``
        :return: the agency query
        :rtype: ``osid.authentication.AgencyQuery``
        :raise: ``NullArgument`` -- ``agency_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``agency_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyQuery


class AgencyAdminSession:
    """This session creates, updates, and deletes ``Agencies``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Agency,`` an ``AgencyForm`` is requested using
    ``get_agency_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AgencyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AgencyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AgencyForm``
    corresponds to an attempted transaction.

    For updates, ``AgencyForms`` are requested to the ``Agency``  ``Id``
    that is to be updated using ``getAgencyFormForUpdate()``. Similarly,
    the ``AgencyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``AgencyForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Agencies``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_agencies(self):
        """Tests if this user can create ``Agencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Agency`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_agency_with_record_types(self, agency_record_types):
        """Tests if this user can create a single ``Agency`` using the desired record types.

        While ``AuthenticationManager.getAgencyRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific ``Agency``.
        Providing an empty array tests if an ``Agency`` can be created
        with no records.

        :param agency_record_types: array of agency record types
        :type agency_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Agency`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agency_form_for_create(self, agency_record_types):
        """Gets the agency form for creating new agencies.

        A new form should be requested for each create transaction.

        :param agency_record_types: array of agency record types
        :type agency_record_types: ``osid.type.Type[]``
        :return: the agency form
        :rtype: ``osid.authentication.AgencyForm``
        :raise: ``NullArgument`` -- ``agency_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyForm

    @abc.abstractmethod
    def create_agency(self, agency_form):
        """Creates a new ``Agency``.

        :param agency_form: the form for this ``Agency``
        :type agency_form: ``osid.authentication.AgencyForm``
        :return: the new ``Agency``
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- ``agency_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``agency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_form`` did not originate from ``get_agency_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    @abc.abstractmethod
    def can_update_agencies(self):
        """Tests if this user can update ``Agencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Agency`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agency_form_for_update(self, agency_id):
        """Gets the agency form for updating an existing agency.

        A new agency form should be requested for each update
        transaction.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: the agency form
        :rtype: ``osid.authentication.AgencyForm``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyForm

    @abc.abstractmethod
    def update_agency(self, agency_form):
        """Updates an existing agency.

        :param agency_form: the form containing the elements to be updated
        :type agency_form: ``osid.authentication.AgencyForm``
        :raise: ``IllegalState`` -- ``agency_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``agency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_form`` did not originate from ``get_agency_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_agencies(self):
        """Tests if this user can delete agencies.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Agency`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_agency(self, agency_id):
        """Deletes an ``Agency``.

        :param agency_id: the ``Id`` of the ``Agency`` to remove
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_agency_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Agencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Agency`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_agency(self, agency_id, alias_id):
        """Adds an ``Id`` to an ``Agency`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Agency`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another agency, it is
        reassigned to the given entry ``Id``.

        :param agency_id: the ``Id`` of an ``Agency``
        :type agency_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgencyNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Agency`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_agency_notifications(self):
        """Tests if this user can register for ``Agency`` notifications.

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
    def reliable_agency_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_agency_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_agency_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_agency_notification(self, notification_id):
        """Acknowledge an agency notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_agencies(self):
        """Register for notifications of new agencies.

        ``AgencyReceiver.newAgencies()`` is invoked when a new
        ``Agency`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agencies(self):
        """Registers for notification of updated agencies.

        ``AgencyReceiver.changedAgencies()`` is invoked when an agency
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agency(self, agency_id):
        """Registers for notification of an updated agency.

        ``AgencyReceiver.changedAgencies()`` is invoked when the
        specified agency is changed.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_agencies(self):
        """Registers for notification of deleted agencies.

        ``AgencyReceiver.deletedAgencies()`` is invoked when an agency
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_agency(self, agency_id):
        """Registers for notification of a deleted agency.

        ``AgencyReceiver.deletedAgencies()`` is invoked when the
        specified agency is deleted.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agency_hierarchy(self):
        """Registers for notification of an updated agency hierarchy structure.

        ``AgencyReceiver.changedChildOfAgencies()`` is invoked when a
        node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agency_hierarchy_for_ancestors(self, agency_id):
        """Registers for notification of an updated agency hierarchy structure.

        ``AgencyReceiver.changedChildOfAgencies()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param agency_id: the ``Id`` of the ``Agency`` node to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_agency_hierarchy_for_descendants(self, agency_id):
        """Registers for notification of an updated agency hierarchy structure.

        ``AgencyReceiver.changedChildOfAgencies()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param agency_id: the ``Id`` of the ``Agency`` node to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_agency_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_agency_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_agency_notification(self, notification_id):
        """Acknowledge an agency notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgencyHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Agency`` objects.

    Each node in the hierarchy is a unique ``Agency``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_agencies()`` and ``getChildAgencies()``. To relate
    these ``Ids`` to another OSID, ``get_agency_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Agency`` available in the Authentication OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_agencies()`` or ``get_child_agencies()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: agency elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_hierarchy_id = property(fget=get_agency_hierarchy_id)

    @abc.abstractmethod
    def get_agency_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    agency_hierarchy = property(fget=get_agency_hierarchy)

    @abc.abstractmethod
    def can_access_agency_hierarchy(self):
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
    def use_comparative_agency_view(self):
        """The returns from the agency methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_agency_view(self):
        """A complete view of the hierarchy returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_agency_ids(self):
        """Gets the root agency ``Ids`` in this hierarchy.

        :return: the root agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_agency_ids = property(fget=get_root_agency_ids)

    @abc.abstractmethod
    def get_root_agencies(self):
        """Gets the root agencies in this agency hierarchy.

        :return: the root agencies
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authentication.AgencyList

    root_agencies = property(fget=get_root_agencies)

    @abc.abstractmethod
    def has_parent_agencies(self, agency_id):
        """Tests if the ``Agency`` has any parents.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the agency has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is a direct parent of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_agency_ids(self, agency_id):
        """Gets the parent ``Ids`` of the given agency.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the agency
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_agencies(self, agency_id):
        """Gets the parents of the given agency.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: the parents of the agency
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def is_ancestor_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is an ancestor of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_agencies(self, agency_id):
        """Tests if an agency has any children.

        :param agency_id: an ``agency_id``
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``agency_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_agency(self, id_, agency_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_agency_ids(self, agency_id):
        """Gets the child ``Ids`` of the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :return: the children of the agency
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_agencies(self, agency_id):
        """Gets the children of the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :return: the children of the agency
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyList

    @abc.abstractmethod
    def is_descendant_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is a descendant of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_agency_node_ids(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an agency node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_agency_nodes(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an agency node
        :rtype: ``osid.authentication.AgencyNode``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyNode


class AgencyHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Agency`` objects.

    Each node in the hierarchy is a unique ``Agency``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    agency_hierarchy_id = property(fget=get_agency_hierarchy_id)

    @abc.abstractmethod
    def get_agency_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    agency_hierarchy = property(fget=get_agency_hierarchy)

    @abc.abstractmethod
    def can_modify_agency_hierarchy(self):
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
    def add_root_agency(self, agency_id):
        """Adds a root agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agency_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``agency`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_agency(self, agency_id):
        """Removes a root agency from this hierarchy.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_agency(self, agency_id, child_id):
        """Adds a child to an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agency_id`` already a parent of ``child_id``
        :raise: ``NotFound`` -- ``agency_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_agency(self, agency_id, child_id):
        """Removes a child from an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id is`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_agencies(self, agency_id):
        """Removes all children from an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
