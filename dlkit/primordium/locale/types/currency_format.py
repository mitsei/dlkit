"""Enumerators for currency format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

JEFFS_CURRENCY_FORMAT_TYPES = {
    'US': 'US ($1,234.56)'
}

TYPE_SET = {
    'JCURFT': JEFFS_CURRENCY_FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'birdland.mit.edu',
            'namespace': 'currency format',
            'identifier': name,
            'domain': 'Currency Format Types',
            'display_name': JEFFS_CURRENCY_FORMAT_TYPES[name] + ' Currency Format Type',
            'display_label': JEFFS_CURRENCY_FORMAT_TYPES[name],
            'description': ('The format type for the ' +
                            JEFFS_CURRENCY_FORMAT_TYPES[name] + ' currency')
        }
    except KeyError:
        raise NotFound('Currency Format Type: ' + name)
