"""Implementations of locale abstract base class sessions."""
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


class TranslationSession:
    """This session defines methods to translate text between a source and target locale."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_language_type(self):
        """Gets the source language used in this session.

        :return: the source language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_language_type = property(fget=get_source_language_type)

    @abc.abstractmethod
    def get_source_script_type(self):
        """Gets the source script used in this session.

        :return: the source script
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_script_type = property(fget=get_source_script_type)

    @abc.abstractmethod
    def get_target_language_type(self):
        """Gets the target language used in this session.

        :return: the target language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_language_type = property(fget=get_target_language_type)

    @abc.abstractmethod
    def get_target_script_type(self):
        """Gets the target script used in this session.

        :return: the target script
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_script_type = property(fget=get_target_script_type)

    @abc.abstractmethod
    def can_translate(self):
        """Tests if this user can perform language translations.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if translation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_translation(self, string):
        """Translates the given string into the target language.

        :param string: the ``string`` to translate
        :type string: ``string``
        :return: the translated ``string``
        :rtype: ``string``
        :raise: ``NotFound`` -- no translation found
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def translate_string(self, string, default_string):
        """Translates the given string into the target language.

        :param string: the ``string`` to translate
        :type string: ``string``
        :param default_string: the default ``string`` if no translation available.
        :type default_string: ``string``
        :return: the translated ``string`` or the given default value if no translation available.
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def translate_strings(self, strings, default_strings):
        """Translates the given strings into the target language.

        :param strings: the ``string`` to translate
        :type strings: ``string[]``
        :param default_strings: the default ``string`` if no translation available.
        :type default_strings: ``string[]``
        :return: the translated ``strings`` or the given default value if no translation available.
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string


class TranslationAdminSession:
    """This session defines methods to translate and format text between a source and target locale."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_language_type(self):
        """Gets the source language used in this session.

        :return: the source language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_language_type = property(fget=get_source_language_type)

    @abc.abstractmethod
    def get_source_script_type(self):
        """Gets the source script used in this session.

        :return: the source script
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_script_type = property(fget=get_source_script_type)

    @abc.abstractmethod
    def get_target_language_type(self):
        """Gets the target language used in this session.

        :return: the target language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_language_type = property(fget=get_target_language_type)

    @abc.abstractmethod
    def get_target_script_type(self):
        """Gets the target script used in this session.

        :return: the target script
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_script_type = property(fget=get_target_script_type)

    @abc.abstractmethod
    def can_update_translation(self):
        """Tests if this user can update localization strings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if changing translation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_translation(self, source_text, target_text):
        """Adds or updates a string translation.

        :param source_text: the source ``string``
        :type source_text: ``string``
        :param target_text: the translated string
        :type target_text: ``string``
        :raise: ``NullArgument`` -- ``source_text`` or ``target_text`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_translation(self, source_text):
        """Removes a translation.

        :param source_text: the source ``string``
        :type source_text: ``string``
        :raise: ``NullArgument`` -- ``source_text`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class NumericFormattingSession:
    """This session defines methods to format and parse numbers."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_numeric_format_type(self):
        """Gets the numeric format type used in this session.

        The numeric format type indicates the format of a number used in
        a culture, such as the use of a period for a decimal place.

        :return: the target language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    numeric_format_type = property(fget=get_numeric_format_type)

    @abc.abstractmethod
    def can_format_numbers(self):
        """Tests if this user can format and parse numbers.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if translation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def cardinal_to_string(self, c):
        """Gets a string representation of a cardinal.

        :param c: a cardinal value
        :type c: ``cardinal``
        :return: the display string
        :rtype: ``string``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def cardinals_to_strings(self, c):
        """Gets a string representation of an array of cardinals.

        :param c: a cardinal value array
        :type c: ``cardinal[]``
        :return: the display strings
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``c`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_cardinal(self, str_):
        """Parses a cardinal string.

        :param str: a cardinal string
        :type str: ``string``
        :return: the cardinal value
        :rtype: ``cardinal``
        :raise: ``InvalidArgument`` -- ``str`` not of ``get_numeric_format_type()``
        :raise: ``NullArgument`` -- ``str`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def decimal_to_string(self, d):
        """Gets a string representation of a decimal.

        :param d: a decimal value
        :type d: ``decimal``
        :return: the display string
        :rtype: ``string``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def decimals_to_strings(self, d):
        """Gets a string representation of an array of decimals.

        :param d: a decimals value array
        :type d: ``decimal[]``
        :return: the display strings
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``d`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def decimal_to_string(self, str_):
        """Parses a decimal string.

        :param str: a decimal string
        :type str: ``string``
        :return: the decimal value
        :rtype: ``decimal``
        :raise: ``InvalidArgument`` -- ``str`` not of ``get_numeric_format_type()``
        :raise: ``NullArgument`` -- ``str`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def integer_to_string(self, i):
        """Gets a string representation of a integer.

        :param i: an integer value
        :type i: ``integer``
        :return: the display string
        :rtype: ``string``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def integers_to_strings(self, i):
        """Gets a string representation of an array of integers.

        :param i: an integer value array
        :type i: ``integer[]``
        :return: the display strings
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``i`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def integer_to_string(self, str_):
        """Parses an integer string.

        :param str: an integer string
        :type str: ``string``
        :return: the integer value
        :rtype: ``integer``
        :raise: ``InvalidArgument`` -- ``str`` not of ``get_numeric_format_type()``
        :raise: ``NullArgument`` -- ``str`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer


class CalendarFormattingSession:
    """This session defines methods to format and parse date times of the calendar and time type defined."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_calendar_type(self):
        """Gets the calendar type for the datetimes used in this session.

        :return: the calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    @abc.abstractmethod
    def get_time_type(self):
        """Gets the time type for the times used in this session.

        :return: the time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_type = property(fget=get_time_type)

    @abc.abstractmethod
    def get_date_format_type(self):
        """Gets the date format type used in this session.

        :return: the target language
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    date_format_type = property(fget=get_date_format_type)

    @abc.abstractmethod
    def get_time_format_type(self):
        """Gets the time format type used in this session.

        :return: the target script
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_format_type = property(fget=get_time_format_type)

    @abc.abstractmethod
    def can_display_primitives(self):
        """Tests if this user can format and parse date times.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if translation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def datetime_to_string(self, datetime):
        """Gets a string representation of a datetime.

        :param datetime: a datetime value
        :type datetime: ``osid.calendaring.DateTime``
        :return: the display string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``datetime.get_calendar_type() != get_calendar_type()`` or ``datetime.get_time_type() != get_time_type()``
        :raise: ``NullArgument`` -- ``datetime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def datetimes_to_strings(self, datetimes):
        """Gets a string representation of a list of datetimes.

        :param datetimes: a datetime value list
        :type datetimes: ``osid.calendaring.DateTimeList``
        :return: the display strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``datetime.get_calendar_type() != get_calendar_type()`` or ``datetime.get_time_type() != get_time_type()``
        :raise: ``NullArgument`` -- ``datetimes`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_date_time(self, s):
        """Parses a date time string.

        :param s: a datetime string
        :type s: ``string``
        :return: the date time value
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``s`` is not of ``get_date_format_type()`` or ``s`` is not of ``get_time_format_type()``
        :raise: ``NullArgument`` -- ``s`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    @abc.abstractmethod
    def time_to_string(self, time):
        """Gets a string representation of a time.

        :param time: a time value
        :type time: ``osid.calendaring.Time``
        :return: the display string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``time.get_time_type() != get_time_type()``
        :raise: ``NullArgument`` -- ``time`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def times_to_strings(self, times):
        """Gets a string representation of a list of times.

        :param times: a time value list
        :type times: ``osid.calendaring.TimeList``
        :return: the display strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``time.get_time_type()`` != ``get_time_type()``
        :raise: ``NullArgument`` -- ``times`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_time(self, s):
        """Parses a time string.

        :param s: a time string
        :type s: ``string``
        :return: the time value
        :rtype: ``osid.calendaring.Time``
        :raise: ``InvalidArgument`` -- ``s`` is not of ``get_time_format_type()``
        :raise: ``NullArgument`` -- ``s`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    @abc.abstractmethod
    def duration_to_string(self, duration):
        """Gets a string representation of a duration.

        :param duration: a duration value
        :type duration: ``osid.calendaring.Duration``
        :return: the display string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``duration.get_calendar_type() !=``  ``get_calendar_type()`` or ``duration.get_time_type() != get_time_type()``
        :raise: ``NullArgument`` -- ``duration`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def durations_to_strings(self, durations):
        """Gets a string representation of a list of durations.

        :param durations: a duration value list
        :type durations: ``osid.calendaring.DurationList``
        :return: the display strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``duration.get_calendar_type() !=``  ``get_calendar_type()`` or ``duration.get_time_type() != get_time_type()``
        :raise: ``NullArgument`` -- ``durations`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_duration(self, s):
        """Parses a duration string.

        :param s: a duration string
        :type s: ``string``
        :return: the duration value
        :rtype: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``s`` is not of ``get_date_format_type()`` or ``s`` is not of ``get_time_format_type()``
        :raise: ``NullArgument`` -- ``s`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration


class CurrencyFormattingSession:
    """This session defines methods to format and parse currency amounts."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_currency_type(self):
        """Gets the currency type for amounts used in this session.

        :return: the currency type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    currency_type = property(fget=get_currency_type)

    @abc.abstractmethod
    def get_numeric_format_type(self):
        """Gets the numeric format type for the amounts used in this session.

        :return: the numeric format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    numeric_format_type = property(fget=get_numeric_format_type)

    @abc.abstractmethod
    def can_format_currencies(self):
        """Tests if this user can format and parse currencies.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if translation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def currency_to_string(self, amount):
        """Gets a string representation of a currency including the currency symbol indicated by the currency type.

        :param amount: a currency value
        :type amount: ``osid.financials.Currency``
        :return: the display string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``amount.get_currency_type() != get_currency_type()``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def currencies_to_strings(self, amounts):
        """Gets a string representation of a list of currency amounts including the currency symbols indicated by the currency type.

        :param amounts: an array of amounts
        :type amounts: ``osid.financials.Currency[]``
        :return: the display strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``amount.get_currency_type() != get_currency_type()``
        :raise: ``NullArgument`` -- ``amounts`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_currency(self, s):
        """Parses a currency amount.

        :param s: a currency string
        :type s: ``string``
        :return: the currency amount
        :rtype: ``osid.financials.Currency``
        :raise: ``InvalidArgument`` -- s is not of ``get_currency_type()`` or s is not of ``get_numeric_format_type()``
        :raise: ``NullArgument`` -- ``s`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency


class CoordinateFormattingSession:
    """This session defines methods to format and parse coordinates."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_coordinate_type(self):
        """Gets the coordinate type used in this session.

        :return: the coordinate type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    coordinate_type = property(fget=get_coordinate_type)

    @abc.abstractmethod
    def get_coordinate_format_type(self):
        """Gets the coordinate format type used in this session.

        :return: the coordinate format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    coordinate_format_type = property(fget=get_coordinate_format_type)

    @abc.abstractmethod
    def can_format_coordinates(self):
        """Tests if this user can format and parse coordinates.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if translation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def coordinate_to_string(self, coordinate):
        """Gets a string representation of a coordinate.

        :param coordinate: a coordinate value
        :type coordinate: ``osid.mapping.Coordinate``
        :return: the display string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``coodrinate.has_record_type(get_coordinate_record_type()`` ) is ``false``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def ccoordinates_to_strings(self, coordinates):
        """Gets a string representation of a list of coordinates.

        :param coordinates: a list of coordinates
        :type coordinates: ``osid.mapping.CoordinateList``
        :return: the display strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``coodrinate.has_record_type(get_coordinate_record_type()`` ) is ``false``
        :raise: ``NullArgument`` -- ``coordinates`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def string_to_coordinate(self, s):
        """Parses a coordinate.

        :param s: a coordinate string
        :type s: ``string``
        :return: the display string
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``InvalidArgument`` -- ``s`` is not of ``get_coordinate_format_type()``
        :raise: ``NullArgument`` -- ``s`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate


class UnitConversionSession:
    """This session defines methods to convert units across measurement systems."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_convert_units(self):
        """Tests if this user can perform unit conversions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_unit(self, source_unit, source_unit_type, target_unit_type):
        """Convert a unit of measurement.

        :param source_unit: the measure to convert
        :type source_unit: ``decimal``
        :param source_unit_type: the type of measure specified
        :type source_unit_type: ``osid.type.Type``
        :param target_unit_type: the type of converted measure
        :type target_unit_type: ``osid.type.Type``
        :return: resulting measure
        :rtype: ``decimal``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LocaleManager.supportsUnitTypesForConversion(measureType, conversionType)`` is false

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def convert_units(self, source_units, source_unit_type, target_unit_type):
        """Convert units of measurement.

        :param source_units: the measures to convert
        :type source_units: ``decimal[]``
        :param source_unit_type: the type of measure specified
        :type source_unit_type: ``osid.type.Type``
        :param target_unit_type: the type of converted measure
        :type target_unit_type: ``osid.type.Type``
        :return: resulting measures
        :rtype: ``decimal``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LocaleManager.supportsUnitTypesForConversion(measureType, conversionType)`` is false

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal


class CurrencyConversionSession:
    """This session defines methods to convert currency."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_currency_type(self):
        """Gets the source currency type used in this session.

        :return: the source currency
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_currency_type = property(fget=get_source_currency_type)

    @abc.abstractmethod
    def get_target_currency_type(self):
        """Gets the target currency type used in this session.

        :return: the target currency
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_currency_type = property(fget=get_target_currency_type)

    @abc.abstractmethod
    def can_convert_currency(self):
        """Tests if this user can perform currency conversions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_currency(self, source_currency_amount):
        """Converts currency.

        :param source_currency_amount: the currency amount to convert
        :type source_currency_amount: ``osid.financials.Currency``
        :return: resulting currency units
        :rtype: ``osid.financials.Currency``
        :raise: ``InvalidArgument`` -- ``sourceCurrencyAmount.get_currency_type() != get_sourcecurrency_type()``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    @abc.abstractmethod
    def convert_currencies(self, source_currency_amounts):
        """Converts currencies.

        :param source_currency_amounts: the currency amounts to convert
        :type source_currency_amounts: ``osid.financials.Currency[]``
        :return: resulting currency units
        :rtype: ``osid.financials.Currency``
        :raise: ``InvalidArgument`` -- ``sourceCurrencyAmount.get_currency_type() != get_sourcecurrency_type()``
        :raise: ``NullArgument`` -- ``source_currency_amounts`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency


class CalendarConversionSession:
    """This session defines methods to convert dates across calendar systems."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_calendar_type(self):
        """Gets the source calendar type used in this session.

        :return: the source calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_calendar_type = property(fget=get_source_calendar_type)

    @abc.abstractmethod
    def get_source_time_type(self):
        """Gets the source time type used in this session.

        :return: the source time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_time_type = property(fget=get_source_time_type)

    @abc.abstractmethod
    def get_target_calendar_type(self):
        """Gets the target calendar type used in this session.

        :return: the target calendar
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_calendar_type = property(fget=get_target_calendar_type)

    @abc.abstractmethod
    def get_target_time_type(self):
        """Gets the target time type used in this session.

        :return: the target time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_time_type = property(fget=get_target_time_type)

    @abc.abstractmethod
    def can_convert_calendars(self):
        """Tests if this user can perform calendar conversions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_calendar(self, source_date):
        """Converts a date.

        :param source_date: the date to convert
        :type source_date: ``osid.calendaring.DateTime``
        :return: the resulting date
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``sourceDate.get_calendar_type() != get_source_calendar_type()`` or ``sourceDate.get_time_type() != get_source_time_type()``
        :raise: ``NullArgument`` -- ``source_date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    @abc.abstractmethod
    def convert_calendars(self, source_date_list):
        """Converts dates.

        :param source_date_list: the dates to convert
        :type source_date_list: ``osid.calendaring.DateTimeList``
        :return: the resulting dates
        :rtype: ``osid.calendaring.DateTimeList``
        :raise: ``InvalidArgument`` -- ``sourceDate.get_calendar_type() != get_source_calendar_type()`` or ``sourceDate.get_time_type() != get_source_time_type()``
        :raise: ``NullArgument`` -- ``source_date_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTimeList


class CoordinateConversionSession:
    """This session defines methods to convert coordinates across coordinate systems."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_coordinate_type(self):
        """Gets the source coordinate type used in this session.

        :return: the source coordinate type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_coordinate_type = property(fget=get_source_coordinate_type)

    @abc.abstractmethod
    def get_target_coordinate_type(self):
        """Gets the target coordinate type used in this session.

        :return: the target coordinate type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_coordinate_type = property(fget=get_target_coordinate_type)

    @abc.abstractmethod
    def can_convert_coordinates(self):
        """Tests if this user can perform coordinate conversions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_coordinate(self, source_coordinate):
        """Converts a coordinate.

        :param source_coordinate: the coordinate to convert
        :type source_coordinate: ``osid.mapping.Coordinate``
        :return: the resulting coordinate
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``InvalidArgument`` -- ``sourceCoordinate.has_type(get_source_coordinate_record_type())`` is ``false``
        :raise: ``NullArgument`` -- ``source_coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    @abc.abstractmethod
    def convert_coordinates(self, source_coordinate_list):
        """Converts coordinates.

        :param source_coordinate_list: the coordinates to convert
        :type source_coordinate_list: ``osid.mapping.CoordinateList``
        :return: the resulting coordinates
        :rtype: ``osid.mapping.CoordinateList``
        :raise: ``InvalidArgument`` -- ``sourceCoordinate.has_type(get_source_coordinate_record_type())`` is ``false``
        :raise: ``NullArgument`` -- ``source_coordinate_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.CoordinateList


class SpatialUnitConversionSession:
    """This session defines methods to convert spatial units."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_spatial_unit_record_type(self):
        """Gets the source spatial unit record type used in this session.

        :return: the source spatial unit record type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_spatial_unit_record_type = property(fget=get_source_spatial_unit_record_type)

    @abc.abstractmethod
    def get_target_spatial_unit_record_type(self):
        """Gets the target spatial unit record type used in this session.

        :return: the target spatial unit record type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_spatial_unit_record_type = property(fget=get_target_spatial_unit_record_type)

    @abc.abstractmethod
    def can_convert_spatial_units(self):
        """Tests if this user can perform spatial unit conversions.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_spatial_unit(self, source_spatial_unit):
        """Converts a spatial unit.

        :param source_spatial_unit: the spatial unit to convert
        :type source_spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the resulting spatial unit
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``InvalidArgument`` -- ``sourceSpatialUnit.has_type(get_source_spatial_unit_record_type())`` is ``false``
        :raise: ``NullArgument`` -- ``source_spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnit

    @abc.abstractmethod
    def convert_spatial_units(self, source_spatial_unit_list):
        """Converts spatial units.

        :param source_spatial_unit_list: the spatial units to convert
        :type source_spatial_unit_list: ``osid.mapping.SpatialUnitList``
        :return: the resulting spatial units
        :rtype: ``osid.mapping.SpatialUnitList``
        :raise: ``InvalidArgument`` -- ``sourceSpatialUnit.has_type(get_source_spatial_unit_record_type())`` is ``false``
        :raise: ``NullArgument`` -- ``source_spatial_unit_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnitList


class FormatConversionSession:
    """This session defines methods to convert text formats."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_source_format_type(self):
        """Gets the source format type used in this session.

        :return: the source text format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    source_format_type = property(fget=get_source_format_type)

    @abc.abstractmethod
    def get_target_format_type(self):
        """Gets the target format type used in this session.

        :return: the target text formattype
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    target_format_type = property(fget=get_target_format_type)

    @abc.abstractmethod
    def can_convert_formats(self):
        """Tests if this user can perform text format.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def convert_format(self, source_text):
        """Converts a format.

        :param source_text: the string to convert
        :type source_text: ``string``
        :return: the resulting string
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- ``source_text`` not of source format
        :raise: ``NullArgument`` -- ``source_text`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def convert_formats(self, source_texts):
        """Converts formats.

        :param source_texts: the strings to convert
        :type source_texts: ``string[]``
        :return: the resulting strings
        :rtype: ``string``
        :raise: ``InvalidArgument`` -- a ``source_text not of source format``
        :raise: ``NullArgument`` -- ``source_texts`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string


class CalendarInfoSession:
    """This session defines methods to examine a calendar."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_calendar_type(self):
        """Gets the calendar type for the calendar system informational methods in this session.

        :return: the calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    @abc.abstractmethod
    def get_time_type(self):
        """Gets the time system type for the time system informational methods in this session.

        :return: the time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_type = property(fget=get_time_type)

    @abc.abstractmethod
    def can_examine_calendars(self):
        """Tests if this user can perform calendar inspections.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if conversion methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_calendar_info(self):
        """Gets information about the calendar.

        :return: calendar information
        :rtype: ``osid.locale.CalendarInfo``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.CalendarInfo

    calendar_info = property(fget=get_calendar_info)

    @abc.abstractmethod
    def get_time_info(self):
        """Gets information about the time system.

        :return: time information
        :rtype: ``osid.locale.TimeInfo``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.TimeInfo

    time_info = property(fget=get_time_info)
