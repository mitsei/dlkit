"""Mongo osid profile elements for authentication.process service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by authentication.process.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo authentication.process'

DESCRIPTION = 'MongoDB based authentication.process implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_authentication_acquisition',
    # 'supports_authentication_validation',
    # 'supports_trust_lookup',
    # 'supports_circle_of_trust',
    # 'supports_challenge',
    # 'supports_credential_export',
]
