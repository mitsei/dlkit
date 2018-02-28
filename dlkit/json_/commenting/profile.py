"""Mongo osid profile elements for commenting service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by commenting.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo commenting'

DESCRIPTION = 'MongoDB based commenting implementation'

VERSIONCOMPONENTS = [0, 1, 39]

RELEASEDATE = "2018-02-27"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_comment_lookup',
    # 'supports_rating_lookup',
    'supports_comment_query',
    # 'supports_comment_search',
    'supports_comment_admin',
    # 'supports_comment_notification',
    'supports_comment_book',
    'supports_comment_book_assignment',
    # 'supports_comment_smart_book',
    'supports_book_lookup',
    # 'supports_book_query',
    # 'supports_book_search',
    'supports_book_admin',
    # 'supports_book_notification',
    'supports_book_hierarchy',
    'supports_book_hierarchy_design',
    # 'supports_commenting_batch',
]
