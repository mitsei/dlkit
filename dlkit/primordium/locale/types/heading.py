"""Enumerators for heading types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

HEADING_TYPES = {
    'DEGREE': 'Degree'
}

TYPE_SET = {
    'HT': HEADING_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'okapia.net',
            'namespace': 'heading',
            'identifier': name,
            'domain': 'Headings',
            'display_name': HEADING_TYPES[name] + ' Heading Type',
            'display_label': HEADING_TYPES[name],
            'description': ('The heading type for the ' +
                            HEADING_TYPES[name] + ' heading.')
        }
    except KeyError:
        raise NotFound('Heading Type:' + name)
