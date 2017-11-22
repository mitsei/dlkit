"""Mongo osid profile elements for osid service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by osid.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo osid'

DESCRIPTION = 'MongoDB based osid implementation'

<<<<<<< HEAD
VERSIONCOMPONENTS = [0, 1, 32]

RELEASEDATE = "2017-11-16"
=======
VERSIONCOMPONENTS = [0, 1, 89]

RELEASEDATE = "2017-11-21"
>>>>>>> jm/testing

SUPPORTS = ['# Remove the # when implementations exist:', '#supports_journal_rollback', '#supports_journal_branching']
