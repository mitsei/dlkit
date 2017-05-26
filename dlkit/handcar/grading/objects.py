# -*- coding: utf-8 -*-

# This module contains all the Object classes used by the MIT Core Concept
# Catalog (MC3) Handcar based implementation of the OSID Learning Service.
# Note that it includes the core objects typically found in the osid
# package as well as the learning package objects for Objectives, Activities
# and ObjectiveBanks that inherit from the core obejcts.

import json
from ...abstract_osid.grading import objects as abc_grading_objects
from ..osid import objects as osid_objects
from ..osid import markers
from ..osid.metadata import Metadata
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import NullArgument, InvalidArgument, NotFound, NoAccess, IllegalState, OperationFailed, Unimplemented, Unsupported

INVALID = 0
VALID = 1


class Grade(abc_grading_objects.Grade, osid_objects.OsidObject):
    """A Grade.

    Grades represent qualified performance levels defined within some
    grading system.

    """
    _namespace = 'grading.Grade'

    def _get_grade_system_map(self, grade_system_identifier):
        if self._grade_system_map is not None:
            return self._grade_system_map
        else:
            raise Unimplemented()  # Handcar currently gives us no way to get a grade system by Id

    def get_grade_system_id(self):
        """Gets the GradeSystem Id in which this grade belongs.

        return: (osid.id.Id) - the grade system Id
        compliance: mandatory - This method must be implemented.

        """
        return Id(self._my_map['gradeSystemId'])

    def get_grade_system(self):
        """Gets the GradeSystem in which this grade belongs.

        return: (osid.grading.GradeSystem) - the grade system
        compliance: mandatory - This method must be implemented.

        """
        return GradeSystem(self._get_grade_system_mep())

    def get_input_score_start_range(self):
        """Gets the low end of the input score range equivalent to this
        grade.

        return: (decimal) - the start range
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['inputScoreStartRange']

    def get_input_score_end_range(self):
        """Gets the high end of the input score range equivalent to this
        grade.

        return: (decimal) - the end range
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['inputScoreEndRange']

    def get_output_score(self):
        """Gets the output score for this grade used for calculating
        cumultives or performing articulation.

        return: (decimal) - the output score
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['outputScore']

    def get_grade_record(self, grade_record_type=None):
        """Gets the grade record corresponding to the given Grade record
        Type.

        This method is used to retrieve an object implementing the
        requested record. The gradeRecordType may be the Type returned
        in get_record_types() or any of its parents in a Type hierarchy
        where hasRecordType(gradeRecordType) is true .

        arg:    gradeRecordType (osid.type.Type): the type of the record
                to retrieve
        return: (osid.grading.records.GradeRecord) - the grade record
        raise:  NullArgument - gradeRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(gradeRecordType) is false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()

    grade_system_id = property(get_grade_system_id)
    grade_system = property(get_grade_system)
    input_score_start_range = property(get_input_score_start_range)
    input_score_end_range = property(get_input_score_end_range)
    output_score = property(get_output_score)


class GradeList(abc_grading_objects.GradeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeList`` provides a means for accessing ``Grade`` elements sequentially either one at a time or many at a time.

    Examples: while (gl.hasNext()) { Grade grade = gl.getNextGrade(); }

    or
      while (gl.hasNext()) {
           Grade[] grades = gl.getNextGrades(gl.available());
      }
    """

    def get_next_grade(self):
        """Gets the next ``Grade`` in this list.

        return: (osid.grading.Grade) - the next ``Grade`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Grade`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        try:
            next_object = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        else:
            return next_object

    def next(self):
        try:
            next_object = osid_objects.OsidList.next(self)
        except StopIteration:
            raise
        except Exception:  # Need to specify exceptions here!
            raise OperationFailed()
        if isinstance(next_object, dict):
            next_object = Grade(next_object)
        return next_object

    __next__ = next

    next_grade = property(fget=get_next_grade)

    def get_next_grades(self, n=None):
        """Gets the next set of ``Grade`` elements in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Grade`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.grading.Grade) - an array of ``Grade``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """

        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(next(self))
                except Exception:  # Need to specify exceptions here!
                    raise OperationFailed()
                x += 1
            return next_list


class GradeSystem(abc_grading_objects.GradeSystem, osid_objects.OsidObject):
    """A GradeSystem represents a grading system.

    The system can be based on assigned Grades or based on a numeric
    scale.

    """
    _namespace = 'grading.GradeSystem'

    def is_based_on_grades(self):
        """Tests if the grading system is based on grades.

        return: (boolean) - true if the grading system is based on
                grades, false if the system is a numeric score
        compliance: mandatory - This method must be implemented.

        """
        return bool(self._my_map['grades'])

    def get_grade_ids(self):
        """Gets the grade Ids in this system ranked from highest to lowest.

        return: (osid.id.IdList) - the list of grades Ids
        raise:  IllegalState - is_based_on_grades() is false
        compliance: mandatory - This method must be implemented.

        """
        id_list = []
        for grade_map in self._my_map['grades']:
            id_list.append(Id(grade_map.id))
        if id_list == []:
            raise IllegalState()
        else:
            return IdList(id_list)

    def get_grades(self):
        """Gets the grades in this system ranked from highest to lowest.

        return: (osid.grading.GradeList) - the list of grades
        raise:  IllegalState - is_based_on_grades() is false
        raise:  OperationFailed - unable to complete request
        compliance: mandatory - This method must be implemented.

        """
        return GradeList(self._my_map['grades'])

    def get_lowest_numeric_score(self):
        """Gets the lowest number in a numeric grading system.

        return: (decimal) - the lowest number
        raise:  IllegalState - is_based_on_grades() is true
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['lowestNumericScore']

    def get_numeric_score_increment(self):
        """Gets the incremental step.

        return: (decimal) - the increment
        raise:  IllegalState - is_based_on_grades() is true
        compliance: mandatory - This method must be implemented.

        """
        raise Unimplemented()

    def get_highest_numeric_score(self):
        """Gets the highest number in a numeric grading system.

        return: (decimal) - the highest number
        raise:  IllegalState - is_based_on_grades() is true
        compliance: mandatory - This method must be implemented.

        """
        return self._my_map['highestNumericScore']

    def get_grade_system_record(self, grade_system_record_type=None):
        """Gets the grade system record corresponding to the given
        GradeSystem record Type.

        This method is used to retrieve an object implementing the
        requested record. The gradeSystemRecordType may be the Type
        returned in get_record_types() or any of its parents in a Type
        hierarchy where hasRecordType(gradeSystemRecordType) is true .

        arg:    gradeSystemRecordType (osid.type.Type): the type of the
                record to retrieve
        return: (osid.grading.records.GradeSystemRecord) - the grade
                system record
        raise:  NullArgument - gradeSystemRecordType is null
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - hasRecordType(gradeSystemRecordType) is
                false
        compliance: mandatory - This method must be implemented.

        """
        if not self.has_record_type():
            raise IllegalState()
        else:  # This should never get called.
            raise Unimplemented()

    grade_ids = property(get_grade_ids)
    grades = property(get_grades)
    lowest_numeric_score = property(get_lowest_numeric_score)
    numeric_score_increment = property(get_numeric_score_increment)
    highest_numeric_score = property(get_highest_numeric_score)
