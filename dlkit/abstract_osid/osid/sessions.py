"""Implementations of osid abstract base class sessions."""
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


class OsidSession:
    """The ``OsidSession`` is the top level interface for all OSID sessions.

    An ``OsidSession`` is created through its corresponding
    ``OsidManager``. A new ``OsidSession`` should be created for each
    user of a service and for each processing thread. A session
    maintains a single authenticated user and is not required to ensure
    thread-protection. A typical OSID session defines a set of service
    methods corresponding to some compliance level as defined by the
    service and is generally responsible for the management and
    retrieval of ``OsidObjects``.

    ``OsidSession`` defines a set of common methods used throughout all
    OSID sessions. An OSID session may optionally support transactions
    through the transaction interface.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_locale(self):  # pragma: no cover
        """Gets the locale indicating the localization preferences in effect for this session.

        :return: the locale
        :rtype: ``osid.locale.Locale``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.Locale

    locale = property(fget=get_locale)

    @abc.abstractmethod
    def is_authenticated(self):  # pragma: no cover
        """Tests if an agent is authenticated to this session.

        :return: ``true`` if valid authentication credentials exist, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authenticated_agent_id(self):  # pragma: no cover
        """Gets the ``Id`` of the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    @abc.abstractmethod
    def get_authenticated_agent(self):  # pragma: no cover
        """Gets the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    authenticated_agent = property(fget=get_authenticated_agent)

    @abc.abstractmethod
    def get_effective_agent_id(self):  # pragma: no cover
        """Gets the ``Id`` of the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)

    @abc.abstractmethod
    def get_effective_agent(self):  # pragma: no cover
        """Gets the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    effective_agent = property(fget=get_effective_agent)

    @abc.abstractmethod
    def get_date(self):  # pragma: no cover
        """Gets the service date which may be the current date or the effective date in which this session exists.

        :return: the service date
        :rtype: ``timestamp``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # timestamp

    date = property(fget=get_date)

    @abc.abstractmethod
    def get_clock_rate(self):  # pragma: no cover
        """Gets the rate of the service clock.

        :return: the clock rate
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    clock_rate = property(fget=get_clock_rate)

    @abc.abstractmethod
    def get_format_type(self):  # pragma: no cover
        """Gets the ``DisplayText`` format ``Type`` preference in effect for this session.

        :return: the effective ``DisplayText`` format ``Type``
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    format_type = property(fget=get_format_type)

    @abc.abstractmethod
    def supports_transactions(self):  # pragma: no cover
        """Tests for the availability of transactions.

        :return: ``true`` if transaction methods are available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def start_transaction(self):  # pragma: no cover
        """Starts a new transaction for this sesson.

        Transactions are a means for an OSID to provide an all-or-
        nothing set of operations within a session and may be used to
        coordinate this service from an external transaction manager. A
        session supports one transaction at a time. Starting a second
        transaction before the previous has been committed or aborted
        results in an ``IllegalState`` error.

        :return: a new transaction
        :rtype: ``osid.transaction.Transaction``
        :raise: ``IllegalState`` -- a transaction is already open
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- transactions not supported

        *compliance: optional -- This method must be implemented if
        ``supports_transactions()`` is true.*
        *implementation notes*: Ideally, a provider that supports
        transactions should guarantee atomicity, consistency, isolation
        and durability in a 2 phase commit process. This is not always
        possible in distributed systems and a transaction provider may
        simply allow for a means of processing bulk updates.  To
        maximize interoperability, providers should honor the one-
        transaction-at-a-time rule.

        """
        return  # osid.transaction.Transaction
