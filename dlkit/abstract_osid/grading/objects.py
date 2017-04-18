"""Implementations of grading abstract base class objects."""
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


class Grade:
    """A ``Grade``.

    Grades represent qualified performance levels defined within some
    grading system.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_id(self):
        """Gets the ``GradeSystem Id`` in which this grade belongs.

        :return: the grade system ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)

    @abc.abstractmethod
    def get_grade_system(self):
        """Gets the ``GradeSystem`` in which this grade belongs.

        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)

    @abc.abstractmethod
    def get_input_score_start_range(self):
        """Gets the low end of the input score range equivalent to this grade.

        :return: the start range
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    input_score_start_range = property(fget=get_input_score_start_range)

    @abc.abstractmethod
    def get_input_score_end_range(self):
        """Gets the high end of the input score range equivalent to this grade.

        :return: the end range
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    input_score_end_range = property(fget=get_input_score_end_range)

    @abc.abstractmethod
    def get_output_score(self):
        """Gets the output score for this grade used for calculating cumultives or performing articulation.

        :return: the output score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    output_score = property(fget=get_output_score)

    @abc.abstractmethod
    def get_grade_record(self, grade_record_type):
        """Gets the grade record corresponding to the given ``Grade`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(grade_record_type)``
        is ``true`` .

        :param grade_record_type: the type of the record to retrieve
        :type grade_record_type: ``osid.type.Type``
        :return: the grade record
        :rtype: ``osid.grading.records.GradeRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeRecord


class GradeForm:
    """This is the form for creating and updating ``Grades``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_input_score_start_range_metadata(self):
        """Gets the metadata for the input score start range.

        :return: metadata for the input score start range
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    input_score_start_range_metadata = property(fget=get_input_score_start_range_metadata)

    @abc.abstractmethod
    def set_input_score_start_range(self, score):
        """Sets the input score start range.

        :param score: the new start range
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``range`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_input_score_start_range(self):
        """Clears the input score start.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_start_range = property(fset=set_input_score_start_range, fdel=clear_input_score_start_range)

    @abc.abstractmethod
    def get_input_score_end_range_metadata(self):
        """Gets the metadata for the input score start range.

        :return: metadata for the input score start range
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    input_score_end_range_metadata = property(fget=get_input_score_end_range_metadata)

    @abc.abstractmethod
    def set_input_score_end_range(self, score):
        """Sets the input score start range.

        :param score: the new start range
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``range`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_input_score_end_range(self):
        """Clears the input score start.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_end_range = property(fset=set_input_score_end_range, fdel=clear_input_score_end_range)

    @abc.abstractmethod
    def get_output_score_metadata(self):
        """Gets the metadata for the output score start range.

        :return: metadata for the output score start range
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    output_score_metadata = property(fget=get_output_score_metadata)

    @abc.abstractmethod
    def set_output_score(self, score):
        """Sets the output score.

        :param score: the new output score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_output_score(self):
        """Clears the output score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    output_score = property(fset=set_output_score, fdel=clear_output_score)

    @abc.abstractmethod
    def get_grade_form_record(self, grade_record_type):
        """Gets the ``GradeFormRecord`` corresponding to the given grade record ``Type``.

        :param grade_record_type: the grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade form record
        :rtype: ``osid.grading.records.GradeFormRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeFormRecord


class GradeList:
    """Like all ``OsidLists,``  ``GradeList`` provides a means for accessing ``Grade`` elements sequentially either one at a time or many at a time.

    Examples: while (gl.hasNext()) { Grade grade = gl.getNextGrade(); }

    or
      while (gl.hasNext()) {
           Grade[] grades = gl.getNextGrades(gl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_grade(self):
        """Gets the next ``Grade`` in this list.

        :return: the next ``Grade`` in this list. The ``has_next()`` method should be used to test that a next ``Grade`` is available before calling this method.
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    next_grade = property(fget=get_next_grade)

    @abc.abstractmethod
    def get_next_grades(self, n):
        """Gets the next set of ``Grade`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Grade`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Grade`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade


class GradeSystem:
    """A ``GradeSystem`` represents a grading system.

    The system can be based on assigned Grades or based on a numeric
    scale.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_based_on_grades(self):
        """Tests if the grading system is based on grades.

        :return: true if the grading system is based on grades, ``false`` if the system is a numeric score
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_ids(self):
        """Gets the grade ``Ids`` in this system ranked from highest to lowest.

        :return: the list of grades ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    grade_ids = property(fget=get_grade_ids)

    @abc.abstractmethod
    def get_grades(self):
        """Gets the grades in this system ranked from highest to lowest.

        :return: the list of grades
        :rtype: ``osid.grading.GradeList``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeList

    grades = property(fget=get_grades)

    @abc.abstractmethod
    def get_lowest_numeric_score(self):
        """Gets the lowest number in a numeric grading system.

        :return: the lowest number
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    lowest_numeric_score = property(fget=get_lowest_numeric_score)

    @abc.abstractmethod
    def get_numeric_score_increment(self):
        """Gets the incremental step.

        :return: the increment
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    numeric_score_increment = property(fget=get_numeric_score_increment)

    @abc.abstractmethod
    def get_highest_numeric_score(self):
        """Gets the highest number in a numeric grading system.

        :return: the highest number
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    highest_numeric_score = property(fget=get_highest_numeric_score)

    @abc.abstractmethod
    def get_grade_system_record(self, grade_system_record_type):
        """Gets the grade system record corresponding to the given ``GradeSystem`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_system_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(grade_system_record_type)`` is ``true`` .

        :param grade_system_record_type: the type of the record to retrieve
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system record
        :rtype: ``osid.grading.records.GradeSystemRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemRecord


class GradeSystemForm:
    """This is the form for creating and updating ``GradeSystems``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeSystemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_based_on_grades_metadata(self):
        """Gets the metadata for a grade-based designation.

        :return: metadata for the grade-based designation
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    based_on_grades_metadata = property(fget=get_based_on_grades_metadata)

    @abc.abstractmethod
    def set_based_on_grades(self, grades):
        """Sets the grade-based designation.

        :param grades: the grade-based designation
        :type grades: ``boolean``
        :raise: ``InvalidArgument`` -- ``grades`` is invalid
        :raise: ``NoAccess`` -- ``grades`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_based_on_grades(self):
        """Clears the based on grades designation.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    based_on_grades = property(fset=set_based_on_grades, fdel=clear_based_on_grades)

    @abc.abstractmethod
    def get_lowest_numeric_score_metadata(self):
        """Gets the metadata for the lowest numeric score.

        :return: metadata for the lowest numeric score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    lowest_numeric_score_metadata = property(fget=get_lowest_numeric_score_metadata)

    @abc.abstractmethod
    def set_lowest_numeric_score(self, score):
        """Sets the lowest numeric score.

        :param score: the lowest numeric score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_lowest_numeric_score(self):
        """Clears the lowest score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    lowest_numeric_score = property(fset=set_lowest_numeric_score, fdel=clear_lowest_numeric_score)

    @abc.abstractmethod
    def get_numeric_score_increment_metadata(self):
        """Gets the metadata for the lowest numeric score.

        :return: metadata for the lowest numeric score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    numeric_score_increment_metadata = property(fget=get_numeric_score_increment_metadata)

    @abc.abstractmethod
    def set_numeric_score_increment(self, increment):
        """Sets the numeric score increment.

        :param increment: the numeric score increment
        :type increment: ``decimal``
        :raise: ``InvalidArgument`` -- ``increment`` is invalid
        :raise: ``NoAccess`` -- ``increment`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_numeric_score_increment(self):
        """Clears the numeric score increment.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    numeric_score_increment = property(fset=set_numeric_score_increment, fdel=clear_numeric_score_increment)

    @abc.abstractmethod
    def get_highest_numeric_score_metadata(self):
        """Gets the metadata for the highest numeric score.

        :return: metadata for the highest numeric score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    highest_numeric_score_metadata = property(fget=get_highest_numeric_score_metadata)

    @abc.abstractmethod
    def set_highest_numeric_score(self, score):
        """Sets the highest numeric score.

        :param score: the highest numeric score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_highest_numeric_score(self):
        """Clears the highest numeric score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    highest_numeric_score = property(fset=set_highest_numeric_score, fdel=clear_highest_numeric_score)

    @abc.abstractmethod
    def get_grade_system_form_record(self, grade_system_record_type):
        """Gets the ``GradeSystemFormRecord`` corresponding to the given grade system record ``Type``.

        :param grade_system_record_type: the grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system form record
        :rtype: ``osid.grading.records.GradeSystemFormRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeSystemFormRecord


class GradeSystemList:
    """Like all ``OsidLists,``  ``GradeSystemList`` provides a means for accessing ``GradeSystem`` elements sequentially either one at a time or many at a time.

    Examples: while (gsl.hasNext()) { GradeSystem system =
    gsl.getNextGradeSystem(); }

    or
      while (gsl.hasNext()) {
           GradeSystem[] systems = gsl.getNextGradeSystems(gsl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_grade_system(self):
        """Gets the next ``GradeSystem`` in this list.

        :return: the next ``GradeSystem`` in this list. The ``has_next()`` method should be used to test that a next ``GradeSystem`` is available before calling this method.
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    next_grade_system = property(fget=get_next_grade_system)

    @abc.abstractmethod
    def get_next_grade_systems(self, n):
        """Gets the next set of ``GradeSystem`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``GradeSystem`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``GradeSystem`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem


class GradeEntry:
    """A ``GradeEntry`` represents an entry in a ``Gradebook``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_column_id(self):
        """Gets the ``Id`` of the ``GradebookColumn``.

        :return: the ``Id`` of the ``GradebookColumn``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    gradebook_column_id = property(fget=get_gradebook_column_id)

    @abc.abstractmethod
    def get_gradebook_column(self):
        """Gets the ``GradebookColumn``.

        :return: the ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumn

    gradebook_column = property(fget=get_gradebook_column)

    @abc.abstractmethod
    def get_key_resource_id(self):
        """Gets the ``Id`` of the key resource of this entry.

        The key resource may be a student or other applicable key to
        identify a row of grading entries.

        :return: ``Id`` of the key resource
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    key_resource_id = property(fget=get_key_resource_id)

    @abc.abstractmethod
    def get_key_resource(self):
        """Gets the key resource of this entry.

        The key resource may be a student or other applicable key to
        identify a row of grading entries.

        :return: the key resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    key_resource = property(fget=get_key_resource)

    @abc.abstractmethod
    def is_derived(self):
        """Tests if this is a calculated entry.

        :return: ``true`` if this entry is a calculated entry, ``false`` otherwise. If ``true,`` then ``overrides_calculated_entry()`` must be ``false``.
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def overrides_calculated_entry(self):
        """Tests if this is a manual entry that overrides a calculated entry.

        :return: ``true`` if this entry overrides a calculated entry, ``false`` otherwise. If ``true,`` then ``is_derived()`` must be ``false``.
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_overridden_calculated_entry_id(self):
        """Gets the calculated entry ``Id`` this entry overrides.

        :return: the calculated entry ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``overrides_derived_entry()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    overridden_calculated_entry_id = property(fget=get_overridden_calculated_entry_id)

    @abc.abstractmethod
    def get_overridden_calculated_entry(self):
        """Gets the calculated entry this entry overrides.

        :return: the calculated entry
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- ``overrides_calculated_entry()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntry

    overridden_calculated_entry = property(fget=get_overridden_calculated_entry)

    @abc.abstractmethod
    def is_ignored_for_calculations(self):
        """Tests if this is entry should be ignored in any averaging, scaling or curve calculation.

        :return: ``true`` if this entry is ignored, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_graded(self):
        """Tests if a grade or score has been assigned to this entry.

        Generally, an entry is created with a grade or score.

        :return: ``true`` if a grade has been assigned, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_grade_id(self):
        """Gets the grade ``Id`` in this entry if the grading system is based on grades.

        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``GradeSystem.isBasedOnGrades()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grade_id = property(fget=get_grade_id)

    @abc.abstractmethod
    def get_grade(self):
        """Gets the grade in this entry if the grading system is based on grades.

        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``GradeSystem.isBasedOnGrades()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Grade

    grade = property(fget=get_grade)

    @abc.abstractmethod
    def get_score(self):
        """Gets the score in this entry if the grading system is not based on grades.

        :return: the score
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``GradeSystem.isBasedOnGrades()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    score = property(fget=get_score)

    @abc.abstractmethod
    def get_time_graded(self):
        """Gets the time the gradeable object was graded.

        :return: the timestamp of the grading entry
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``is_derived()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    time_graded = property(fget=get_time_graded)

    @abc.abstractmethod
    def get_grader_id(self):
        """Gets the ``Id`` of the ``Resource`` that created this entry.

        :return: the ``Id`` of the ``Resource``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``is_derived()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grader_id = property(fget=get_grader_id)

    @abc.abstractmethod
    def get_grader(self):
        """Gets the ``Resource`` that created this entry.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- ``is_graded() is false or is_derived() is true``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.resource.Resource

    grader = property(fget=get_grader)

    @abc.abstractmethod
    def get_grading_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` that created this entry.

        :return: the ``Id`` of the ``Agent``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_graded()`` is ``false`` or ``is_derived()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grading_agent_id = property(fget=get_grading_agent_id)

    @abc.abstractmethod
    def get_grading_agent(self):
        """Gets the ``Agent`` that created this entry.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``is_graded() is false or is_derived() is true``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.Agent

    grading_agent = property(fget=get_grading_agent)

    @abc.abstractmethod
    def get_grade_entry_record(self, grade_entry_record_type):
        """Gets the grade entry record corresponding to the given ``GradeEntry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_entry_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(grade_entry_record_type)`` is ``true`` .

        :param grade_entry_record_type: the type of the record to retrieve
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the grade entry record
        :rtype: ``osid.grading.records.GradeEntryRecord``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntryRecord


class GradeEntryForm:
    """This is the form for creating and updating ``GradeEntries``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_ignored_for_calculations_metadata(self):
        """Gets the metadata for the ignore flag.

        :return: metadata for the ignore flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    ignored_for_calculations_metadata = property(fget=get_ignored_for_calculations_metadata)

    @abc.abstractmethod
    def set_ignored_for_calculations(self, ignore):
        """Sets the ignore for calculations flag.

        :param ignore: the new ignore flag
        :type ignore: ``boolean``
        :raise: ``InvalidArgument`` -- ``ignore`` is invalid
        :raise: ``NoAccess`` -- ``ignore`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ignored_for_calculations(self):
        """Clears the ignore for calculations flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ignored_for_calculations = property(fset=set_ignored_for_calculations, fdel=clear_ignored_for_calculations)

    @abc.abstractmethod
    def get_grade_metadata(self):
        """Gets the metadata for a grade.

        :return: metadata for the grade
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    grade_metadata = property(fget=get_grade_metadata)

    @abc.abstractmethod
    def set_grade(self, grade_id):
        """Sets the grade.

        :param grade_id: the new grade
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid or ``GradebookColumn.getGradeSystem().isBasedOnGrades()`` is ``false``
        :raise: ``NoAccess`` -- ``grade_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade(self):
        """Clears the grade.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade = property(fset=set_grade, fdel=clear_grade)

    @abc.abstractmethod
    def get_score_metadata(self):
        """Gets the metadata for a score.

        :return: metadata for the score
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    score_metadata = property(fget=get_score_metadata)

    @abc.abstractmethod
    def set_score(self, score):
        """Sets the score.

        :param score: the new score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid or ``GradebookColumn.getGradeSystem().isBasedOnGrades()`` is ``true``
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_score(self):
        """Clears the score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score = property(fset=set_score, fdel=clear_score)

    @abc.abstractmethod
    def get_grade_entry_form_record(self, grade_entry_record_type):
        """Gets the ``GradeEntryFormRecord`` corresponding to the given grade entry record ``Type``.

        :param grade_entry_record_type: the grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the grade entry form record
        :rtype: ``osid.grading.records.GradeEntryFormRecord``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradeEntryFormRecord


class GradeEntryList:
    """Like all ``OsidLists,``  ``GradeEntryList`` provides a means for accessing ``GradeEntry`` elements sequentially either one at a time or many at a time.

    Examples: while (gel.hasNext()) { GradeEntry entry =
    gel.getNextGradeEntry(); }

    or
      while (gel.hasNext()) {
           GradeEntry[] entries = gel.getNextGradeEntries(gel.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_grade_entry(self):
        """Gets the next ``GradeEntry`` in this list.

        :return: the next ``GradeEntry`` in this list. The ``has_next()`` method should be used to test that a next ``GradeEntry`` is available before calling this method.
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntry

    next_grade_entry = property(fget=get_next_grade_entry)

    @abc.abstractmethod
    def get_next_grade_entries(self, n):
        """Gets the next set of ``GradeEntry`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``GradeEntry`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``GradeEntry`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeEntry


class GradebookColumn:
    """A ``GradebookColumn`` represents a series of grade entries in a gradebook.

    Each GradeEntry in a column share the same ``GradeSystem``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_id(self):
        """Gets the ``GradeSystem Id`` in which this grade belongs.

        :return: the grade system ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)

    @abc.abstractmethod
    def get_grade_system(self):
        """Gets the ``GradeSystem`` in which this grade belongs.

        :return: the package grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)

    @abc.abstractmethod
    def get_gradebook_column_record(self, gradebook_column_record_type):
        """Gets the gradebook column record corresponding to the given ``GradeBookColumn`` record ``Type``.

        This method ie used to retrieve an object implementing the
        requested record. The ``gradebook_column_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_column_record_type)`` is ``true`` .

        :param gradebook_column_record_type: the type of the record to retrieve
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the gradebook column record
        :rtype: ``osid.grading.records.GradebookColumnRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnRecord


class GradebookColumnForm:
    """This is the form for creating and updating ``GradebookColumns``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_grade_system_metadata(self):
        """Gets the metadata for a grade system.

        :return: metadata for the grade system
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    grade_system_metadata = property(fget=get_grade_system_metadata)

    @abc.abstractmethod
    def set_grade_system(self, grade_system_id):
        """Sets the grade system.

        :param grade_system_id: the new grade system
        :type grade_system_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_system_id`` is invalid
        :raise: ``NoAccess`` -- ``grade_system_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_grade_system(self):
        """Clears the grade system.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system = property(fset=set_grade_system, fdel=clear_grade_system)

    @abc.abstractmethod
    def get_gradebook_column_form_record(self, gradebook_column_record_type):
        """Gets the ``GradebookColumnFormRecord`` corresponding to the given gradebook column record ``Type``.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the gradebook column form record
        :rtype: ``osid.grading.records.GradebookColumnFormRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnFormRecord


class GradebookColumnList:
    """Like all ``OsidLists,``  ``GradebookColumnList`` provides a means for accessing ``GradebookColumn`` elements sequentially either one at a time or many at a time.

    Examples: while (gcl.hasNext()) { GradebookColumn column =
    gcl.getNextGradebookColumn(); }

    or
      while (gcl.hasNext()) {
           GradebookColumn[] columns = gcl.getNextGradebookColumns(gcl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_gradebook_column(self):
        """Gets the next ``GradebookColumn`` in this list.

        :return: the next ``GradebookColumn`` in this list. The ``has_next()`` method should be used to test that a next ``GradebookColumn`` is available before calling this method.
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumn

    next_gradebook_column = property(fget=get_next_gradebook_column)

    @abc.abstractmethod
    def get_next_gradebook_columns(self, n):
        """Gets the next set of ``GradebookColumn`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``GradebookColumn`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``GradebookColumn`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumn


class GradebookColumnSummary:
    """A ``GradebookColumnSummary`` is a summary of all entries within a gradebook column."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_column_id(self):
        """Gets the ``Id`` of the ``GradebookColumn``.

        :return: the ``Id`` of the ``GradebookColumn``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    gradebook_column_id = property(fget=get_gradebook_column_id)

    @abc.abstractmethod
    def get_gradebook_column(self):
        """Gets the ``GradebookColumn``.

        :return: the ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookColumn

    gradebook_column = property(fget=get_gradebook_column)

    @abc.abstractmethod
    def get_mean(self):
        """Gets the mean score.

        If this system is based on grades, the mean output score is
        returned.

        :return: the mean score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    mean = property(fget=get_mean)

    @abc.abstractmethod
    def get_median(self):
        """Gets the median score.

        If this system is based on grades, the mean output score is
        returned.

        :return: the median score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    median = property(fget=get_median)

    @abc.abstractmethod
    def get_mode(self):
        """Gets the mode of the score.

        If this system is based on grades, the mode of the output score
        is returned.

        :return: the median score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    mode = property(fget=get_mode)

    @abc.abstractmethod
    def get_rms(self):
        """Gets the root mean square of the score.

        If this system is based on grades, the RMS of the output score
        is returned.

        :return: the median score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    rms = property(fget=get_rms)

    @abc.abstractmethod
    def get_standard_deviation(self):
        """Gets the standard deviation.

        If this system is based on grades, the spread of the output
        scores is returned.

        :return: the standard deviation
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    standard_deviation = property(fget=get_standard_deviation)

    @abc.abstractmethod
    def get_sum(self):
        """Gets the sum of the scores.

        If this system is based on grades, the sum of the output scores
        is returned.

        :return: the median score
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    sum = property(fget=get_sum)

    @abc.abstractmethod
    def get_gradebook_column_summary_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary record corresponding to the given ``GradebookColumnSummary`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_column_summary_record_type``
        may be the ``Type`` returned in ``get_record_types()`` or any of
        its parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_column_summary_record_type)`` is
        ``true`` .

        :param gradebook_column_summary_record_type: the type of the record to retrieve
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: the gradebook column summary record
        :rtype: ``osid.grading.records.GradebookColumnSummaryRecord``
        :raise: ``NullArgument`` -- ``gradebook_column_summary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_column_summary_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookColumnSummaryRecord


class Gradebook:
    """A gradebook defines a collection of grade entries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_record(self, gradebook_record_type):
        """Gets the gradebook record corresponding to the given ``Gradebook`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_record_type)`` is ``true`` .

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook record
        :rtype: ``osid.grading.records.GradebookRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookRecord


class GradebookForm:
    """This is the form for creating and updating ``Gradebooks``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook_form_record(self, gradebook_record_type):
        """Gets the ``GradebookFormRecord`` corresponding to the given gradebook record ``Type``.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook form record
        :rtype: ``osid.grading.records.GradebookFormRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.records.GradebookFormRecord


class GradebookList:
    """Like all ``OsidLists,``  ``GradebookList`` provides a means for accessing ``Gradebook`` elements sequentially either one at a time or many at a time.

    Examples: while (gl.hasNext()) { Gradebook gradebook =
    gl.getNextGradebook(); }

    or
      while (gl.hasNext()) {
           Gradebook[] gradebooks = gl.getNextGradebooks(gl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_gradebook(self):
        """Gets the next ``Gradebook`` in this list.

        :return: the next ``Gradebook`` in this list. The ``has_next()`` method should be used to test that a next ``Gradebook`` is available before calling this method.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Gradebook

    next_gradebook = property(fget=get_next_gradebook)

    @abc.abstractmethod
    def get_next_gradebooks(self, n):
        """Gets the next set of ``Gradebook`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Gradebook`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Gradebook`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Gradebook


class GradebookNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``GradebookHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gradebook(self):
        """Gets the ``Gradebook`` at this node.

        :return: the gradebook represented by this node
        :rtype: ``osid.grading.Gradebook``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    @abc.abstractmethod
    def get_parent_gradebook_nodes(self):
        """Gets the parents of this gradebook.

        :return: the parents of the ``id``
        :rtype: ``osid.grading.GradebookNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookNodeList

    parent_gradebook_nodes = property(fget=get_parent_gradebook_nodes)

    @abc.abstractmethod
    def get_child_gradebook_nodes(self):
        """Gets the children of this gradebook.

        :return: the children of this gradebook
        :rtype: ``osid.grading.GradebookNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookNodeList

    child_gradebook_nodes = property(fget=get_child_gradebook_nodes)


class GradebookNodeList:
    """Like all ``OsidLists,``  ``GradebookNodeList`` provides a means for accessing ``GradebookNode`` elements sequentially either one at a time or many at a time.

    Examples: while (gnl.hasNext()) { GradebookNode node =
    gnl.getNextGradebookNode(); }

    or
      while (gnl.hasNext()) {
           GradebookNode[] nodes = gnl.getNextGradebookNodes(gnl.available());
      }

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_gradebook_node(self):
        """Gets the next ``GradebookNode`` in this list.

        :return: the next ``GradebookNode`` in this list. The ``has_next()`` method should be used to test that a next ``GradebookNode`` is available before calling this method.
        :rtype: ``osid.grading.GradebookNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookNode

    next_gradebook_node = property(fget=get_next_gradebook_node)

    @abc.abstractmethod
    def get_next_gradebook_nodes(self, n):
        """Gets the next set of ``GradebookNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``GradebookNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``GradebookNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.GradebookNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.grading.GradebookNode
