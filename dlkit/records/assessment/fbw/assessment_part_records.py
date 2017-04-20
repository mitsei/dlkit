"""
records.assessment.fbw.assessment_part_records.py
"""
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import NoAccess, InvalidArgument
from dlkit.primordium.id.primitives import Id

from ...osid.base_records import QueryInitRecord,\
    ObjectInitRecord


class AssessmentPartWithLearningObjectiveRecord(ObjectInitRecord):
    """No new methods on the taken record"""
    _implemented_record_type_identifiers = [
        'learning-objective'
    ]

    # show the new parameters?
    @property
    def learning_objective_id(self):
        return self.my_osid_object._my_map['learningObjectiveId']

    @property
    def minimum_proficiency(self):
        return self.my_osid_object._my_map['minimumProficiency']


class AssessmentPartWithLearningObjectiveFormRecord(ObjectInitRecord):
    """No new methods on the form record"""
    _implemented_record_type_identifiers = [
        'learning-objective'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(AssessmentPartWithLearningObjectiveFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['learningObjectiveId'] = \
            str(self._learning_objective_id_metadata['default_id_values'][0])
        self.my_osid_object_form._my_map['minimumProficiency'] = \
            str(self._minimum_proficiency_metadata['default_id_values'][0])

    def _init_metadata(self):
        """stub"""
        self._learning_objective_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'learning_objective_id'),
            'element_label': 'Learning Objective Id',
            'instructions': 'accepts a valid OSID Id string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }
        self._minimum_proficiency_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'minimum_proficiency'),
            'element_label': 'Minimum Proficiency in the given Objective to "pass"',
            'instructions': 'accepts a valid OSID Id string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_learning_objective_id_metadata(self):
        """stub"""
        return Metadata(**self._learning_objective_id_metadata)

    def get_minimum_proficiency_metadata(self):
        """stub"""
        return Metadata(**self._minimum_proficiency_metadata)

    def set_learning_objective_id(self, learning_objective_id):
        self.my_osid_object_form._my_map['learningObjectiveId'] = str(learning_objective_id)

    def clear_learning_objective_id(self):
        if (self.get_learning_objective_id_metadata().is_read_only() or
                self.get_learning_objective_id_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['learningObjectiveId'] = \
            str(self._learning_objective_id_metadata['default_id_values'][0])

    def set_minimum_proficiency(self, minimum_proficiency):
        if not self.my_osid_object_form._is_valid_id(
                minimum_proficiency):
            raise InvalidArgument('minimumProficiency')
        self.my_osid_object_form._my_map['minimumProficiency'] = str(minimum_proficiency)

    def clear_minimum_proficiency(self):
        self.my_osid_object_form._my_map['minimumProficiency'] = \
            int(self._minimum_proficiency_metadata['default_id_values'][0])
