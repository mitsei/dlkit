"""Enumerators for coordinate types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

CELESTIAL_COORDINATE_TYPES = {
    # Ecliptic Coordinate System #
    'ECLIPTIC': 'Ecliptic',

    # Equatorial Coordinate System #
    'EQUATORIAL': 'Equatorial',

    # Galactic Coordinate System #
    'GCS': 'Galactic',

    # Horizontal Altitude-Azimuth Coordinate System #
    'HORIZON': 'Horizon',

    # Supergalactic Coordinate System #
    'SUPERGALACTIC': 'Supergalactic'
}

GEOGRAPHIC_COORDINATE_TYPES = {
    # Earth Gravitational Model 1996 #
    'EGM96': 'EGM96, Geodetic Earth Gravitational Model 1996 Coordinate',

    # Geocentric #
    'GEOCENTRIC': 'Geocentric',

    # Geodetic Reference System 1980 #
    'GRS80': 'GRS80, Geodetic Reference System 80 Coordinate',

    # North American Datum of 1927 #
    'NAD27': 'NAD27, Geodetic North American Datum of 1927 Coordinate',

    # North American Datum of 1983 #
    'NAD83': 'NAD83, Geodetic North American Datum of 1983 Coordinate',

    # Maidenhead Locator System  #
    'MAIDENHEAD': 'Maidenhead, Maidenhead Locator',

    # Military Grid Reference System  #
    'MGRS': 'MGRS, Military Grid Reference',

    # World Geodetic System 1960  #
    'WGS60': 'WGS60, World Geodetic System of 1960 Coordinate',

    # World Geodetic System 1966  #
    'WGS66': 'WGS66, World Geodetic System of 1966 Coordinate',

    # World Geodetic System 1972  #
    'WGS72': 'WGS72, World Geodetic System of 1972 Coordinate',

    # World Geodetic System 1984 (used by GPS) #
    'WGS84': 'WGS84, World Geodetic System of 1984 Coordinate',

    # US Zip Codes  #
    'USPOSTAL': 'USPostal, United States Postal Code',

    # Universal Polar Stereographic System  #
    'UPS': 'UPS, Universal Polar Stereographic Coordinate',

    # Universal Transverse Mercator  System #
    'UTM': 'UTM, Universal Transverse Mercator Coordinate',

    # AT&T V and H System #
    'VH': 'V&H, AT&T V and H Coordinate',

    # VOR-DME System #
    'VOR': 'VOR-DME, VOR-DME Coordinate'
}

TYPE_SET = {
    'CCT': CELESTIAL_COORDINATE_TYPES,
    'GCT': GEOGRAPHIC_COORDINATE_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    if name in CELESTIAL_COORDINATE_TYPES:
        domain = 'Celestial Coordinate Systems'
        coordinate_name = CELESTIAL_COORDINATE_TYPES[name]
    elif name in GEOGRAPHIC_COORDINATE_TYPES:
        domain = 'Geographic Coordinate Systems'
        coordinate_name = GEOGRAPHIC_COORDINATE_TYPES[name]
    else:
        raise NotFound('Coordinate Type' + name)

    return {
        'authority': 'okapia.net',
        'namespace': 'coordinate',
        'identifier': name,
        'domain': domain,
        'display_name': coordinate_name + ' Type',
        'display_label': coordinate_name,
        'description': ('The type for the ' + coordinate_name + ' System.')
    }
