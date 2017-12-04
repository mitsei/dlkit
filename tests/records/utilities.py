from __future__ import unicode_literals

import sys


TEST_OBJECT_MAP = {
    "displayName": {
        "text": "Test object",
        "languageTypeId": "639-2%3AENG%40ISO",
        "formatTypeId": "TextFormats%3APLAIN%40okapia.net",
        "scriptTypeId": "15924%3ALATN%40ISO"
    },
    "recordTypeIds": [],
    "license": {
        "text": "",
        "languageTypeId": "639-2%3AENG%40ISO",
        "formatTypeId": "TextFormats%3APLAIN%40okapia.net",
        "scriptTypeId": "15924%3ALATN%40ISO"
    },
    "providerId": "",
    "brandingIds": [],
    "genusTypeId": "DEFAULT%3ADEFAULT%40DEFAULT",
    "type": "Object",
    "id": "testing.Object%3A577fcf75c89cd90cbd1216f8%40ODL.MIT.EDU",
    "description": {
        "text": "Test object",
        "languageTypeId": "639-2%3AENG%40ISO",
        "formatTypeId": "TextFormats%3APLAIN%40okapia.net",
        "scriptTypeId": "15924%3ALATN%40ISO"
    }
}


def add_class(original_object, new_class, initialize=False):
    """The records tests require that we instantiate simple objects for each record class. With the current
        record schema, where we modify the object's __class__.__bases__ instead of using .my_osid_object,
        this helper method takes care of adding the new record.

    Optional flag to run init_metadata and init_map"""
    object_name = original_object._namespace.split('.')[-1]
    if 'FormRecord' in str(new_class):
        object_name += 'Form'
    if sys.version_info < (3, 0, 0):
        object_name = str(object_name)
    original_object.__class__ = type(object_name,
                                     (new_class, original_object.__class__,), {})

    if initialize:
        new_class.__init__(original_object, block_super=True)
        if original_object._mdata is None:
            # Should only happen for tests for utils like MultiLanguageUtils
            # Typically the mdata gets initialized in the object form initers
            original_object._mdata = {}
        new_class._init_metadata(original_object, block_super=True)
        new_class._init_map(original_object, block_super=True)
    return original_object
