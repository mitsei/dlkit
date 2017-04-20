"""
records.assessment.fbw.assessment_records.py
"""
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import NoAccess, InvalidArgument
from dlkit.primordium.id.primitives import Id

from ...osid.base_records import QueryInitRecord,\
    ObjectInitRecord


class AssessmentWithFollowOnPhaseRecord(ObjectInitRecord):
    """No new methods on the assessment record"""
    _implemented_record_type_identifiers = [
        'assessment-with-follow-on-phase'
    ]

    # show the new parameters?
    @property
    def spawned(self):
        return bool(self.my_osid_object._my_map['hasSpawnedFollowOnPhase'])


class AssessmentWithFollowOnPhaseFormRecord(ObjectInitRecord):
    """No new methods on the form record"""
    _implemented_record_type_identifiers = [
        'assessment-with-follow-on-phase'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(AssessmentWithFollowOnPhaseFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['hasSpawnedFollowOnPhase'] = \
            bool(self._follow_on_phase_metadata['default_boolean_values'][0])

    def _init_metadata(self):
        """stub"""
        self._follow_on_phase_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'has_spawned_follow_on_phase'),
            'element_label': 'Has Spawned Follow On Phase',
            'instructions': 'accepts a valid boolean',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [False],
            'syntax': 'BOOLEAN',
        }

    def get_follow_on_phase_metadata(self):
        """stub"""
        return Metadata(**self._follow_on_phase_metadata)

    def set_follow_on_phase_state(self, follow_on_phase_state):
        self.my_osid_object_form._my_map['hasSpawnedFollowOnPhase'] = bool(follow_on_phase_state)

    def clear_follow_on_phase_state(self):
        if (self.get_follow_on_phase_metadata().is_read_only() or
                self.get_follow_on_phase_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['hasSpawnedFollowOnPhase'] = \
            bool(self._follow_on_phase_metadata['default_boolean_values'][0])


class GeneratedAssessmentRecord(ObjectInitRecord):
    """No new methods on the assessment record"""
    _implemented_record_type_identifiers = [
        'generated-assessment'
    ]

    # show the new parameters?
    @property
    def source_assessment_taken_id(self):
        return Id(self.my_osid_object._my_map['sourceAssessmentTakenId'])


class GeneratedAssessmentFormRecord(ObjectInitRecord):
    """No new methods on the form record"""
    _implemented_record_type_identifiers = [
        'generated-assessment'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(GeneratedAssessmentFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['sourceAssessmentTakenId'] = \
            str(self._source_assessment_taken_id_metadata['default_id_values'][0])

    def _init_metadata(self):
        """stub"""
        self._source_assessment_taken_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'source_assessment_taken_id'),
            'element_label': 'Source Assessment Taken ID that generated this one',
            'instructions': 'accepts a valid OSID Id string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_source_assessment_taken_id_metadata(self):
        """stub"""
        return Metadata(**self._source_assessment_taken_id_metadata)

    def set_source_assessment_taken_id(self, assessment_taken_id):
        if not isinstance(assessment_taken_id, Id):
            raise InvalidArgument('assessment_taken_id')
        self.my_osid_object_form._my_map['sourceAssessmentTakenId'] = str(assessment_taken_id)

    def clear_source_assessment_taken_id(self):
        if (self.get_source_assessment_taken_id_metadata().is_read_only() or
                self.get_source_assessment_taken_id_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['sourceAssessmentTakenId'] = \
            str(self._source_assessment_taken_id_metadata['default_id_values'][0])


class GeneratedAssessmentQueryRecord(QueryInitRecord):
    """add ability to query by source assessment taken ID"""
    def match_source_assessment_taken_id(self, assessment_taken_id, match):
        if not isinstance(assessment_taken_id, Id):
            raise InvalidArgument('assessment_taken_id')
        self._my_osid_query._add_match('sourceAssessmentTakenId', str(assessment_taken_id), match)

    def clear_source_assessment_taken_id(self):
        self._my_osid_query._clear_terms('sourceAssessmentTakenId')
