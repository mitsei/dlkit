"""Default metadata configurations for osid.osid"""

from .. import types
from ..primitives import Type
import datetime
DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))
DEFAULT_GENUS_TYPE = Type(**types.Genus().get_type_data('DEFAULT'))

# MIN_DATETIME = {
#     'year': datetime.datetime.min.year,
#     'month': datetime.datetime.min.month,
#     'day': datetime.datetime.min.day,
#     'hour': datetime.datetime.min.hour,
#     'minute': datetime.datetime.min.minute,
#     'second': datetime.datetime.min.second,
#     'microsecond': datetime.datetime.min.microsecond,
# }
#
# MAX_DATETIME = {
#     'year': datetime.datetime.max.year,
#     'month': datetime.datetime.max.month,
#     'day': datetime.datetime.max.day,
#     'hour': datetime.datetime.max.hour,
#     'minute': datetime.datetime.max.minute,
#     'second': datetime.datetime.max.second,
#     'microsecond': datetime.datetime.max.microsecond,
# }


def get_osid_form_mdata():
    """Return default mdata map for OsidForm"""
    return {
        'journal_comment': {
            'element_label': 'Journal Comment',
            'instructions': 'Optional form submission journal comment, 255 character maximum',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 256,
            'string_set': []
        }
    }

# OSID_FORM = {
#     'journal_comment': {
#         'element_label': 'Journal Comment',
#         'instructions': 'Optional form submission journal comment, 255 character maximum',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_string_values': [{
#             'text': '',
#             'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
#             'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
#             'formatTypeId': str(DEFAULT_FORMAT_TYPE),
#             }],
#         'syntax': 'STRING',
#         'minimum_string_length': 0,
#         'maximum_string_length': 256,
#         'string_set': []
#     }
# }


def get_osid_object_mdata():
    """Return default mdata map for OsidObject"""
    return {
        'display_name': {
            'element_label': 'Display Name',
            'instructions': 'Required, 255 character maximum',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 256,
            'string_set': []
        },
        'description': {
            'element_label': 'Description',
            'instructions': 'Optional',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        },
        'genus_type': {
            'element_label': 'Genus Type',
            'instructions': 'Required genus Type of type osid.type.Type',
            'required': True,
            'value': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_type_values': [str(DEFAULT_GENUS_TYPE)],
            'syntax': 'TYPE',
            'type_set': []
        }
    }

# OSID_OBJECT = {
#     'display_name': {
#         'element_label': 'Display Name',
#         'instructions': 'Required, 255 character maximum',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_string_values': [{
#             'text': '',
#             'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
#             'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
#             'formatTypeId': str(DEFAULT_FORMAT_TYPE),
#             }],
#         'syntax': 'STRING',
#         'minimum_string_length': 0,
#         'maximum_string_length': 256,
#         'string_set': []
#     },
#     'description': {
#         'element_label': 'Description',
#         'instructions': 'Optional',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_string_values': [{
#             'text': '',
#             'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
#             'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
#             'formatTypeId': str(DEFAULT_FORMAT_TYPE),
#             }],
#         'syntax': 'STRING',
#         'minimum_string_length': 0,
#         'maximum_string_length': 1024,
#         'string_set': []
#     },
#     'genus_type': {
#         'element_label': 'Genus Type',
#         'instructions': 'Required genus Type of type osid.type.Type',
#         'required': True,
#         'value': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_type_values': [str(DEFAULT_GENUS_TYPE)],
#         'syntax': 'TYPE',
#         'type_set': []
#     }
# }


def get_osid_temporal_mdata():
    """Return default mdata map for OsidTemporal"""
    return {
        'start_date': {
            'element_label': 'Start Date',
            'instructions': 'enter a valid datetime object.',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_date_time_values': [datetime.datetime.min],
            'syntax': 'DATETIME',
            'date_time_set': [],
        },
        'end_date': {
            'element_label': 'End Date',
            'instructions': 'enter a valid datetime object.',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_date_time_values': [datetime.datetime.max],
            'syntax': 'DATETIME',
            'date_time_set': [],
        }
    }

# OSID_TEMPORAL = {
#     'start_date': {
#         'element_label': 'Start Date',
#         'instructions': 'enter a valid datetime object.',
#         'required': True,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_date_time_values': [datetime.datetime.min],
#         'syntax': 'DATETIME',
#         'date_time_set': [],
#         },
#     'end_date': {
#         'element_label': 'End Date',
#         'instructions': 'enter a valid datetime object.',
#         'required': True,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_date_time_values': [datetime.datetime.max],
#         'syntax': 'DATETIME',
#         'date_time_set': [],
#     }
# }


def get_osid_containable_mdata():
    """Return default mdata map for OsidContainable"""
    return {
        'sequestered': {
            'element_label': 'sequestered',
            'instructions': 'enter either true or false.',
            'required': False,
            'read_only': False,
            'linked': False,
            'default_boolean_values': [False],
            'array': False,
            'syntax': 'BOOLEAN',
        }
    }

# OSID_CONTAINABLE = {
#     'sequestered': {
#         'element_label': 'sequestered',
#         'instructions': 'enter either true or false.',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'default_boolean_values': [False],
#         'array': False,
#         'syntax': 'BOOLEAN',
#     }
# }


def get_osid_sourceable_mdata():
    """Return default mdata map for OsidSourceable"""
    return {
        'provider': {
            'element_label': 'provider',
            'instructions': 'accepts an osid.id.Id object',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': [],
        },
        'branding': {
            'element_label': 'branding',
            'instructions': 'accepts an osid.id.Id object',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_id_values': [],
            'syntax': 'ID',
            'id_set': [],
        },
        'license': {
            'element_label': 'License',
            'instructions': 'Optional',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': None,
            'string_set': []
        }
    }

# OSID_SOURCEABLE = {
#     'provider': {
#         'element_label': 'provider',
#         'instructions': 'accepts an osid.id.Id object',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_id_values': [''],
#         'syntax': 'ID',
#         'id_set': [],
#     },
#     'branding': {
#         'element_label': 'branding',
#         'instructions': 'accepts an osid.id.Id object',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': True,
#         'default_id_values': [],
#         'syntax': 'ID',
#         'id_set': [],
#     },
#     'license': {
#         'element_label': 'License',
#         'instructions': 'Optional',
#         'required': False,
#         'read_only': False,
#         'linked': False,
#         'array': False,
#         'default_string_values': [{
#             'text': '',
#             'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
#             'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
#             'formatTypeId': str(DEFAULT_FORMAT_TYPE),
#             }],
#         'syntax': 'STRING',
#         'minimum_string_length': 0,
#         'maximum_string_length': None,
#         'string_set': []
#     }
# }
