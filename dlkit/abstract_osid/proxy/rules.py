"""Implementations of proxy abstract base class rules."""
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


class Proxy:
    """A ``Proxy`` is used to transfer external information from an application server into an OSID Provider."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def has_authentication(self):
        """Tests if an authentication is available.

        :return: ``true`` if an ``Authentication`` is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_authentication(self):
        """Gets the ``Authentication`` for this proxy.

        :return: the authentication
        :rtype: ``osid.authentication.process.Authentication``
        :raise: ``IllegalState`` -- ``has_authentication()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.process.Authentication

    authentication = property(fget=get_authentication)

    @abc.abstractmethod
    def has_effective_agent(self):
        """Tests if an effective agent is available.

        :return: ``true`` if an effective agent is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_effective_agent_id(self):
        """Gets the effective ``Agent Id`` for this proxy.

        :return: the effective agent ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_effective_agent()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)

    @abc.abstractmethod
    def get_effective_agent(self):
        """Gets the effective ``Agent`` for this proxy.

        :return: the effective agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``has_effective_agent()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    effective_agent = property(fget=get_effective_agent)

    @abc.abstractmethod
    def has_effective_date(self):
        """Tests if an effective date is available.

        :return: ``true`` if an effective date is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_effective_date(self):
        """Gets the effective date.

        :return: the effective date
        :rtype: ``timestamp``
        :raise: ``IllegalState`` -- ``has_effective_date()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # timestamp

    effective_date = property(fget=get_effective_date)

    @abc.abstractmethod
    def get_effective_clock_rate(self):
        """Gets the rate of the clock.

        :return: the rate
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``has_effective_date()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    effective_clock_rate = property(fget=get_effective_clock_rate)

    @abc.abstractmethod
    def get_locale(self):
        """Gets the locale.

        :return: a locale
        :rtype: ``osid.locale.Locale``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.Locale

    locale = property(fget=get_locale)

    @abc.abstractmethod
    def has_format_type(self):
        """Tests if a ``DisplayText`` format ``Type`` is available.

        :return: ``true`` if a format type is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type``.

        :return: the format ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``has_format_type()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    format_type = property(fget=get_format_type)

    @abc.abstractmethod
    def get_proxy_record(self, proxy_record_type):
        """Gets the proxy record corresponding to the given ``Proxy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proxy_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(proxy_record_type)``
        is ``true`` .

        :param proxy_record_type: the type of proxy record to retrieve
        :type proxy_record_type: ``osid.type.Type``
        :return: the proxy record
        :rtype: ``osid.proxy.records.ProxyRecord``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proxy_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.proxy.records.ProxyRecord


class ProxyCondition:
    """A ``ProxyCondition`` is used to transfer external information into a proxy."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_effective_agent_id(self, agent_id):
        """Sets the effective agent ``Id`` to indicate acting on behalf of.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    effective_agent_id = property(fset=set_effective_agent_id)

    @abc.abstractmethod
    def set_effective_date(self, date, rate):
        """Sets the effective date.

        :param date: a date
        :type date: ``timestamp``
        :param rate: the rate at which the clock should tick from the given effective date. 0 is a clock that is fixed
        :type rate: ``decimal``
        :raise: ``NullArgument`` -- ``date`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def set_language_type(self, language_type):
        """Sets the language type.

        :param language_type: the language type
        :type language_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``language_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    language_type = property(fset=set_language_type)

    @abc.abstractmethod
    def set_script_type(self, script_type):
        """Sets the script type.

        :param script_type: the script type
        :type script_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``script_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    script_type = property(fset=set_script_type)

    @abc.abstractmethod
    def set_calendar_type(self, calendar_type):
        """Sets the calendar type.

        :param calendar_type: the calendar type
        :type calendar_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    calendar_type = property(fset=set_calendar_type)

    @abc.abstractmethod
    def set_time_type(self, time_type):
        """Sets the time type.

        :param time_type: the time type
        :type time_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_type = property(fset=set_time_type)

    @abc.abstractmethod
    def set_currency_type(self, currency_type):
        """Sets the currency type.

        :param currency_type: the currency type
        :type currency_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``currency_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    currency_type = property(fset=set_currency_type)

    @abc.abstractmethod
    def set_unit_system_type(self, unit_system_type):
        """Sets the unit system type.

        :param unit_system_type: the unit system type
        :type unit_system_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``unit_system_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    unit_system_type = property(fset=set_unit_system_type)

    @abc.abstractmethod
    def set_format_type(self, format_type):
        """Sets the ``DisplayText`` format type.

        :param format_type: the format type
        :type format_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``format_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    format_type = property(fset=set_format_type)

    @abc.abstractmethod
    def get_proxy_condition_record(self, proxy_condition_type):
        """Gets the proxy condition record corresponding to the given ``Proxy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proxy_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(proxy_record_type)``
        is ``true`` .

        :param proxy_condition_type: the type of proxy condition record to retrieve
        :type proxy_condition_type: ``osid.type.Type``
        :return: the proxy condition record
        :rtype: ``osid.proxy.records.ProxyConditionRecord``
        :raise: ``NullArgument`` -- ``proxy_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proxy_condition_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.proxy.records.ProxyConditionRecord
