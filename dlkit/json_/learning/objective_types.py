"""Special types for learning service"""
# -*- coding: utf-8 -*-
# THIS STILL NEEDS LOTS OF WORK AND SOUL SEARCNING ###

from dlkit.abstract_osid.osid.errors import NotFound

OBJECTIVE_TYPES = {
    'TOPIC': 'Topic',
    'LO': 'Learning Outcome'
}

TYPE_SET = {'OT': OBJECTIVE_TYPES}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    try:
        return {
            'authority': 'birdland.mit.edu',
            'namespace': 'Genus Types',
            'identifier': name,
            'domain': 'Generic Types',
            'display_name': OBJECTIVE_TYPES[name] + ' Genus Type',
            'display_label': OBJECTIVE_TYPES[name],
            'description': ('The ' + OBJECTIVE_TYPES[name] +
                            ' Genus Type.')
        }
    except IndexError:
        raise NotFound('Objective Genus Type: ' + name)
