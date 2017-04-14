"""Enumerators for numeric format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

# THIS NEEDS WORK!!!  in gnu format the #.# specifies places
# Can this numeric format enumerator take place argument?
GNU_BASIC_NUMERIC_FORMAT_TYPES = {
    'F8.2': 'F8.2 (3141.59, -3141.59)',
    'COMMA9.2': 'COMMA9.2 (3,141.59, -3,141.59)',
    'DOT9.2': 'DOT9.2 (3.141,59, -3.141,59)',
    'DOLLAR10.2': 'DOLLAR10.2 ($3,141.59, -$3,141.59)',
    'PCT9.2': 'PCT9.2 (3141.59%, -3141.59%)',
    'E8.1': 'E8.1, (3.1E+003, -3.1E+003)'
}

TYPE_SET = {
    'GNUBNFT': GNU_BASIC_NUMERIC_FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'gnu.org',
            'namespace': 'Basic Numeric Formats',
            'identifier': name,
            'domain': 'Numeric Format Types',
            'display_name': GNU_BASIC_NUMERIC_FORMAT_TYPES[name] + ' Numeric Format Type',
            'display_label': GNU_BASIC_NUMERIC_FORMAT_TYPES[name],
            'description': ('The type for the ' +
                            GNU_BASIC_NUMERIC_FORMAT_TYPES[name] +
                            ' numeric format.')
        }
    except IndexError:
        raise NotFound('NumericFormat Type: ' + name)
