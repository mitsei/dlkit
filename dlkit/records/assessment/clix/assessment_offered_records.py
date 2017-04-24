from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata

from dlkit.runtime.primitives import Id
from dlkit.runtime.errors import NotFound,\
    IllegalState,\
    InvalidArgument,\
    NullArgument,\
    NoAccess

from ...osid.base_records import ObjectInitRecord


class NofMAssessmentOfferedRecord(ObjectInitRecord):
    """A record for an ``AssessmentOffered``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'n-of-m'
    ]


class NofMAssessmentOfferedFormRecord(osid_records.OsidRecord):
    """A record for an ``AssessmentOfferedForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'n-of-m'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(NofMAssessmentOfferedFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['nOfM'] = \
            self._n_of_m_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._n_of_m_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'nOfM'),
            'element_label': 'nOfM',
            'instructions': 'Student is expected to do N of M questions',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [-1],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }

    def get_n_of_m_metadata(self):
        """stub"""
        return Metadata(**self._n_of_m_metadata)

    def set_n_of_m(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_n_of_m_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_integer(value,
                                                          self.get_n_of_m_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['nOfM'] = value

    def clear_n_of_m(self):
        """stub"""
        if (self.get_n_of_m_metadata().is_read_only() or
                self.get_n_of_m_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['nOfM'] = \
            self._n_of_m_metadata['default_object_values'][0]

    n_of_m = property(fset=set_n_of_m, fdel=clear_n_of_m)
