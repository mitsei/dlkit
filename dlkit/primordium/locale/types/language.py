# -*- coding: utf-8 -*-

"""Enumerators for language types"""
# pylint: disable=too-many-lines
#    There are a LOT of languages

from dlkit.abstract_osid.osid.errors import NotFound

ISO_LANGUAGE_CODES = {
    'AA': 'AAR',
    'AB': 'ABK',
    'AF': 'AFR',
    'AK': 'AKA',
    'SQ': 'ALB',
    'AM': 'AMH',
    'AR': 'ARA',
    'AN': 'ARG',
    'HY': 'ARM',
    'AS': 'ASM',
    'AV': 'AVA',
    'AE': 'AVE',
    'AY': 'AYM',
    'AZ': 'AZE',
    'BA': 'BAK',
    'BM': 'BAM',
    'EU': 'BAQ',
    'BE': 'BEL',
    'BN': 'BEN',
    'BH': 'BIH',
    'BI': 'BIS',
    'BS': 'BOS',
    'BR': 'BRE',
    'BG': 'BUL',
    'MY': 'BUR',
    'CA': 'CAT',
    'CH': 'CHA',
    'CE': 'CHE',
    'ZH': 'CHI',
    'CU': 'CHU',
    'CV': 'CHV',
    'KW': 'COR',
    'CO': 'COS',
    'CR': 'CRE',
    'CS': 'CZE',
    'DA': 'DAN',
    'DV': 'DIV',
    'NL': 'DUT',
    'DZ': 'DZO',
    'EN': 'ENG',
    'EO': 'EPO',
    'ET': 'EST',
    'EE': 'EWE',
    'FO': 'FAO',
    'FJ': 'FIJ',
    'FI': 'FIN',
    'FR': 'FRE',
    'FY': 'FRY',
    'FF': 'FUL',
    'KA': 'GEO',
    'DE': 'GER',
    'GD': 'GLA',
    'GA': 'GLE',
    'GL': 'GLG',
    'GV': 'GLV',
    'EL': 'GRE',
    'GN': 'GRN',
    'GU': 'GUJ',
    'HT': 'HAT',
    'HA': 'HAU',
    'HE': 'HEB',
    'HZ': 'HER',
    'HI': 'HIN',
    'HO': 'HMO',
    'HR': 'HRV',
    'HU': 'HUN',
    'IG': 'IBO',
    'IS': 'ICE',
    'IO': 'IDO',
    'II': 'III',
    'IU': 'IKU',
    'IE': 'ILE',
    'IA': 'INA',
    'ID': 'IND',
    'IK': 'IPK',
    'IT': 'ITA',
    'JV': 'JAV',
    'JA': 'JPN',
    'KL': 'KAL',
    'KN': 'KAN',
    'KS': 'KAS',
    'KR': 'KAU',
    'KK': 'KAZ',
    'KM': 'KHM',
    'KI': 'KIK',
    'RW': 'KIN',
    'KY': 'KIR',
    'KV': 'KOM',
    'KG': 'KON',
    'KO': 'KOR',
    'KJ': 'KUA',
    'KU': 'KUR',
    'LO': 'LAO',
    'LA': 'LAT',
    'LV': 'LAV',
    'LI': 'LIM',
    'LN': 'LIN',
    'LT': 'LIT',
    'LB': 'LTZ',
    'LU': 'LUB',
    'LG': 'LUG',
    'MK': 'MAC',
    'MH': 'MAH',
    'ML': 'MAL',
    'MI': 'MAO',
    'MR': 'MAR',
    'MS': 'MAY',
    'MG': 'MLG',
    'MT': 'MLT',
    'MN': 'MON',
    'NA': 'NAU',
    'NV': 'NAV',
    'NR': 'NBL',
    'ND': 'NDE',
    'NG': 'NDO',
    'NE': 'NEP',
    'NN': 'NNO',
    'NB': 'NOB',
    'NO': 'NOR',
    'NY': 'NYA',
    'OC': 'OCI',
    'OJ': 'OJI',
    'OR': 'ORI',
    'OM': 'ORM',
    'OS': 'OSS',
    'PA': 'PAN',
    'FA': 'PER',
    'PI': 'PLI',
    'PL': 'POL',
    'PT': 'POR',
    'PS': 'PUS',
    'QU': 'QUE',
    'RM': 'ROH',
    'RO': 'RUM',
    'RN': 'RUN',
    'RU': 'RUS',
    'SG': 'SAG',
    'SA': 'SAN',
    'SI': 'SIN',
    'SK': 'SLO',
    'SL': 'SLV',
    'SE': 'SME',
    'SM': 'SMO',
    'SN': 'SNA',
    'SD': 'SND',
    'SO': 'SOM',
    'ST': 'SOT',
    'ES': 'SPA',
    'SC': 'SRD',
    'SR': 'SRP',
    'SS': 'SSW',
    'SU': 'SUN',
    'SW': 'SWA',
    'SV': 'SWE',
    'TY': 'TAH',
    'TA': 'TAM',
    'TT': 'TAT',
    'TE': 'TEL',
    'TG': 'TGK',
    'TL': 'TGL',
    'TH': 'THA',
    'BO': 'TIB',
    'TI': 'TIR',
    'TO': 'TON',
    'TN': 'TSN',
    'TS': 'TSO',
    'TK': 'TUK',
    'TR': 'TUR',
    'TW': 'TWI',
    'UG': 'UIG',
    'UK': 'UKR',
    'UR': 'URD',
    'UZ': 'UZB',
    'VE': 'VEN',
    'VI': 'VIE',
    'VO': 'VOL',
    'CY': 'WEL',
    'WA': 'WLN',
    'WO': 'WOL',
    'XH': 'XHO',
    'YI': 'YID',
    'YO': 'YOR',
    'ZA': 'ZHA',
    'ZU': 'ZUL'
}

ISO_MAJOR_LANGUAGE_TYPES = {
    'AAR': 'Afar',
    'ABK': 'Abkhazian',
    'ACE': 'Achinese',
    'ACH': 'Acoli',
    'ADA': 'Adangme',
    'ADY': 'Adyghe, Adygei',
    'AFR': 'Afrikaans',
    'AIN': 'Ainu',
    'ALE': 'Aleut',
    'ALT': 'Southern Altai',
    'AMH': 'Amharic',
    'ANP': 'Angika',
    'ARA': 'Arabic',
    'ARG': 'Aragonese',
    'ARM': 'Armenian',
    'ARN': 'Mapudungun, Mapuche',
    'ARP': 'Arapaho',
    'ARW': 'Arawak',
    'ASM': 'Assamese',
    'AST': 'Asturian, Bable, Leonese, Asturleonese',
    'AVA': 'Avaric',
    'AWA': 'Awadhi',
    'BAK': 'Bashkir',
    'BAL': 'Baluchi',
    'BAM': 'Bambara',
    'BAN': 'Balinese',
    'BAQ': 'Basque',
    'BAS': 'Basa',
    'BEJ': 'Beja, Bedawiyet',
    'BEL': 'Belarusian',
    'BEM': 'Bemba',
    'BEN': 'Bengali',
    'BHO': 'Bhojpuri',
    'BIN': 'Bini, Edo',
    'BIS': 'Bislama',
    'BLA': 'Siksika',
    'BNT': 'Bantu (Other)',
    'BOS': 'Bosnian',
    'BRA': 'Braj',
    'BRE': 'Breton',
    'BUG': 'Buginese',
    'BUL': 'Bulgarian',
    'BUR': 'Burmese',
    'BYN': 'Blin, Bilin',
    'CAD': 'Caddo',
    'CAR': 'Galibi Carib',
    'CAT': 'Catalan, Valencian',
    'CEB': 'Cebuano',
    'CHA': 'Chamorro',
    'CHE': 'Chechen',
    'CHI': 'Chinese',
    'CHK': 'Chuukese',
    'CHM': 'Mari',
    'CHN': 'Chinook jargon',
    'CHO': 'Choctaw',
    'CHP': 'Chipewyan, Dene Suline',
    'CHR': 'Cherokee',
    'CHV': 'Chuvash',
    'CHY': 'Cheyenne',
    'COR': 'Cornish',
    'COS': 'Corsican',
    'CPE': 'Creoles and pidgins, English based',
    'CPF': 'Creoles and pidgins, French-based',
    'CPP': 'Creoles and pidgins, Portuguese-based',
    'CRH': 'Crimean Tatar, Crimean Turkish',
    'CRP': 'Creoles and pidgins',
    'CSB': 'Kashubian',
    'CZE': 'Czech',
    'DAK': 'Dakota',
    'DAN': 'Danish',
    'DAR': 'Dargwa',
    'DGR': 'Dogrib',
    'DIV': 'Divehi, Dhivehi, Maldivian',
    'DOI': 'Dogri',
    'DSB': 'Lower Sorbian',
    'DUA': 'Duala',
    'DUT': 'Dutch, Flemish',
    'DYU': 'Dyula',
    'DZO': 'Dzongkha',
    'EFI': 'Efik',
    'EKA': 'Ekajuk',
    'ENG': 'English',
    'EPO': 'Esperanto',
    'EWE': 'Ewe',
    'EWO': 'Ewondo',
    'FAN': 'Fang',
    'FAO': 'Faroese',
    'FAT': 'Fanti',
    'FIJ': 'Fijian',
    'FIL': 'Filipino, Pilipino',
    'FIN': 'Finnish',
    'FON': 'Fon',
    'FRE': 'French',
    'FRR': 'Northern Frisian',
    'FRS': 'Eastern Frisian',
    'FRY': 'Western Frisian',
    'FUR': 'Friulian',
    'GAA': 'Ga',
    'GAY': 'Gayo',
    'GEO': 'Georgian',
    'GER': 'German',
    'GIL': 'Gilbertese',
    'GLA': 'Gaelic, Scottish Gaelic',
    'GLE': 'Irish',
    'GLG': 'Galician',
    'GLV': 'Manx',
    'GOR': 'Gorontalo',
    'GRC': 'Greek, Ancient (to 1453)',
    'GRE': 'Greek, Modern (1453-)',
    'GSW': 'Swiss German, Alemannic, Alsatian',
    'GUJ': 'Gujarati',
    'GWI': 'Gwich\'in',
    'HAT': 'Haitian, Haitian Creole',
    'HAU': 'Hausa',
    'HAW': 'Hawaiian',
    'HEB': 'Hebrew',
    'HER': 'Herero',
    'HIL': 'Hiligaynon',
    'HIN': 'Hindi',
    'HMO': 'Hiri Motu',
    'HRV': 'Croatian',
    'HSB': 'Upper Sorbian',
    'HUN': 'Hungarian',
    'HUP': 'Hupa',
    'IBA': 'Iban',
    'IBO': 'Igbo',
    'ICE': 'Icelandic',
    'III': 'Sichuan Yi, Nuosu',
    'ILO': 'Iloko',
    'IND': 'Indonesian',
    'INH': 'Ingush',
    'ITA': 'Italian',
    'JAV': 'Javanese',
    'JPN': 'Japanese',
    'JPR': 'Judeo-Persian',
    'KAA': 'Kara-Kalpak',
    'KAB': 'Kabyle',
    'KAC': 'Kachin, Jingpho',
    'KAL': 'Kalaallisut, Greenlandic',
    'KAM': 'Kamba',
    'KAN': 'Kannada',
    'KAS': 'Kashmiri',
    'KAZ': 'Kazakh',
    'KBD': 'Kabardian',
    'KHA': 'Khasi',
    'KHM': 'Central Khmer',
    'KHO': 'Khotanese, Sakan',
    'KIK': 'Kikuyu, Gikuyu',
    'KIN': 'Kinyarwanda',
    'KIR': 'Kirghiz, Kyrgyz',
    'KMB': 'Kimbundu',
    'KOR': 'Korean',
    'KOS': 'Kosraean',
    'KRC': 'Karachay-Balkar',
    'KRL': 'Karelian',
    'KRU': 'Kurukh',
    'KUA': 'Kuanyama, Kwanyama',
    'KUM': 'Kumyk',
    'KUT': 'Kutenai',
    'LAD': 'Ladino',
    'LAM': 'Lamba',
    'LAO': 'Lao',
    'LAV': 'Latvian',
    'LEZ': 'Lezghian',
    'LIM': 'Limburgan, Limburger, Limburgish',
    'LIN': 'Lingala',
    'LIT': 'Lithuanian',
    'LOL': 'Mongo',
    'LOZ': 'Lozi',
    'LTZ': 'Luxembourgish, Letzeburgesch',
    'LUA': 'Luba-Lulua',
    'LUB': 'Luba-Katanga',
    'LUG': 'Ganda',
    'LUI': 'Luiseno',
    'LUN': 'Lunda',
    'LUO': 'Luo (Kenya and Tanzania)',
    'LUS': 'Lushai',
    'MAC': 'Macedonian',
    'MAD': 'Madurese',
    'MAG': 'Magahi',
    'MAH': 'Marshallese',
    'MAI': 'Maithili',
    'MAK': 'Makasar',
    'MAL': 'Malayalam',
    'MAO': 'Maori',
    'MAR': 'Marathi',
    'MAS': 'Masai',
    'MDF': 'Moksha',
    'MDR': 'Mandar',
    'MEN': 'Mende',
    'MIC': 'Mi\'kmaq, Micmac',
    'MIN': 'Minangkabau',
    'MLT': 'Maltese',
    'MNC': 'Manchu',
    'MNI': 'Manipuri',
    'MOH': 'Mohawk',
    'MOS': 'Mossi',
    'MUS': 'Creek',
    'MWL': 'Mirandese',
    'MYV': 'Erzya',
    'NAP': 'Neapolitan',
    'NAU': 'Nauru',
    'NAV': 'Navajo, Navaho',
    'NBL': 'Ndebele, South, South Ndebele',
    'NDE': 'Ndebele, North, North Ndebele',
    'NDO': 'Ndonga',
    'NDS': 'Low German, Low Saxon, German, Low, Saxon, Low',
    'NEP': 'Nepali',
    'NEW': 'Nepal Bhasa, Newari',
    'NIA': 'Nias',
    'NIU': 'Niuean',
    'NNO': 'Norwegian Nynorsk, Nynorsk, Norwegian',
    'NOB': 'Bokmål, Norwegian, Norwegian Bokmål',
    'NOG': 'Nogai',
    'NQO': 'N\'Ko',
    'NSO': 'Pedi, Sepedi, Northern Sotho',
    'NWC': 'Classical Newari, Old Newari, Classical Nepal Bhasa',
    'NYA': 'Chichewa, Chewa, Nyanja',
    'NYM': 'Nyamwezi',
    'NYN': 'Nyankole',
    'NYO': 'Nyoro',
    'NZI': 'Nzima',
    'OCI': 'Occitan (post 1500), Provençal',
    'ORI': 'Oriya',
    'OSA': 'Osage',
    'OSS': 'Ossetian, Ossetic',
    'PAG': 'Pangasinan',
    'PAM': 'Pampanga, Kapampangan',
    'PAN': 'Panjabi, Punjabi',
    'PAP': 'Papiamento',
    'PAU': 'Palauan',
    'PER': 'Persian',
    'POL': 'Polish',
    'PON': 'Pohnpeian',
    'POR': 'Portuguese',
    'PUS': 'Pushto, Pashto',
    'RAP': 'Rapanui',
    'RAR': 'Rarotongan, Cook Islands Maori',
    'ROH': 'Romansh',
    'RUM': 'Romanian, Moldavian, Moldovan',
    'RUN': 'Rundi',
    'RUP': 'Aromanian, Arumanian, Macedo-Romanian',
    'RUS': 'Russian',
    'SAD': 'Sandawe',
    'SAG': 'Sango',
    'SAH': 'Yakut',
    'SAI': 'South American Indian (Other)',
    'SAS': 'Sasak',
    'SAT': 'Santali',
    'SCN': 'Sicilian',
    'SCO': 'Scots',
    'SEL': 'Selkup',
    'SHN': 'Shan',
    'SID': 'Sidamo',
    'SIN': 'Sinhala, Sinhalese',
    'SLO': 'Slovak',
    'SLV': 'Slovenian',
    'SMA': 'Southern Sami',
    'SME': 'Northern Sami',
    'SMJ': 'Lule Sami',
    'SMN': 'Inari Sami',
    'SMO': 'Samoan',
    'SMS': 'Skolt Sami',
    'SNA': 'Shona',
    'SND': 'Sindhi',
    'SNK': 'Soninke',
    'SOM': 'Somali',
    'SOT': 'Sotho, Southern',
    'SPA': 'Spanish, Castilian',
    'SRN': 'Sranan Tongo',
    'SRP': 'Serbian',
    'SRR': 'Serer',
    'SSW': 'Swati',
    'SUK': 'Sukuma',
    'SUN': 'Sundanese',
    'SUS': 'Susu',
    'SWE': 'Swedish',
    'TAH': 'Tahitian',
    'TAM': 'Tamil',
    'TAT': 'Tatar',
    'TEL': 'Telugu',
    'TEM': 'Timne',
    'TER': 'Tereno',
    'TET': 'Tetum',
    'TGK': 'Tajik',
    'TGL': 'Tagalog',
    'THA': 'Thai',
    'TIB': 'Tibetan',
    'TIG': 'Tigre',
    'TIR': 'Tigrinya',
    'TIV': 'Tiv',
    'TKL': 'Tokelau',
    'TLI': 'Tlingit',
    'TOG': 'Tonga (Nyasa)',
    'TON': 'Tonga (Tonga Islands)',
    'TPI': 'Tok Pisin',
    'TSI': 'Tsimshian',
    'TSN': 'Tswana',
    'TSO': 'Tsonga',
    'TUK': 'Turkmen',
    'TUM': 'Tumbuka',
    'TUR': 'Turkish',
    'TVL': 'Tuvalu',
    'TWI': 'Twi',
    'TYV': 'Tuvinian',
    'UDM': 'Udmurt',
    'UIG': 'Uighur, Uyghur',
    'UKR': 'Ukrainian',
    'UMB': 'Umbundu',
    'UND': 'Undetermined',
    'URD': 'Urdu',
    'VAI': 'Vai',
    'VEN': 'Venda',
    'VIE': 'Vietnamese',
    'VOT': 'Votic',
    'WAL': 'Walamo',
    'WAR': 'Waray',
    'WAS': 'Washo',
    'WEL': 'Welsh',
    'WLN': 'Walloon',
    'WOL': 'Wolof',
    'XAL': 'Kalmyk, Oirat',
    'XHO': 'Xhosa',
    'YAO': 'Yao',
    'YAP': 'Yapese',
    'YOR': 'Yoruba',
    'ZAP': 'Zapotec',
    'ZEN': 'Zenaga',
    'ZUL': 'Zulu',
    'ZUN': 'Zuni'
}

ISO_OTHER_LANGUAGE_TYPES = {
    # ISO Ancient Language Types
    'AKK': 'Akkadian',
    'ARC': 'Official Aramaic (700-300 BCE)',
    'AVE': 'Avestan',
    'CHU': 'Church Slavi',
    'CMS': 'Messapic',
    'ECR': 'Eteocretan',
    'ECY': 'Eteocypriot',
    'EGY': 'Egyptian (Ancient)',
    'ELX': 'Elamite',
    'ETT': 'Etruscan',
    'GEZ': 'Geez',
    'GMY': 'Mycenaean Greek',
    'GOT': 'Gothic',
    'HIT': 'Hittite',
    'HLU': 'Hieroglyphic Luwian',
    'HTX': 'Middle Hittite',
    'IMS': 'Marsian',
    'IMY': 'Milyan',
    'INM': 'Minaean',
    'KAW': 'Kawi',
    'KHO': 'Khotanese',
    'LAB': 'Linear A',
    'LAT': 'Lati',
    'LNG': 'Langobardic',
    'NEI': 'Neo-Hittite',
    'NRC': 'Nori',
    'NRP': 'North Picene',
    'NXM': 'Numidian',
    'OAR': 'Old Aramaic (up to 700 BCE)',
    'OBM': 'Moabite',
    'OCH': 'Old Chinese',
    'OHT': 'Old Hittite',
    'OMN': 'Minoan',
    'OOS': 'Old Ossetic',
    'OSC': 'Osca',
    'OTY': 'Old Tamil',
    'PAL': 'Pahlavi',
    'PGL': 'Primitive Irish',
    'PGN': 'Paelignian',
    'PHN': 'Phoenician',
    'PLI': 'Pali',
    'PLQ': 'Palaic',
    'PYX': 'Pyu (Myanmar',
    'SAN': 'Sanskrit',
    'SBV': 'Sabine',
    'SCX': 'Sice',
    'SOG': 'Sogdian',
    'SPX': 'South Picene',
    'SUX': 'Sumerian',
    'SXC': 'Sicanian',
    'SXO': 'Sorothaptic',
    'TXB': 'Tokharian B',
    'TXG': 'Tangut',
    'TXH': 'Thracian',
    'TXR': 'Tartessian',
    'UGA': 'Ugaritic',
    'UMC': 'Marrucinian',
    'XAE': 'Aequian',
    'XAQ': 'Aquitanian',
    'XBC': 'Bactrian',
    'XCC': 'Camunic',
    'XCE': 'Celtiberian',
    'XCG': 'Cisalpine Gaulish',
    'XCO': 'Chorasmian',
    'XCR': 'Carian',
    'XDC': 'Dacian',
    'XDM': 'Edomite',
    'XEB': 'Ebla',
    'XEP': 'Epi-Olmec',
    'XFA': 'Faliscan',
    'XHA': 'Harami',
    'XHD': 'Hadrami',
    'XHR': 'Hernican',
    'XHT': 'Hattic',
    'XHU': 'Hurrian',
    'XIB': 'Iberian',
    'XIL': 'Illyrian',
    'XIV': 'Indus Valley Languag',
    'XLC': 'Lycian',
    'XLD': 'Lydian',
    'XLE': 'Lemnian',
    'XLG': 'Ligurian (Ancient)',
    'XLI': 'Liburnian',
    'XLN': 'Alanic',
    'XLP': 'Lepontic',
    'XLS': 'Lusitanian',
    'XLU': 'Cuneiform Luwian',
    'XLY': 'Elymian',
    'XME': 'Median',
    'XMK': 'Ancient Macedonian',
    'XMR': 'Meroitic',
    'XNA': 'Ancient North Arabia',
    'XPG': 'Phrygian',
    'XPR': 'Parthian',
    'XPU': 'Puni',
    'XQT': 'Qatabanian',
    'XRR': 'Raetic',
    'XSA': 'Sabaean',
    'XSC': 'Scythian',
    'XSD': 'Sidetic',
    'XTG': 'Transalpine Gaulish',
    'XTO': 'Tokharian A',
    'XTR': 'Early Tripur',
    'XUM': 'Umbrian',
    'XUR': 'Urartian',
    'XVE': 'Venetic',
    'XVN': 'Vandalic',
    'XVO': 'Volscian',
    'XVS': 'Vestinian',
    'XZH': 'Zhang-Zhung',
    'YMS': 'Mysian',
    'ZSK': 'Kaskean',
    # ISO Constructed Language Types
    'AFH': 'Afrihili',
    'AVK': 'Kotava',
    'BZT': 'Brithenig',
    'DWS': 'Dutton World Speedwords',
    'EPO': 'Esperanto',
    'IDO': 'Ido',
    'IGS': 'Interglossa',
    'ILE': 'Interlingue',
    'INA': 'Interlingua (International Auxiliary Language Association)',
    'JBO': 'Lojban',
    'LDN': 'Láadan',
    'LFN': 'Lingua Franca Nova',
    'NEU': 'Neo',
    'NOV': 'Novial',
    'QYA': 'Quenya',
    'RMV': 'Romanova',
    'SJN': 'Sindarin',
    'TLH': 'Klingon',
    'VOL': 'Volapük',
    'ZBL': 'Blissymbols',
    # ISO Extinct Language Types
    'AAQ': 'Eastern Abnaki',
    'ABE': 'Western Abnaki',
    'ABJ': 'Aka-Bea',
    'ACI': 'Aka-Cari',
    'ACK': 'Aka-Kora',
    'ACL': 'Akar-Bale',
    'ACS': 'Acro',
    'AEA': 'Areb',
    'AES': 'Alse',
    'AGA': 'Aguano',
    'AHO': 'Ahom',
    'AID': 'Alngith',
    'AIT': 'Arikem',
    'AJW': 'Ajaw',
    'AKJ': 'Aka-Jeru',
    'AKM': 'Aka-Bo',
    'AKX': 'Aka-Kede',
    'AKY': 'Aka-Kol',
    'AMA': 'Amanayé',
    'AMZ': 'Atampaya',
    'ANA': 'Andaqui',
    'ANB': 'Ando',
    'ANS': 'Anserma',
    'AOH': 'Arma',
    'AOR': 'Aore',
    'APV': 'Alapmunte',
    'AQP': 'Atakapa',
    'ARD': 'Arabana',
    'ARJ': 'Arapaso',
    'ARU': 'Aruá (Amazonas State',
    'ASH': 'Abishira',
    'ATC': 'Atsahuaca',
    'AUO': 'Auyokawa',
    'AUX': 'Aurá',
    'AVM': 'Angkamuthi',
    'AVO': 'Agavotaguerr',
    'AVS': 'Aushiri',
    'AWG': 'Anguthimri',
    'AWK': 'Awabakal',
    'AXB': 'Abipon',
    'AXE': 'Ayerrerenge',
    'AXG': 'Mato Grosso Arára',
    'AYD': 'Ayabadhu',
    'AYY': 'Tayabas Ayta',
    'BAE': 'Baré',
    'BJB': 'Banggarla',
    'BJY': 'Bayali',
    'BLL': 'Biloxi',
    'BMN': 'Bina (Papua New Guinea)',
    'BOI': 'Barbareño',
    'BOW': 'Rema',
    'BPB': 'Barbacoas',
    'BPT': 'Barrow Point',
    'BQF': 'Baga Kaloum',
    'BRC': 'Berbice Creole Dutch',
    'BRK': 'Birked',
    'BSL': 'Basa-Gumna',
    'BSV': 'Baga Sobané',
    'BTE': 'Gamo-Ningi',
    'BUE': 'Beothuk',
    'BVV': 'Baniva',
    'BXI': 'Pirlatapa',
    'BYG': 'Bayg',
    'BYQ': 'Basa',
    'BYT': 'Bert',
    'BZR': 'Biri',
    'CAJ': 'Chan',
    'CAZ': 'Canichana',
    'CBE': 'Chipiajes',
    'CBH': 'Cagu',
    'CCA': 'Cauc',
    'CCR': 'Cacaopera',
    'CEA': 'Lower Chehalis',
    'CHB': 'Chibcha',
    'CHC': 'Catawba',
    'CHG': 'Chagatai',
    'CHT': 'Cholón',
    'CID': 'Chimariko',
    'CJH': 'Upper Chehalis',
    'CMM': 'Michigamea',
    'COB': 'Chicomucelte',
    'COJ': 'Cochimi',
    'COP': 'Coptic',
    'COQ': 'Coquille',
    'COW': 'Cowlitz',
    'COY': 'Coyaima',
    'CPG': 'Cappadocian Greek',
    'CRB': 'Island Carib',
    'CRF': 'Caramanta',
    'CRR': 'Carolina Algonquian',
    'CRZ': 'Cruzeño',
    'CSI': 'Coast Miwok',
    'CSS': 'Southern Ohlone',
    'CTM': 'Chitimacha',
    'CUM': 'Cumeral',
    'CUO': 'Cumanagoto',
    'CUP': 'Cupeño',
    'CYB': 'Cayubaba',
    'CZK': 'Knaanic',
    'DCR': 'Negerholland',
    'DDA': 'Dadi Dadi',
    'DDR': 'Dhudhuroa',
    'DEP': 'Pidgin Delaware',
    'DGN': 'Dagoman',
    'DGT': 'Ndrag\'ngith',
    'DGW': 'Daungwurrung',
    'DHU': 'Dhurga',
    'DIF': 'Dier',
    'DIT': 'Dirari',
    'DJA': 'Djadjawurrun',
    'DJF': 'Djangun',
    'DJL': 'Djiwarli',
    'DJW': 'Djaw',
    'DLM': 'Dalmatian',
    'DMD': 'Madhi Madhi',
    'DRQ': 'Dura',
    'DRR': 'Dororo',
    'DTH': 'Adithinngithigh',
    'DUY': 'Dicamay Agta',
    'DUZ': 'Duli',
    'DYB': 'Dyaberdyaber',
    'DYD': 'Dyugun',
    'DYG': 'Villa Viciosa Agta',
    'EEE': 'E',
    'ELI': 'Ndin',
    'EMM': 'Mamulique',
    'EMO': 'Emok',
    'EMY': 'Epigraphic Mayan',
    'ERR': 'Erre',
    'ESM': 'Esum',
    'ESQ': 'Esselen',
    'ETC': 'Etchemin',
    'EYA': 'Eyak',
    'FLN': 'Flinders Island',
    'FOS': 'Siraya',
    'FRK': 'Frankish',
    'GCD': 'Ganggalida',
    'GCE': 'Galice',
    'GDC': 'Gugu Badhun',
    'GFT': 'Gafa',
    'GGD': 'Gugadj',
    'GGK': 'Kungarakany',
    'GGR': 'Aghu Tharnggalu',
    'GHC': 'Hiberno-Scottish Gaelic',
    'GHO': 'Ghomara',
    'GKO': 'Kok-Nar',
    'GLI': 'Guliguli',
    'GLY': 'Gule',
    'GMA': 'Gambera',
    'GNC': 'Guanche',
    'GNL': 'Gangulu',
    'GNR': 'Gureng Guren',
    'GQN': 'Guana (Brazil)',
    'GUV': 'Gey',
    'GVY': 'Guyani',
    'GWM': 'Awngthim',
    'GWU': 'Guwamu',
    'GYF': 'Gungabula',
    'GYY': 'Guny',
    'HIB': 'Hibito',
    'HMK': 'Maek',
    'HOD': 'Holm',
    'HOM': 'Homa',
    'HOR': 'Horo',
    'HUW': 'Hukumina',
    'IFF': 'Ifo',
    'IHW': 'Bidhawal',
    'ILG': 'Garig-Ilgar',
    'IML': 'Milu',
    'INZ': 'Ineseño',
    'IOW': 'Iowa-Oto',
    'ITE': 'Iten',
    'JAN': 'Jandai',
    'JBW': 'Yawijibaya',
    'JGB': 'Ngbe',
    'JNG': 'Yangman',
    'JOR': 'Jorá',
    'JUC': 'Jurchen',
    'JUI': 'Ngadjuri',
    'JVD': 'Javindo',
    'KAE': 'Ketangalan',
    'KBA': 'Kalarko',
    'KBB': 'Kaxuiâna',
    'KBF': 'Kakauhua',
    'KDA': 'Worimi',
    'KGL': 'Kunggari',
    'KGM': 'Karipúna',
    'KII': 'Kitsai',
    'KLA': 'Klamath-Modo',
    'KOC': 'Kpat',
    'KOF': 'Kubi',
    'KOX': 'Coxima',
    'KPN': 'Kepkiriwát',
    'KQU': 'Sero',
    'KQZ': 'Korana',
    'KRB': 'Karkin',
    'KRK': 'Kere',
    'KTG': 'Kalkutung',
    'KTK': 'Kaniet',
    'KTQ': 'Katabaga',
    'KTW': 'Kato',
    'KUZ': 'Kunz',
    'KWZ': 'Kwad',
    'KXO': 'Kano',
    'KZK': 'Kazukuru',
    'KZW': 'Karirí-Xocó',
    'LAZ': 'Aribwatsa',
    'LBA': 'Lui',
    'LBY': 'Lamu-Lamu',
    'LEN': 'Lenc',
    'LHS': 'Mlahsö',
    'LLF': 'Hermit',
    'LLJ': 'Ladji Ladji',
    'LLK': 'Lela',
    'LMC': 'Limilngan',
    'LMZ': 'Lumbee',
    'LNJ': 'Leningitij',
    'LRE': 'Laurentian',
    'LRG': 'Laragia',
    'MBE': 'Molale',
    'MCL': 'Macaguaje',
    'MEM': 'Mangala',
    'MFW': 'Mulaha',
    'MJE': 'Muskum',
    'MJQ': 'Malaryan',
    'MJY': 'Mahican',
    'MKQ': 'Bay Miwok',
    'MMV': 'Miriti',
    'MNT': 'Maykulan',
    'MOD': 'Mobilian',
    'MOM': 'Mangue',
    'MRE': 'Martha\'s Vineyard Sign Language',
    'MSP': 'Maritsauá',
    'MTM': 'Mato',
    'MTN': 'Matagalpa',
    'MVB': 'Mattole',
    'MVL': 'Mbara (Australia)',
    'MWU': 'Mitt',
    'MXI': 'Mozarabic',
    'MYS': 'Mesmes',
    'MZO': 'Matipuhy',
    'NAY': 'Narrinyeri',
    'NBX': 'Ngur',
    'NCZ': 'Natchez',
    'NDF': 'Nadruvian',
    'NGV': 'Nagumi',
    'NHC': 'Tabasco Nahuatl',
    'NID': 'Ngandi',
    'NIG': 'Ngalakan',
    'NKP': 'Niuatoputapu',
    'NMP': 'Nimanbur',
    'NMR': 'Nimbari',
    'NMV': 'Ngamini',
    'NNR': 'Narungga',
    'NNT': 'Nanticoke',
    'NNV': 'Nugunu (Australia)',
    'NNY': 'Nyangga',
    'NOK': 'Nooksack',
    'NOM': 'Nocamán',
    'NRN': 'Norn',
    'NRT': 'Northern Kalapuya',
    'NRX': 'Ngurmbur',
    'NTS': 'Natagaimas',
    'NTW': 'Nottoway',
    'NUC': 'Nukuini',
    'NUG': 'Nungali',
    'NWA': 'Nawathinehen',
    'NWG': 'Ngayawung',
    'NWO': 'Nauo',
    'NWY': 'Nottoway-Meherrin',
    'NXN': 'Ngawun',
    'NXU': 'Nara',
    'NYP': 'Nyang\'i',
    'NYT': 'Nyawaygi',
    'NYV': 'Nyulnyul',
    'NYX': 'Nganyaywana',
    'OBI': 'Obispeño',
    'OFO': 'Ofo',
    'OKG': 'Koko Babangk',
    'OKJ': 'Oko-Juwoi',
    'OKL': 'Old Kentish Sign Language',
    'OMC': 'Mochica',
    'OME': 'Omejes',
    'OMK': 'Omok',
    'OMU': 'Omurano',
    'OPT': 'Opat',
    'OTI': 'Oti',
    'OTU': 'Otuk',
    'OUM': 'Ouma',
    'PAF': 'Paranawát',
    'PAX': 'Pankararé',
    'PAZ': 'Pankararú',
    'PBG': 'Paraujano',
    'PEB': 'Eastern Pomo',
    'PEF': 'Northeastern Pomo',
    'PEJ': 'Northern Pom',
    'PIE': 'Piro',
    'PIJ': 'Pija',
    'PIM': 'Powhatan',
    'PIT': 'Pitta Pitta',
    'PKC': 'Paekche',
    'PMC': 'Palumata',
    'PMD': 'Pallanganmiddang',
    'PMK': 'Pamlico',
    'PML': 'Lingua Franc',
    'PMZ': 'Southern Pam',
    'PNO': 'Panobo',
    'POD': 'Ponares',
    'POG': 'Potiguára',
    'POX': 'Polabian',
    'PPU': 'Papora',
    'PRR': 'Puri',
    'PSM': 'Pauserna',
    'PSY': 'Piscataway',
    'PTH': 'Pataxó Hã-Ha-Hãe',
    'PTW': 'Pentlatch',
    'PUQ': 'Puquina',
    'PUY': 'Purisimeño',
    'QUN': 'Quinault',
    'QWM': 'Kuman (Russia)',
    'QWT': 'Kwalhioqua-Tlatskana',
    'QYP': 'Quiripi',
    'RBP': 'Barababaraba',
    'REM': 'Remo',
    'RER': 'Rer Bare',
    'RGK': 'Rangkas',
    'RMD': 'Traveller Danish',
    'RNA': 'Runa',
    'RNR': 'NariNari',
    'RRT': 'Arritinngithigh',
    'SAM': 'Samaritan Aramaic',
    'SAR': 'Saraveca',
    'SDS': 'Sene',
    'SDT': 'Shuadit',
    'SGM': 'Sing',
    'SHT': 'Shasta',
    'SIA': 'Akkala Sami',
    'SIS': 'Siuslaw',
    'SJK': 'Kemi Sami',
    'SJS': 'Senhaja De Srair',
    'SKW': 'Skepi Creole Dutch',
    'SLN': 'Salinan',
    'SMC': 'Som',
    'SMP': 'Samaritan',
    'SMU': 'Somray',
    'SNH': 'Shinabo',
    'SNI': 'Sens',
    'SQN': 'Susquehannoc',
    'SUT': 'Subtiaba',
    'SVX': 'Skalvian',
    'SWW': 'Sowa',
    'SXK': 'Southern Kalapuya',
    'SXL': 'Selian',
    'SZD': 'Seru',
    'TAS': 'Tay Boi',
    'TBB': 'Tapeba',
    'TBH': 'Thurawal',
    'TBU': 'Tuba',
    'TCL': 'Taman (Myanmar)',
    'TEB': 'Tetete',
    'TEN': 'Tama (Colombia)',
    'TEP': 'Tepecano',
    'TGV': 'Tingui-Boto',
    'TGY': 'Togoyo',
    'TGZ': 'Tagalaka',
    'TIL': 'Tillamook',
    'TJM': 'Timucua',
    'TJN': 'Tonjon',
    'TJU': 'Tjurruru',
    'TKA': 'Truk',
    'TKF': 'Tukumanféd',
    'TKM': 'Takelma',
    'TME': 'Tremembé',
    'TMG': 'Ternateño',
    'TMR': 'Jewish Babylonian Aramaic (ca. 200-1200 CE)',
    'TMZ': 'Tamanaku',
    'TNQ': 'Tain',
    'TOE': 'Tomedes',
    'TPK': 'Tupinikin',
    'TPN': 'Tupinambá',
    'TPW': 'Tupí',
    'TQR': 'Torona',
    'TQW': 'Tonkawa',
    'TRY': 'Turung',
    'TRZ': 'Torá',
    'TTA': 'Tutelo',
    'TUD': 'Tuxá',
    'TUN': 'Tunica',
    'TUX': 'Tuxináwa',
    'TVY': 'Timor Pidgin',
    'TWA': 'Twan',
    'TWC': 'Teshenawa',
    'TWT': 'Turiwára',
    'TXC': 'Tsetsaut',
    'TYP': 'Thaypan',
    'UAM': 'Uamu',
    'UBY': 'Ubyk',
    'UGB': 'Kuku-Ugbanh',
    'UKY': 'Kuuk-Yak',
    'UMD': 'Umbindhamu',
    'UMG': 'Umbuygamu',
    'UMO': 'Umotína',
    'UMR': 'Umbugarla',
    'UNM': 'Unam',
    'URC': 'Urningangg',
    'URF': 'Uradhi',
    'URU': 'Urum',
    'URV': 'Uruava',
    'VEO': 'Ventureño',
    'VKA': 'Kariyarra',
    'VKM': 'Kamakan',
    'VMB': 'Mbabaram',
    'VMI': 'Miwa',
    'VML': 'Malgana',
    'VMS': 'Moksela',
    'VMU': 'Muluridyi',
    'VMV': 'Valley Maidu',
    'WAF': 'Wakoná',
    'WAM': 'Wampanoag',
    'WAO': 'Wapp',
    'WDU': 'Wadjigu',
    'WEA': 'Wewa',
    'WGA': 'Wagaya',
    'WGG': 'Wangganguru',
    'WGU': 'Wirangu',
    'WIE': 'Wik-Epa',
    'WIF': 'Wik-Keyangan',
    'WIL': 'Wilawila',
    'WIR': 'Wiraféd',
    'WIY': 'Wiyo',
    'WKA': 'Kw\'adza',
    'WKW': 'Wakawaka',
    'WLK': 'Wailaki',
    'WLU': 'Wuliwuli',
    'WLY': 'Waling',
    'WMA': 'Mawa (Nigeria)',
    'WMI': 'Wami',
    'WMN': 'Waamwang',
    'WND': 'Wandarang',
    'WNM': 'Wanggamala',
    'WOY': 'Weyt',
    'WRB': 'Warluwara',
    'WRG': 'Warungu',
    'WRH': 'Wiradhuri',
    'WRI': 'Wariyangga',
    'WRO': 'Worrorra',
    'WRW': 'Gugu Warra',
    'WRZ': 'Waray (Australia)',
    'WSU': 'Wasu',
    'WSV': 'Wotapuri-Katarqalai',
    'WUR': 'Wurrugu',
    'WWB': 'Wakabunga',
    'WWR': 'Warrwa',
    'XAD': 'Adai',
    'XAG': 'Aghwan',
    'XAI': 'Kaimbé',
    'XAM': '/Xam',
    'XAP': 'Apalachee',
    'XAR': 'Karami',
    'XAS': 'Kama',
    'XBA': 'Kamba (Brazil)',
    'XBB': 'Lower Burdekin',
    'XBN': 'Kenaboi',
    'XBO': 'Bolgarian',
    'XBW': 'Kambiwá',
    'XBX': 'Kabixí',
    'XCB': 'Cumbric',
    'XCH': 'Chemakum',
    'XCM': 'Comecrudo',
    'XCN': 'Cotoname',
    'XCU': 'Curonian',
    'XCV': 'Chuvantsy',
    'XCW': 'Coahuilteco',
    'XCY': 'Cayuse',
    'XEG': '//Xegwi',
    'XGB': 'Gbin',
    'XGF': 'Gabrielino-Fernandeñ',
    'XGL': 'Galindan',
    'XGR': 'Garz',
    'XHC': 'Hunnic',
    'XIN': 'Xinc',
    'XIP': 'Xipináwa',
    'XIR': 'Xiriâna',
    'XKR': 'Xakriabá',
    'XLB': 'Loup B',
    'XLO': 'Loup A',
    'XMP': 'Kuku-Mu\'inh',
    'XMQ': 'Kuku-Mangk',
    'XMU': 'Kamu',
    'XNT': 'Narragansett',
    'XOC': 'O\'chi\'chi\'',
    'XOO': 'Xukurú',
    'XPC': 'Pecheneg',
    'XPI': 'Pictish',
    'XPJ': 'Mpalitjanh',
    'XPM': 'Pumpokol',
    'XPN': 'Kapinawá',
    'XPO': 'Pochutec',
    'XPP': 'Puyo-Paekche',
    'XPQ': 'Mohegan-Pequot',
    'XPS': 'Pisidian',
    'XPY': 'Puyo',
    'XRM': 'Armazic',
    'XRN': 'Arin',
    'XRT': 'Aranama-Tamique',
    'XSO': 'Solano',
    'XSS': 'Assa',
    'XSV': 'Sudovian',
    'XTZ': 'Tasmanian',
    'XUD': 'Umiida',
    'XUN': 'Unggarranggu',
    'XUP': 'Upper Umpqua',
    'XUT': 'Kuthant',
    'XWC': 'Woccon',
    'XWO': 'Written Oira',
    'XXB': 'Boro (Ghana)',
    'XXR': 'Koropó',
    'XXT': 'Tambora',
    'XYL': 'Yalakalore',
    'XZM': 'Zemgalian',
    'YBN': 'Yabaâna',
    'YEI': 'Yeni',
    'YGA': 'Malyangapa',
    'YIL': 'Yindjilandji',
    'YLR': 'Yalarnnga',
    'YME': 'Yame',
    'YMT': 'Mator-Taygi-Karagas',
    'YND': 'Yandruwandha',
    'YNN': 'Yana',
    'YNU': 'Yahuna',
    'YOB': 'Yoba',
    'YOL': 'Yola',
    'YSC': 'Yassic',
    'YSR': 'Sirenik Yupi',
    'YUB': 'Yugambal',
    'YUG': 'Yug',
    'YUK': 'Yuki',
    'YVT': 'Yavitero',
    'YWW': 'Yawarawarga',
    'YXG': 'Yagara',
    'YXY': 'Yabula Yabul',
    'ZIR': 'Ziriya',
    'ZKB': 'Koibal',
    'ZKG': 'Koguryo',
    'ZKH': 'Khorezmian',
    'ZKK': 'Karankawa',
    'ZKO': 'Kott',
    'ZKP': 'São Paulo Kaingáng',
    'ZKT': 'Kita',
    'ZKU': 'Kaurna',
    'ZKV': 'Krevinian',
    'ZKZ': 'Khazar',
    'ZMC': 'Margany',
    'ZME': 'Mangerr',
    'ZMH': 'Makolkol',
    'ZMK': 'Mandandanyi',
    'ZMU': 'Muruwari',
    'ZMV': 'Mbariman-Gudhinma',
    'ZNK': 'Manangkari',
    'ZRA': 'Kara (Korea)',
    'ZRP': 'Zarphatic'
}

TYPE_SET = {
    'ISOMLT': ISO_MAJOR_LANGUAGE_TYPES,
    'ISOOLT': ISO_OTHER_LANGUAGE_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    if name in ISO_LANGUAGE_CODES:
        name = ISO_LANGUAGE_CODES[name]
    if name in ISO_MAJOR_LANGUAGE_TYPES:
        namespace = '639-2'
        lang_name = ISO_MAJOR_LANGUAGE_TYPES[name]
    elif name in ISO_OTHER_LANGUAGE_TYPES:
        namespace = '639-3'
        lang_name = ISO_OTHER_LANGUAGE_TYPES[name]
    else:
        raise NotFound('Language Type: ' + name)

    return {
        'authority': 'ISO',
        'namespace': namespace,
        'identifier': name,
        'domain': 'DisplayText Languages',
        'display_name': lang_name + ' Language Type',
        'display_label': lang_name,
        'description': ('The display text language type for the ' +
                        lang_name + ' language.')
    }
