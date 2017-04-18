"""Implementations of authorization abstract base class sessions."""
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


class AuthorizationSession:
    """This is the basic session for verifying authorizations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_access_authorizations(self):
        """Tests if this user can perform authorization checks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if authorization methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_authorized(self, agent_id, function_id, qualifier_id):
        """Determines if the given agent is authorized.

        An agent is authorized if an active authorization exists whose
        ``Agent,`` ``Function`` and ``Qualifier`` matches the supplied
        parameters. Authorizations may be defined using groupings or
        hieratchical structures for both the ``Agent`` and the
        ``Qualifier`` but are queried in the de-nornmalized form.

        The ``Agent`` is generally determined through the use of an
        Authentication OSID. The ``Function`` and ``Qualifier`` are
        already known as they map to the desired authorization to
        validate.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the user is authorized, ``false`` othersise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` , ``function_id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Authorizations may be stored in a
        normalized form with respect to various Resources and created
        using specific nodes in a ``Function`` or ``Qualifer``
        hierarchy. The provider needs to maintain a de-normalized
        implicit authorization store or expand the applicable
        hierarchies on the fly to honor this query.  Querying the
        authorization service may in itself require a separate
        authorization. A ``PermissionDenied`` is a result of this
        authorization failure. If no explicit or implicit authorization
        exists for the queried tuple, this method should return
        ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_condition(self, function_id):
        """Gets the ``AuthorizationCondition`` for making conditional authorization checks.

        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: an authorization condition
        :rtype: ``osid.authorization.AuthorizationCondition``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationCondition

    @abc.abstractmethod
    def is_authorized_on_condition(self, agent_id, function_id, qualifier_id, condition):
        """Determines if the given agent is authorized.

        An agent is authorized if an active authorization exists whose
        ``Agent,`` ``Function`` and ``Qualifier`` matches the supplied
        parameters. Authorizations may be defined using groupings or
        hieratchical structures for both the ``Agent`` and the
        ``Qualifier`` but are queried in the de-nornmalized form.

        The ``Agent`` is generally determined through the use of an
        Authentication OSID. The ``Function`` and ``Qualifier`` are
        already known as they map to the desired authorization to
        validate.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param condition: an authorization condition
        :type condition: ``osid.authorization.AuthorizationCondition``
        :return: ``true`` if the user is authorized, ``false`` othersise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` , ``function_id, qualifier_id`` , or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request
        :raise: ``Unsupported`` -- ``condition`` is not of this service

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Authorizations may be stored in a
        normalized form with respect to various Resources and created
        using specific nodes in a ``Function`` or ``Qualifer``
        hierarchy. The provider needs to maintain a de-normalized
        implicit authorization store or expand the applicable
        hierarchies on the fly to honor this query.  Querying the
        authorization service may in itself require a separate
        authorization. A ``PermissionDenied`` is a result of this
        authorization failure. If no explicit or implicit authorization
        exists for the queried tuple, this method should return
        ``false``.

        """
        return  # boolean


class AuthorizationLookupSession:
    """This session defines methods to search and retrieve ``Authorization`` mappings."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_lookup_authorizations(self):
        """Tests if this user can perform authorization lookups.

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
    def use_comparative_authorization_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_authorization_view(self):
        """A complete view of the ``Authorization`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_effective_authorization_view(self):
        """Only authorizations whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_effective_authorization_view(self):
        """All authorizations of any effective dates are returned by all methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.

        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.

        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_authorization(self, authorization_id):
        """Gets the ``Authorization`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Authorization`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Authorization`` and
        retained for compatibility.

        :param authorization_id: the ``Id`` of the ``Authorization`` to retrieve
        :type authorization_id: ``osid.id.Id``
        :return: the returned ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``NotFound`` -- no ``Authorization`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Authorization

    @abc.abstractmethod
    def get_authorizations_by_ids(self, authorization_ids):
        """Gets an ``AuthorizationList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        authorizations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Authorizations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param authorization_ids: the list of ``Ids`` to retrieve
        :type authorization_ids: ``osid.id.IdList``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``authorization_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_by_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` which does not include authorizations of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_genus_type: an authorization genus type
        :type authorization_genus_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_by_parent_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` and include authorizations of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_genus_type: an authorization genus type
        :type authorization_genus_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_by_record_type(self, authorization_record_type):
        """Gets an ``AuthorizationList`` containing the given authorization record ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_record_type: an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_on_date(self, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_resource(self, resource_id):
        """Gets a list of ``Authorizations`` associated with a given resource.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_resource_on_date(self, resource_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_agent(self, agent_id):
        """Gets a list of ``Authorizations`` associated with a given agent.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_agent_on_date(self, agent_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive but not confined to the date range.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``agent_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_function(self, function_id):
        """Gets a list of ``Authorizations`` associated with a given function.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_function_on_date(self, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given function and effective during the entire given date range inclusive but not confined to the date range.

        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_resource_and_function(self, resource_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given resource.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_resource_and_function_on_date(self, resource_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_agent_and_function(self, agent_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given agent.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``agent_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_for_agent_and_function_on_date(self, agent_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive but not confined to the date range.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``agent_id, function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_by_qualifier(self, qualifier_id):
        """Gets a list of ``Authorizations`` associated with a given qualifier.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_explicit_authorization(self, authorization_id):
        """Gets the explicit ``Authorization`` that generated the given implicit authorization.

        If the given ``Authorization`` is explicit, then the same
        ``Authorization`` is returned.

        :param authorization_id: an authorization
        :type authorization_id: ``osid.id.Id``
        :return: the explicit ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Authorization

    @abc.abstractmethod
    def get_authorizations(self):
        """Geta all ``Authorizations``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :return: a list of ``Authorizations``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    authorizations = property(fget=get_authorizations)


class AuthorizationQuerySession:
    """This session provides methods for searching ``Authorization`` objects.

    The search query is constructed using the ``AuthorizationQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated view: searches include authorizations in ``Vaults`` of
        which this vault is a ancestor in the vault hierarchy
      * isolated view: searches are restricted to authorizations in this
        ``Vault``
      * implicit authorization view: authorizations include implicit
        authorizations
      * explicit authorization view: only explicit authorizations are
        returned

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_search_authorizations(self):
        """Tests if this user can perform authorization searches.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.

        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicit_aut``



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.

        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_authorization_query(self):
        """Gets an authorization query.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    @abc.abstractmethod
    def get_authorizations_by_query(self, authorization_query):
        """Gets a list of ``Authorizations`` matching the given query.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :return: the returned ``AuthorizationList``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList


class AuthorizationSearchSession:
    """This session provides methods for searching ``Authorization`` objects.

    The search query is constructed using the ``AuthorizationQuery``.

    ``get_authorizations_by_query()`` is the basic search method and
    returns a list of ``Authorizations``. A more advanced search may be
    performed with ``getAuthorizationsBySearch()``. It accepts an
    ``AgentSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_authorizationss_by_search()`` returns an
    ``AuthorizationSearchResults`` that can be used to access the
    resulting ``AuthorizationList`` or be used to perform a search
    within the result set through ``AuthorizationSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated view: searches include authorizations in ``Vaults`` of
        which this vault is a ancestor in the vault hierarchy
      * isolated view: searches are restricted to authorizations in this
        ``Vault``
      * implicit authorization view: authorizations include implicit
        authorizations
      * explicit authorization view: only explicit authorizations are
        returned

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_authorization_search(self):
        """Gets an authorization search.

        :return: the authorization search
        :rtype: ``osid.authorization.AuthorizationSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationSearch

    authorization_search = property(fget=get_authorization_search)

    @abc.abstractmethod
    def get_authorization_search_order(self):
        """Gets an authorization search order.

        The ``AuthorizationSearchOrder`` is supplied to an
        ``AuthorizationSearch`` to specify the ordering of results.

        :return: the authorization search order
        :rtype: ``osid.authorization.AuthorizationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationSearchOrder

    authorization_search_order = property(fget=get_authorization_search_order)

    @abc.abstractmethod
    def get_authorizations_by_search(self, authorization_query, authorization_search):
        """Gets the search results matching the given search query using the given search.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :param authorization_search: the authorization search
        :type authorization_search: ``osid.authorization.AuthorizationSearch``
        :return: the returned search results
        :rtype: ``osid.authorization.AuthorizationSearchResults``
        :raise: ``NullArgument`` -- ``authorization_query`` or ``authorization_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_search`` or ``authorization_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationSearchResults

    @abc.abstractmethod
    def get_authorization_query_from_inspector(self, authorization_query_inspector):
        """Gets an authorization query from an inspector.

        The inspector is available from an
        ``AuthorizationSearchResults``.

        :param authorization_query_inspector: an authorization query inspector
        :type authorization_query_inspector: ``osid.authorization.AuthorizationQueryInspector``
        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``NullArgument`` -- ``authorization_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``authorization_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQuery


class AuthorizationAdminSession:
    """This session creates, updates, and deletes ``Authorizations``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Authorization,`` an ``AuthorizationForm`` is requested using
    ``get_authorization_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``AuthorizationForm`` will
    indicate that it is to be used with a create operation and can be
    used to examine metdata or validate data prior to creation. Once the
    ``AuthorizationForm`` is submiited to a create operation, it cannot
    be reused with another create operation unless the first operation
    was unsuccessful. Each ``AuthorizationForm`` corresponds to an
    attempted transaction.

    For updates, ``AuthorizationForms`` are requested to the
    ``Authorization``  ``Id`` that is to be updated using
    ``getAuthorizationFormForUpdate()``. Similarly, the
    ``AuthorizationForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AuthorizationForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Authorizations``. To unmap an
    ``Authorization`` from the current ``Vault,`` the
    ``AuthorizationVaultAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Authorization`` itself thus
    removing it from all known ``Vault`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_create_authorizations(self):
        """Tests if this user can create ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Authorization`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_authorization_with_record_types(self, authorization_record_types):
        """Tests if this user can create a single ``Authorization`` using the desired record types.

        While ``AuthorizationManager.getAuthorizationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Authorization``. Providing an empty array tests if an
        ``Authorization`` can be created with no records.

        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Authorization`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_form_for_create_for_agent(self, agent_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param agent_id: the agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: the function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``agent_id, function_id`` or ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id, function_id, qualifier_id`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationForm

    @abc.abstractmethod
    def get_authorization_form_for_create_for_resource(self, resource_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: the function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``resource_id, function_id`` or ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id, function_id, qualifier_id,`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationForm

    @abc.abstractmethod
    def get_authorization_form_for_create_for_resource_and_trust(self, resource_id, trust_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param trust_id: an ``Id`` for a circle of trust
        :type trust_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``resource_id, trust_id, function_id`` , or ``qualifierid`` is not found
        :raise: ``NullArgument`` -- ``resource_id, trust_id`` , ``resource_id, qualifier_id`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationForm

    @abc.abstractmethod
    def create_authorization(self, authorization_form):
        """Creates a new explicit ``Authorization``.

        :param authorization_form: the authorization form
        :type authorization_form: ``osid.authorization.AuthorizationForm``
        :return: ``t`` he new ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- ``authorization_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``authorization_form`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_form`` did not originate from this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Authorization

    @abc.abstractmethod
    def can_update_authorizations(self):
        """Tests if this user can update ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if authorization modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_form_for_update(self, authorization_id):
        """Gets the authorization form for updating an existing authorization.

        A new authorization form should be requested for each update
        transaction.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationForm

    @abc.abstractmethod
    def update_authorization(self, authorization_form):
        """Updates an existing authorization.

        :param authorization_form: the authorization ``Id``
        :type authorization_form: ``osid.authorization.AuthorizationForm``
        :raise: ``IllegalState`` -- ``authorization_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``authorization_form`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_form`` did not originate from ``get_authorization_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_authorizations(self):
        """Tests if this user can delete ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_authorization(self, authorization_id):
        """Deletes the ``Authorization`` identified by the given ``Id``.

        :param authorization_id: the ``Id`` of the ``Authorization`` to delete
        :type authorization_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Authorization`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_authorization_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_authorization(self, authorization_id, alias_id):
        """Adds an ``Id`` to an ``Authorization`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Authorization`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another authorization. it
        is reassigned to the given authorization ``Id``.

        :param authorization_id: the ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``authorization_id`` not found
        :raise: ``NullArgument`` -- ``authorization_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AuthorizationNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Authorizations``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``AuthorizationLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_register_for_authorization_notifications(self):
        """Tests if this user can register for ``Authorization`` notifications.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for authorizations in
        this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_authorization_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_authorization_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_authorization_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_authorization_notification(self, notification_id):
        """Acknowledge an authorization notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.

        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.

        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_authorizations(self):
        """Register for notifications of new authorizations.

        ``AuthorizationReceiver.newAuthorizations()`` is invoked when a
        new ``Authorization`` appears in this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_authorizations_for_resource(self, resource_id):
        """Registers for notification of new authorizations for the given resource including any authorizations related to the resource through an agent.

        ``AuthorizationReceiver.newAuthorizations()`` is invoked when an
        authorization appears in this vault.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_authorizations_for_function(self, function_id):
        """Register for notifications of new authorizations for the given function.

        ``AuthorizationReceiver.newAuthorizations()`` is invoked when a
        new ``Authorization`` appears in this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_authorizations(self):
        """Registers for notification of updated authorizations.

        ``AuthorizationReceiver.changedAuthorizations()`` is invoked
        when an authorization in this vault is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_authorizations_for_resource(self, resource_id):
        """Registers for notification of updated authorizations for the given resource including any authorizations related to the resource through an agent.

        ``AuthorizationReceiver.changedAuthorizations()`` is invoked
        when an authorization in this vault is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_authorizations_for_function(self, function_id):
        """Registers for notification of updated authorizations for the given function.

        ``AuthorizationReceiver.changedAuthorizations()`` is invoked
        when an authorization in this vault is changed.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_authorization(self, authorization_id):
        """Registers for notification of an updated authorization.

        ``AuthorizationReceiver.changedAuthorizations()`` is invoked
        when the specified authorization in this vault is changed.

        :param authorization_id: the ``Id`` of the ``Authorization`` to monitor
        :type authorization_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_authorizations(self):
        """Registers for notification of deleted authorizations.

        ``AuthorizationReceiver.deletedAuthorizations()`` is invoked
        when an authorization is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_authorizations_for_resource(self, resource_id):
        """Registers for notification of deleted authorizations for the given resource including any authorizations related to the resource through an agent.

        ``AuthorizationReceiver.deletedAuthorizations()`` is invoked
        when an authorization is removed from this vault.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_authorizations_for_function(self, function_id):
        """Registers for notification of deleted authorizations for the given function.

        ``AuthorizationReceiver.deletedAuthorizations()`` is invoked
        when an authorization is removed from this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_authorization(self, authorization_id):
        """Registers for notification of a deleted authorization.

        ``AuthorizationReceiver.deletedAuthorizations()`` is invoked
        when the specified authorization is removed from this vault.

        :param authorization_id: the ``Id`` of the ``Authorization`` to monitor
        :type authorization_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_authorization_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_authorization_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_authorization_notification(self, notification_id):
        """Acknowledge an authorization notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AuthorizationVaultSession:
    """This session provides methods to retrieve ``Authorization`` to ``Vault`` mappings.

    An ``Authorization`` may appear in multiple ``Vaults``. Each
    ``Vault`` may have its own authorizations governing who is allowed
    to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_vault_view(self):
        """A complete view of the ``Authorization`` and ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_lookup_authorization_vault_mappings(self):
        """Tests if this user can perform lookups of authorization/vault mappings.

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
    def get_authorization_ids_by_vault(self, vault_id):
        """Gets the list of ``Authorization``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related authorization ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_authorizations_by_vault(self, vault_id):
        """Gets the list of ``Authorizations`` associated with a ``Vault``.

        :param vault_id: ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related authorization
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_authorizations_ids_by_vault(self, vault_ids):
        """Gets the list of ``Authorization Ids`` corresponding to a list of ``Vault`` objects.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of authorization ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_authorizations_by_vault(self, vault_ids):
        """Gets the list of ``Authorizations`` corresponding to a list of ``Vault``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of authorizations
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationList

    @abc.abstractmethod
    def get_vault_ids_by_authorization(self, authorization_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to an ``Authorization``.

        :param authorization_id: ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_vault_by_authorization(self, authorization_id):
        """Gets the list of ``Vault`` objects mapped to an ``Authorization``.

        :param authorization_id: ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList


class AuthorizationVaultAssignmentSession:
    """This session provides methods to re-assign ``Authorizations`` to ``Vault``.

    An ``Authorization`` may map to multiple ``Vault`` objects and
    removing the last reference to a ``Authorization`` is the equivalent
    of deleting it. Each ``Vault`` may have its own authorizations
    governing who is allowed to operate on it.

    Moving or adding a reference of a ``Authorization`` to another
    ``Vault`` is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_authorizations(self):
        """Tests if this user can alter authorization/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_authorizations_to_vault(self, vault_id):
        """Tests if this user can alter authorization/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_vault_ids(self, vault_id):
        """Gets a list of vault including and under the given vault node in which any authorization can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_vault_ids_for_authorization(self, vault_id, authorization_id):
        """Gets a list of vault including and under the given vault node in which a specific authorization can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_authorization_to_vault(self, authorization_id, vault_id):
        """Adds an existing ``Authorization`` to a ``Vault``.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``authorization_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``authorization_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_authorization_from_vault(self, authorization_id, vault_id):
        """Removes an ``Authorization`` from a ``Vault``.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``authorization_id`` or ``vault_id`` not found or ``authorization_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``authorization_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_authorization_to_vault(self, authorization_id, from_vault_id, to_vault_id):
        """Moves an ``Authorization`` from one ``Vault`` to another.

        Mappings to other ``Vaults`` are unaffected.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param from_vault_id: the ``Id`` of the current ``Vault``
        :type from_vault_id: ``osid.id.Id``
        :param to_vault_id: the ``Id`` of the destination ``Vault``
        :type to_vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``authorization_id, from_vault_id,`` or ``to_vault_id`` not found or ``authorization_id`` not mapped to ``from_vault_id``
        :raise: ``NullArgument`` -- ``authorization_id, from_vault_id,`` or ``to_vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AuthorizationSmartVaultSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``AuthorizationQuery`` can be retrieved from this session and
    mapped to this ``Vault`` to create a virtual collection of
    ``Authorizations``. The authorizations may be sequenced using the
    ``AuthorizationSearchOrder`` from this session.

    This ``Vault`` has a default query that matches any authorization
    and a default search order that specifies no sequencing. The queries
    may be examined using a ``AuthorizationQueryInspector``. The query
    may be modified by converting the inspector back to a
    ``AuthorizationQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_manage_smart_vault(self):
        """Tests if this user can manage smart vault.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart vault management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authorization_query(self):
        """Gets a authorization query.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    @abc.abstractmethod
    def get_authorization_search_order(self):
        """Gets a authorization search order.

        :return: the authorization search order.
        :rtype: ``osid.authorization.AuthorizationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationSearchOrder

    authorization_search_order = property(fget=get_authorization_search_order)

    @abc.abstractmethod
    def apply_authorization_query(self, authorization_query):
        """Applies a authorization query to this vault.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :raise: ``NullArgument`` -- ``authorization_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``authorization_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_authorization_query(self):
        """Gets a authorization query inspector for this vault.

        :return: the authorization query inspector
        :rtype: ``osid.authorization.AuthorizationQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQueryInspector

    @abc.abstractmethod
    def apply_authorization_sequencing(self, authorization_search_order):
        """Applies a authorization search order to this vault.

        :param authorization_search_order: the authorization search order
        :type authorization_search_order: ``osid.authorization.AuthorizationSearchOrder``
        :raise: ``NullArgument`` -- ``authorization_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``authorization_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_authorization_query_from_inspector(self, authorization_query_inspector):
        """Gets a authorization query from an inspector.

        :param authorization_query_inspector: a resorce relationship query inspector
        :type authorization_query_inspector: ``osid.authorization.AuthorizationQueryInspector``
        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``NullArgument`` -- ``authorization_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``authorization_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.AuthorizationQuery


class FunctionLookupSession:
    """This session provides methods for retrieving ``Function`` objects."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_lookup_functions(self):
        """Tests if this user can perform ``Function`` lookups.

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
    def use_comparative_function_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_function_view(self):
        """A complete view of the ``Function`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include functions in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_active_function_view(self):
        """Only active functions are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_function_view(self):
        """Active and inactive functions are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_function(self, function_id):
        """Gets the ``Function`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Function`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Function`` and retained for
        compatibility.

        :param function_id: the ``Id`` of the ``Function`` to retrieve
        :type function_id: ``osid.id.Id``
        :return: the returned ``Function``
        :rtype: ``osid.authorization.Function``
        :raise: ``NotFound`` -- no ``Function`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Function

    @abc.abstractmethod
    def get_functions_by_ids(self, function_ids):
        """Gets a ``FunctionList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the functions
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Functions`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param function_ids: the list of ``Ids`` to retrieve
        :type function_ids: ``osid.id.IdList``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``function_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_functions_by_genus_type(self, function_genus_type):
        """Gets a ``FunctionList`` corresponding to the given function genus ``Type`` which does not include functions of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_genus_type: a function genus type
        :type function_genus_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_functions_by_parent_genus_type(self, function_genus_type):
        """Gets a ``FunctionList`` corresponding to the given function genus ``Type`` and include any additional functions with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_genus_type: a function genus type
        :type function_genus_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_functions_by_record_type(self, function_record_type):
        """Gets a ``FunctionList`` containing the given function record ``Type``.

        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_record_type: a function record type
        :type function_record_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_functions(self):
        """Gets all ``Functions``.

        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :return: a list of ``Functions``
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    functions = property(fget=get_functions)


class FunctionQuerySession:
    """This session provides methods for searching ``Function`` objects.

    The search query is constructed using the ``FunctionQuery``. The
    function record ``Type`` also specifies the query record for the
    function query.

    This session defines views that offer differing behaviors for
    searching.

      * federated vault view: searches include functions in vaults of
        which this vault is a ancestor in the vault hierarchy
      * isolated vault view: searches are restricted to functions in
        this vault


    Functions may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``FunctionQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_search_functions(self):
        """Tests if this user can perform ``Function`` searches.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include functions in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_function_query(self):
        """Gets a function query.

        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQuery

    function_query = property(fget=get_function_query)

    @abc.abstractmethod
    def get_functions_by_query(self, function_query):
        """Gets a list of ``Functions`` matching the given query.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :return: the returned ``FunctionList``
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList


class FunctionSearchSession:
    """This session provides methods for searching ``Function`` objects.

    The search query is constructed using the ``FunctionQuery``. The
    function record ``Type`` also specifies the record for the function
    query.

    ``get_functions_by_query()`` is the basic search method and returns
    a list of ``Functions``. A more advanced search may be performed
    with ``getFunctionsBySearch()``. It accepts a ``FunctionSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_functions_by_search()`` returns an ``FunctionSearchResults``
    that can be used to access the resulting ``FunctionList`` or be used
    to perform a search within the result set through
    ``FunctionSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated vault view: searches include functions in vaults of
        which this vault is a ancestor in the vault hierarchy
      * isolated vault view: searches are restricted to functions in
        this vault


    Functions may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``FunctionQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_function_search(self):
        """Gets a function search.

        :return: the function search
        :rtype: ``osid.authorization.FunctionSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionSearch

    function_search = property(fget=get_function_search)

    @abc.abstractmethod
    def get_function_search_order(self):
        """Gets a function search order.

        The ``FunctionSearchOrder`` is supplied to a ``FunctionSearch``
        to specify the ordering of results.

        :return: the function search order
        :rtype: ``osid.authorization.FunctionSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionSearchOrder

    function_search_order = property(fget=get_function_search_order)

    @abc.abstractmethod
    def get_functions_by_search(self, function_query, function_search):
        """Gets the search results matching the given search query using the given search.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :param function_search: the function search
        :type function_search: ``osid.authorization.FunctionSearch``
        :return: the returned search results
        :rtype: ``osid.authorization.FunctionSearchResults``
        :raise: ``NullArgument`` -- ``function_query`` or ``function_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_search`` or ``function_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionSearchResults

    @abc.abstractmethod
    def get_function_query_from_inspector(self, function_query_inspector):
        """Gets a function query from an inspector.

        The inspector is available from a ``FunctionSearchResults``.

        :param function_query_inspector: a function query inspector
        :type function_query_inspector: ``osid.authorization.FunctionQueryInspector``
        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``
        :raise: ``NullArgument`` -- ``function_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``function_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQuery


class FunctionAdminSession:
    """This session creates, updates, and deletes ``Functions``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Function,`` a ``FunctionForm`` is requested using
    ``get_function_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``FunctionForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``FunctionForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``FunctionForm`` corresponds to an attempted
    transaction.

    For updates, ``FunctionForms`` are requested to the ``Function``
    ``Id`` that is to be updated using ``getFunctionFormForUpdate()``.
    Similarly, the ``FunctionForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``FunctionForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Functions``. To unmap a ``Function``
    from the current ``Vault,`` the ``FunctionVaultAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Function`` itself thus removing it from all known ``Vault``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the vault
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_create_functions(self):
        """Tests if this user can create ``Functions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Function`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_function_with_record_types(self, function_record_types):
        """Tests if this user can create a single ``Function`` using the desired record types.

        While ``AuthorizationManager.getFunctionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Function``. Providing an empty array tests if a ``Function``
        can be created with no records.

        :param function_record_types: array of function record types
        :type function_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Function`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_form_for_create(self, function_record_types):
        """Gets the function form for creating new functions.

        A new form should be requested for each create transaction.

        :param function_record_types: array of function record types
        :type function_record_types: ``osid.type.Type[]``
        :return: the function form
        :rtype: ``osid.authorization.FunctionForm``
        :raise: ``NullArgument`` -- ``function_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionForm

    @abc.abstractmethod
    def create_function(self, function_form):
        """Creates a new ``Function``.

        :param function_form: the form for this ``Function``
        :type function_form: ``osid.authorization.FunctionForm``
        :return: the new ``Function``
        :rtype: ``osid.authorization.Function``
        :raise: ``IllegalState`` -- ``function_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``function_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_form`` did not originate from ``get_function_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Function

    @abc.abstractmethod
    def can_update_functions(self):
        """Tests if this user can update ``Functions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if function modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_form_for_update(self, function_id):
        """Gets the function form for updating an existing function.

        A new function form should be requested for each update
        transaction.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :return: the function form
        :rtype: ``osid.authorization.FunctionForm``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionForm

    @abc.abstractmethod
    def update_function(self, function_form):
        """Updates an existing function.

        :param function_form: the form containing the elements to be updated
        :type function_form: ``osid.authorization.FunctionForm``
        :raise: ``IllegalState`` -- ``function_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``function_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_form`` did not originate from ``get_function_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_functions(self):
        """Tests if this user can delete ``Functions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Function`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_function(self, function_id):
        """Deletes the ``Function`` identified by the given ``Id``.

        :param function_id: the ``Id`` of the ``Function`` to delete
        :type function_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Function`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_function_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Functions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Function`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_function(self, function_id, alias_id):
        """Adds an ``Id`` to a ``Function`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Function`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another function, it is
        reassigned to the given function ``Id``.

        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``function_id`` not found
        :raise: ``NullArgument`` -- ``function_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FunctionNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Function`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``FunctionLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_register_for_function_notifications(self):
        """Tests if this user can register for ``Function`` notifications.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include functions in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_function_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_function_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_function_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_function_notification(self, notification_id):
        """Acknowledge a function notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_functions(self):
        """Register for notifications of new functions.

        ``FunctionReceiver.newFunctions()`` is invoked when a new
        Function is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_functions(self):
        """Registers for notification of updated functions.

        ``FunctionReceiver.changedFunctions()`` is invoked when a
        function is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_function(self, function_id):
        """Registers for notification of an updated function.

        ``FunctionReceiver.changedFunctions()`` is invoked when the
        specified function is changed.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_functions(self):
        """Registers for notification of deleted functions.

        ``FunctionReceiver.deletedFunctions()`` is invoked when a
        function is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_function(self, function_id):
        """Registers for notification of a deleted function.

        ``FunctionReceiver.changedFunctions()`` is invoked when the
        specified function is removed from this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_function_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_function_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_function_notification(self, notification_id):
        """Acknowledge an function notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FunctionVaultSession:
    """This session provides methods to retrieve ``Function`` to ``Vault`` mappings.

    A ``Function`` may appear in multiple ``Vaults``. Each ``Vault`` may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_function_vault_mappings(self):
        """Tests if this user can perform lookups of function/vault mappings.

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
    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_vault_view(self):
        """A complete view of the ``Function`` and ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_function_ids_by_vault(self, vault_id):
        """Gets the list of ``Function``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related function ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_functions_by_vault(self, vault_id):
        """Gets the list of ``Functions`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related functions
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_function_ids_by_vaults(self, vault_ids):
        """Gets the list of ``Function Ids`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of function ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_functions_by_vaults(self, vault_ids):
        """Gets the list of ``Functions`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of functions
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionList

    @abc.abstractmethod
    def get_vault_ids_by_function(self, function_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to a ``Function``.

        :param function_id: ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_vaults_by_function(self, function_id):
        """Gets the list of ``Vaults`` mapped to a ``Function``.

        :param function_id: ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList


class FunctionVaultAssignmentSession:
    """This session provides methods to re-assign ``Functions`` to ``Vaults``.

    A ``Function`` may map to multiple ``Vaults`` and removing the last
    reference to a ``Function`` is the equivalent of deleting it. Each
    ``Vault`` may have its own authorizations governing who is allowed
    to operate on it.

    Adding a reference of a ``Function`` to another ``Vault`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_functions(self):
        """Tests if this user can alter function/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_functions_to_vault(self, vault_id):
        """Tests if this user can alter function/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_vault_ids(self, vault_id):
        """Gets a list of vault including and under the given vault node in which any function can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_vault_ids_for_function(self, vault_id, function_id):
        """Gets a list of vault including and under the given vault node in which a specific function can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_function_to_vault(self, function_id, vault_id):
        """Adds an existing ``Function`` to a ``Vault``.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``function_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``function_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_function_from_vault(self, function_id, vault_id):
        """Removes a ``Function`` from a ``Vault``.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``function_id`` or ``vault_id`` not found or ``function_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``function_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_function_to_vault(self, function_id, from_vault_id, to_vault_id):
        """Moves a ``Function`` from one ``Vault`` to another.

        Mappings to other ``Vaults`` are unaffected.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :param from_vault_id: the ``Id`` of the current ``Vault``
        :type from_vault_id: ``osid.id.Id``
        :param to_vault_id: the ``Id`` of the destination ``Vault``
        :type to_vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``function_id, from_vault_id,`` or ``to_vault_id`` not found or ``function_id`` not mapped to ``from_vault_id``
        :raise: ``NullArgument`` -- ``function_id, from_vault_id,`` or ``to_vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class FunctionSmartVaultSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``FunctionQuery`` can be retrieved from this session and mapped to
    this ``Vault`` to create a virtual collection of ``Functions``. The
    functions may be sequenced using the ``FunctionSearchOrder`` from
    this session.

    This ``Vault`` has a default query that matches any function and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``FunctionQueryInspector``. The query may be
    modified by converting the inspector back to a ``FunctionQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_manage_smart_vaults(self):
        """Tests if this user can manage smart vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart vault management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_query(self):
        """Gets a function query.

        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQuery

    function_query = property(fget=get_function_query)

    @abc.abstractmethod
    def get_function_search_order(self):
        """Gets a function search order.

        :return: the function search order
        :rtype: ``osid.authorization.FunctionSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionSearchOrder

    function_search_order = property(fget=get_function_search_order)

    @abc.abstractmethod
    def apply_function_query(self, function_query):
        """Applies a function query to this vault.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :raise: ``NullArgument`` -- ``function_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``function_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_function_query(self):
        """Gets a function query inspector for this vault.

        :return: the function query inspector
        :rtype: ``osid.authorization.FunctionQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQueryInspector

    @abc.abstractmethod
    def apply_function_sequencing(self, function_search_order):
        """Applies a function search order to this vault.

        :param function_search_order: the function search order
        :type function_search_order: ``osid.authorization.FunctionSearchOrder``
        :raise: ``NullArgument`` -- ``function_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``function_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_function_query_from_inspector(self, function_query_inspector):
        """Gets a function query from an inspector.

        :param function_query_inspector: a function query inspector
        :type function_query_inspector: ``osid.authorization.FunctionQueryInspector``
        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``
        :raise: ``NullArgument`` -- ``function_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``function_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.FunctionQuery


class QualifierLookupSession:
    """This session defines methods for retrieving qualifiers."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_lookup_qualifiers(self):
        """Tests if this user can perform ``Qualifier`` lookups.

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
    def use_comparative_qualifier_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_qualifier_view(self):
        """A complete view of the ``Qualifier`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include qualifiers in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_qualifier(self, qualifier_id):
        """Gets the ``Qualifier`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Qualifier`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Qualifier`` and retained
        for compatibility.

        :param qualifier_id: ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: the qualifier
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authorization.Qualifier

    @abc.abstractmethod
    def get_qualifiers_by_ids(self, qualifier_ids):
        """Gets a ``QualifierList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        qualifiers specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Qualifiers`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param qualifier_ids: the list of ``Ids`` to retrieve
        :type qualifier_ids: ``osid.id.IdList``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``qualifier_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_qualifiers_by_genus_type(self, qualifier_genus_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier genus ``Type`` which does not include qualifiers of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.
        In both cases, the order of the set is not specified.

        :param qualifier_genus_type: a qualifier genus type
        :type qualifier_genus_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_qualifiers_by_parent_genus_type(self, qualifier_genus_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier genus ``Type`` and include any additional qualifiers with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.

        :param qualifier_genus_type: a qualifier genus type
        :type qualifier_genus_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_qualifiers_by_record_type(self, qualifier_record_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier record ``Type``.

        The set of qualifiers implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        qualifiers or an error results. Otherwise, the returned list may
        contain only those qualifiers that are accessible through this
        session.

        :param qualifier_record_type: a qualifier record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_qualifiers(self):
        """Gets all ``Qualifiers``.

        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.

        :return: a list of ``Qualifiers``
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    qualifiers = property(fget=get_qualifiers)


class QualifierQuerySession:
    """This session provides methods for searching among ``Qualifier`` objects.

    The search query is constructed using the ``QualifierQuery``. If
    more than one search element is specified within a single
    ``QualifierQuery,`` these elements form a boolean AND.

    This session defines views that offer differing behaviors for
    searching.

      * federated vault view: searches include qualifiers in vaults of
        which this vault is an ancestor in the vault hierarchy
      * isolated vault view: searches are restricted to qualifiers in
        this vault


    Qualifiers may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``QualifierQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_search_qualifiers(self):
        """Tests if this user can perform ``Qualifier`` searches.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include qualifiers in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_qualifier_query(self):
        """Gets a qualifier query.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQuery

    qualifier_query = property(fget=get_qualifier_query)

    @abc.abstractmethod
    def get_qualifiers_by_query(self, qualifier_query):
        """Gets a list of ``Qualifiers`` matching the given search.

        :param qualifier_query: the search query array
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :return: the returned ``QualifierList``
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList


class QualifierSearchSession:
    """This session provides methods for searching among ``Qualifier`` objects.

    The search query is constructed using the ``QualifierQuery``. If
    more than one search element is specified within a single
    ``QualifierQuery,`` these elements form a boolean AND.

    ``get_qualifiers_by_query()`` is the basic search method and returns
    a list of ``Qualifiers``. A more advanced search may be performed
    with ``getQualifiersBySearch()``. It accepts a ``QualifierSearch``
    in addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_qualifiers_by_search()`` returns a ``QualifierSearchResults``
    that can be used to access the resulting ``QualifierList`` or be
    used to perform a search within the result set through
    ``QualifierSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated vault view: searches include qualifiers in vaults of
        which this vault is an ancestor in the vault hierarchy
      * isolated vault view: searches are restricted to qualifiers in
        this vault


    Qualifiers may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``QualifierQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_search(self):
        """Gets a qualifier search.

        :return: the qualifier search
        :rtype: ``osid.authorization.QualifierSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierSearch

    qualifier_search = property(fget=get_qualifier_search)

    @abc.abstractmethod
    def get_qualifier_search_order(self):
        """Gets a qualifier search order.

        The ``QualifierSearchOrder`` is supplied to a
        ``QualifierSearch`` to specify the ordering of results.

        :return: the qualifier search order
        :rtype: ``osid.authorization.QualifierSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierSearchOrder

    qualifier_search_order = property(fget=get_qualifier_search_order)

    @abc.abstractmethod
    def get_qualifiers_by_search(self, qualifier_query, qualifier_search):
        """Gets the search results matching the given search query using the given search.

        :param qualifier_query: the qualifier query
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :param qualifier_search: the qualifier search
        :type qualifier_search: ``osid.authorization.QualifierSearch``
        :return: the search results
        :rtype: ``osid.authorization.QualifierSearchResults``
        :raise: ``NullArgument`` -- ``qualifier_queriy`` or ``qualifier_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_query`` or ``qualifier_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierSearchResults

    @abc.abstractmethod
    def get_qualifier_query_from_inspector(self, qualifier_query_inspector):
        """Gets a qualifier query from an inspector.

        The inspector is available from a ``QualifierSearchResults``.

        :param qualifier_query_inspector: a qualifier query inspector
        :type qualifier_query_inspector: ``osid.authorization.QualifierQueryInspector``
        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``NullArgument`` -- ``qualifier_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``qualifier_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQuery


class QualifierAdminSession:
    """This session creates, updates, and deletes ``Qualifiers``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Qualifier,`` a ``QualifierForm`` is requested using
    ``get_qualifier_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``QualifierForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``QualifierForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``QualifierForm`` corresponds to an attempted
    transaction.

    For updates, ``QualifierForms`` are requested to the ``Qualifier``
    ``Id`` that is to be updated using ``getQualifierFormForUpdate()``.
    Similarly, the ``QualifierForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``QualifierForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Qualifiers``. To unmap a
    ``Qualifier`` from the current ``Vault,`` the
    ``QualifierVaultAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Qualifier`` itself thus removing
    it from all known ``Vault`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_create_qualifiers(self):
        """Tests if this user can create ``Qualifiers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_qualifier_with_record_types(self, qualifier_record_types):
        """Tests if this user can create a single ``Qualifier`` using the desired record types.

        While ``AuthorizationManager.getQualifierRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Qualifier``. Providing an empty array tests if a ``Qualifier``
        can be created with no records.

        :param qualifier_record_types: array of qualifier record types
        :type qualifier_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Qualifier`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_form_for_create(self, qualifier_record_types):
        """Gets the qualifier form for creating new qualifiers.

        A new form should be requested for each create transaction.

        :param qualifier_record_types: array of qualifier record types
        :type qualifier_record_types: ``osid.type.Type[]``
        :return: the qualifier form
        :rtype: ``osid.authorization.QualifierForm``
        :raise: ``NullArgument`` -- ``qualifier_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierForm

    @abc.abstractmethod
    def create_qualifier(self, qualifier_form):
        """Creates a new ``Qualifier``.

        :param qualifier_form: the form for this ``Qualifier``
        :type qualifier_form: ``osid.authorization.QualifierForm``
        :return: the new ``Qualifier``
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``IllegalState`` -- ``qualifier_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``qualifier_forms`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_form`` did not originate from ``get_qualifier_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Qualifier

    @abc.abstractmethod
    def can_update_qualifiers(self):
        """Tests if this user can update ``Qualifiers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_form_for_update(self, qualifier_id):
        """Gets the qualifier form for updating an existing qualifier.

        A new qualifier form should be requested for each update
        transaction.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: the qualifier form
        :rtype: ``osid.authorization.QualifierForm``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierForm

    @abc.abstractmethod
    def update_qualifier(self, qualifier_form):
        """Updates an existing qualifier.

        :param qualifier_form: the form containing the elements to be updated
        :type qualifier_form: ``osid.authorization.QualifierForm``
        :raise: ``IllegalState`` -- ``qualifier_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``qualifier_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_form`` did not originate from ``get_qualifier_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_qualifiers(self):
        """Tests if this user can delete ``Qualifiers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_qualifier(self, qualifier_id):
        """Deletes a ``Qualifier``.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to remove
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_qualifier_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Qualifiers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_qualifier(self, qualifier_id, alias_id):
        """Adds an ``Id`` to a ``Qualifier`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Qualifier`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another qualifier, it is
        reassigned to the given qualifier ``Id``.

        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class QualifierNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Qualifier`` objects in this ``Vault``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``QualifierLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_register_for_qualifier_notifications(self):
        """Tests if this user can register for ``Qualifier`` notifications.

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
    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for qualifiers in
        vaults which are children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for qualifiers to this
        vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_qualifier_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_qualifier_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_qualifier_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_qualifier_notification(self, notification_id):
        """Acknowledge a qualifier notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_qualifiers(self):
        """Register for notifications of new qualifiers.

        ``QualifierReceiver.newQualifiers()`` is invoked when a new
        ``Qualifier`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_qualifiers(self):
        """Registers for notification of updated qualifiers.

        ``QualifierReceiver.changedQualifiers()`` is invoked when a
        qualifier is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_qualifier(self, qualifier_id):
        """Registers for notification of an updated qualifier.

        ``QualifierReceiver.changedQualifiers()`` is invoked when the
        specified qualifier is changed.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_qualifiers(self):
        """Registers for notification of deleted qualifiers.

        ``QualifierReceiver.deletedQualifiers()`` is invoked when a
        qualifier is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_qualifier(self, qualifier_id):
        """Registers for notification of a deleted qualifier.

        ``QualifierReceiver.deletedQualifiers()`` is invoked when the
        specified qualifier is removed from this vault.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_qualifier_hierarchy(self):
        """Registers for notification of an updated qualifier hierarchy structure.

        ``QualifierReceiver.changedChildOfQualfiers()`` is invoked when
        a node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_qualifier_hierarchy_for_ancestors(self, qualifier_id):
        """Registers for notification of an updated qualifier hierarchy structure.

        ``QualifierReceiver.changedChildOfQualifiers()`` is invoked when
        the specified node or any of its ancestors experiences a change
        in its children.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` node to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_qualifier_hierarchy_for_descendants(self, qualifier_id):
        """Registers for notification of an updated qualifier hierarchy structure.

        ``QualifierReceiver.changedChildOfQualifiers()`` is invoked when
        the specified node or any of its descendants experiences a
        change in its children.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` node to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_qualifier_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_qualifier_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_qualifier_notification(self, notification_id):
        """Acknowledge an qualifier notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class QualifierHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Qualifier`` objects.

    Each node in the hierarchy is a unique ``Qualifier``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_qualifiers()`` and ``getChildQualifiers()``. To relate
    these ``Ids`` to another OSID, ``get_qualifier_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Qualifier`` available in the Authorization OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_qualifiers()`` or ``get_child_qualifiers()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: qualifier elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    @abc.abstractmethod
    def get_qualifier_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    @abc.abstractmethod
    def can_access_qualifier_hierarchy(self):
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
    def use_comparative_qualifier_view(self):
        """The returns from the qualifier methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_qualifier_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_qualifier_ids(self):
        """Gets the root qualifier ``Ids`` in this hierarchy.

        :return: the root qualifier ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_qualifier_ids = property(fget=get_root_qualifier_ids)

    @abc.abstractmethod
    def get_root_qualifiers(self):
        """Gets the root qualifiers in this qualifier hierarchy.

        :return: the root qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authorization.QualifierList

    root_qualifiers = property(fget=get_root_qualifiers)

    @abc.abstractmethod
    def has_parent_qualifiers(self, qualifier_id):
        """Tests if the ``Qualifier`` has any parents.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the qualifier has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is a direct parent of qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_qualifier_ids(self, qualifier_id):
        """Gets the parent ``Ids`` of the given qualifier.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the qualifier
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_qualifiers(self, qualifier_id):
        """Gets the parents of the given qualifier.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the parents of the qualifier
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def is_ancestor_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is an ancestor of a qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_qualifiers(self, qualifier_id):
        """Tests if a qualifier has any children.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``qualifier_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_qualifier(self, id_, qualifier_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_qualifier_ids(self, qualifier_id):
        """Gets the child ``Ids`` of the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :return: the children of the qualifier
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_qualifiers(self, qualifier_id):
        """Gets the children of the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :return: the children of the qualifier
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def is_descendant_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is a descendant of a qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_node_ids(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a qualifier node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_qualifier_nodes(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a qualifier node
        :rtype: ``osid.authorization.QualifierNode``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierNode


class QualifierHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Qualifier`` objects.

    Each node in the hierarchy is a unique ``Qualifier``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    @abc.abstractmethod
    def get_qualifier_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    @abc.abstractmethod
    def can_modify_qualifier_hierarchy(self):
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
    def add_root_qualifier(self, qualifier_id):
        """Adds a root qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_qualifier(self, qualifier_id):
        """Removes a root qualifier from this hierarchy.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_qualifier(self, qualifier_id, child_id):
        """Adds a child to a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_qualifier(self, qualifier_id, child_id):
        """Removes a child from a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_qualifiers(self, qualifier_id):
        """Removes all children from a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class QualifierVaultSession:
    """This session provides methods to retrieve ``Qualifier`` to ``Vault`` mappings.

    A ``Qualifier`` may appear in multiple ``Vaults``. Each ``Vault``
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_qualifier_vault_mappings(self):
        """Tests if this user can perform lookups of qualifier/vault mappings.

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
    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_vault_view(self):
        """A complete view of the ``Qualifier`` and ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_qualifier_ids_by_vault(self, vault_id):
        """Gets the list of ``Qualifier``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related qualifier ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_qualifiers_by_vault(self, vault_id):
        """Gets the list of ``Qualifier`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_qualifier_ids_by_vaults(self, vault_ids):
        """Gets the list of ``Qualifier Ids`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_qualifiers_by_vaults(self, vault_ids):
        """Gets the list of ``Qualifiers`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierList

    @abc.abstractmethod
    def get_vault_ids_by_qualifier(self, qualifier_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to a ``Qualifier``.

        :param qualifier_id: ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_vaults_by_qualifier(self, qualifier_id):
        """Gets the list of ``Vaults`` mapped to a ``Qualifier``.

        :param qualifier_id: ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList


class QualifierVaultAssignmentSession:
    """This session provides methods to re-assign ``Qualifiers`` to ``Vaults``.

    A ``Qualifier`` may map to multiple ``Vaults`` and removing the last
    reference to a ``Qualifier`` is the equivalent of deleting it. Each
    ``Vault`` may have its own authorizations governing who is allowed
    to operate on it.

    Adding a reference of a ``Qualifier`` to another ``Vault`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_qualifiers(self):
        """Tests if this user can alter qualifier/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_qualifiers_to_vault(self, vault_id):
        """Tests if this user can alter qualifier/vault mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_vault_ids(self, vault_id):
        """Gets a list of vault including and under the given vault node in which any qualifier can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_vault_ids_for_qualifier(self, vault_id, qualifier_id):
        """Gets a list of vault including and under the given vault node in which a specific qualifier can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_qualifier_to_vault(self, qualifier_id, vault_id):
        """Adds an existing ``Qualifier`` to a ``Vault``.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_qualifier_from_vault(self, qualifier_id, vault_id):
        """Removes a ``Qualifier`` from a ``Vault``.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``vault_id`` not found or ``qualifier_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_qualifier_to_vault(self, qualifier_id, from_vault_id, to_vault_id):
        """Moves a ``Qualifier`` from one ``Vault`` to another.

        Mappings to other ``Vaults`` are unaffected.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param from_vault_id: the ``Id`` of the current ``Vault``
        :type from_vault_id: ``osid.id.Id``
        :param to_vault_id: the ``Id`` of the destination ``Vault``
        :type to_vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualfiier_id, from_vault_id,`` or ``to_vault_id`` not found or ``qualfiier_id,`` not mapped to ``from_vault_id``
        :raise: ``NullArgument`` -- ``qualfiier_id,, from_vault_id,`` or ``to_vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class QualifierSmartVaultSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``QualifierQuery`` can be retrieved from this session and mapped
    to this ``Vault`` to create a virtual collection of ``Qualifiers``.
    The qualifiers may be sequenced using the ``QualifierSearchOrder``
    from this session.

    This ``Vault`` has a default query that matches any qualifier and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``QualifierQueryInspector``. The query may be
    modified by converting the inspector back to a ``QualifierQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_id = property(fget=get_vault_id)

    @abc.abstractmethod
    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    vault = property(fget=get_vault)

    @abc.abstractmethod
    def can_manage_smart_vaults(self):
        """Tests if this user can manage smart vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart vault management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_query(self):
        """Gets a qualifier query.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQuery

    qualifier_query = property(fget=get_qualifier_query)

    @abc.abstractmethod
    def get_qualifier_search_order(self):
        """Gets a qualifier search order.

        :return: the qualifier search order
        :rtype: ``osid.authorization.QualifierSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierSearchOrder

    qualifier_search_order = property(fget=get_qualifier_search_order)

    @abc.abstractmethod
    def apply_qualifier_query(self, qualifier_query):
        """Applies a qualifier query to this vault.

        :param qualifier_query: the qualifier query
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :raise: ``NullArgument`` -- ``qualifier_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``qualifier_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_qualifier_query(self):
        """Gets a qualifier query inspector for this vault.

        :return: the qualifier query inspector
        :rtype: ``osid.authorization.QualifierQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQueryInspector

    @abc.abstractmethod
    def apply_qualifier_sequencing(self, qualifier_search_order):
        """Applies a qualifier search order to this vault.

        :param qualifier_search_order: the qualifier search order
        :type qualifier_search_order: ``osid.authorization.QualifierSearchOrder``
        :raise: ``NullArgument`` -- ``qualifier_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``qualifier_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_qualifier_query_from_inspector(self, qualifier_query_inspector):
        """Gets a qualifier query from an inspector.

        :param qualifier_query_inspector: a query inspector
        :type qualifier_query_inspector: ``osid.authorization.QualifierQueryInspector``
        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``NullArgument`` -- ``qualifier_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``qualifier_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.QualifierQuery


class VaultLookupSession:
    """This session provides methods for retrieving ``Vault`` objects.

    The ``Vault`` represents a collection of ``Functions`` and
    ``Authorizations``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Vaults`` it can access, without breaking execution.
    However, an administrative application may require all ``Vault``
    elements to be available.

    Vaults may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Vault``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_vaults(self):
        """Tests if this user can perform ``Vault`` lookups.

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
    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_vault(self, vault_id):
        """Gets the ``Vault`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Vault`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Vault`` and retained for compatibility.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault
        :rtype: ``osid.authorization.Vault``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authorization.Vault

    @abc.abstractmethod
    def get_vaults_by_ids(self, vault_ids):
        """Gets a ``VaultList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the vaults
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Vault`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param vault_ids: the list of ``Ids`` to retrieve
        :type vault_ids: ``osid.id.IdList``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def get_vaults_by_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` which does not include vaults of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` and include any additional vaults with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def get_vaults_by_record_type(self, vault_record_type):
        """Gets a ``VaultList`` containing the given vault record ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def get_vaults_by_provider(self, resource_id):
        """Gets a ``VaultList`` from the given provider ````.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def get_vaults(self):
        """Gets all ``Vaults``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :return: a ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    vaults = property(fget=get_vaults)


class VaultQuerySession:
    """This session provides methods for searching among ``Vault`` objects.

    The search query is constructed using the ``VaultQuery``.

    Vaults may have a query record indicated by their respective record
    types. The query record is accessed via the ``VaultQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_vaults(self):
        """Tests if this user can perform ``Vault`` searches.

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
    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    @abc.abstractmethod
    def get_vaults_by_query(self, vault_query):
        """Gets a list of ``Vault`` objects matching the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :return: the returned ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList


class VaultSearchSession:
    """This session provides methods for searching among ``Vault`` objects.

    The search query is constructed using the ``VaultQuery``.

    ``get_vaults_by_query()`` is the basic search method and returns a
    list of ``Vault`` objects.A more advanced search may be performed
    with ``getVaultsBySearch()``. It accepts a ``VaultSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_vaults_by_search()`` returns a ``VaultSearchResults`` that can
    be used to access the resulting ``VaultList`` or be used to perform
    a search within the result set through ``VaultSearch``.

    Vaults may have a query record indicated by their respective record
    types. The query record is accessed via the ``VaultQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_search(self):
        """Gets a vault search.

        :return: a vault search
        :rtype: ``osid.authorization.VaultSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultSearch

    vault_search = property(fget=get_vault_search)

    @abc.abstractmethod
    def get_vault_search_order(self):
        """Gets a vault search order.

        The ``VaultSearchOrder`` is supplied to a ``VaultSearch`` to
        specify the ordering of results.

        :return: the vault search order
        :rtype: ``osid.authorization.VaultSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultSearchOrder

    vault_search_order = property(fget=get_vault_search_order)

    @abc.abstractmethod
    def get_vaults_by_search(self, vault_query, vault_search):
        """Gets the search results matching the given search query using the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :param vault_search: the vault search
        :type vault_search: ``osid.authorization.VaultSearch``
        :return: the search results
        :rtype: ``osid.authorization.VaultSearchResults``
        :raise: ``NullArgument`` -- ``vault_query`` or ``vault_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` or ``vault_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultSearchResults

    @abc.abstractmethod
    def get_vault_query_from_inspector(self, vault_query_inspector):
        """Gets a vault query from an inspector.

        The inspector is available from a ``VaultSearchResults``.

        :param vault_query_inspector: a vault query inspector
        :type vault_query_inspector: ``osid.authorization.VaultQueryInspector``
        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``NullArgument`` -- ``vault_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``vault_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultQuery


class VaultAdminSession:
    """This session creates, updates, and deletes ``Vaults``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Vault,`` a ``VaultForm`` is requested using
    ``get_vault_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``VaultForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``VaultForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``VaultForm`` corresponds
    to an attempted transaction.

    For updates, ``VaultForms`` are requested to the ``Vault``  ``Id``
    that is to be updated using ``getVaultFormForUpdate()``. Similarly,
    the ``VaultForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``VaultForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Vaults``. It is safer to remove all
    mappings to the ``Vault`` catalogs before deletion.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_vaults(self):
        """Tests if this user can create ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_vault_with_record_types(self, vault_record_types):
        """Tests if this user can create a single ``Vault`` using the desired record types.

        While ``AuthorizationManager.getVaultRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Vault``.
        Providing an empty array tests if a ``Vault`` can be created
        with no records.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Vault`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_vault_form_for_create(self, vault_record_types):
        """Gets the vault form for creating new vaults.

        A new form should be requested for each create transaction.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultForm

    @abc.abstractmethod
    def create_vault(self, vault_form):
        """Creates a new ``Vault``.

        :param vault_form: the form for this ``Vault``
        :type vault_form: ``osid.authorization.VaultForm``
        :return: the new ``Vault``
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- ``vault_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.Vault

    @abc.abstractmethod
    def can_update_vaults(self):
        """Tests if this user can update ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_vault_form_for_update(self, vault_id):
        """Gets the vault form for updating an existing vault.

        A new vault form should be requested for each update
        transaction.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultForm

    @abc.abstractmethod
    def update_vault(self, vault_form):
        """Updates an existing vault.

        :param vault_form: the form containing the elements to be updated
        :type vault_form: ``osid.authorization.VaultForm``
        :raise: ``IllegalState`` -- ``vault_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_vaults(self):
        """Tests if this user can delete vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.

        :param vault_id: the ``Id`` of the ``Vault`` to remove
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_vault_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Vault`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_vault(self, vault_id, alias_id):
        """Adds an ``Id`` to a ``Vault`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Vault`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :param vault_id: the ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class VaultNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Vault`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_vault_notifications(self):
        """Tests if this user can register for ``Vault`` notifications.

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
    def reliable_vault_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_vault_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_vault_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_vault_notification(self, notification_id):
        """Acknowledge a vault notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_vaults(self):
        """Register for notifications of new vaults.

        ``VaultReceiver.newVaults()`` is invoked when a new ``Vault`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_vaults(self):
        """Registers for notification of updated vaults.

        ``VaultReceiver.changedVaults()`` is invoked when a vault is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_vault(self, vault_id):
        """Registers for notification of an updated vault.

        ``VaultReceiver.changedVaults()`` is invoked when the specified
        vault is changed.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_vaults(self):
        """Registers for notification of deleted vaults.

        ``VaultReceiver.deletedVaults()`` is invoked when a vault is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_vault(self, vault_id):
        """Registers for notification of a deleted vault.

        ``VaultReceiver.deletedVaults()`` is invoked when the specified
        vault is deleted.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_vault_hierarchy(self):
        """Registers for notification of an updated vault hierarchy structure.

        ``VaultReceiver.changedChildOfVaults()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_vault_hierarchy_for_ancestors(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.

        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_vault_hierarchy_for_descendants(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.

        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_vault_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_vault_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_vault_notification(self, notification_id):
        """Acknowledge an vault notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class VaultHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Vault`` objects.

    Each node in the hierarchy is a unique ``Vault``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_vaults()`` and ``getChildVaults()``. To relate these
    ``Ids`` to another OSID, ``get_vault_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Vault`` available in the Authorization OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_vaults()`` or ``get_child_vaults()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: vault elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    @abc.abstractmethod
    def get_vault_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    vault_hierarchy = property(fget=get_vault_hierarchy)

    @abc.abstractmethod
    def can_access_vault_hierarchy(self):
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
    def use_comparative_vault_view(self):
        """The returns from the vault methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_vault_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_vault_ids(self):
        """Gets the root vault ``Ids`` in this hierarchy.

        :return: the root vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_vault_ids = property(fget=get_root_vault_ids)

    @abc.abstractmethod
    def get_root_vaults(self):
        """Gets the root vaults in this vault hierarchy.

        :return: the root vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.authorization.VaultList

    root_vaults = property(fget=get_root_vaults)

    @abc.abstractmethod
    def has_parent_vaults(self, vault_id):
        """Tests if the ``Vault`` has any parents.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the vault has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a direct parent of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_vault_ids(self, vault_id):
        """Gets the parent ``Ids`` of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_vaults(self, vault_id):
        """Gets the parents of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parents of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def is_ancestor_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is an ancestor of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_vaults(self, vault_id):
        """Tests if a vault has any children.

        :param vault_id: a ``vault_id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``vault_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_vault(self, id_, vault_id):
        """Tests if a vault is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_vault_ids(self, vault_id):
        """Gets the child ``Ids`` of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_vaults(self, vault_id):
        """Gets the children of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultList

    @abc.abstractmethod
    def is_descendant_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a descendant of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_vault_node_ids(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_vault_nodes(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.VaultNode


class VaultHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Vault`` objects.

    Each node in the hierarchy is a unique ``Vault``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    @abc.abstractmethod
    def get_vault_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    vault_hierarchy = property(fget=get_vault_hierarchy)

    @abc.abstractmethod
    def can_modify_vault_hierarchy(self):
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
    def add_root_vault(self, vault_id):
        """Adds a root vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_vault(self, vault_id):
        """Removes a root vault from this hierarchy.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_vault(self, vault_id, child_id):
        """Adds a child to a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``vault_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_vault(self, vault_id, child_id):
        """Removes a child from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_vaults(self, vault_id):
        """Removes all children from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
