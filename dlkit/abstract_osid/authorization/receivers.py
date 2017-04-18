"""Implementations of authorization abstract base class receivers."""
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


class AuthorizationReceiver:
    """The authorization receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Authorizations``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_authorizations(self, notification_id, authorization_ids):
        """The callback for notifications of new authorizations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the new ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_authorizations(self, notification_id, authorization_ids):
        """The callback for notification of updated authorization.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the updated ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_authorizations(self, notification_id, authorization_ids):
        """The callback for notification of deleted authorizations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the deleted ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FunctionReceiver:
    """The function receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Functions``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_functions(self, notification_id, function_ids):
        """The callback for notifications of new functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the new ``Functions``
        :type function_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_functions(self, notification_id, function_ids):
        """The callback for notification of updated functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the updated ``Functions``
        :type function_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_functions(self, notification_id, function_ids):
        """The callback for notification of deleted functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the deleted ``Functions``
        :type function_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class QualifierReceiver:
    """The qualifier receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Qualifier`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_qualifiers(self, notification_id, qualifier_ids):
        """The callback for notifications of new qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the new ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_qualifiers(self, notification_id, qualifier_ids):
        """The callback for notification of updated qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the updated ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_qualifiers(self, notification_id, qualifier_ids):
        """the callback for notification of deleted qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the deleted ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_billings(self, notification_id, qualifier_ids):
        """The callback for notifications of changes to children of qualifier hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Ids`` of the ``Qualifiers`` whose children have changed
        :type qualifier_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class VaultReceiver:
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Vault`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def new_vaults(self, notification_id, vault_ids):
        """The callback for notifications of new vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the new ``Vaults``
        :type vault_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_vaults(self, notification_id, vault_ids):
        """The callback for notification of updated vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the updated ``Vaults``
        :type vault_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def deleted_vaults(self, notification_id, vault_ids):
        """The callback for notification of deleted vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the deleted ``Vaults``
        :type vault_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def changed_child_of_vaults(self, notification_id, vault_ids):
        """The callback for notifications of changes to children of vault hierarchy nodes.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Ids`` of the ``Vaults`` whose children have changed
        :type vault_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass
