"""Implementations of authentication abstract base class objects."""
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


class Agent:
    """An ``Agent`` represents an authenticatable identity.

    Like all OSID objects, an ``Agent`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agent_record(self, agent_record_type):
        """Gets the agent record corresponding to the given ``Agent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``agent_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(agent_record_type)``
        is ``true`` .

        :param agent_record_type: the type of the record to retrieve
        :type agent_record_type: ``osid.type.Type``
        :return: the agent record
        :rtype: ``osid.authentication.records.AgentRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgentRecord


class AgentForm:
    """This is the form for creating and updating ``Agents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AgentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agent_form_record(self, agent_record_type):
        """Gets the ``AgentFormRecord`` corresponding to the given agent record ``Type``.

        :param agent_record_type: the agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent form record
        :rtype: ``osid.authentication.records.AgentFormRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgentFormRecord


class AgentList:
    """Like all ``OsidLists,``  ``AgentList`` provides a means for accessing ``Agent`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Agent agent = al.getNextAgent(); }

    or
      while (al.hasNext()) {
           Agent[] agents = al.getNextAgents(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_agent(self):
        """Gets the next ``Agent`` in this list.

        :return: the next ``Agent`` in this list. The ``has_next()`` method should be used to test that a next ``Agent`` is available before calling this method.
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    next_agent = property(fget=get_next_agent)

    @abc.abstractmethod
    def get_next_agents(self, n):
        """Gets the next set of ``Agent`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Agent`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Agent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent


class Agency:
    """An agency defines a collection of agents."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_record(self, agency_record_type):
        """Gets the agency record corresponding to the given ``Agency`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``agency_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(agency_record_type)``
        is ``true`` .

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency record
        :rtype: ``osid.authentication.records.AgencyRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgencyRecord


class AgencyForm:
    """This is the form for creating and updating agencies.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AgencyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_form_record(self, agency_record_type):
        """Gets the ``AgencyFormRecord`` corresponding to the given agency record ``Type``.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency form record
        :rtype: ``osid.authentication.records.AgencyFormRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgencyFormRecord


class AgencyList:
    """Like all ``OsidLists,``  ``AgencyList`` provides a means for accessing ``Agency`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Agency agency = al.getNextAgency();
    }

    or
      while (al.hasNext()) {
           Agency[] agencies = al.getNextAgencies(al.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_agency(self):
        """Gets the next ``Agency`` in this list.

        :return: the next ``Agency`` in this list. The ``has_next()`` method should be used to test that a next ``Agency`` is available before calling this method.
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    next_agency = property(fget=get_next_agency)

    @abc.abstractmethod
    def get_next_agencies(self, n):
        """Gets the next set of ``Agency`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Agency`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Agency`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency


class AgencyNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``AgencyHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency(self):
        """Gets the ``Agency`` at this node.

        :return: the agency represented by this node
        :rtype: ``osid.authentication.Agency``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agency

    agency = property(fget=get_agency)

    @abc.abstractmethod
    def get_parent_agency_nodes(self):
        """Gets the parents of this agency.

        :return: the parents of the ``id``
        :rtype: ``osid.authentication.AgencyNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyNodeList

    parent_agency_nodes = property(fget=get_parent_agency_nodes)

    @abc.abstractmethod
    def get_child_agency_nodes(self):
        """Gets the children of this agency.

        :return: the children of this agency
        :rtype: ``osid.authentication.AgencyNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyNodeList

    child_agency_nodes = property(fget=get_child_agency_nodes)


class AgencyNodeList:
    """Like all ``OsidLists,``  ``AgencyNodeList`` provides a means for accessing ``AgencyNode`` elements sequentially either one at a time or many at a time.

    Examples: while (anl.hasNext()) { AgencyNode node =
    anl.getNextAgencyNode(); }

    or
      while (anl.hasNext()) {
           AgencyNode[] nodes = anl.getNextAgencyNodes(anl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_agency_node(self):
        """Gets the next ``AgencyNode`` in this list.

        :return: the next ``AgencyNode`` in this list. The ``has_next()`` method should be used to test that a next ``AgencyNode`` is available before calling this method.
        :rtype: ``osid.authentication.AgencyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyNode

    next_agency_node = property(fget=get_next_agency_node)

    @abc.abstractmethod
    def get_next_agency_nodes(self, n):
        """Gets the next set of ``AgencyNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``AgencyNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``AgencyNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.AgencyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.AgencyNode
