"""JSON osid metadata configurations for logging service."""

from .. import types
from ..primitives import Type

import datetime

MIN_DATETIME = {
    'year': datetime.datetime.min.year,
    'month': datetime.datetime.min.month,
    'day': datetime.datetime.min.day,
    'hour': datetime.datetime.min.hour,
    'minute': datetime.datetime.min.minute,
    'second': datetime.datetime.min.second,
    'microsecond': datetime.datetime.min.microsecond,
}
DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data("DEFAULT"))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data("DEFAULT"))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data("DEFAULT"))
DEFAULT_GENUS_TYPE = Type(**types.Genus().get_type_data("DEFAULT"))


def get_log_entry_mdata():
    """Return default mdata map for LogEntry"""
    return {
        'priority': {
            'element_label': 'priority',
            'instructions': 'accepts an osid.type.Type object',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_type_values': ['NoneType%3ANONE%40dlkit.mit.edu'],
            'syntax': 'TYPE',
            'type_set': [],
        },
        'timestamp': {
            'element_label': 'timestamp',
            'instructions': 'enter a valid datetime object.',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_date_time_values': [MIN_DATETIME],
            'syntax': 'DATETIME',
            'date_time_set': []
        },
        'agent': {
            'element_label': 'agent',
            'instructions': 'accepts an osid.id.Id object',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': [],
        },
    }


def get_log_mdata():
    """Return default mdata map for Log"""
    return {
    }
