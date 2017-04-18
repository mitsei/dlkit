"""Implementations of authorization abstract base class searches."""
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


class AuthorizationSearch:
    """``AuthorizationSearch`` defines the interface for specifying authorization search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_authorizations(self, authorization_ids):
        """Execute this search among the given list of authorizations.

        :param authorization_ids: list of authorizations
        :type authorization_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``authorization_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_authorization_results(self, authorization_search_order):
        """Specify an ordering to the search results.

        :param authorization_search_order: authorization search order
        :type authorization_search_order: ``osid.authorization.AuthorizationSearchOrder``
        :raise: ``NullArgument`` -- ``authorization_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``authorization_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_authorization_search_record(self, authorization_search_record_type):
        """Gets the authorization search record corresponding to the given authorization search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param authorization_search_record_type: an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: the authorization search record
        :rtype: ``osid.authorization.records.AuthorizationSearchRecord``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationSearchRecord


class AuthorizationSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorizations(self):
        """Gets the authorization list resulting from the search.

        :return: the authorization list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    authorizations = property(fget=get_authorizations)

    @abc.abstractmethod
    def get_authorization_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.authorization.AuthorizationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQueryInspector

    authorization_query_inspector = property(fget=get_authorization_query_inspector)

    @abc.abstractmethod
    def get_authorization_search_results_record(self, authorization_search_record_type):
        """Gets the authorization search results record corresponding to the given authorization search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param authorization_search_record_type: an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: the authorization search results record
        :rtype: ``osid.authorization.records.AuthorizationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationSearchResultsRecord


class FunctionSearch:
    """``FunctionSearch`` defines the interface for specifying function search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_functions(self, function_ids):
        """Execute this search among the given list of functions.

        :param function_ids: list of functions
        :type function_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``function_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_function_results(self, function_search_order):
        """Specify an ordering to the search results.

        :param function_search_order: function search order
        :type function_search_order: ``osid.authorization.FunctionSearchOrder``
        :raise: ``NullArgument`` -- ``function_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``function_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_function_search_record(self, function_search_record_type):
        """Gets the function search record corresponding to the given function search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param function_search_record_type: a function search record type
        :type function_search_record_type: ``osid.type.Type``
        :return: the function search record
        :rtype: ``osid.authorization.records.FunctionSearchRecord``
        :raise: ``NullArgument`` -- ``function_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.FunctionSearchRecord


class FunctionSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_functions(self):
        """Gets the function list resulting from the search.

        :return: the function list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    functions = property(fget=get_functions)

    @abc.abstractmethod
    def get_function_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the function query inspector
        :rtype: ``osid.authorization.FunctionQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQueryInspector

    function_query_inspector = property(fget=get_function_query_inspector)

    @abc.abstractmethod
    def get_function_search_results_record(self, function_search_record_type):
        """Gets the function search results record corresponding to the given function search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param function_search_record_type: a function search record type
        :type function_search_record_type: ``osid.type.Type``
        :return: the function search results record
        :rtype: ``osid.authorization.records.FunctionSearchResultsRecord``
        :raise: ``NullArgument`` -- ``function_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.FunctionSearchResultsRecord


class QualifierSearch:
    """``QualifierSearch`` defines the interface for specifying qualifier search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_qualifiers(self, qualifier_ids):
        """Execute this search among the given list of qualifiers.

        :param qualifier_ids: list of qualifiers
        :type qualifier_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``qualifier_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_qualifier_results(self, qualifier_search_order):
        """Specify an ordering to the search results.

        :param qualifier_search_order: qualifier search order
        :type qualifier_search_order: ``osid.authorization.QualifierSearchOrder``
        :raise: ``NullArgument`` -- ``qualifier_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``qualifier_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_qualifier_search_record(self, qualifier_search_record_type):
        """Gets the qualifier search record corresponding to the given qualifier search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param qualifier_search_record_type: a qualifier search record type
        :type qualifier_search_record_type: ``osid.type.Type``
        :return: the qualifier search record
        :rtype: ``osid.authorization.records.QualifierSearchRecord``
        :raise: ``NullArgument`` -- ``qualifier_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.QualifierSearchRecord


class QualifierSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifiers(self):
        """Gets the qualifier list resulting from the search.

        :return: the qualifier list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    qualifiers = property(fget=get_qualifiers)

    @abc.abstractmethod
    def get_qualifier_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.authorization.QualifierQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQueryInspector

    qualifier_query_inspector = property(fget=get_qualifier_query_inspector)

    @abc.abstractmethod
    def get_qualifier_search_results_record(self, qualifier_search_record_type):
        """Gets the qualifier search results record corresponding to the given qualifier search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param qualifier_search_record_type: a qualifier search record type
        :type qualifier_search_record_type: ``osid.type.Type``
        :return: the qualifier search results record
        :rtype: ``osid.authorization.records.QualifierSearchResultsRecord``
        :raise: ``NullArgument`` -- ``qualifier_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.QualifierSearchResultsRecord


class VaultSearch:
    """The interface for governing vault searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_vaults(self, vault_ids):
        """Execute this search among the given list of vaults.

        :param vault_ids: list of vaults
        :type vault_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_vault_results(self, vault_search_order):
        """Specify an ordering to the search results.

        :param vault_search_order: vault search order
        :type vault_search_order: ``osid.authorization.VaultSearchOrder``
        :raise: ``NullArgument`` -- ``vault_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``vault_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_vault_search_record(self, vault_search_record_type):
        """Gets the vault search record corresponding to the given vault search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param vault_search_record_type: a vault search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: the vault search record
        :rtype: ``osid.authorization.records.VaultSearchRecord``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.VaultSearchRecord


class VaultSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vaults(self):
        """Gets the vault list resulting from the search.

        :return: the vault list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    vaults = property(fget=get_vaults)

    @abc.abstractmethod
    def get_vault_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the vault query inspector
        :rtype: ``osid.authorization.VaultQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultQueryInspector

    vault_query_inspector = property(fget=get_vault_query_inspector)

    @abc.abstractmethod
    def get_vault_search_results_record(self, vault_search_record_type):
        """Gets the vault search results record corresponding to the given vault search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param vault_search_record_type: a vault search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: the vault search results record
        :rtype: ``osid.authorization.records.VaultSearchResultsRecord``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.VaultSearchResultsRecord
