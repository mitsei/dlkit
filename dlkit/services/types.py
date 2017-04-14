"""Language types that are now elsewhere. Duplicate!"""
# -*- coding: utf-8 -*-
# pylint disable=too-few-public-arguments
from .osid_errors import NotFound
from .settings import LANGUAGETYPE, SCRIPTTYPE, FORMATTYPE


class Language(object):
    """Language type"""
    def get_type_data(self, name):
        """gets type dictionary object"""
        if name == 'DEFAULT':
            return LANGUAGETYPE
        else:
            raise NotFound('DEFAULT Language Type')


class Script(object):
    """Script type"""
    def get_type_data(self, name):
        """gets type dictionary object"""
        if name == 'DEFAULT':
            return SCRIPTTYPE
        else:
            raise NotFound('DEFAULT Script Type')


class Format(object):
    """Format type"""
    def get_type_data(self, name):
        """gets type dictionary object"""
        if name == 'DEFAULT':
            return FORMATTYPE
        else:
            raise NotFound('DEFAULT Format Type')
