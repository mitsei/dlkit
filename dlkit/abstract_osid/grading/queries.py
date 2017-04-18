"""Implementations of grading abstract base class queries."""
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


class GradeQuery:
    """This is the query for searching gradings.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    @abc.abstractmethod
    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available for querying grade systems.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    @abc.abstractmethod
    def clear_grade_system_terms(self):
        """Clears the grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    @abc.abstractmethod
    def match_input_score_start_range(self, start, end, match):
        """Matches grades with the start input score inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_input_score_start_range_terms(self):
        """Clears the nput score start range terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_start_range_terms = property(fdel=clear_input_score_start_range_terms)

    @abc.abstractmethod
    def match_input_score_end_range(self, start, end, match):
        """Matches grades with the end input score inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_input_score_end_range_terms(self):
        """Clears the nput score start range terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_end_range_terms = property(fdel=clear_input_score_end_range_terms)

    @abc.abstractmethod
    def match_input_score(self, start, end, match):
        """Matches grades with the input score range contained within the given range inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_input_score_terms(self):
        """Clears the input score start range terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_terms = property(fdel=clear_input_score_terms)

    @abc.abstractmethod
    def match_output_score(self, start, end, match):
        """Matches grades with the output score contained within the given range inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_output_score_terms(self):
        """Clears the output score terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    output_score_terms = property(fdel=clear_output_score_terms)

    @abc.abstractmethod
    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)

    @abc.abstractmethod
    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available for querying grade entries.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    @abc.abstractmethod
    def match_any_grade_entry(self, match):
        """Matches grades that are assigned to any grade entry.

        :param match: ``true`` to match grades used in any grade entry, ``false`` to match grades that are not used in any grade entries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)

    @abc.abstractmethod
    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    @abc.abstractmethod
    def clear_gradebook_terms(self):
        """Clears the gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    @abc.abstractmethod
    def get_grade_query_record(self, grade_record_type):
        """Gets the grade query record corresponding to the given ``Grade`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param grade_record_type: a grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade query record
        :rtype: ``osid.grading.records.GradeQueryRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeQueryRecord


class GradeSystemQuery:
    """This is the query for searching grade systems.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_based_on_grades(self, match):
        """Matches grade systems based on grades.

        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_based_on_grades_terms(self):
        """Clears the grade ``based`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    based_on_grades_terms = property(fdel=clear_based_on_grades_terms)

    @abc.abstractmethod
    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_id_terms(self):
        """Clears the grade ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)

    @abc.abstractmethod
    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available for querying grades.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)

    @abc.abstractmethod
    def match_any_grade(self, match):
        """Matches grade systems with any grade.

        :param match: ``true`` to match grade systems with any grade, ``false`` to match systems with no grade
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_terms(self):
        """Clears the grade terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_terms = property(fdel=clear_grade_terms)

    @abc.abstractmethod
    def match_lowest_numeric_score(self, start, end, match):
        """Matches grade systems whose low end score falls in the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_lowest_numeric_score_terms(self):
        """Clears the lowest numeric score terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    lowest_numeric_score_terms = property(fdel=clear_lowest_numeric_score_terms)

    @abc.abstractmethod
    def match_numeric_score_increment(self, start, end, match):
        """Matches grade systems numeric score increment is between the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_numeric_score_increment_terms(self):
        """Clears the numeric score increment terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    numeric_score_increment_terms = property(fdel=clear_numeric_score_increment_terms)

    @abc.abstractmethod
    def match_highest_numeric_score(self, start, end, match):
        """Matches grade systems whose high end score falls in the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_highest_numeric_score_terms(self):
        """Clears the highest numeric score terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    highest_numeric_score_terms = property(fdel=clear_highest_numeric_score_terms)

    @abc.abstractmethod
    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    @abc.abstractmethod
    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    @abc.abstractmethod
    def match_any_gradebook_column(self, match):
        """Matches grade systems assigned to any gradebook column.

        :param match: ``true`` to match grade systems mapped to any column, ``false`` to match systems mapped to no columns
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    @abc.abstractmethod
    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    @abc.abstractmethod
    def clear_gradebook_terms(self):
        """Clears the gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    @abc.abstractmethod
    def get_grade_system_query_record(self, grade_system_record_type):
        """Gets the grade system query record corresponding to the given ``GradeSystem`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system query record
        :rtype: ``osid.grading.records.GradeSystemQueryRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemQueryRecord


class GradeEntryQuery:
    """This is the query for searching grade entries.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    @abc.abstractmethod
    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available for querying creators.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    @abc.abstractmethod
    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    @abc.abstractmethod
    def match_key_resource_id(self, resource_id, match):
        """Sets the key resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_key_resource_id_terms(self):
        """Clears the key resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    key_resource_id_terms = property(fdel=clear_key_resource_id_terms)

    @abc.abstractmethod
    def supports_key_resource_query(self):
        """Tests if a ``ResourceQUery`` is available for querying key resources.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_key_resource_query(self):
        """Gets the query for a key resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_key_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_key_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    key_resource_query = property(fget=get_key_resource_query)

    @abc.abstractmethod
    def match_any_key_resource(self, match):
        """Matches grade entries with any key resource.

        :param match: ``true`` to match grade entries with any key resource, ``false`` to match entries with no key resource
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_key_resource_terms(self):
        """Clears the key resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    key_resource_terms = property(fdel=clear_key_resource_terms)

    @abc.abstractmethod
    def match_derived(self, match):
        """Matches derived grade entries.

        :param match: ``true`` to match derived grade entries , ``false`` to match manual entries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_derived_terms(self):
        """Clears the derived terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    derived_terms = property(fdel=clear_derived_terms)

    @abc.abstractmethod
    def match_overridden_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for an overridden calculated grade entry.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_overridden_grade_entry_id_terms(self):
        """Clears the overridden grade entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    overridden_grade_entry_id_terms = property(fdel=clear_overridden_grade_entry_id_terms)

    @abc.abstractmethod
    def supports_overridden_grade_entry_query(self):
        """Tests if a ``GradeEntry`` is available for querying overridden calculated grade entries.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_overridden_grade_entry_query(self):
        """Gets the query for an overridden derived grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_overridden_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_overridden_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuery

    overridden_grade_entry_query = property(fget=get_overridden_grade_entry_query)

    @abc.abstractmethod
    def match_any_overridden_grade_entry(self, match):
        """Matches grade entries overriding any calculated grade entry.

        :param match: ``true`` to match grade entries overriding any grade entry, ``false`` to match entries not overriding any entry
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_overridden_grade_entry_terms(self):
        """Clears the overridden grade entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    overridden_grade_entry_terms = property(fdel=clear_overridden_grade_entry_terms)

    @abc.abstractmethod
    def match_ignored_for_calculations(self, match):
        """Matches grade entries ignored for calculations.

        :param match: ``true`` to match grade entries ignored for calculations, ``false`` to match entries used in calculations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ignored_for_calculations_terms(self):
        """Clears the ignored for calculation entries terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ignored_for_calculations_terms = property(fdel=clear_ignored_for_calculations_terms)

    @abc.abstractmethod
    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_id_terms(self):
        """Clears the grade ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)

    @abc.abstractmethod
    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available for querying grades.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_query()`` is ``true``.*

        """
        return  # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)

    @abc.abstractmethod
    def match_any_grade(self, match):
        """Matches grade entries with any grade.

        :param match: ``true`` to match grade entries with any grade, ``false`` to match entries with no grade
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_terms(self):
        """Clears the grade terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_terms = property(fdel=clear_grade_terms)

    @abc.abstractmethod
    def match_score(self, start, end, match):
        """Matches grade entries which score is between the specified score inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_score(self, match):
        """Matches grade entries with any score.

        :param match: ``true`` to match grade entries with any score, ``false`` to match entries with no score
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score_terms(self):
        """Clears the score terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_terms = property(fdel=clear_score_terms)

    @abc.abstractmethod
    def match_time_graded(self, start, end, match):
        """Matches grade entries which graded time is between the specified times inclusive.

        :param start: start of range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of range
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_time_graded_terms(self):
        """Clears the time graded terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_graded_terms = property(fdel=clear_time_graded_terms)

    @abc.abstractmethod
    def match_grader_id(self, resource_id, match):
        """Sets the agent ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grader_id_terms(self):
        """Clears the grader ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grader_id_terms = property(fdel=clear_grader_id_terms)

    @abc.abstractmethod
    def supports_grader_query(self):
        """Tests if a ``ResourceQuery`` is available for querying graders.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grader_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return  # osid.resource.ResourceQuery

    grader_query = property(fget=get_grader_query)

    @abc.abstractmethod
    def match_any_grader(self, match):
        """Matches grade entries with any grader.

        :param match: ``true`` to match grade entries with any grader, ``false`` to match entries with no grader
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grader_terms(self):
        """Clears the grader terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grader_terms = property(fdel=clear_grader_terms)

    @abc.abstractmethod
    def match_grading_agent_id(self, agent_id, match):
        """Sets the grading agent ``Id`` for this query.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grading_agent_id_terms(self):
        """Clears the grader ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grading_agent_id_terms = property(fdel=clear_grading_agent_id_terms)

    @abc.abstractmethod
    def supports_grading_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying grading agents.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grading_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_grading_agent_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_agent_query()`` is ``true``.*

        """
        return  # osid.authentication.AgentQuery

    grading_agent_query = property(fget=get_grading_agent_query)

    @abc.abstractmethod
    def match_any_grading_agent(self, match):
        """Matches grade entries with any grading agent.

        :param match: ``true`` to match grade entries with any grading agent, ``false`` to match entries with no grading agent
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grading_agent_terms(self):
        """Clears the grading agent terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grading_agent_terms = property(fdel=clear_grading_agent_terms)

    @abc.abstractmethod
    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available for querying resources.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    @abc.abstractmethod
    def clear_gradebook_terms(self):
        """Clears the gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    @abc.abstractmethod
    def get_grade_entry_query_record(self, grade_entry_record_type):
        """Gets the grade entry query record corresponding to the given ``GradeEntry`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the grade entry query record
        :rtype: ``osid.grading.records.GradeEntryQueryRecord``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntryQueryRecord


class GradebookColumnQuery:
    """This is the query for searching gradings.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    @abc.abstractmethod
    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available for querying grade systems.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    @abc.abstractmethod
    def match_any_grade_system(self, match):
        """Matches gradebook columns with any grade system assigned.

        :param match: ``true`` to match columns with any grade system, ``false`` to match columns with no grade system
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_terms(self):
        """Clears the grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    @abc.abstractmethod
    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)

    @abc.abstractmethod
    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available for querying grade entries.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    @abc.abstractmethod
    def match_any_grade_entry(self, match):
        """Matches gradebook columns with any grade entry assigned.

        :param match: ``true`` to match columns with any grade entry, ``false`` to match columns with no grade entries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)

    @abc.abstractmethod
    def supports_gradebook_column_summary_query(self):
        """Tests if a ``GradebookColumnSummaryQuery`` is available for querying grade systems.

        :return: ``true`` if a gradebook column summary query interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_summary_query(self):
        """Gets the query interface for a gradebook column summary.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column summary query
        :rtype: ``osid.grading.GradebookColumnSummaryQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_summary_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_summary_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnSummaryQuery

    gradebook_column_summary_query = property(fget=get_gradebook_column_summary_query)

    @abc.abstractmethod
    def clear_gradebook_column_summary_terms(self):
        """Clears the gradebook column summary terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_summary_terms = property(fdel=clear_gradebook_column_summary_terms)

    @abc.abstractmethod
    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available for querying grade systems.

        :return: ``true`` if a gradebook query interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_query(self):
        """Gets the query interface for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    @abc.abstractmethod
    def clear_gradebook_terms(self):
        """Clears the gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_column_query_record(self, gradebook_column_record_type):
        """Gets the gradebook column query record corresponding to the given ``GradebookColumn`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the gradebook column query record
        :rtype: ``osid.grading.records.GradebookColumnQueryRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnQueryRecord


class GradebookColumnSummaryQuery:
    """This is the query for searching gradebook column summaries.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradeboo column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    @abc.abstractmethod
    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available for querying gradebook column.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    @abc.abstractmethod
    def match_any_gradebook_column(self, match):
        """Matches gradebook column derivations with any gradebookc olumn.

        :param match: ``true`` to match gradebook column derivations with any gradebook column, ``false`` to match gradebook column derivations with no gradebook columns
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_terms(self):
        """Clears the source grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    @abc.abstractmethod
    def match_mean(self, low, high, match):
        """Matches a mean between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_mean_terms(self):
        """Clears the mean terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    mean_terms = property(fdel=clear_mean_terms)

    @abc.abstractmethod
    def match_minimum_mean(self, value, match):
        """Matches a mean greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_mean_terms(self):
        """Clears the minimum mean terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_mean_terms = property(fdel=clear_minimum_mean_terms)

    @abc.abstractmethod
    def match_median(self, low, high, match):
        """Matches a median between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_median_terms(self):
        """Clears the median terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    median_terms = property(fdel=clear_median_terms)

    @abc.abstractmethod
    def match_minimum_median(self, value, match):
        """Matches a median greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_median_terms(self):
        """Clears the minimum median terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_median_terms = property(fdel=clear_minimum_median_terms)

    @abc.abstractmethod
    def match_mode(self, low, high, match):
        """Matches a mode between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_mode_terms(self):
        """Clears the mode terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    mode_terms = property(fdel=clear_mode_terms)

    @abc.abstractmethod
    def match_minimum_mode(self, value, match):
        """Matches a mode greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_mode_terms(self):
        """Clears the minimum mode terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_mode_terms = property(fdel=clear_minimum_mode_terms)

    @abc.abstractmethod
    def match_rms(self, low, high, match):
        """Matches a root mean square between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_rms_terms(self):
        """Clears the root mean square terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rms_terms = property(fdel=clear_rms_terms)

    @abc.abstractmethod
    def match_minimum_rms(self, value, match):
        """Matches a root mean square greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_rms_terms(self):
        """Clears the minimum RMS terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_rms_terms = property(fdel=clear_minimum_rms_terms)

    @abc.abstractmethod
    def match_standard_deviation(self, low, high, match):
        """Matches a standard deviation mean square between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_standard_deviation_terms(self):
        """Clears the standard deviation terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    standard_deviation_terms = property(fdel=clear_standard_deviation_terms)

    @abc.abstractmethod
    def match_minimum_standard_deviation(self, value, match):
        """Matches a standard deviation greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_standard_deviation_terms(self):
        """Clears the minimum standard deviation terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_standard_deviation_terms = property(fdel=clear_minimum_standard_deviation_terms)

    @abc.abstractmethod
    def match_sum(self, low, high, match):
        """Matches a sum mean square between the given values inclusive.

        :param low: low end of range
        :type low: ``decimal``
        :param high: high end of range
        :type high: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_sum_terms(self):
        """Clears the sum terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    sum_terms = property(fdel=clear_sum_terms)

    @abc.abstractmethod
    def match_minimum_sum(self, value, match):
        """Matches a sum greater than or equal to the given value.

        :param value: minimum value
        :type value: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_minimum_sum_terms(self):
        """Clears the minimum sum terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_sum_terms = property(fdel=clear_minimum_sum_terms)

    @abc.abstractmethod
    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    @abc.abstractmethod
    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    @abc.abstractmethod
    def clear_gradebook_terms(self):
        """Clears the gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_column_summary_query_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary query record corresponding to the given ``GradebookColumnSummary`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param gradebook_column_summary_record_type: a gradebook column summary record type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: the gradebook column summary query record
        :rtype: ``osid.grading.records.GradebookColumnSummaryQueryRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_summary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_summary_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSummaryQueryRecord


class GradebookQuery:
    """This is the query for searching gradebooks.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    @abc.abstractmethod
    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return  # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    @abc.abstractmethod
    def match_any_grade_system(self, match):
        """Matches gradebooks that have any grade system.

        :param match: ``true`` to match gradebooks with any grade system, ``false`` to match gradebooks with no grade system
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system_terms(self):
        """Clears the grade system terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    @abc.abstractmethod
    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)

    @abc.abstractmethod
    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return  # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    @abc.abstractmethod
    def match_any_grade_entry(self, match):
        """Matches gradebooks that have any grade entry.

        :param match: ``true`` to match gradebooks with any grade entry, ``false`` to match gradebooks with no grade entry
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)

    @abc.abstractmethod
    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    @abc.abstractmethod
    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    @abc.abstractmethod
    def match_any_gradebook_column(self, match):
        """Matches gradebooks that have any column.

        :param match: ``true`` to match gradebooks with any column, ``false`` to match gradebooks with no column
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    @abc.abstractmethod
    def match_ancestor_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as an ancestor.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_gradebook_id_terms(self):
        """Clears the ancestor gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_gradebook_id_terms = property(fdel=clear_ancestor_gradebook_id_terms)

    @abc.abstractmethod
    def supports_ancestor_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_gradebook_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    ancestor_gradebook_query = property(fget=get_ancestor_gradebook_query)

    @abc.abstractmethod
    def match_any_ancestor_gradebook(self, match):
        """Matches gradebook with any ancestor.

        :param match: ``true`` to match gradebooks with any ancestor, ``false`` to match root gradebooks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_gradebook_terms(self):
        """Clears the ancestor gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_gradebook_terms = property(fdel=clear_ancestor_gradebook_terms)

    @abc.abstractmethod
    def match_descendant_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as a descendant.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_gradebook_id_terms(self):
        """Clears the descendant gradebook ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_gradebook_id_terms = property(fdel=clear_descendant_gradebook_id_terms)

    @abc.abstractmethod
    def supports_descendant_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_gradebook_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_gradebook_query()`` is ``true``.*

        """
        return  # osid.grading.GradebookQuery

    descendant_gradebook_query = property(fget=get_descendant_gradebook_query)

    @abc.abstractmethod
    def match_any_descendant_gradebook(self, match):
        """Matches gradebook with any descendant.

        :param match: ``true`` to match gradebooks with any descendant, ``false`` to match leaf gradebooks
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_gradebook_terms(self):
        """Clears the descendant gradebook terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_gradebook_terms = property(fdel=clear_descendant_gradebook_terms)

    @abc.abstractmethod
    def get_gradebook_query_record(self, gradebook_record_type):
        """Gets the gradebook query record corresponding to the given ``Gradebook`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook query record
        :rtype: ``osid.grading.records.GradebookQueryRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookQueryRecord
