"""
records.repository.vcb.vcb_records.py
"""

from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.repository import record_templates as abc_repository_records
from dlkit.abstract_osid.osid.errors import InvalidArgument, NullArgument, NoAccess
from dlkit.primordium.id.primitives import Id


class TimeStampRecord(abc_repository_records.AssetContentRecord,
                      osid_records.OsidRecord):
    """A record for an ``AssetContent``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'vcb-video-timestamp'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(TimeStampRecord, self).__init__()

    def has_start_timestamp(self):
        """stub"""
        return bool(self.my_osid_object._my_map['startTimestamp'])

    def get_start_timestamp(self):
        """stub"""
        return self.my_osid_object._my_map['startTimestamp']

    def has_end_timestamp(self):
        """stub"""
        return bool(self.my_osid_object._my_map['endTimestamp'])

    def get_end_timestamp(self):
        """stub"""
        return self.my_osid_object._my_map['endTimestamp']


class TimeStampFormRecord(abc_repository_records.AssetContentFormRecord,
                          osid_records.OsidRecord):
    """A record for an ``AssetForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'vcb-video-timestamp'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(TimeStampFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['startTimestamp'] = \
            self._start_timestamp_metadata['default_integer_values'][0]
        self.my_osid_object_form._my_map['endTimestamp'] = \
            self._end_timestamp_metadata['default_integer_values'][0]

    def _init_metadata(self):
        """stub"""
        self._start_timestamp_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'start_timestamp'),
            'element_label': 'start timestamp',
            'instructions': 'enter an integer number of seconds for the start time',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'syntax': 'INTEGER',
            'minimum_integer': 0,
            'maximum_integer': None,
            'integer_set': [],
            'default_integer_values': [0]
        }
        self._end_timestamp_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'end_timestamp'),
            'element_label': 'end timestamp',
            'instructions': 'enter an integer number of seconds for the end time',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'syntax': 'INTEGER',
            'minimum_integer': 0,
            'maximum_integer': None,
            'integer_set': [],
            'default_integer_values': [0]
        }

    def get_start_timestamp_metadata(self):
        """stub"""
        return Metadata(**self._start_timestamp_metadata)

    def set_start_timestamp(self, start_timestamp=None):
        """stub"""
        if start_timestamp is None:
            raise NullArgument()
        if self.get_start_timestamp_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_integer(
                start_timestamp,
                self.get_start_timestamp_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['startTimestamp'] = start_timestamp

    def clear_start_timestamp(self):
        """stub"""
        if (self.get_start_timestamp_metadata().is_read_only() or
                self.get_start_timestamp_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['startTimestamp'] = \
            self.get_start_timestamp_metadata().get_default_integer_values()

    def get_end_timestamp_metadata(self):
        """stub"""
        return Metadata(**self._end_timestamp_metadata)

    def set_end_timestamp(self, end_timestamp=None):
        """stub"""
        if end_timestamp is None:
            raise NullArgument()
        if self.get_end_timestamp_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_integer(
                end_timestamp,
                self.get_end_timestamp_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['endTimestamp'] = end_timestamp

    def clear_end_timestamp(self):
        """stub"""
        if (self.get_end_timestamp_metadata().is_read_only() or
                self.get_end_timestamp_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['endTimestamp'] = \
            self.get_end_timestamp_metadata().get_default_integer_values()
