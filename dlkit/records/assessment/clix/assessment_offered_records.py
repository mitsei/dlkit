from dlkit.json_ import types, utilities
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata

from dlkit.primordium.type.primitives import Type
from dlkit.runtime.primitives import Id
from dlkit.runtime.errors import NotFound,\
    IllegalState,\
    InvalidArgument,\
    NullArgument,\
    NoAccess

from ...osid.base_records import ObjectInitRecord


DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


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
            int(self._n_of_m_metadata['default_object_values'][0])

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
        if isinstance(value, bool):
            # because True / False are also int types...
            raise InvalidArgument('value must be integer')
        if value is not None and not isinstance(value, int):
            raise InvalidArgument('value must be integer')
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
            int(self._n_of_m_metadata['default_object_values'][0])

    n_of_m = property(fset=set_n_of_m, fdel=clear_n_of_m)


class UnlockPreviousButtonAssessmentOfferedRecord(ObjectInitRecord):
    """Offer a flag for the previous button setting, i.e. ``unlock_prev`` in OEA player"""
    _implemented_record_type_identifiers = [
        'unlock-previous-button'
    ]

    def has_unlock_previous(self):
        """stub"""
        if 'unlockPrevious' not in self.my_osid_object._my_map or \
                self.my_osid_object._my_map['unlockPrevious'] is None:
            return False
        return True

    def get_unlock_previous(self):
        """stub"""
        if self.has_unlock_previous():
            return self.my_osid_object._my_map['unlockPrevious']
        raise IllegalState()

    unlock_previous = property(fget=get_unlock_previous)


class UnlockPreviousButtonAssessmentOfferedFormRecord(osid_records.OsidRecord):
    """Offer a flag for the previous button setting, i.e. ``unlock_prev`` in OEA player"""

    _implemented_record_type_identifiers = [
        'unlock-previous-button'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(UnlockPreviousButtonAssessmentOfferedFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['unlockPrevious'] = \
            str(self._unlock_previous_metadata['default_string_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_string_length = None
        self._max_string_length = None
        self._unlock_previous_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'unlock_previous'),
            'element_label': 'unlock_previous',
            'instructions': 'Indicator to UI on how to treat the previous button',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': ['always'],
            'syntax': 'STRING',
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }

    def get_unlock_previous_metadata(self):
        """stub"""
        return Metadata(**self._unlock_previous_metadata)

    def set_unlock_previous(self, unlock_previous):
        """use a string -- for now, ``always`` and ``never`` are the options"""
        if unlock_previous is None:
            raise NullArgument('unlock_previous cannot be None')
        if unlock_previous is not None and not utilities.is_string(unlock_previous):
            raise InvalidArgument('unlock_previous must be a string')
        self.my_osid_object_form._my_map['unlockPrevious'] = unlock_previous

    def clear_unlock_previous(self):
        """stub"""
        if (self.get_unlock_previous_metadata().is_read_only() or
                self.get_unlock_previous_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['unlockPrevious'] = \
            str(self._unlock_previous_metadata['default_string_values'][0])
