"""Type definition for AWS Asset Content"""

from .primitives import Type

AWS_ASSET_CONTENT_RECORD_TYPE = Type(**{'authority': 'odl.mit.edu',
                                        'namespace': 'asset_content_record_type',
                                        'identifier': 'amazon-web-services'})
