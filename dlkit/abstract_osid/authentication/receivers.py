"""Implementations of authentication abstract base class receivers."""
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


class AgentReceiver:
    """The agent receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Agent`` objects.

    A change to a key is a change to an ``Agent``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_agents(self, notification_id, agent_ids):
        """The callback for notifications of new agents.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agent_ids: the ``Id`` of the new ``Agents``
        :type agent_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_agents(self, notification_id, agent_ids):
        """The callback for notification of updated agents.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agent_ids: the ``Id`` of the updated ``Agents``
        :type agent_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_agents(self, notification_id, agent_ids):
        """the callback for notification of deleted agents.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agent_ids: the ``Id`` of the deleted ``Agents``
        :type agent_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AgencyReceiver:
    """The agency receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Agency`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_agencies(self, notification_id, agency_ids):
        """The callback for notifications of new agencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agency_ids: the ``Ids`` of the new ``Agencies``
        :type agency_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_agencies(self, notification_id, agency_ids):
        """The callback for notification of updated agencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agency_ids: the ``Ids`` of the updated ``Agencies``
        :type agency_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_agencies(self, notification_id, agency_ids):
        """The callback for notification of deleted agencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agency_ids: the ``Ids`` of the deleted ``Agencies``
        :type agency_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_agencies(self, notification_id, agency_ids):
        """The callback for notifications of changes to children of agency hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param agency_ids: the ``Ids`` of the ``Agencies`` whose children have changed
        :type agency_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
