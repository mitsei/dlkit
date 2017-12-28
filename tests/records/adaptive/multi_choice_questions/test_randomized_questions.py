import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.json_ import utilities as dlkit_utilities
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.records.adaptive.multi_choice_questions.randomized_questions import *

from ... import utilities


class TestMultiChoiceRandomizeChoicesQuestionFormRecord(unittest.TestCase):
    """Tests for MultiChoiceRandomizeChoicesQuestionFormRecord"""
    def setUp(self):
        self.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        self.osid_object_form._authority = 'TESTING.MIT.EDU'
        self.osid_object_form._namespace = 'records.Testing'

    def test_block_super_prevents_calling_initer(self):
        self.osid_object_form._min_string_length = 255
        form = utilities.add_class(self.osid_object_form,
                                   MultiChoiceRandomizeChoicesQuestionFormRecord,
                                   initialize=True)
        self.assertEqual(form._min_string_length, 255)

    def test_block_super_prevents_calling_init_metadata(self):
        self.osid_object_form._text_metadata = 'foo'
        form = utilities.add_class(self.osid_object_form,
                                   MultiChoiceRandomizeChoicesQuestionFormRecord,
                                   initialize=True)
        self.assertEqual(form._text_metadata, 'foo')

    def test_block_super_prevents_calling_init_map(self):
        self.osid_object_form._my_map['fileIds'] = {
            'label': {
                'assetContentId': '123'
            }
        }
        form = utilities.add_class(self.osid_object_form,
                                   MultiChoiceRandomizeChoicesQuestionFormRecord,
                                   initialize=True)
        self.assertEqual(form._my_map['fileIds'],
                         {
            'label': {
                'assetContentId': '123'
            }
        })
