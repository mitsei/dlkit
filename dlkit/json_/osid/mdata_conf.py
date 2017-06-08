"""Metadata configurations for osid.osid"""

from .. import types
from ..primitives import Type
import datetime
DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))
DEFAULT_GENUS_TYPE = Type(**types.Genus().get_type_data('DEFAULT'))

MIN_DATETIME = {
    'year': datetime.datetime.min.year,
    'month': datetime.datetime.min.month,
    'day': datetime.datetime.min.day,
    'hour': datetime.datetime.min.hour,
    'minute': datetime.datetime.min.minute,
    'second': datetime.datetime.min.second,
    'microsecond': datetime.datetime.min.microsecond,
}

MAX_DATETIME = {
    'year': datetime.datetime.max.year,
    'month': datetime.datetime.max.month,
    'day': datetime.datetime.max.day,
    'hour': datetime.datetime.max.hour,
    'minute': datetime.datetime.max.minute,
    'second': datetime.datetime.max.second,
    'microsecond': datetime.datetime.max.microsecond,
}

JOURNAL_COMMENT = {
    'element_label': {
        'text': 'Journal Comment',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'Optional form submission journal comment, 255 character maximum',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
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

DISPLAY_NAME = {
    'element_label': {
        'text': 'Display Name',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'Required, 255 character maximum',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
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

DESCRIPTION = {
    'element_label': {
        'text': 'Description',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'Optional',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
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
}

GENUS_TYPE = {
    'element_label': {
        'text': 'Genus Type',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'Required genus Type of type osid.type.Type',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': True,
    'value': False,
    'read_only': False,
    'linked': False,
    'array': False,
    'default_type_values': [str(DEFAULT_GENUS_TYPE)],
    'syntax': 'TYPE',
    'type_set': []
}

START_DATE = {
    'element_label': {
        'text': 'Start Date',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'enter a valid datetime object.',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': True,
    'read_only': False,
    'linked': False,
    'array': False,
    'default_date_time_values': [MIN_DATETIME],
    'syntax': 'DATETIME',
    'date_time_set': [],
}

END_DATE = {
    'element_label': {
        'text': 'End Date',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'enter a valid datetime object.',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': True,
    'read_only': False,
    'linked': False,
    'array': False,
    'default_date_time_values': [MAX_DATETIME],
    'syntax': 'DATETIME',
    'date_time_set': [],
}

SEQUESTERED = {
    'element_label': {
        'text': 'sequestered',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'enter either true or false.',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': False,
    'read_only': False,
    'linked': False,
    'array': False,
    'syntax': 'BOOLEAN',
}

PROVIDER = {
    'element_label': {
        'text': 'provider',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'accepts an osid.id.Id object',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': False,
    'read_only': False,
    'linked': False,
    'array': False,
    'default_id_values': [''],
    'syntax': 'ID',
    'id_set': [],
}

BRANDING = {
    'element_label': {
        'text': 'branding',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'accepts an osid.id.Id object',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'required': False,
    'read_only': False,
    'linked': False,
    'array': True,
    'default_id_values': [],
    'syntax': 'ID',
    'id_set': [],
    'minimum_elements': 0,
    'maximum_elements': 999999999
}

LICENSE = {
    'element_label': {
        'text': 'License',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
    'instructions': {
        'text': 'Optional',
        'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
        'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
        'formatTypeId': str(DEFAULT_FORMAT_TYPE),
    },
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
