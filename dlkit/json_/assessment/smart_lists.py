"""Special osid list implementations"""

from .. import utilities
from dlkit.abstract_osid.assessment import objects as abc_assessment_objects
from ..osid import objects as osid_objects
from dlkit.primordium.osid.errors import BlockIteration


class AssessmentTakenSectionList(abc_assessment_objects.AssessmentSectionList, osid_objects.OsidList):
    """Blocking list that takes an AssessmentTaken and iterates through underlying Assessment Sections"""

    def __init__(self, assessment_taken, proxy=None, **kwargs):
        self._assessment_taken = assessment_taken
        self._assessment = assessment_taken.get_assessment_offered().get_assessment()
        self._sections_sequential = assessment_taken.get_assessment_offered().are_sections_sequential()
        if self._are_sections_sequential:
            osid_object.OsidList.__init__(self, self._assessment.get_sections(), proxy=proxy, **kwargs)
        else:
            pass

    def has_next(self):
        """Overrides osid_objects.OsidList.has_next()"""
        if self._sections_sequential:
            pass  # Do Somethign
            # mgr = utilities.
        else:
            return osid_objects.OsidList.has_next(self)

    def get_next_assessment_section(self):
        """Gets the next ``AssessmentSection`` in this list.

        return: (osid.assessment.AssessmentSection) - the next
                ``AssessmentSection`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentSection`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return next(self)

    def next(self):
        if self._sections_sequential:
            next_object = self._get_next_object(AssessmentSection)
        elif self.has_next and self.available == 0:
            raise BlockIteration()
        else:
            pass
            # next_object = ask self._assessment_taken???
        if str(next_object.get_id()) not in self._assessment_taken._my_map['sections']:
            pass

    __next__ = next

    next_assessment_section = property(fget=get_next_assessment_section)

    @utilities.arguments_not_none
    def get_next_assessment_sections(self, n):
        """Gets the next set of ``AssessmentSection`` elements in this list which must be less than or equal to the number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentSection``
                elements requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentSection) - an array of
                ``AssessmentSection`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_next_n(n)
