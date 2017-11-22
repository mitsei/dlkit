"""
records.assessment.fbw.assessment_bank_records.py
"""
from dlkit.json_ import types
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import NoAccess
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from ...osid.base_records import QueryInitRecord,\
    ObjectInitRecord


DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


class AssessmentBankWithObjectiveBankRecord(ObjectInitRecord):
    """No new methods on the taken record"""
    _implemented_record_type_identifiers = [
        'objective-bank'
    ]

    # show the new parameters?


class AssessmentBankWithObjectiveBankFormRecord(ObjectInitRecord):
    """No new methods on the form record"""
    _implemented_record_type_identifiers = [
        'objective-bank'
    ]

    def __init__(self, **kwargs):
        super(AssessmentBankWithObjectiveBankFormRecord, self).__init__(**kwargs)
        self._objective_bank_id_metadata = None

    def _init_map(self, **kwargs):
        """stub"""
        super(AssessmentBankWithObjectiveBankFormRecord, self)._init_map(**kwargs)
        self._my_map['objectiveBankId'] = \
            self._objective_bank_id_metadata['default_id_values'][0]

    def _init_metadata(self, **kwargs):
        """stub"""
        super(AssessmentBankWithObjectiveBankFormRecord, self)._init_metadata(**kwargs)
        self._objective_bank_id_metadata = {
            'element_id': Id(self._authority,
                             self._namespace,
                             'objective_bank_id'),
            'element_label': 'Objective Bank Id',
            'instructions': 'accepts a valid OSID Id string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_objective_bank_id_metadata(self):
        """stub"""
        return Metadata(**self._objective_bank_id_metadata)

    def set_objective_bank_id(self, objective_bank_id):
        """stub"""
        self._my_map['objectiveBankId'] = str(objective_bank_id)

    def clear_objective_bank_id(self):
        """stub"""
        if (self.get_objective_bank_id_metadata().is_read_only() or
                self.get_objective_bank_id_metadata().is_required()):
            raise NoAccess()
        self._my_map['objectiveBankId'] = ''
