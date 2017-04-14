"""Enumerators for calendar format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

JEFFS_CALENDAR_FORMAT_TYPES = {
    'MMDDYYYY': 'MM/DD/YYYY'
}

TYPE_SET = {
    'JCALFT': JEFFS_CALENDAR_FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'birdland.mit.edu',
            'namespace': 'calendar format',
            'identifier': name,
            'domain': 'Calendar Format Types',
            'display_name': JEFFS_CALENDAR_FORMAT_TYPES[name] + ' Calendar Format Type',
            'display_label': JEFFS_CALENDAR_FORMAT_TYPES[name],
            'description': ('The calendar format type for ' +
                            JEFFS_CALENDAR_FORMAT_TYPES[name])
        }
    except KeyError:
        raise NotFound('Calendar Format Type: ' + name)
