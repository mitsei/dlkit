"""Type definition for Filesystem Asset Content"""

from .primitives import Type

FILESYSTEM_ASSET_CONTENT_RECORD_TYPE = Type(**{'authority': 'odl.mit.edu',
                                               'namespace': 'asset_content_record_type',
                                               'identifier': 'filesystem'})
