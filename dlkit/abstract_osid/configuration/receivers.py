"""Implementations of configuration abstract base class receivers."""
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


class ParameterReceiver:
    """The parameter receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted ``Parameter`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_parameters(self, notification_id, parameter_ids):
        """The callback for notifications of new parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the new ``Parameters``
        :type parameter_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_parameters(self, notification_id, parameter_ids):
        """The callback for notification of updated parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the updated ``Parameters``
        :type parameter_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_parameters(self, notification_id, parameter_ids):
        """the callback for notification of deleted parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the deleted ``Parameters``
        :type parameter_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ValueReceiver:
    """The value receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``Values``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_values(self, notification_id, value_ids):
        """The callback for notification of new values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_values(self, notification_id, value_ids):
        """The callback for notification of changed values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_values(self, notification_id, value_ids):
        """The callback for notification of removed values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ConfigurationReceiver:
    """The configuration receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted ``Configuration`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_configurations(self, notification_id, configuration_ids):
        """The callback for notifications of new configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the new ``Configurations``
        :type configuration_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_configurations(self, notification_id, configuration_ids):
        """The callback for notification of updated configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the updated ``Configurations``
        :type configuration_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_configurations(self, notification_id, configuration_ids):
        """The callback for notification of deleted configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the deleted ``Configurations``
        :type configuration_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_confgurations(self, notification_id, configuration_ids):
        """The callback for notifications of changes to children of configuration hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the ``Configurations`` whose children have changed
        :type configuration_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
