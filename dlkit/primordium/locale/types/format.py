"""Enumerators for format types"""
# -*- coding: utf-8 -*-

from dlkit.abstract_osid.osid.errors import NotFound

FORMAT_TYPES = {
    'ASCIIDOC': 'AsciiDoc',
    'CREOLE': 'Creole',
    'DOCBOOK': 'DocBook',
    'GROFF': 'Groff',
    'HTML': 'HTML',
    'LATEX': 'LaTeX',
    'MARKDOWN': 'Markdown',
    'MMD': 'MultiMarkdown',
    'NROFF': 'nroff',
    'PLAIN': 'plain',
    'REST': 'reStricturedText',
    'RUNOFF': 'RUNOFF',
    'SCRIBE': 'Scribe',
    'TEX': 'TeX',
    'TEXINFO': 'Texinfo',
    'TEXTILE': 'Textile',
    'TROFF': 'troff',
    'Z': 'ZFormat'
}

TYPE_SET = {
    'FT': FORMAT_TYPES
}


def get_type_data(name):
    """Return dictionary representation of type.

    Can be used to initialize primordium.type.primitives.Type

    """
    name = name.upper()
    try:
        return {
            'authority': 'okapia.net',
            'namespace': 'TextFormats',
            'identifier': name,
            'domain': 'DisplayText Formats',
            'display_name': FORMAT_TYPES[name] + ' Format Type',
            'display_label': FORMAT_TYPES[name],
            'description': ('The display text format type for the ' +
                            FORMAT_TYPES[name] + ' format.')
        }
    except KeyError:
        raise NotFound('Format Type:' + name)
