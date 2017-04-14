"""Enumerators for time types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

CELESTIAL_TIME_TYPES = {
    # Ephemeris Time #
    'ET': 'Ephemeris',

    # Barycentric Coordinate Time #
    'TCB': 'Barycentric Coordinate',

    # Barycentric Dynamic Time #
    'TDB': 'Barycentric Dynamic',

    # Geocentric Coordinate Time #
    'TCG': 'Geocentric Coordinate',

    # Terrestrial Dynamic Time #
    'TDT': 'Terrestrial Dynamic'
}

EARTH_TIME_TYPES = {
    # GPS Time #
    'GPS': 'GPS',

    # Metric Time #
    'METRIC': 'Metric',

    # International Atomic Time #
    'TAI': 'International Atomic',

    # Universal Time #
    'UT0': 'Universal (UT0)',

    # Universal Time #
    'UT1': 'Universal (UT1)',

    # Universal Time #
    'UT1R': 'Universal (UT1R)',

    # Universal Time #
    'UT2': 'Universal (UT2)',

    # Universal Time #
    'UT2R': 'Universal (UT2R)',

    # Coordinated Universal Time #
    'UTC': 'Coordinate Universal'
}

SUPER_FUN_TIME_TYPES = {
    # Frakkin' Centon Time #
    'COLONIAL': 'Colonial, Battlestar Galactica',

    # New Earth Time #
    'NET': 'NewEarth, New Earth',

    # Swatch Internet Time #
    'SWATCH': 'Swatch, Swatch Internet'
}

TYPE_SET = {
    'CTT': CELESTIAL_TIME_TYPES,
    'ETT': EARTH_TIME_TYPES,
    'SFTT': SUPER_FUN_TIME_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    if name in CELESTIAL_TIME_TYPES:
        namespace = 'time'
        domain = 'Celestial Time Systems'
        time_name = CELESTIAL_TIME_TYPES[name]
    elif name in EARTH_TIME_TYPES:
        namespace = 'time'
        domain = 'Earth Time Systems'
        time_name = EARTH_TIME_TYPES[name]
    elif name in SUPER_FUN_TIME_TYPES:
        namespace = 'time'
        domain = 'Alternative Time Systems'
        time_name = SUPER_FUN_TIME_TYPES[name]
    else:
        raise NotFound('Time Type: ' + name)

    return {
        'authority': 'okapia.net',
        'namespace': namespace,
        'identifier': name,
        'domain': domain,
        'display_name': time_name + ' Time Type',
        'display_label': time_name,
        'description': ('The time type for ' + time_name + ' time.')
    }
