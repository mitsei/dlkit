# -*- coding: utf-8 -*-
"""Enumerators for calendar types"""

from dlkit.abstract_osid.osid.errors import NotFound

CALENDAR_TYPES = {
    # Akan Calendar #
    'AKAN': 'Akan',

    # Bahai Calendar #
    'BAHAI': 'Bahai, Bahá\'í',

    # Bengali Calendar #
    'BENGALI': 'Bengali',

    # Berber Calendar #
    'BERBER': 'Berber',

    # Buddhist Calendar #
    'BUDDHIST': 'Buddhist',

    # Chinese Calendar #
    'CHINESE': 'Chinese',

    # Coptic Calendar #
    'COPTIC': 'Coptic',

    # Discordian Calendar #
    'DISCORDIAN': 'Discordian',

    # Ethiopian Calendar #
    'ETHIOPIAN': 'Ethiopian',

    # Gregorian Calendar #
    'GREGORIAN': 'Gregorian',

    # Hebrew Calendar #
    'HEBREW': 'Hebrew',

    # Hellenic Calendar #
    'HELLENIC': 'Hellenic',

    # Igbo Calendar #
    'IGBO': 'Igbo',

    # Indian Calendar #
    'INDIAN': 'Indian, Indian National',

    # ISO8601 Calendar #
    'ISO_8601': 'ISO8601, ISO 8601',

    # ISOWeekdate Calendar #
    'ISO_WEEKDATE': 'ISOWeekdate, ISO Week Date',

    # Islamic Calendar #
    'ISLAMIC': 'Islamic',

    # Japanese Calendar #
    'JAPANESE': 'Japanese',

    # Javanese Calendar #
    'JAVANESE': 'Javanese',

    # Juche Calendar #
    'JUCHE': 'Juche, Juche Era',

    # Jualian Calendar #
    'JULIAN': 'Jualian',

    # Kurdish Calendar #
    'KURDISH': 'Kurdish',

    # Malayalam Calendar #
    'MALAYALAM': 'Malayalam',

    # Nanakshahi Calendar #
    'NANAKSHAHI': 'Nanakshahi',

    # Nepali Calendar #
    'NEPALI': 'Nepali',

    # NepalSambat Calendar #
    'NEPAL_SAMBAT': 'NepalSambat, Nepal Sambat',

    # RevisedJulian Calendar #
    'REVISED_JULIAN': 'RevisedJulian, Revised Julian',

    # Romanian Calendar #
    'ROMANIAN': 'Romanian',

    # Rumi Calendar #
    'RUMI': 'Rumi',

    # Runic Calendar #
    'RUNIC': 'Runic',

    # Tamil Calendar #
    'TAMIL': 'Tamil',

    # ThaiLunar Calendar #
    'THAI_LUNAR': 'ThaiLunar, Thai Lunar',

    # ThaiSolar Calendar #
    'THAI_SOLAR': 'ThaiSolar, Thai Solar',

    # Tibetan Calendar #
    'TIBETAN': 'Tibetan',

    # Zoroastrian Calendar #
    'ZOROASTRIAN': 'Zoroastrian',

    # Xhosa Calendar #
    'XHOSA': 'Xhosa',

    # Yoruba Calendar #
    'YORUBA': 'Yoruba'
}

ANCIENT_CALENDAR_TYPES = {
    # Armenian Calendar #
    'ARMENIAN': 'Armenian',

    # Assyrian Calendar #
    'ASSYRIAN': 'Assyrian',

    # Attic Calendar #
    'ATTIC': 'Attic',

    # Aztec Calendar #
    'AZTEC': 'Aztec',

    # Babylonian Calendar #
    'BABYLONIAN': 'Babylonian',

    # Boeotian Calendar #
    'BOEOTIAN': 'Boeotian',

    # Bulgar Calendar #
    'BULGAR': 'Bulgar',

    # Byzantine Calendar #
    'BYZANTINE': 'Byzantine',

    # Coligny Calendar #
    'COLIGNY': 'Coligny',

    # Cretan Calendar #
    'CRETAN': 'Cretan',

    # Delphic Calendar #
    'DELPHIC': 'Delphic',

    # Egyptian Calendar #
    'EGYPTIAN': 'Egyptian',

    # Epirotic Calendar #
    'EPIROTIC': 'Epirotic',

    # Enoch Calendar #
    'ENOCH': 'Enoch',

    # Florentine Calendar #
    'FLORENTINE': 'Florentine',

    # FrenchRepublican Calendar #
    'FRENCH_REPUBLICAN': 'FrenchRepublican, French Republican',

    # Germanic Calendar #
    'GERMANIC': 'Germanic',

    # Gaelic Calendar #
    'GAELIC': 'Gaelic',

    # Laconian Calendar #
    'LACONIAN': 'Laconian',

    # Lithuanian Calendar #
    'LITHUANIAN': 'Lithuanian',

    # Macedonian Calendar #
    'MACEDONIAN': 'Macedonian, Ancient Macedonian',

    # Maya Calendar #
    'MAYA': 'Maya',

    # Minguo Calendar #
    'MINGUO': 'Minguo',

    # Pentecontad Calendar #
    'PENTECONTAD': 'Pentecontad',

    # RapaNui Calendar #
    'RAPA_NUI': 'RapaNui, Rapa Nui',

    # Rhodian Calendar #
    'RHODIAN': 'Rhodian',

    # Roman Calendar #
    'ROMAN': 'Roman',

    # Runic Calendar #
    'RUNIC': 'Runic',

    # Sicilian Calendar #
    'SICILIAN': 'Sicilian',

    # Soviet Calendar #
    'SOVIET': 'Soviet',

    # Swedish Calendar #
    'SWEDISH': 'Swedish'
}

ALTERNATE_CALENDAR_TYPES = {
    # 360-day Calendar #
    'C360': '360-day',

    # Astronomical Calendar #
    'ASTRONOMICAL': 'Astronomical',

    # Colonial Calendar #
    'COLONIAL': 'Colonial, Battlestar Galactica',

    # Common-Civil-Calendar-and-Time #
    'COMMON_CIVIL': 'CommonCivil, Common-Civil-Calendar-and-Time',

    # Darian Calendar #
    'DARIAN': 'Darian',

    # Discworld Calendar #
    'DISCWORLD': 'Discworld',

    # Hanke-Henry Permanent Calendar #
    'HANKE_HENRY': 'Hanke-Henry, Hanke-Henry Permanent',

    # holocene Calendar #
    'HOLOCENE': 'holocene',

    # InternationalFixed Calendar #
    'INTERNATIONAL_FIXED': 'InternationalFixed, International Fixed',

    # MiddleEarth Calendar #
    'MIDDLE_EARTH': 'MiddleEarth, Middle-earth',

    # Pax Calendar #
    'PAX': 'Pax',

    # Positivist Calendar #
    'POSITIVIST': 'Positivist',

    # Stardate Calendar #
    'STARDATE': 'Stardate',

    # Symmetry454 Calendar #
    'SYMMETRY454': 'Symmetry454',

    # Tranquility Calendar #
    'TRANQUILITY': 'Tranquility',

    # World Calendar #
    'WORLD': 'World',

    # WorldSeason Calendar #
    'WORLD_SEASON': 'WorldSeason, World Season'
}

TYPE_SET = {
    'CT': CALENDAR_TYPES,
    'ACT': ANCIENT_CALENDAR_TYPES,
    'ALTCT': ALTERNATE_CALENDAR_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    if name in CALENDAR_TYPES:
        domain = 'Calendar Types'
        calendar_name = CALENDAR_TYPES[name]
    elif name in ANCIENT_CALENDAR_TYPES:
        domain = 'Ancient Calendar Types'
        calendar_name = ANCIENT_CALENDAR_TYPES[name]
    elif name in ALTERNATE_CALENDAR_TYPES:
        domain = 'Alternative Calendar Types'
        calendar_name = ALTERNATE_CALENDAR_TYPES[name]
    else:
        raise NotFound('Calendar Type: ' + name)

    return {
        'authority': 'okapia.net',
        'namespace': 'calendar',
        'identifier': name,
        'domain': domain,
        'display_name': calendar_name + ' Calendar Type',
        'display_label': calendar_name,
        'description': ('The time type for the ' + calendar_name + ' calendar.')
    }
