# -*- coding: utf-8 -*-
"""Enumerators for script types"""

from dlkit.abstract_osid.osid.errors import NotFound

ISO_SCRIPT_TYPES = {
    'AFAK': 'Afak',
    'ARAB': 'Arabic',
    'ARMI': 'ImperialAramaic, Imperial Aramaic',
    'ARMN': 'Armenian',
    'AVST': 'Avestan',
    'BALI': 'Balinese',
    'BAMU': 'Bamum',
    'BASS': 'BassaVah, Bassa Vah',
    'BATK': 'Batak',
    'BENG': 'Bengali',
    'BLIS': 'Bissymbols',
    'BOPO': 'Bopomofo',
    'BRAH': 'Brahmi',
    'BUGI': 'Buginese',
    'BUHD': 'Buhid',
    'CAKM': 'Chakma',
    'CANS': 'UCAS, Unified Canadian Aboriginal Syllabics',
    'CARI': 'Carian',
    'CHAM': 'Cham',
    'CHER': 'Cherokee',
    'CIRT': 'Cirth',
    'COPT': 'Coptic',
    'CPRT': 'Cypriot',
    'CYRL': 'Cyrillic',
    'DEVA': 'Devanagari',
    'DSRT': 'Deseret',
    'DUPL': 'Duployan',
    'EGYD': 'EgyptianDemotic, Egyptian Demotic',
    'EGYH': 'EgyptianHieratic, Egyptian Hieratic',
    'EGYP': 'EgyptianHieroglyphs, Egyptian Hieroglyphs',
    'ELBA': 'Elbasan',
    'ETHI': 'Ethopic',
    'GEOK': 'Khutsuri',
    'GEOR': 'Georgian',
    'GLAG': 'Glagolotic',
    'GOTH': 'Gothic',
    'GRAN': 'Grantha',
    'GREK': 'Greek',
    'GUJR': 'Gujarati',
    'GURU': 'Gurmukhi',
    'HANG': 'Hangul',
    'HANI': 'Han',
    'HANS': 'HanSimple, Han Simplified',
    'HANT': 'HanTraditional, Han Traditional',
    'HEBR': 'Hebrew',
    'HIRA': 'Hiragana',
    'HLUW': 'AnatolianHieroglyphs, Anatolian, Luwian, Hittite Hieroglyphs',
    'HMNG': 'PahawhHmong, Pahawh Hmong',
    'HRKT': 'HiraganaKatakana, Japanese Hiragana and Katakana',
    'HUNG': 'OldHungarian, Old Hungarian',
    'INDS': 'Indus',
    'Ital': 'OldItalic, Old Italic',
    'JAVA': 'Javanese',
    'JPAN': 'Japanese, Japanese Han, Hiragana, and Katakana',
    'JURC': 'Jurchen',
    'KALI': 'KayahLi, Kayah Li',
    'KANA': 'Katakana',
    'KHAR': 'Kharoshthi',
    'KHMR': 'Khmer',
    'KHOJ': 'Khojki',
    'KNDA': 'Kannada',
    'KORE': 'Korean, Koran Hangul and Han',
    'KPEL': 'Kpelle',
    'KTHI': 'Kaithi',
    'LANA': 'TaiTham, Tai Tham',
    'LAOO': 'Lao',
    'LATF': 'LatinFraktur, Latin Fra',
    'LATG': 'LatinGaelic, Latin Gaelic',
    'LATN': 'Latin',
    'LEPC': 'Lepcha',
    'LIMB': 'Limbu',
    'LINA': 'LinearA, Linear A',
    'LINB': 'LinearB, Linear B',
    'LISU': 'Lisu',
    'LOMA': 'Loma',
    'LYCI': 'Lycian',
    'LYDI': 'Lydian',
    'MAND': 'Mandaic',
    'MANI': 'Manichaean',
    'MAYA': 'Mayan, Mayan Hieroglyphs',
    'MEND': 'Mende',
    'MERC': 'MeroiticCursive, Meroitic Cursive',
    'MERO': 'MeroiticHieroglyphs, Meroitic Hieroglyphs',
    'MLYM': 'Malayalam',
    'MONG': 'Mongolian',
    'MOON': 'Moon',
    'MROO': 'Mro',
    'MTEI': 'MeiteiMayek, Meitei Mayek',
    'MYMR': 'Myanmar',
    'NARB': 'OldNorthArabian, Old North Arabian',
    'NBAT': 'Nabataean',
    'NKGB': 'NakhiGeba, Nakhi Geba',
    'NKOO': 'N\'Ko, N\'Ko',
    'NSHU': 'Nüshu",  "NüshuO',
    'OGAM': 'Ogham',
    'OLCK': 'OlChiki, Ol Chiki',
    'ORKH': 'OldTurkic, Old Turkic',
    'ORYA': 'Oriya',
    'OSMA': 'Osmanya',
    'PALM': 'Palmyrene',
    'PERM': 'OldPermic, OldPermic',
    'PHAG': 'Phags-pa',
    'PHLI': 'InscriptionalPahlavi, Inscriptional Pahlavi',
    'PHLP': 'Psalter Pahlavi, Psalter Pahlavi',
    'PHLV': 'Book Pahlavi, Book Pahlavi',
    'PHNX': 'Phoenician',
    'PLRD': 'Miao',
    'PRTI': 'InscriptionalParthian, Inscriptional Parthian',
    'RJNG': 'Rejang',
    'RORO': 'Rongorongo',
    'RUNR': 'Runic',
    'SAMR': 'Samaritan',
    'SARA': 'Sarati',
    'SARB': 'OldSouthArabian, Old South Arabian',
    'SAUR': 'Saurashtra',
    'SGNW': 'SignWriting',
    'SHAW': 'Shavian',
    'SHRD': 'Sharada',
    'SIND': 'Khudawadi',
    'SINH': 'Sinhala',
    'SORA': 'SoraSompeng, Sora Sompeng',
    'SUND': 'Sundanese',
    'SYLO': 'SylotiNagri, Syloti Nagri',
    'SYRC': 'Syriac',
    'SYRE': 'SyriacEstrangelo, Syriac Estrangelo',
    'SYRJ': 'SyriacWestern, Syriac Western',
    'SYRN': 'SyriacEastern, Syriac Eastern',
    'TAGB': 'Tagbanwa',
    'TAKR': 'Takri',
    'TALE': 'TaiLe, Tai Le',
    'TALU': 'NewTaiLue, New Tai Lue',
    'TAML': 'Tamil',
    'TANG': 'Tangut',
    'TAVT': 'TaiViet, Tai Viet',
    'TELU': 'Telugu',
    'TENG': 'Tengwar',
    'TFNG': 'Tifinagh',
    'TGLG': 'Tagalog',
    'THAA': 'Thaana',
    'THAI': 'Thai',
    'TIBT': 'Tibetan',
    'TIRH': 'Tirhuta',
    'UGAR': 'Ugaritic',
    'VAII': 'Vai',
    'VISP': 'VisibleSpeech, Visible Speech',
    'WARA': 'WarangCiti, Warang Citi',
    'WOLE': 'Woleai',
    'XPEO': 'OldPersian, Old Persian',
    'XSUX': 'Cuneiform',
    'YIII': 'Yi',
    'ZMTH': 'Mathematical, Mathematical Notation',
    'ZSYM': 'Symbols',
    'ZYYY': 'Undetermined, Undetermined Script',
    'ZZZZ': 'Uncoded, Uncoded Script'
}

TYPE_SET = {
    'ISOST': ISO_SCRIPT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'ISO',
            'namespace': '15924',
            'identifier': name,
            'domain': 'ISO Script Types',
            'display_name': ISO_SCRIPT_TYPES[name] + ' Script Type',
            'display_label': ISO_SCRIPT_TYPES[name],
            'description': ('The display text script type for the ' +
                            ISO_SCRIPT_TYPES[name] + ' script.')
        }
    except KeyError:
        raise NotFound('Script Type:' + name)
