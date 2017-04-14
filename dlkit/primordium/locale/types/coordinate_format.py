"""Enumerators for coordinate format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

JEFFS_COORDINATE_FORMAT_TYPES = {
    'DMS': 'Degree/Minute/Second'
}

TYPE_SET = {
    'JCRDFT': JEFFS_COORDINATE_FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'birdland.mit.edu',
            'namespace': 'coordinate format',
            'identifier': name,
            'domain': 'Currency Format Types',
            'display_name': JEFFS_COORDINATE_FORMAT_TYPES[name] + ' Coordinate Format Type',
            'display_label': JEFFS_COORDINATE_FORMAT_TYPES[name],
            'description': ('The type for the ' +
                            JEFFS_COORDINATE_FORMAT_TYPES[name] +
                            ' Geographic coordinate format.')
        }
    except KeyError:
        raise NotFound('CoordinateFormat Type: ' + name)
