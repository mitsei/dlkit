# -*- coding: utf-8 -*-
"""Enumerators for currency types"""

from dlkit.abstract_osid.osid.errors import NotFound

ISO_CURRENCY_TYPES = {
    # UAE Dirham #
    'AED': 'UAE Dirham',

    # Afghani #
    'AFN': 'Afghani',

    # Lek #
    'ALL': 'Lek',

    # Armenian Dram #
    'AMD': 'Armenian Dram',

    # Netherlands Antillean Guilder #
    'ANG': 'Netherlands Antillean Guilder',

    # Kwanza #
    'AOA': 'Kwanza',

    # Argentine Peso #
    'ARS': 'Argentine Peso',

    # Australian Dollar #
    'AUD': 'Australian Dollar',

    # Aruban Florin #
    'AWG': 'Aruban Florin',

    # Azerbaijanian Manat #
    'AZN': 'Azerbaijanian Manat',

    # Convertible Mark #
    'BAM': 'Convertible Mark',

    # Barbados Dollar #
    'BBD': 'Barbados Dollar',

    # Taka #
    'BDT': 'Taka',

    # Bulgarian Lev #
    'BGN': 'Bulgarian Lev',

    # Bahraini Dinar #
    'BHD': 'Bahraini Dinar',

    # Burundi Franc #
    'BIF': 'Burundi Franc',

    # Bermudian Dollar #
    'BMD': 'Bermudian Dollar',

    # Brunei Dollar #
    'BND': 'Brunei Dollar',

    # Boliviano #
    'BOB': 'Boliviano',

    # Mvdol #
    'BOV': 'Mvdol',

    # Brazilian Real #
    'BRL': 'Brazilian Real',

    # Bahamian Dollar #
    'BSD': 'Bahamian Dollar',

    # Ngultrum #
    'BTN': 'Ngultrum',

    # Pula #
    'BWP': 'Pula',

    # Belarussian Ruble #
    'BYR': 'Belarussian Ruble',

    # Belize Dollar #
    'BZD': 'Belize Dollar',

    # Canadian Dollar #
    'CAD': 'Canadian Dollar',

    # Congolese Franc #
    'CDF': 'Congolese Franc',

    # WIR Euro #
    'CHE': 'WIR Euro',

    # Swiss Franc #
    'CHF': 'Swiss Franc',

    # WIR Franc #
    'CHW': 'WIR Franc',

    # Unidades de fomento #
    'CLF': 'Unidades de fomento',

    # Chilean Peso #
    'CLP': 'Chilean Peso',

    # Yuan Renminbi #
    'CNY': 'Yuan Renminbi',

    # Colombian Peso #
    'COP': 'Colombian Peso',

    # Unidad de Valor Real #
    'COU': 'Unidad de Valor Real',

    # Costa Rican Colon #
    'CRC': 'Costa Rican Colon',

    # Peso Convertible #
    'CUC': 'Peso Convertible',

    # Cuban Peso #
    'CUP': 'Cuban Peso',

    # Cape Verde Escudo #
    'CVE': 'Cape Verde Escudo',

    # Czech Koruna #
    'CZK': 'Czech Koruna',

    # Djibouti Franc #
    'DJF': 'Djibouti Franc',

    # Danish Krone #
    'DKK': 'Danish Krone',

    # Dominican Peso #
    'DOP': 'Dominican Peso',

    # Algerian Dinar #
    'DZD': 'Algerian Dinar',

    # Egyptian Pound #
    'EGP': 'Egyptian Pound',

    # Nakfa #
    'ERN': 'Nakfa',

    # Ethiopian Birr #
    'ETB': 'Ethiopian Birr',

    # Euro #
    'EUR': 'Euro',

    # Fiji Dollar #
    'FJD': 'Fiji Dollar',

    # Falkland Islands Pound #
    'FKP': 'Falkland Islands Pound',

    # Pound Sterling #
    'GBP': 'Pound Sterling',

    # Lari #
    'GEL': 'Lari',

    # Ghana Cedi #
    'GHS': 'Ghana Cedi',

    # Gibraltar Pound #
    'GIP': 'Gibraltar Pound',

    # Dalasi #
    'GMD': 'Dalasi',

    # Guinea Franc #
    'GNF': 'Guinea Franc',

    # Quetzal #
    'GTQ': 'Quetzal',

    # Guyana Dollar #
    'GYD': 'Guyana Dollar',

    # Hong Kong Dollar #
    'HKD': 'Hong Kong Dollar',

    # Lempira #
    'HNL': 'Lempira',

    # Croatian Kuna #
    'HRK': 'Croatian Kuna',

    # Gourde #
    'HTG': 'Gourde',

    # Forint #
    'HUF': 'Forint',

    # Rupiah #
    'IDR': 'Rupiah',

    # New Israeli Sheqel #
    'ILS': 'New Israeli Sheqel',

    # Indian Rupee #
    'INR': 'Indian Rupee',

    # Iraqi Dinar #
    'IQD': 'Iraqi Dinar',

    # Iranian Rial #
    'IRR': 'Iranian Rial',

    # Iceland Krona #
    'ISK': 'Iceland Krona',

    # Jamaican Dollar #
    'JMD': 'Jamaican Dollar',

    # Jordanian Dinar #
    'JOD': 'Jordanian Dinar',

    # Yen #
    'JPY': 'Yen',

    # Kenyan Shilling #
    'KES': 'Kenyan Shilling',

    # Som #
    'KGS': 'Som',

    # Riel #
    'KHR': 'Riel',

    # Comoro Franc #
    'KMF': 'Comoro Franc',

    # North Korean Won #
    'KPW': 'North Korean Won',

    # Won #
    'KRW': 'Won',

    # Kuwaiti Dinar #
    'KWD': 'Kuwaiti Dinar',

    # Cayman Islands Dollar #
    'KYD': 'Cayman Islands Dollar',

    # Tenge #
    'KZT': 'Tenge',

    # Kip #
    'LAK': 'Kip',

    # Lebanese Pound #
    'LBP': 'Lebanese Pound',

    # Sri Lanka Rupee #
    'LKR': 'Sri Lanka Rupee',

    # Liberian Dollar #
    'LRD': 'Liberian Dollar',

    # Loti #
    'LSL': 'Loti',

    # Lithuanian Litas #
    'LTL': 'Lithuanian Litas',

    # Latvian Lats #
    'LVL': 'Latvian Lats',

    # Libyan Dinar #
    'LYD': 'Libyan Dinar',

    # Moroccan Dirham #
    'MAD': 'Moroccan Dirham',

    # Moldovan Leu #
    'MDL': 'Moldovan Leu',

    # Malagasy Ariary #
    'MGA': 'Malagasy Ariary',

    # Denar #
    'MKD': 'Denar',

    # Kyat #
    'MMK': 'Kyat',

    # Tugrik #
    'MNT': 'Tugrik',

    # Pataca #
    'MOP': 'Pataca',

    # Ouguiya #
    'MRO': 'Ouguiya',

    # Mauritius Rupee #
    'MUR': 'Mauritius Rupee',

    # Rufiyaa #
    'MVR': 'Rufiyaa',

    # Kwacha #
    'MWK': 'Kwacha',

    # Malaysian Ringgit #
    'MYR': 'Malaysian Ringgit',

    # Mozambique Metical #
    'MZN': 'Mozambique Metical',

    # Namibia Dollar #
    'NAD': 'Namibia Dollar',

    # Naira #
    'NGN': 'Naira',

    # Cordoba Oro #
    'NIO': 'Cordoba Oro',

    # Norwegian Krone #
    'NOK': 'Norwegian Krone',

    # Nepalese Rupee #
    'NPR': 'Nepalese Rupee',

    # New Zealand Dollar #
    'NZD': 'New Zealand Dollar',

    # Rial Omani #
    'OMR': 'Rial Omani',

    # Balboa #
    'PAB': 'Balboa',

    # Nuevo Sol #
    'PEN': 'Nuevo Sol',

    # Kina #
    'PGK': 'Kina',

    # Philippine Peso #
    'PHP': 'Philippine Peso',

    # Pakistan Rupee #
    'PKR': 'Pakistan Rupee',

    # Guarani #
    'PYG': 'Guarani',

    # Qatari Rial #
    'QAR': 'Qatari Rial',

    # New Romanian Leu #
    'RON': 'New Romanian Leu',

    # Serbian Dinar #
    'RSD': 'Serbian Dinar',

    # Russian Ruble #
    'RUB': 'Russian Ruble',

    # Rwanda Franc #
    'RWF': 'Rwanda Franc',

    # Saudi Riyal #
    'SAR': 'Saudi Riyal',

    # Seychelles Rupee #
    'SCR': 'Seychelles Rupee',

    # Sudanese Pound #
    'SDG': 'Sudanese Pound',

    # Swedish Krona #
    'SEK': 'Swedish Krona',

    # Singapore Dollar #
    'SGD': 'Singapore Dollar',

    # Saint Helena Pound #
    'SHP': 'Saint Helena Pound',

    # Leone #
    'SLL': 'Leone',

    # Somali Shilling #
    'SOS': 'Somali Shilling',

    # Surinam Dollar #
    'SRD': 'Surinam Dollar',

    # South Sudanese Pound #
    'SSP': 'South Sudanese Pound',

    # Dobra #
    'STD': 'Dobra',

    # El Salvador Colon #
    'SVC': 'El Salvador Colon',

    # Syrian Pound #
    'SYP': 'Syrian Pound',

    # Lilangeni #
    'SZL': 'Lilangeni',

    # Baht #
    'THB': 'Baht',

    # Somoni #
    'TJS': 'Somoni',

    # Turkmenistan New Manat #
    'TMT': 'Turkmenistan New Manat',

    # Tunisian Dinar #
    'TND': 'Tunisian Dinar',

    # Pa’anga #
    'TOP': 'Pa’anga',

    # Turkish Lira #
    'TRY': 'Turkish Lira',

    # Trinidad and Tobago Dollar #
    'TTD': 'Trinidad and Tobago Dollar',

    # New Taiwan Dollar #
    'TWD': 'New Taiwan Dollar',

    # Tanzanian Shilling #
    'TZS': 'Tanzanian Shilling',

    # Hryvnia #
    'UAH': 'Hryvnia',

    # Uganda Shilling #
    'UGX': 'Uganda Shilling',

    # US Dollar #
    'USD': 'US Dollar',

    # US Dollar (Next day) #
    'USN': 'US Dollar (Next day)',

    # US Dollar (Same day) #
    'USS': 'US Dollar (Same day)',

    # Uruguay Peso en Unidades Indexadas (URUIURUI) #
    'UYI': 'Uruguay Peso en Unidades Indexadas (URUIURUI)',

    # Peso Uruguayo #
    'UYU': 'Peso Uruguayo',

    # Uzbekistan Sum #
    'UZS': 'Uzbekistan Sum',

    # Bolivar Fuerte #
    'VEF': 'Bolivar Fuerte',

    # Dong #
    'VND': 'Dong',

    # Vatu #
    'VUV': 'Vatu',

    # Tala #
    'WST': 'Tala',

    # CFA Franc BEAC #
    'XAF': 'CFA Franc BEAC',

    # East Caribbean Dollar #
    'XCD': 'East Caribbean Dollar',

    # SDR (Special Drawing Right) #
    'XDR': 'SDR (Special Drawing Right)',

    # UIC-Franc #
    'XFU': 'UIC-Franc',

    # CFA Franc BCEAO #
    'XOF': 'CFA Franc BCEAO',

    # CFP Franc #
    'XPF': 'CFP Franc',

    # Yemeni Rial #
    'YER': 'Yemeni Rial',

    # Rand #
    'ZAR': 'Rand',

    # Zambian Kwacha #
    'ZMK': 'Zambian Kwacha',

    # Zimbabwe Dollar #
    'ZWL': 'Zimbabwe Dollar'
}

ISO_CURRENCY_ELEMENT_TYPES = {
    # Platinum #
    'XPT': 'Platinum',

    # Testing #
    'XTS': 'Testing',

    # Palladium #
    'XPD': 'Palladium',

    # Silver #
    'XAG': 'Silver',

    # Gold #
    'XAU': 'Gold',
}

TYPE_SET = {
    'ISOCT': ISO_CURRENCY_TYPES,
    'ISOCET': ISO_CURRENCY_ELEMENT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    if name in ISO_CURRENCY_TYPES:
        article = 'the '
        type_name = ISO_CURRENCY_TYPES[name]
    elif name in ISO_CURRENCY_ELEMENT_TYPES:
        article = ''
        type_name = ISO_CURRENCY_ELEMENT_TYPES[name]
    else:
        raise NotFound('Currency Type: ' + name)

    return {
        'authority': 'ISO',
        'namespace': '4217',
        'identifier': name,
        'domain': 'ISO Currency Types',
        'display_name': type_name + ' Currency Type',
        'display_label': type_name,
        'description': ('The ISO currency type for ' + article +
                        type_name + '.')
    }
