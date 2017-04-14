"""Enumerators for time format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

JEFFS_TIME_FORMAT_TYPES = {
    'HHMMSS': '24 Hour Clock (hh:mm:ss)',
    'HHMMSSAMPM': '12 Hour Clock (hh:mm:ss am/pm)'
}

TYPE_SET = {
    'JTIMEFT': JEFFS_TIME_FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'birdland.mit.edu',
            'namespace': 'time format',
            'identifier': name,
            'domain': 'Time Format Types',
            'display_name': JEFFS_TIME_FORMAT_TYPES[name] + ' Time Format Type',
            'display_label': JEFFS_TIME_FORMAT_TYPES[name],
            'description': ('The time format type for ' +
                            JEFFS_TIME_FORMAT_TYPES[name])
        }
    except KeyError:
        raise NotFound('Time Format Type: ' + name)
