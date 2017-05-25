# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from dlkit.runtime import errors
from dlkit.runtime import configs
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.primordium import DataInputStream, Type, Id, DisplayText, InitializableLocale
from dlkit.primordium.locale.types import string as String
from dlkit.records.registry import ASSESSMENT_RECORD_TYPES, ITEM_RECORD_TYPES,\
    ANSWER_GENUS_TYPES, QUESTION_RECORD_TYPES, ANSWER_RECORD_TYPES,\
    ASSESSMENT_PART_RECORD_TYPES, ASSESSMENT_OFFERED_RECORD_TYPES,\
    ASSESSMENT_TAKEN_RECORD_TYPES, ASSET_CONTENT_GENUS_TYPES

from random import randint

try:
    # python 3
    from urllib.parse import unquote
except ImportError:
    # python 2
    from urllib import unquote

from .utilities.testing import DLKitTestCase, ABS_PATH, get_manager

SIMPLE_SEQUENCE_ASSESSMENT_RECORD = Type(**ASSESSMENT_RECORD_TYPES['simple-child-sequencing'])
WORDIGNORECASE_STRING_MATCH_TYPE = Type(**String.get_type_data('WORDIGNORECASE'))

MC_ANSWER_RECORD = Type(**ANSWER_RECORD_TYPES['multi-choice-with-files-and-feedback'])
MC_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-choice-with-text-and-files'])
MC_RANDOMIZED_RECORD = Type(**QUESTION_RECORD_TYPES['multi-choice-randomized'])
MC_RANDOMIZED_ITEM_RECORD = Type(**ITEM_RECORD_TYPES['multi-choice-randomized'])
MC_ITEM_RECORD = Type(**ITEM_RECORD_TYPES['multi-choice'])
PROVENANCE_ITEM_RECORD = Type(**ITEM_RECORD_TYPES['provenance'])
SOURCEABLE_RECORD = Type(**ITEM_RECORD_TYPES['sourceable'])
WRONG_ANSWER_ITEM_RECORD = Type(**ITEM_RECORD_TYPES['wrong-answer'])

RIGHT_ANSWER_GENUS = Type(**ANSWER_GENUS_TYPES['right-answer'])
WRONG_ANSWER_GENUS = Type(**ANSWER_GENUS_TYPES['wrong-answer'])

ASSESSMENT_SECTION_WITH_OBJECTIVE = Type(**ASSESSMENT_PART_RECORD_TYPES['objective-based'])
MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING = Type(**ASSESSMENT_PART_RECORD_TYPES['scaffold-down'])
SIMPLE_SEQUENCE_PART_RECORD_TYPE = Type(**ASSESSMENT_PART_RECORD_TYPES['simple-child-sequencing'])

ADVANCED_QUERY_TAKEN = Type(**ASSESSMENT_TAKEN_RECORD_TYPES['advanced-query'])
REVIEWABLE_OFFERED = Type(**ASSESSMENT_OFFERED_RECORD_TYPES['review-options'])
REVIEWABLE_TAKEN = Type(**ASSESSMENT_TAKEN_RECORD_TYPES['review-options'])

MULTI_LANGUAGE_OBJECT_RECORD = Type(**ITEM_RECORD_TYPES['multi-language'])
MULTI_LANGUAGE_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-language-question-string'])
MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-language-multiple-choice'])
MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-language-ordered-choice'])
MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-language-inline-choice'])
RANDOMIZED_INLINE_CHOICE_ITEM_RECORD = Type(**ITEM_RECORD_TYPES['qti-inline-choice'])
QTI_QUESTION_RECORD = Type(**QUESTION_RECORD_TYPES['qti'])
MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD = Type(**ANSWER_RECORD_TYPES['multi-language-answer-with-feedback'])
MULTI_LANGUAGE_TEXT_INTERACTION_RECORD = Type(**QUESTION_RECORD_TYPES['multi-language-text-interaction'])

FBW_PHASE_I_ASSESSMENT_RECORD = Type(**ASSESSMENT_RECORD_TYPES['fbw-phase-i'])
FBW_PHASE_II_ASSESSMENT_RECORD = Type(**ASSESSMENT_RECORD_TYPES['fbw-phase-ii'])

OV_SET_SMALL_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['ortho-view-set-small'])
OV_SET_LARGE_ASSET_CONTENT_TYPE = Type(**ASSET_CONTENT_GENUS_TYPES['ortho-view-set-large'])


class EdXTests(DLKitTestCase):
    def setUp(self):
        super(EdXTests, self).setUp()

        self._bank = self._get_test_bank()

    def tearDown(self):
        """
        """
        super(EdXTests, self).tearDown()


class EdXMultiChoiceTests(EdXTests):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([self.item_type])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        form.set_genus_type(self.item_genus_type)
        form.add_text('Please answer the question.', 'questionString')
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [self.question_type])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        question_form.set_text('Please answer the question.')
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [self.answer_type])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def set_item_irt(self, item):
        self.irt = {
            'difficulty': -2.1,
            'discrimination': 1.5
        }

        form = self._bank.get_item_form_for_update(item.ident)
        form.set_difficulty_value(self.irt['difficulty'])
        form.set_discrimination_value(self.irt['discrimination'])
        return self._bank.update_item(form)

    def setUp(self):
        super(EdXMultiChoiceTests, self).setUp()

        self.item_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'item-record-type',
            'identifier': 'edx_item',
            'display_name': 'edX Item',
            'display_label': 'edX Item',
            'description': 'Assessment Item record extension for edX based Items',
            'domain': 'assessment.Item',
        })
        self.item_genus_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'item-genus-type',
            'identifier': 'edx-multi-choice-problem-type',
            'display_name': 'edX Multi-Choice Problem Type',
            'display_label': 'edX Multi-Choice Problem Type',
            'description': 'An assessment item for an edX multiple choice problem',
            'domain': 'assessment.Item'
        })
        self.question_type = Type('question-record-type%3Amulti-choice-edx%40ODL.MIT.EDU')
        self.answer_type = Type('answer-record-type%3Amulti-choice-edx%40ODL.MIT.EDU')

        self._top = ABS_PATH + '/files/top.jpg'
        self.top = open(self._top, 'rb')

        self._item = self.add_item(self._bank)

    def tearDown(self):
        """
        """
        super(EdXMultiChoiceTests, self).tearDown()

        self.top.close()

    def test_can_set_choices(self):
        form = self._bank.get_question_form_for_update(self._item.ident)
        form.add_choice('Yes')
        self._bank.update_question(form)

        question_map = self._bank.get_item(self._item.ident).get_question().object_map
        self.assertEqual(
            len(question_map['choices']),
            1
        )
        self.assertEqual(
            question_map['choices'][0]['name'],
            ''
        )
        self.assertEqual(
            question_map['choices'][0]['text'],
            'Yes'
        )

    def test_can_set_choices_with_names(self):
        form = self._bank.get_question_form_for_update(self._item.ident)
        form.add_choice('Yes', 'yes')
        self._bank.update_question(form)

        question_map = self._bank.get_item(self._item.ident).get_question().object_map
        self.assertEqual(
            len(question_map['choices']),
            1
        )
        self.assertEqual(
            question_map['choices'][0]['name'],
            'yes'
        )
        self.assertEqual(
            question_map['choices'][0]['text'],
            'Yes'
        )

    def test_can_upload_files_with_item(self):
        JPG_ASSET_CONTENT_GENUS_TYPE = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'jpg',
            'display_name': 'Image/JPG',
            'display_label': 'Image/JPG',
            'description': 'A JPG image',
            'domain': 'repository.AssetContent'
        })
        EDX_IMAGE_ASSET_GENUS_TYPE = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'asset-genus-type',
            'identifier': 'edx-img',
            'display_name': 'edX Image',
            'display_label': 'edX Image',
            'description': 'An image found in an edx course',
            'domain': 'repository.Asset'
        })

        form = self._bank.get_item_form_for_update(self._item.ident)
        form.add_file(DataInputStream(self.top),
                      label='TopView',
                      asset_type=EDX_IMAGE_ASSET_GENUS_TYPE,
                      asset_content_type=JPG_ASSET_CONTENT_GENUS_TYPE,
                      asset_name='My View',
                      asset_description='Top view of something')

        self._bank.update_item(form)

        item = self._bank.get_item(self._item.ident)

        item_files = item.get_files()
        self.assertEqual(
            len(list(item_files.keys())),
            1
        )
        self.assertEqual(
            list(item_files.keys())[0],
            'TopView'
        )
        self.is_streamable_url(item_files['TopView'])
        self.assertIn(
            item.object_map['fileIds']['TopView']['assetContentId'],
            item_files['TopView']
        )

    def test_can_get_olx_from_item(self):
        form = self._bank.get_question_form_for_update(self._item.ident)
        form.add_choice('Yes', 'true')
        form.add_choice('No', 'false')
        form.add_choice('Maybe', 'maybe')
        self._bank.update_question(form)

        question_map = self._bank.get_item(self._item.ident).get_question().object_map

        form = self._bank.get_answer_form_for_update(next(self._item.get_answer_ids()))
        form.add_choice_id(question_map['choices'][1]['id'])
        self._bank.update_answer(form)

        olx = self._bank.get_item(self._item.ident).get_edxml()
        self.assertEqual(
            str(olx),
            ('<problem display_name="a test item!" max_attempts="0" rerandomize="never" '
             'showanswer="closed">\n <p>\n  Please answer the question.\n </p>\n '
             '<multiplechoiceresponse>\n  <choicegroup direction="vertical">\n   '
             '<choice correct="false" name="true">\n    <text>\n     Yes\n    </text>\n   '
             '</choice>\n   <choice correct="true" name="false">\n    <text>\n     No\n    '
             '</text>\n   </choice>\n   <choice correct="false" name="maybe">\n    '
             '<text>\n     Maybe\n    </text>\n   </choice>\n  </choicegroup>\n '
             '</multiplechoiceresponse>\n</problem>')
        )

    def test_can_set_olx_metadata(self):
        item_map = self._bank.get_item(self._item.ident).object_map
        new_metadata = {
            'attempts': item_map['attempts'] - 1,
            'markdown': 'second fake markdown',
            'rerandomize': 'second fake rerandomize',
            'showanswer': 'second fake showanswer',
            'weight': item_map['weight'] / 2
        }

        for attr, val in new_metadata.items():
            if attr == 'rerandomize':
                form = self._bank.get_question_form_for_update(self._item.ident)
                getattr(form, 'add_' + attr)(val)
                self._bank.update_question(form)

                refreshed_item = self._bank.get_item(self._item.ident).object_map
                self.assertEqual(
                    val,
                    refreshed_item['question'][attr]
                )
            else:
                form = self._bank.get_item_form_for_update(self._item.ident)
                getattr(form, 'add_' + attr)(val)
                self._bank.update_item(form)

                refreshed_item = self._bank.get_item(self._item.ident).object_map
                self.assertEqual(
                    val,
                    refreshed_item[attr]
                )

    def test_can_set_irt_metadata(self):
        irt = {
            'difficulty': -2.1,
            'discrimination': 1.5
        }

        form = self._bank.get_item_form_for_update(self._item.ident)
        form.set_difficulty_value(irt['difficulty'])
        form.set_discrimination_value(irt['discrimination'])
        self._bank.update_item(form)

        item = self._bank.get_item(self._item.ident)
        self.assertEqual(
            item.get_difficulty_value(),
            irt['difficulty']
        )
        self.assertEqual(
            item.get_discrimination_value(),
            irt['discrimination']
        )

    def test_can_query_irt_max_difficulty(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_maximum_difficulty(float(0.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_maximum_difficulty(float(-5.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_min_difficulty(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(-5.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(0.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_difficulty_inclusive(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(-5.0), True)
        querier.match_maximum_difficulty(float(0.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(0.0), True)
        querier.match_maximum_difficulty(float(3.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_difficulty_exclusive(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(0.0), False)
        querier.match_maximum_difficulty(float(-5.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(0.0), False)
        querier.match_maximum_difficulty(float(5.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_difficulty_flipped(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(0.0), False)
        querier.match_maximum_difficulty(float(5.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_difficulty(float(-5.0), False)
        querier.match_maximum_difficulty(float(0.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_discrimination(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_maximum_discrimination(float(2.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_maximum_discrimination(float(1.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_min_discrimination(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(1.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(2.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_discrimination_inclusive(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(1.0), True)
        querier.match_maximum_discrimination(float(2.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(0.0), True)
        querier.match_maximum_discrimination(float(1.0), True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_discrimination_exclusive(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(2.0), False)
        querier.match_maximum_discrimination(float(1.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(1.0), False)
        querier.match_maximum_discrimination(float(2.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_irt_max_and_min_discrimination_flipped(self):
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(0.0), False)
        querier.match_maximum_discrimination(float(5.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

        querier = self._bank.get_item_query()
        querier.match_minimum_discrimination(float(-5.0), False)
        querier.match_maximum_discrimination(float(0.0), False)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_query_display_name(self):
        WORDIGNORECASE_STRING_MATCH_TYPE = Type(**{
            'authority': 'okapia.net',
            'namespace': 'string match types',
            'identifier': 'WORDIGNORECASE',
            'domain': 'String Match Types',
            'display_name': 'Word Ignore Case String Match Type',
            'display_label': 'Word Ignore Case',
            'description': 'The string match type for the Word Ignore Case'
        })
        self._item = self.set_item_irt(self._item)
        querier = self._bank.get_item_query()
        querier.match_display_name('a test', WORDIGNORECASE_STRING_MATCH_TYPE, True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )

        querier = self._bank.get_item_query()
        querier.match_display_name('foo', WORDIGNORECASE_STRING_MATCH_TYPE, True)
        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_set_learning_objectives(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        id_list = ['bank@123:MIT']
        id_list_obj = [Id(id_list[0])]
        form.set_learning_objectives(id_list_obj)
        updated_item = self._bank.update_item(form)

        item_map = self._bank.get_item(self._item.ident).object_map
        self.assertEqual(
            item_map['learningObjectiveIds'],
            id_list
        )

    def test_can_query_by_learning_objective(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        id_list = ['bank@123:MIT']
        id_list_obj = [Id(id_list[0])]
        form.set_learning_objectives(id_list_obj)
        updated_item = self._bank.update_item(form)

        querier = self._bank.get_item_query()
        querier.match_learning_objective_id(id_list_obj[0], match=True)

        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )
        querier = self._bank.get_item_query()
        querier.match_learning_objective_id(Id('foo@bar:baz'), match=True)

        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    # Deprecated, this is now done via the RESTful API
    # def test_rerandomize_flag_changes_question_choices_order(self):
    #     choices = ['yes', 'no', 'maybe']
    #
    #     question_form = self._bank.get_question_form_for_update(self._item.ident)
    #     for ind, choice in enumerate(choices):
    #         question_form.add_choice(choice, 'Choice ' + str(int(ind) + 1))
    #     question_form.add_rerandomize('always')
    #     self._bank.update_question(question_form)
    #
    #     taken = self.create_taken_for_items(self._bank,
    #                                         [self._item])
    #     first_section = self._bank.get_first_assessment_section(taken.ident)
    #     questions = self._bank.get_questions(first_section.ident)
    #     original_choices = questions.next().object_map['choices']
    #
    #     questions = self._bank.get_questions(first_section.ident)
    #     new_choices = questions.next().object_map['choices']
    #
    #     self.assertNotEqual(
    #         original_choices,
    #         new_choices
    #     )


class MecQBankTests(DLKitTestCase):
    def setUp(self):
        super(MecQBankTests, self).setUp()

        self._bank = self._get_test_bank()

    def tearDown(self):
        """
        """
        super(MecQBankTests, self).tearDown()


class GeneralTests(DLKitTestCase):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        form.set_learning_objectives([Id(self._lo)])
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def setUp(self):
        super(GeneralTests, self).setUp()

        self._lo = 'foo%3A1%40MIT'
        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(GeneralTests, self).tearDown()

    def test_can_get_all_banks(self):
        from .utilities.testing import get_manager
        am = get_manager(self.req, 'assessment')
        banks = am.banks
        self.assertEqual(
            banks.available(),
            1
        )


class MecQBankAssessmentTests(MecQBankTests):
    def add_assessment(self, bank):
        MECQBANK_ASSESSMENT_RECORD_TYPE = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'assessment-record-type',
            'identifier': 'mecqbank-assessment',
            'display_name': 'MecQBank Assessment',
            'display_label': 'MecQBank Assessment',
            'description': 'Assessment record extension for MecQBank based Assessments',
            'domain': 'assessment.Assessment'
        })
        form = bank.get_assessment_form_for_create([MECQBANK_ASSESSMENT_RECORD_TYPE,
                                                    SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = 'a test assessment!'
        form.description = 'for testing with'
        new_assessment = bank.create_assessment(form)
        return new_assessment

    def setUp(self):
        super(MecQBankAssessmentTests, self).setUp()

        self.assessment_genus_types = {
            'pset': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'assessment-type',
                'identifier': 'pset',
                'display_name': 'Problem Set Assessment',
                'display_label': 'Problem Set Assessment',
                'description': 'Assessment used as a problem set',
                'domain': 'assessment.Assessment'}),
            'quiz': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'assessment-type',
                'identifier': 'quiz',
                'display_name': 'Quiz Assessment',
                'display_label': 'Quiz Assessment',
                'description': 'Assessment used as a quiz',
                'domain': 'assessment.Assessment'})
        }

        self._assessment = self.add_assessment(self._bank)

    def tearDown(self):
        """
        """
        super(MecQBankAssessmentTests, self).tearDown()

    def test_can_set_published_flag(self):
        self.assertFalse(self._assessment.object_map['published'])
        form = self._bank.get_assessment_form_for_update(self._assessment.ident)
        form.set_published(True)
        self._bank.update_assessment(form)
        self.assertTrue(self._bank.get_assessment(self._assessment.ident).object_map['published'])

    def test_can_set_genus_type(self):
        self.assertIn(
            'DEFAULT',
            self._assessment.object_map['genusTypeId']
        )

        form = self._bank.get_assessment_form_for_update(self._assessment.ident)
        form.set_genus_type(self.assessment_genus_types['pset'])
        self._bank.update_assessment(form)

        self.assertIn(
            'pset',
            self._bank.get_assessment(self._assessment.ident).object_map['genusTypeId']
        )


class MecQBankItemTests(MecQBankTests):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([self.item_type])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [self.question_type])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [self.answer_type])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def general_add_file_test(self, file_, ac_genus, label):
        if not isinstance(file_, DataInputStream):
            file_ = DataInputStream(file_)

        form = self._bank.get_item_form_for_update(self._item.ident)
        form.add_file(file_,
                      label=label,
                      asset_type=self.mecqbank_asset_genus_type,
                      asset_content_type=ac_genus,
                      asset_name='my file name')
        self._bank.update_item(form)
        item = self._bank.get_item(self._item.ident)

        item_files = item.get_files()
        self.assertIn(
            label,
            item_files
        )
        self.is_streamable_url(item_files[label])

        self.assertIn(
            item.object_map['fileIds'][label]['assetContentId'],
            item_files[label]
        )

    def general_add_preview_test(self, type_, file_, name):
        if not isinstance(file_, DataInputStream):
            file_ = DataInputStream(file_)

        if type_ == 'question':
            form = self._bank.get_question_form_for_update(self._item.ident)
            execute = self._bank.update_question
        else:
            form = self._bank.get_answer_form_for_update(next(self._item.get_answer_ids()))
            execute = self._bank.update_answer

        form.add_preview(file_, name)
        execute(form)

        item = self._bank.get_item(self._item.ident)

        if type_ == 'question':
            files = item.get_question().get_files()
            expected_asset_content_id = item.object_map['question']['fileIds']['preview']['assetContentId']
        else:
            files = item.get_answers().next().get_files()
            expected_asset_content_id = item.object_map['answers'][0]['fileIds']['preview']['assetContentId']

        self.assertIn(
            'preview',
            files
        )
        self.is_streamable_url(files['preview'])
        self.assertIn(
            expected_asset_content_id,
            files['preview']
        )

    def get_asset_content_full_path(self, item, label, source=None):
        mgr = get_manager(self.req, 'repository')
        repo = mgr.get_repository(self._bank.ident)
        try:
            if source == 'question':
                ac_id_str = item.object_map['question']['fileIds'][label]['assetContentId']
            elif source == 'answer':
                ac_id_str = item.object_map['answers'][0]['fileIds'][label]['assetContentId']
            else:
                ac_id_str = item.object_map['fileIds'][label]['assetContentId']
            ac = repo.get_asset_content(
                Id(ac_id_str))
        except errors.NotFound:
            return None
        else:
            # this is super hacky
            return os.path.join(ac._config_map['data_store_full_path'],
                                ac._my_map['url'])

    def reset_files(self):
        self.solution_preview_file.seek(0)
        self.solution_tex_file.seek(0)
        self.metadata_file.seek(0)
        self.question_preview_file.seek(0)
        self.question_tex_file.seek(0)
        self.figure_file.seek(0)
        self.non_pdf_file.seek(0)
        self.solution_image_file.seek(0)
        self.solution_with_image.seek(0)

    def file_exists(self, file_):
        # check on the filesystem that the file is there
        return os.path.isfile(file_)

    def setUp(self):
        super(MecQBankItemTests, self).setUp()

        self.item_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'item-record-type',
            'identifier': 'mecqbank-item',
            'display_name': 'MecQBank Item',
            'display_label': 'MecQBank Item',
            'description': 'Assessment Item record extension for MecQBank based Items',
            'domain': 'assessment.Item',
            'module_path': 'dlkit.mongo.assessment.records.mecqbank.item_records',
            'object_record_class_name': 'MecQBankItemRecord',
            'form_record_class_name': 'MecQBankItemFormRecord',
            'query_record_class_name': 'MecQBankItemQueryRecord'
        })
        self.question_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'question-record-type',
            'identifier': 'mecqbank-question',
            'display_name': 'MecQBank Generic Question',
            'display_label': 'MecQBank Generic Question',
            'description': 'Assessment Question record extension for generic MecQBank questions',
            'domain': 'assessment.Question',
            'module_path': 'dlkit.mongo.assessment.records.mecqbank.item_records',
            'object_record_class_name': 'MecQBankQuestionRecord',
            'form_record_class_name': 'MecQBankQuestionFormRecord'
        })
        self.answer_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'answer-record-type',
            'identifier': 'mecqbank-answer',
            'display_name': 'MecQBank Generic Answer',
            'display_label': 'MecQBank Generic Answer',
            'description': 'Assessment Answer record extension for MecQBank answers',
            'domain': 'assessment.Answer',
            'module_path': 'dlkit.mongo.assessment.records.mecqbank.item_records',
            'object_record_class_name': 'MecQBankAnswerRecord',
            'form_record_class_name': 'MecQBankAnswerFormRecord'
        })

        self.mecqbank_asset_genus_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'asset-genus-type',
            'identifier': 'mecqbank-file',
            'display_name': 'MecQBank File',
            'display_label': 'MecQBank File',
            'description': 'A file found in a MecQBank problem',
            'domain': 'repository.Asset'
        })

        self.latex_genus_type = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'latex',
            'display_name': 'application/x-tex',
            'display_label': 'application/x-tex',
            'description': 'LaTeX content',
            'domain': 'repository.AssetContent'
        })

        self.pdf_genus_type = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'pdf',
            'display_name': 'application/pdf',
            'display_label': 'application/pdf',
            'description': 'PDF content',
            'domain': 'repository.AssetContent'
        })

        self.docx_genus_type = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'docx',
            'display_name': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'display_label': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'description': 'Word Doc content',
            'domain': 'repository.AssetContent'
        })

        self.eps_genus_type = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'eps',
            'display_name': 'application/postscript',
            'display_label': 'application/postscript',
            'description': 'EPS File',
            'domain': 'repository.AssetContent'
        })

        self.meta_genus_type = Type(**{
            'authority': 'iana.org',
            'namespace': 'asset-content-genus-type',
            'identifier': 'meta',
            'display_name': 'application/metadata',
            'display_label': 'application/metadata',
            'description': 'Item metadata',
            'domain': 'repository.AssetContent'
        })

        self.item_genus_types = {
            'long': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-long-question',
                'display_name': 'MecQBank Long Format Question',
                'display_label': 'MecQBank Long Format Question',
                'description': 'Assessment Question that requires a long format Answer',
                'domain': 'assessment.Question'}),
            'concept': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-concept-question',
                'display_name': 'MecQBank Concept Question',
                'display_label': 'MecQBank Concept Question',
                'description': 'Assessment Question that requires a concept Answer',
                'domain': 'assessment.Question'}),
            'mcq': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-mcq-question',
                'display_name': 'MecQBank Multiple Choice Question',
                'display_label': 'MecQBank Multiple Choice Question',
                'description': 'Assessment Question that requires a choice Answer',
                'domain': 'assessment.Question'}),
            'true/false': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-tf-question',
                'display_name': 'MecQBank True / False Question',
                'display_label': 'MecQBank True / False Question',
                'description': 'Assessment Question that requires a true or false Answer',
                'domain': 'assessment.Question'}),
            'code': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-code-question',
                'display_name': 'MecQBank Code Question',
                'display_label': 'MecQBank Code Question',
                'description': 'Assessment Question that requires a code Answer',
                'domain': 'assessment.Question'}),
            'unknown': Type(**{
                'authority': 'ODL.MIT.EDU',
                'namespace': 'question-type',
                'identifier': 'mecqbank-unknown-question',
                'display_name': 'MecQBank Unknown Format Question',
                'display_label': 'MecQBank Unknown Format Question',
                'description': 'Assessment Question that requires an unknown Answer',
                'domain': 'assessment.Question'})
        }

        # for *.tex files that will be read in and stuck into a DisplayText object,
        # don't read them in as binary -- that will break the DisplayText output.
        self.solution_preview_file = open(ABS_PATH + '/files/MecQBank/CONT0001_Sol.pdf', 'rb')
        self.solution_tex_file = open(ABS_PATH + '/files/MecQBank/CONT0001_Sol.tex', 'r')
        self.metadata_file = open(ABS_PATH + '/files/MecQBank/CONT0001.meta', 'rb')
        self.question_preview_file = open(ABS_PATH + '/files/MecQBank/CONT0001.pdf', 'rb')
        self.question_tex_file = open(ABS_PATH + '/files/MecQBank/CONT0001.tex', 'r')
        self.figure_file = open(ABS_PATH + '/files/MecQBank/solution_with_image.pdf', 'rb')
        self.non_pdf_file = open(ABS_PATH + '/files/MecQBank/test_doc.docx', 'rb')
        self.solution_image_file = open(ABS_PATH + '/files/MecQBank/draggable.green.dot.png', 'rb')
        self.solution_with_image = open(ABS_PATH + '/files/MecQBank/solution_with_image.tex', 'r')

        self._item = self.add_item(self._bank)

    def tearDown(self):
        """
        """
        super(MecQBankItemTests, self).tearDown()

        self.solution_preview_file.close()
        self.solution_tex_file.close()
        self.metadata_file.close()
        self.question_preview_file.close()
        self.question_tex_file.close()
        self.figure_file.close()
        self.non_pdf_file.close()
        self.solution_image_file.close()
        self.solution_with_image.close()

    def test_can_add_objectives(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        id_list = ['bank@123:MIT']
        id_list_obj = [Id(id_list[0])]
        form.set_learning_objectives(id_list_obj)
        updated_item = self._bank.update_item(form)

        item_map = self._bank.get_item(self._item.ident).object_map
        self.assertEqual(
            item_map['learningObjectiveIds'],
            id_list
        )

    def test_can_add_comment(self):
        book = self.get_book(self._bank.ident)
        form = book.get_comment_form_for_create(self._item.ident,
                                                [])

        form.set_text('My favorite item')

        new_comment = book.create_comment(form)

        comments = book.get_comments()

        comments = [comment for comment in comments if comment.get_reference_id() == self._item.ident]

        self.assertEqual(
            len(comments),
            1
        )
        self.assertEqual(
            comments[0].get_text().text,
            'My favorite item'
        )

    def test_can_set_genus_type(self):
        self.assertIn(
            'DEFAULT',
            self._item.object_map['genusTypeId']
        )

        form = self._bank.get_item_form_for_update(self._item.ident)
        form.set_genus_type(self.item_genus_types['true/false'])
        self._bank.update_item(form)

        self.assertIn(
            'mecqbank-tf-question',
            self._bank.get_item(self._item.ident).object_map['genusTypeId']
        )

    def test_can_add_general_file(self):
        self.general_add_file_test(self.figure_file,
                                   self.pdf_genus_type,
                                   'image_file')

    def test_can_add_eps_image_file(self):
        self.general_add_file_test(self.solution_image_file,
                                   self.eps_genus_type,
                                   'image_file')

    def test_can_add_answer_latex(self):
        form = self._bank.get_answer_form_for_update(next(self._item.get_answer_ids()))
        form.add_text(self.solution_tex_file.read(), 'latex')
        self._bank.update_answer(form)

        self.reset_files()

        self.assertEqual(
            self._bank.get_item(self._item.ident).get_answers().next().get_raw_latex().text,
            self.solution_tex_file.read()
        )

    def test_can_add_question_latex(self):
        form = self._bank.get_question_form_for_update(self._item.ident)
        form.add_text(self.question_tex_file.read(), 'latex')
        self._bank.update_question(form)

        self.reset_files()

        self.assertEqual(
            self._bank.get_item(self._item.ident).get_question().get_raw_latex().text,
            self.question_tex_file.read()
        )

    def test_can_add_metadata_file(self):
        self.general_add_file_test(self.metadata_file,
                                   self.meta_genus_type,
                                   'metadata_file')

    def test_can_add_non_pdf_question_preview(self):
        self.general_add_preview_test('question',
                                      DataInputStream(self.non_pdf_file),
                                      'nonpdf_preview')

    def test_can_add_non_pdf_answer_preview(self):
        self.general_add_preview_test('answer',
                                      self.non_pdf_file,
                                      'nonpdf_preview')

    def test_can_add_pdf_question_preview(self):
        self.general_add_preview_test('question',
                                      self.question_preview_file,
                                      'pdf_preview')

    def test_can_add_pdf_answer_preview(self):
        self.general_add_preview_test('answer',
                                      self.solution_preview_file,
                                      'pdf_preview')

    def test_can_set_provenance(self):
        item2 = self.add_item(self._bank)
        form = self._bank.get_item_form_for_update(item2.ident)
        form.set_provenance(str(self._item.ident))
        self._bank.update_item(form)

        self.assertEqual(
            str(self._bank.get_item(item2.ident).get_provenance_id()),
            str(self._item.ident)
        )

    def test_can_clear_provenance(self):
        item2 = self.add_item(self._bank)
        form = self._bank.get_item_form_for_update(item2.ident)
        form.clear_provenance()
        self._bank.update_item(form)

        self.assertFalse(self._bank.get_item(item2.ident).has_provenance())

    def test_can_delete_objective(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        form.set_learning_objectives([])
        updated_item = self._bank.update_item(form)

        item_map = self._bank.get_item(self._item.ident).object_map
        self.assertEqual(
            item_map['learningObjectiveIds'],
            []
        )

    def test_can_delete_general_file(self):
        self.general_add_file_test(self.figure_file,
                                   self.pdf_genus_type,
                                   'image_file')
        item = self._bank.get_item(self._item.ident)
        original_file_location = self.get_asset_content_full_path(item,
                                                                  'image_file')
        self.assertTrue(self.file_exists(original_file_location))

        form = self._bank.get_item_form_for_update(self._item.ident)
        form.clear_file('image_file')
        self._bank.update_item(form)
        with self.assertRaises(errors.IllegalState):
            self._bank.get_item(self._item.ident).get_files()
        self.assertFalse(self.file_exists(original_file_location))

    def test_can_delete_pdf_question_preview(self):
        self.general_add_preview_test('question',
                                      self.question_preview_file,
                                      'preview')

        item = self._bank.get_item(self._item.ident)
        original_file_location = self.get_asset_content_full_path(item,
                                                                  'preview',
                                                                  source='question')
        self.assertTrue(self.file_exists(original_file_location))

        form = self._bank.get_question_form_for_update(self._item.ident)
        form.clear_file('preview')
        self._bank.update_question(form)
        with self.assertRaises(errors.IllegalState):
            self._bank.get_item(self._item.ident).get_question().get_files()
        self.assertFalse(self.file_exists(original_file_location))

    def test_can_delete_pdf_answer_preview(self):
        self.general_add_preview_test('answer',
                                      self.solution_preview_file,
                                      'preview')

        item = self._bank.get_item(self._item.ident)
        original_file_location = self.get_asset_content_full_path(item,
                                                                  'preview',
                                                                  source='answer')
        self.assertTrue(self.file_exists(original_file_location))

        form = self._bank.get_answer_form_for_update(next(self._item.get_answer_ids()))
        form.clear_file('preview')
        self._bank.update_answer(form)
        with self.assertRaises(errors.IllegalState):
            self._bank.get_item(self._item.ident).get_answers().next().get_files()
        self.assertFalse(self.file_exists(original_file_location))

    def test_can_delete_non_pdf_question_preview(self):
        self.general_add_preview_test('question',
                                      self.non_pdf_file,
                                      'preview')
        item = self._bank.get_item(self._item.ident)
        original_file_location = self.get_asset_content_full_path(item,
                                                                  'preview',
                                                                  source='question')
        self.assertTrue(self.file_exists(original_file_location))

        form = self._bank.get_question_form_for_update(self._item.ident)
        form.clear_file('preview')
        self._bank.update_question(form)
        with self.assertRaises(errors.IllegalState):
            self._bank.get_item(self._item.ident).get_question().get_files()
        self.assertFalse(self.file_exists(original_file_location))

    def test_can_delete_non_pdf_answer_preview(self):
        self.general_add_preview_test('answer',
                                      self.non_pdf_file,
                                      'preview')

        item = self._bank.get_item(self._item.ident)
        original_file_location = self.get_asset_content_full_path(item,
                                                                  'preview',
                                                                  source='answer')
        self.assertTrue(self.file_exists(original_file_location))

        form = self._bank.get_answer_form_for_update(next(self._item.get_answer_ids()))
        form.clear_file('preview')
        self._bank.update_answer(form)
        with self.assertRaises(errors.IllegalState):
            self._bank.get_item(self._item.ident).get_answers().next().get_files()
        self.assertFalse(self.file_exists(original_file_location))

    def test_can_set_difficulty(self):
        difficulties = ['low', 'medium', 'hard']
        for diff in difficulties:
            form = self._bank.get_item_form_for_update(self._item.ident)
            form.set_difficulty(diff)
            self._bank.update_item(form)
            self.assertEqual(
                self._bank.get_item(self._item.ident).get_difficulty_value(),
                diff
            )

    def test_can_set_source(self):
        self.assertEqual(
            self._bank.get_item(self._item.ident).get_source_value(),
            ''
        )
        form = self._bank.get_item_form_for_update(self._item.ident)
        form.set_source('foobar')
        self._bank.update_item(form)
        self.assertEqual(
            self._bank.get_item(self._item.ident).get_source_value(),
            'foobar'
        )


class Ortho3DTests(DLKitTestCase):
    def check_files(self, file1, file2):
        """ assumes file2 is a self.<file>, whereas file1 is from DLKit item/question
        :param file1:
        :param file2:
        :return:
        """
        self.reset_files()
        self.assertEqual(
            file1.read(),
            file2.read()
        )
        file1.close()  # assumes file2 is always the class instance one...

    def reset_files(self):
        self.manip.seek(0)
        self.front.seek(0)
        self.side.seek(0)
        self.top.seek(0)
        self.choice0sm.seek(0)
        self.choice0big.seek(0)
        self.choice1sm.seek(0)
        self.choice1big.seek(0)

    def setUp(self):
        super(Ortho3DTests, self).setUp()

        self._bank = self._get_test_bank()

        self._manip_file = ABS_PATH + '/files/myAssetBundle.unity3d'
        self.manip = open(self._manip_file, 'rb')

        self._front = ABS_PATH + '/files/front.jpg'
        self.front = open(self._front, 'rb')

        self._side = ABS_PATH + '/files/side.jpg'
        self.side = open(self._side, 'rb')

        self._top = ABS_PATH + '/files/top.jpg'
        self.top = open(self._top, 'rb')

        self._choice0sm = ABS_PATH + '/files/choice0sm.jpg'
        self.choice0sm = open(self._choice0sm, 'rb')

        self._choice0big = ABS_PATH + '/files/choice0big.jpg'
        self.choice0big = open(self._choice0big, 'rb')

        self._choice1sm = ABS_PATH + '/files/choice1sm.jpg'
        self.choice1sm = open(self._choice1sm, 'rb')

        self._choice1big = ABS_PATH + '/files/choice1big.jpg'
        self.choice1big = open(self._choice1big, 'rb')

    def tearDown(self):
        """
        """
        super(Ortho3DTests, self).tearDown()

        self.manip.close()
        self.front.close()
        self.side.close()
        self.top.close()
        self.choice0big.close()
        self.choice0sm.close()
        self.choice1big.close()
        self.choice1sm.close()


class Ortho3DLabelFacesTests(Ortho3DTests):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [self.question_type])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        question_form.set_text('Please answer the question.')
        question_form.set_manip(DataInputStream(self.manip))
        question_form.set_ortho_view_set(front_view=DataInputStream(self.front),
                                         side_view=DataInputStream(self.side),
                                         top_view=DataInputStream(self.top))
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [self.answer_type])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        answer_form.set_face_values(front_face_value=self.answer['frontFaceValue'],
                                    side_face_value=self.answer['sideFaceValue'],
                                    top_face_value=self.answer['topFaceValue'])
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def setUp(self):
        super(Ortho3DLabelFacesTests, self).setUp()

        self.question_type = Type('question-record-type%3Alabel-ortho-faces%40ODL.MIT.EDU')
        self.answer_type = Type('answer-record-type%3Alabel-ortho-faces%40ODL.MIT.EDU')
        self.answer = {
            "frontFaceValue": 1,
            "sideFaceValue": 2,
            "topFaceValue": 3
        }

        self._item = self.add_item(self._bank)
        self._taken = self.create_taken_for_items(self._bank, [self._item])

    def tearDown(self):
        """
        """
        super(Ortho3DLabelFacesTests, self).tearDown()

    def test_can_submit_wrong_answer(self):
        wrong_response = {
            "frontFaceValue": 0,
            "sideFaceValue": 1,
            "topFaceValue": 2
        }

        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        null_response = self._bank.get_response(first_section.ident, self._item.ident)
        try:
            null_response.object_map
        except errors.IllegalState:
            pass
        else:
            self.fail('null response did not throw illegal state')

        response_form = self._bank.get_response_form(assessment_section_id=first_section.ident,
                                                     item_id=self._item.ident)

        response_form.set_face_values(front_face_value=wrong_response['frontFaceValue'],
                                      side_face_value=wrong_response['sideFaceValue'],
                                      top_face_value=wrong_response['topFaceValue'])

        self._bank.submit_response(first_section.ident, self._item.ident, response_form)

        response = self._bank.get_response(first_section.ident, self._item.ident).object_map

        for key, val in response['integerValues'].items():
            self.assertEqual(
                val,
                wrong_response[key]
            )

    def test_can_submit_right_answer(self):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        null_response = self._bank.get_response(first_section.ident, self._item.ident)

        try:
            null_response.object_map
        except errors.IllegalState:
            pass
        else:
            self.fail('Did not raise illegal state on unanswered response')

        response_form = self._bank.get_response_form(assessment_section_id=first_section.ident,
                                                     item_id=self._item.ident)

        response_form.set_face_values(front_face_value=self.answer['frontFaceValue'],
                                      side_face_value=self.answer['sideFaceValue'],
                                      top_face_value=self.answer['topFaceValue'])

        self._bank.submit_response(first_section.ident, self._item.ident, response_form)

        response = self._bank.get_response(first_section.ident, self._item.ident).object_map

        for key, val in response['integerValues'].items():
            self.assertEqual(
                val,
                self.answer[key]
            )

    def test_taken_question_contains_expected_files(self):
        first_section = self._bank.get_first_assessment_section(self._taken.ident)
        question = self._bank.get_question(first_section.ident, self._item.ident)

        self.reset_files()

        test_cases = [(question.get_manip(), self.manip),
                      (question.get_front_view(), self.front),
                      (question.get_side_view(), self.side),
                      (question.get_top_view(), self.top)]

        for case in test_cases:
            self.assertEqual(
                case[1].read(),
                case[0].read()
            )

    def test_responding_to_one_question_makes_next_one_available(self):
        self.reset_files()
        self._item2 = self.add_item(self._bank)
        self._taken2 = self.create_taken_for_items(self._bank, [self._item, self._item2])

        first_section = self._bank.get_first_assessment_section(self._taken2.ident)
        first_question = self._bank.get_first_unanswered_question(first_section.ident)

        response_form = self._bank.get_response_form(assessment_section_id=first_section.ident,
                                                     item_id=first_question.ident)

        response_form.set_face_values(front_face_value=self.answer['frontFaceValue'],
                                      side_face_value=self.answer['sideFaceValue'],
                                      top_face_value=self.answer['topFaceValue'])

        self._bank.submit_response(first_section.ident, first_question.ident, response_form)

        second_question = self._bank.get_first_unanswered_question(first_section.ident)

        self.assertNotEqual(
            str(first_question.ident),
            str(second_question.ident)
        )

    def test_can_set_first_angle_on_item(self):
        self.assertFalse(self._item.object_map['question']['firstAngle'])
        q_edit_form = self._bank.get_question_form_for_update(self._item.ident)
        q_edit_form.set_first_angle_projection(True)
        updated_q = self._bank.update_question(q_edit_form)

        item = self._bank.get_item(self._item.ident)
        item_map = item.object_map
        self.assertTrue(item_map['question']['firstAngle'])

    def test_can_update_single_ovs_view(self):
        question = self._bank.get_item(self._item.ident).get_question()

        top_view = question.get_top_view()
        self.check_files(top_view, self.top)
        top_view.close()

        update_form = self._bank.get_question_form_for_update(self._item.ident)

        update_form.set_ovs_view(DataInputStream(self.choice0big), 'topView')

        self._bank.update_question(update_form)

        question = self._bank.get_item(self._item.ident).get_question()

        top_view = question.get_top_view()
        self.check_files(top_view, self.choice0big)
        top_view.close()


class Ortho3DMultiChoiceTests(Ortho3DTests):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [self.question_type])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        question_form.set_text('Please answer the question.')
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [self.answer_type])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def get_asset_content_by_genus_type(self, asset_id, genus_type):
            mgr = get_manager(self.req, 'repository')
            repo = mgr.get_repository(self._bank.ident)
            asset = repo.get_asset(asset_id)
            ac = None
            for content in asset.get_asset_contents():
                if content.genus_type == genus_type:
                    return content
            return ac

    def setUp(self):
        super(Ortho3DMultiChoiceTests, self).setUp()

        self.question_type = Type('question-record-type%3Amulti-choice-ortho%40ODL.MIT.EDU')
        self.answer_type = Type('answer-record-type%3Amulti-choice-ortho%40ODL.MIT.EDU')
        self.answer = {
            "choiceId": 2
        }

        self._item = self.add_item(self._bank)
        self._taken = self.create_taken_for_items(self._bank, [self._item])

    def tearDown(self):
        """
        """
        super(Ortho3DMultiChoiceTests, self).tearDown()

    def test_can_set_manip_with_right_answer_choice_files(self):
        question_map = self._item.object_map['question']
        self.assertEqual(
            {},
            question_map['fileIds']
        )
        update_form = self._bank.get_question_form_for_update(self._item.ident)
        update_form.set_manip(DataInputStream(self.manip),
                              DataInputStream(self.choice0sm),
                              DataInputStream(self.choice0big),
                              'manip')
        self._bank.update_question(update_form)
        question = self._bank.get_item(self._item.ident).get_question()

        question_manip = question.get_manip()
        self.check_files(question_manip, self.manip)
        question_manip.close()

        repo = self.get_repo(self._bank.ident)
        manip_asset = repo.get_asset(question.get_manip_id())

        self.assertEqual(
            manip_asset.get_asset_contents().available(),
            3
        )

    def test_can_set_manip_without_right_answer_choice_files(self):
        question_map = self._item.object_map['question']
        self.assertEqual(
            {},
            question_map['fileIds']
        )
        update_form = self._bank.get_question_form_for_update(self._item.ident)
        update_form.set_manip(DataInputStream(self.manip),
                              name='manip')
        self._bank.update_question(update_form)
        question = self._bank.get_item(self._item.ident).get_question()

        question_manip = question.get_manip()
        self.check_files(question_manip, self.manip)
        question_manip.close()

        repo = self.get_repo(self._bank.ident)
        manip_asset = repo.get_asset(question.get_manip_id())

        self.assertEqual(
            manip_asset.get_asset_contents().available(),
            1
        )

    def test_invalid_argument_thrown_if_non_datainputstream_passed_in(self):
        update_form = self._bank.get_question_form_for_update(self._item.ident)
        self.assertRaises(errors.InvalidArgument,
                          update_form.set_manip,
                          self.manip)
        self.assertRaises(errors.InvalidArgument,
                          update_form.set_ortho_choice,
                          self.choice0sm,
                          DataInputStream(self.choice0big))
        self.assertRaises(errors.InvalidArgument,
                          update_form.set_ortho_choice,
                          DataInputStream(self.choice0sm),
                          self.choice0big)

    def test_can_set_choice_files(self):
        question_map = self._item.object_map['question']
        self.assertEqual(
            {},
            question_map['fileIds']
        )
        update_form = self._bank.get_question_form_for_update(self._item.ident)
        update_form.set_ortho_choice(small_asset_data=DataInputStream(self.choice0sm),
                                     large_asset_data=DataInputStream(self.choice0big),
                                     name='Choice 1')
        self._bank.update_question(update_form)
        question = self._bank.get_item(self._item.ident).get_question()
        choice_files = question.get_files()
        self.assertEqual(
            len(choice_files['choices']),
            1
        )
        asset_id = Id(question.object_map['choices'][0]['assetId'])
        small_ac = self.get_asset_content_by_genus_type(asset_id,
                                                        OV_SET_SMALL_ASSET_CONTENT_TYPE)
        large_ac = self.get_asset_content_by_genus_type(asset_id,
                                                        OV_SET_LARGE_ASSET_CONTENT_TYPE)
        choice = choice_files['choices'][0]
        self.is_streamable_url(choice['largeOrthoViewSet'])
        self.is_streamable_url(choice['smallOrthoViewSet'])
        self.assertNotEqual(
            choice['largeOrthoViewSet'],
            choice['smallOrthoViewSet']
        )
        self.assertEqual(
            choice['name'],
            'Choice 1'
        )
        self.assertIn(
            str(large_ac.ident),
            choice['largeOrthoViewSet']
        )
        self.assertIn(
            str(small_ac.ident),
            choice['smallOrthoViewSet']
        )

    def test_can_set_answer(self):
        update_form = self._bank.get_question_form_for_update(self._item.ident)
        update_form.set_ortho_choice(small_asset_data=DataInputStream(self.choice0sm),
                                     large_asset_data=DataInputStream(self.choice0big),
                                     name='Choice 1')
        self._bank.update_question(update_form)

        choice_id = self._bank.get_item(self._item.ident).get_question().object_map['choices'][0]['id']
        answer_id = next(self._item.get_answer_ids())
        update_form = self._bank.get_answer_form_for_update(answer_id)
        update_form.add_choice_id(choice_id)
        self._bank.update_answer(update_form)

        answer_map = self._bank.get_item(self._item.ident).get_answers().next().object_map
        self.assertEqual(
            choice_id,
            answer_map['choiceIds'][0]
        )

    def test_can_set_review_options(self):
        def update_offered(offered_id, payload):
            offering_form = self._bank.get_assessment_offered_form_for_update(offered_id)

            offering_form.set_review_whether_correct(**payload)
            return self._bank.update_assessment_offered(offering_form)

        assessment2 = self.create_assessment_for_items(self._bank, [self._item])
        reviewable_type = Type(**{
            'authority': 'MOODLE.ORG',
            'namespace': 'assessment-offered-record-type',
            'identifier': 'review-options'
        })
        offering_form = self._bank.get_assessment_offered_form_for_create(assessment2.ident,
                                                                          [reviewable_type])
        new_offered = self._bank.create_assessment_offered(offering_form)

        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        for option, val in offered['reviewOptions']['whetherCorrect'].items():
            self.assertTrue(val)

        update_offered(new_offered.ident, {'during_attempt': False})
        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['afterDeadline'])

        update_offered(new_offered.ident, {'after_attempt': False})
        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['afterDeadline'])

        update_offered(new_offered.ident, {'before_deadline': False})
        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertTrue(offered['reviewOptions']['whetherCorrect']['afterDeadline'])

        update_offered(new_offered.ident, {'after_deadline': False})
        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertFalse(offered['reviewOptions']['whetherCorrect']['afterDeadline'])

    def test_can_set_learning_objectives(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        id_list = ['bank@123:MIT']
        id_list_obj = [Id(id_list[0])]
        form.set_learning_objectives(id_list_obj)
        updated_item = self._bank.update_item(form)

        item_map = self._bank.get_item(self._item.ident).object_map
        self.assertEqual(
            item_map['learningObjectiveIds'],
            id_list
        )

    def test_can_query_by_learning_objective(self):
        form = self._bank.get_item_form_for_update(self._item.ident)
        id_list = ['bank@123:MIT']
        id_list_obj = [Id(id_list[0])]
        form.set_learning_objectives(id_list_obj)
        updated_item = self._bank.update_item(form)

        querier = self._bank.get_item_query()
        querier.match_learning_objective_id(id_list_obj[0], match=True)

        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            1
        )
        self.assertEqual(
            str(results.next().ident),
            str(self._item.ident)
        )
        querier = self._bank.get_item_query()
        querier.match_learning_objective_id(Id('foo@bar:baz'), match=True)

        results = self._bank.get_items_by_query(querier)
        self.assertEqual(
            results.available(),
            0
        )

    def test_can_set_max_attempts_on_offered(self):
        reviewable_type = Type(**{
            'authority': 'MOODLE.ORG',
            'namespace': 'assessment-offered-record-type',
            'identifier': 'review-options'
        })
        assessment2 = self.create_assessment_for_items(self._bank, [self._item])
        offering_form = self._bank.get_assessment_offered_form_for_create(assessment2.ident,
                                                                          [reviewable_type])
        offering_form.set_max_attempts(2)
        new_offered = self._bank.create_assessment_offered(offering_form)

        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertEqual(
            offered['maxAttempts'],
            2
        )

        offering_form = self._bank.get_assessment_offered_form_for_update(new_offered.ident)
        offering_form.set_max_attempts(5)
        new_offered = self._bank.update_assessment_offered(offering_form)

        offered = self._bank.get_assessment_offered(new_offered.ident).object_map
        self.assertEqual(
            offered['maxAttempts'],
            5
        )

    def test_exception_thrown_if_taker_attempts_more_than_max_allowed(self):
        """taking = # takens...but can submit multiple times to the same taken"""
        reviewable_type = Type(**{
            'authority': 'MOODLE.ORG',
            'namespace': 'assessment-offered-record-type',
            'identifier': 'review-options'
        })
        assessment2 = self.create_assessment_for_items(self._bank, [self._item])
        offering_form = self._bank.get_assessment_offered_form_for_create(assessment2.ident,
                                                                          [reviewable_type])
        offering_form.set_max_attempts(1)
        new_offered = self._bank.create_assessment_offered(offering_form)

        form = self._bank.get_assessment_taken_form_for_create(new_offered.ident, [])
        taken2 = self._bank.create_assessment_taken(form)

        form = self._bank.get_assessment_taken_form_for_create(new_offered.ident, [])
        self.assertRaises(errors.PermissionDenied, self._bank.create_assessment_taken, form)


class QuestionLOTests(DLKitTestCase):
    def add_item(self, bank):
        form = bank.get_item_form_for_create([])
        form.display_name = 'a test item!'
        form.description = 'for testing with'
        form.set_learning_objectives([Id(self._lo)])
        new_item = bank.create_item(form)

        question_form = bank.get_question_form_for_create(new_item.ident,
                                                          [])
        question_form.display_name = 'Question for ' + new_item.display_name.text
        question_form.description = ''
        new_question = bank.create_question(question_form)

        answer_form = bank.get_answer_form_for_create(new_item.ident,
                                                      [])
        answer_form.display_name = 'Answer for ' + new_item.display_name.text
        new_answer = bank.create_answer(answer_form)

        item = bank.get_item(new_item.ident)
        return item

    def setUp(self):
        super(QuestionLOTests, self).setUp()

        self._lo = 'foo%3A1%40MIT'
        self._bank = self._get_test_bank()
        self._item = self.add_item(self._bank)

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(QuestionLOTests, self).tearDown()

    def test_question_object_map_has_item_learning_objective_ids(self):
        question = self._item.get_question()
        data = question.object_map
        self.assertEqual(
            data['learningObjectiveIds'],
            [self._lo]
        )


class QTITests(DLKitTestCase):
    def setUp(self):
        super(QTITests, self).setUp()

        self._bank = self._get_test_bank()
        # don't use the 'b' flag when reading, because we need it as string, not bytes
        self.test_file_1 = open(ABS_PATH + '/files/qti_multi_choice.xml', 'r')
        self.right_answer_choice_id = 'id8d815c87-4f7e-4ac6-b4ea-77124057eb33'
        self.item_types = [Type('item-record-type%3Aqti%40ODL.MIT.EDU'),
                           Type('osid-object%3Amulti-language%40ODL.MIT.EDU')]
        self.question_types = [Type('question-record-type%3Aqti%40ODL.MIT.EDU'),
                               Type('osid-object%3Amulti-language%40ODL.MIT.EDU')]
        self.answer_types = [Type('answer-record-type%3Aqti%40ODL.MIT.EDU'),
                             Type('answer-record-type%3Amulti-language-answer-with-feedback%40ODL.MIT.EDU')]

    def tearDown(self):
        """
        """
        self.test_file_1.close()
        super(QTITests, self).tearDown()

    def test_can_import_qti_multi_choice_xml(self):
        qti_xml = self.test_file_1.read()

        form = self._bank.get_item_form_for_create(self.item_types)
        form.display_name = 'qti multiple choice test'
        item = self._bank.create_item(form)

        q_form = self._bank.get_question_form_for_create(item.ident, self.question_types)
        q_form.load_from_qti_item(qti_xml)
        self._bank.create_question(q_form)

        a_form = self._bank.get_answer_form_for_create(item.ident, self.answer_types)
        a_form.load_from_qti_item(qti_xml, correct=True)
        self._bank.create_answer(a_form)

        item = self._bank.get_item(item.ident)

        item_map = item.object_map

        self.assertEqual(
            item_map['answers'][0]['choiceIds'][0],
            self.right_answer_choice_id
        )

        self.assertEqual(
            len(item_map['question']['choices']),
            4
        )

        choice_ids = [c['id'] for c in item_map['question']['choices']]
        self.assertIn(self.right_answer_choice_id, choice_ids)


class SearchItemPaginationTests(DLKitTestCase):
    def create_item(self, name="my new item"):
        form = self._bank.get_item_form_for_create([])

        form.display_name = str(name)
        form.description = 'Test item'

        return self._bank.create_item(form)

    def setUp(self):
        super(SearchItemPaginationTests, self).setUp()

        self._bank = self._get_test_bank()
        for i in range(1, 20):
            self.create_item(name=str(i))

    def tearDown(self):
        """
        Remove the test user from all groups in Membership
        Start from the smallest groupId because need to
        remove "parental" roles like for DepartmentAdmin / DepartmentOfficer
        """
        super(SearchItemPaginationTests, self).tearDown()

    def test_specifying_start_and_end_returns_right_objects(self):
        querier = self._bank.get_item_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bank.get_item_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._bank.get_items_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        items_found = results.get_items()
        self.assertEqual(
            items_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        for expected_name in expected_names:
            self.assertEqual(
                items_found.next().display_name.text,
                expected_name
            )

    def test_null_start_and_end_throws_exception(self):
        searcher = self._bank.get_item_search()

        self.assertRaises(errors.NullArgument, searcher.limit_result_set, 1, None)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, 5)
        self.assertRaises(errors.NullArgument, searcher.limit_result_set, None, None)

    def test_end_less_than_start_throws_exception(self):
        searcher = self._bank.get_item_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 1)

    def test_end_equal_to_start_throws_exception(self):
        searcher = self._bank.get_item_search()

        self.assertRaises(errors.InvalidArgument, searcher.limit_result_set, 5, 5)

    def test_end_greater_than_total_docs_returns_everything(self):
        querier = self._bank.get_item_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bank.get_item_search()
        searcher.limit_result_set(1, 25)  # should return 11 results, 1 + 10-19

        results = self._bank.get_items_by_search(querier, searcher)
        items_found = results.get_items()
        self.assertEqual(
            items_found.available(),
            11
        )

        expected_names = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
        for expected_name in expected_names:
            self.assertEqual(
                items_found.next().display_name.text,
                expected_name
            )

    def test_can_search_within_an_id_list(self):
        querier = self._bank.get_item_query()
        querier.match_keyword('1', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bank.get_item_search()
        searcher.limit_result_set(1, 5)  # should return 5 results, numbered 1, 10, 11, 12, 13

        results = self._bank.get_items_by_search(querier, searcher)
        self.assertEqual(
            results.get_result_size(),
            5
        )
        items_found = results.get_items()
        self.assertEqual(
            items_found.available(),
            5
        )

        expected_names = ['1', '10', '11', '12', '13']
        new_id_to_search_on = []
        for expected_name in expected_names:
            if expected_name == '12':
                new_id_to_search_on.append(items_found.next().ident)
            else:
                next(items_found)

        querier = self._bank.get_item_query()
        querier.match_keyword('2', WORDIGNORECASE_STRING_MATCH_TYPE, True)

        searcher = self._bank.get_item_search()
        searcher.search_among_items(new_id_to_search_on)

        results = self._bank.get_items_by_search(querier, searcher)  # should only return "12", and not "2"
        self.assertEqual(
            results.get_result_size(),
            1
        )
        items_found = results.get_items()
        self.assertEqual(
            items_found.available(),
            1
        )

        self.assertEqual(
            str(items_found.next().ident),
            str(new_id_to_search_on[0])
        )


class MagicMultipleChoiceItemTests(GeneralTests):
    def create_assessment_offered_for_items(self, item_ids):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = 'a test assessment'
        form.description = 'for testing with'
        new_assessment = self._bank.create_assessment(form)

        for item_id in item_ids:
            if isinstance(item_id, str):
                item_id = Id(item_id)
            self._bank.add_item(new_assessment.ident, item_id)

        form = self._bank.get_assessment_offered_form_for_create(new_assessment.ident, [])
        new_offered = self._bank.create_assessment_offered(form)

        return new_offered

    def create_mc_item(self):
        form = self._bank.get_item_form_for_create([WRONG_ANSWER_ITEM_RECORD,
                                                    SOURCEABLE_RECORD,
                                                    PROVENANCE_ITEM_RECORD,
                                                    MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'FbW MC item'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident,
                                                       [MC_RANDOMIZED_RECORD])

        form.display_name = "my question"
        form.set_text('what is life about? {0}'.format(str(randint(0, 10))))
        for index, choice in enumerate(['1', '42', '81']):
            form.add_choice(choice, 'Choice {0}'.format(str(index)))
        question = self._bank.create_question(form)

        choices = question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]

        form = self._bank.get_answer_form_for_create(item.ident,
                                                     [MC_ANSWER_RECORD])
        form.add_choice_id(right_answer['id'])
        form.set_genus_type(RIGHT_ANSWER_GENUS)
        form.set_feedback('right!')
        self._bank.create_answer(form)

        form = self._bank.get_answer_form_for_create(item.ident,
                                                     [MC_ANSWER_RECORD])
        form.add_choice_id(wrong_answer['id'])
        self._confused_lo_id = 'foo%3A123%40MIT'
        form.set_confused_learning_objective_ids([self._confused_lo_id])
        form.set_genus_type(WRONG_ANSWER_GENUS)
        form.set_feedback('wrong ...')
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        return item

    def create_taken_for_items(self, item_ids):
        new_offered = self.create_assessment_offered_for_items(item_ids)

        form = self._bank.get_assessment_taken_form_for_create(new_offered.ident, [])
        taken = self._bank.create_assessment_taken(form)
        return taken, new_offered

    def setUp(self):
        super(MagicMultipleChoiceItemTests, self).setUp()

    def tearDown(self):
        super(MagicMultipleChoiceItemTests, self).tearDown()

    def test_taken_preserves_the_question_choice_order(self):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        taken, offered = self.create_taken_for_items([item1.ident, item2.ident])

        first_section = self._bank.get_first_assessment_section(taken.ident)
        questions = self._bank.get_questions(first_section.ident)

        question_1 = next(questions)
        question_1_map = question_1.object_map

        question_2 = next(questions)
        question_2_map = question_2.object_map

        original_question_1_id = question_1_map['id']
        original_question_2_id = question_2_map['id']
        original_choice_order_1 = question_1_map['choices']
        original_choice_order_2 = question_2_map['choices']

        for i in range(0, 10):
            questions = self._bank.get_questions(first_section.ident)

            new_question_1 = next(questions)
            new_question_1_map = new_question_1.object_map

            new_question_2 = next(questions)
            new_question_2_map = new_question_2.object_map

            self.assertEqual(
                new_question_1_map['choices'],
                original_choice_order_1
            )
            self.assertEqual(
                new_question_2_map['choices'],
                original_choice_order_2
            )
            self.assertEqual(
                new_question_1_map['id'],
                original_question_1_id
            )
            self.assertEqual(
                new_question_2_map['id'],
                original_question_2_id
            )

    def test_different_users_see_different_orders(self):
        student_am = get_manager(self.student_req, 'assessment')
        student_bank = student_am.get_bank(self._bank.ident)

        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        taken, offered = self.create_taken_for_items([item1.ident, item2.ident])

        instructor_first_section = self._bank.get_first_assessment_section(taken.ident)
        instructor_questions = self._bank.get_questions(instructor_first_section.ident)
        instructor_question_1 = next(instructor_questions)
        instructor_question_1_map = instructor_question_1.object_map

        instructor_question_2 = next(instructor_questions)
        instructor_question_2_map = instructor_question_2.object_map

        # this might fail sometimes, so try multiple times
        has_same_choice_order = 0
        for i in range(0, 20):
            form = student_bank.get_assessment_taken_form_for_create(offered.ident, [])
            student_taken = student_bank.create_assessment_taken(form)

            student_first_section = student_bank.get_first_assessment_section(student_taken.ident)
            student_questions = student_bank.get_questions(student_first_section.ident)

            student_question_1 = next(student_questions)
            student_question_1_map = student_question_1.object_map

            student_question_2 = next(student_questions)
            student_question_2_map = student_question_2.object_map

            # with unique question IDs, check that they are different, then
            # check the choices to see if they do match
            self.assertNotEqual(instructor_question_1_map['id'], student_question_1_map['id'])
            self.assertNotEqual(instructor_question_2_map['id'], student_question_2_map['id'])
            if (instructor_question_1_map['choices'] == student_question_1_map['choices'] or
                    instructor_question_2_map['choices'] == student_question_2_map['choices']):
                has_same_choice_order += 1
            self._bank.delete_assessment_taken(student_taken.ident)

        self.assertTrue(0 < has_same_choice_order <= 19)  # not all should be the same, but it could happen


class AssessmentSectionLOTests(GeneralTests):
    def create_mc_item(self):
        form = self._bank.get_item_form_for_create([WRONG_ANSWER_ITEM_RECORD,
                                                    SOURCEABLE_RECORD,
                                                    PROVENANCE_ITEM_RECORD,
                                                    MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'FbW MC item'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident,
                                                       [MC_RANDOMIZED_RECORD])

        form.display_name = "my question"
        form.set_text('what is life about? {0}'.format(str(randint(0, 10))))
        for index, choice in enumerate(['1', '42', '81']):
            form.add_choice(choice, 'Choice {0}'.format(str(index)))
        question = self._bank.create_question(form)

        choices = question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]

        form = self._bank.get_answer_form_for_create(item.ident,
                                                     [MC_ANSWER_RECORD])
        form.add_choice_id(right_answer['id'])
        form.set_genus_type(RIGHT_ANSWER_GENUS)
        form.set_feedback('right!')
        self._bank.create_answer(form)

        form = self._bank.get_answer_form_for_create(item.ident,
                                                     [MC_ANSWER_RECORD])
        form.add_choice_id(wrong_answer['id'])
        self._confused_lo_id = 'foo%3A123%40MIT'
        form.set_confused_learning_objective_ids([self._confused_lo_id])
        form.set_genus_type(WRONG_ANSWER_GENUS)
        form.set_feedback('wrong ...')
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        return item

    def create_taken_for_assessment(self, assessment):
        # make sure this data still shows up when taking the assessment
        offered_form = self._bank.get_assessment_offered_form_for_create(assessment.ident, [])
        offered = self._bank.create_assessment_offered(offered_form)

        taken_form = self._bank.get_assessment_taken_form_for_create(offered.ident, [])
        return self._bank.create_assessment_taken(taken_form)

    def setUp(self):
        super(AssessmentSectionLOTests, self).setUp()

    def tearDown(self):
        super(AssessmentSectionLOTests, self).tearDown()

    def test_can_create_multiple_sections_per_assessment(self):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident, [])
        form.display_name = 'part 1'
        part_1 = self._bank.create_assessment_part_for_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident, [])
        form.display_name = 'part 2'
        part_2 = self._bank.create_assessment_part_for_assessment(form)
        assessment = self._bank.get_assessment(assessment.ident)

        next_part_id = assessment.get_next_assessment_part_id()
        self.assertEqual(
            str(next_part_id),
            str(part_1.ident)
        )

        next_part_id = assessment.get_next_assessment_part_id(next_part_id)
        self.assertEqual(
            str(next_part_id),
            str(part_2.ident)
        )

        # make sure this shows up as two section when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_section_map = first_section.object_map
        self.assertNotEqual(
            first_section_map['id'],
            str(part_1.ident)
        )
        self.assertEqual(
            first_section._my_map['assessmentPartId'],
            str(part_1.ident)
        )

        second_section = self._bank.get_next_assessment_section(first_section.ident)
        second_section_map = second_section.object_map
        self.assertNotEqual(
            second_section_map['id'],
            str(part_2.ident)
        )
        self.assertEqual(
            second_section._my_map['assessmentPartId'],
            str(part_2.ident)
        )

    def test_can_set_section_items_on_create(self):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        item3 = self.create_mc_item()

        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident, [])
        form.display_name = 'part 1'
        part_1 = self._bank.create_assessment_part_for_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident, [])
        form.display_name = 'part 2'
        part_2 = self._bank.create_assessment_part_for_assessment(form)

        self._bank.add_item(item1.ident, part_1.ident)
        self._bank.add_item(item2.ident, part_1.ident)
        self._bank.add_item(item3.ident, part_2.ident)

        assessment = self._bank.get_assessment(assessment.ident)

        next_part_id = assessment.get_next_assessment_part_id()
        self.assertEqual(
            str(next_part_id),
            str(part_1.ident)
        )
        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            2
        )
        self.assertEqual(
            str(items.next().ident),
            str(item1.ident)
        )
        self.assertEqual(
            str(items.next().ident),
            str(item2.ident)
        )

        next_part_id = assessment.get_next_assessment_part_id(next_part_id)
        self.assertEqual(
            str(next_part_id),
            str(part_2.ident)
        )
        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            1
        )
        self.assertEqual(
            str(items.next().ident),
            str(item3.ident)
        )

        # make sure the right questions come out via the right sections when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_questions = self._bank.get_questions(first_section.ident)
        self.assertEqual(
            first_questions.available(),
            2
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        self.assertNotIn(item1.ident.identifier, first_questions.next().ident.identifier)
        self.assertNotIn(item2.ident.identifier, first_questions.next().ident.identifier)

        second_section = self._bank.get_next_assessment_section(first_section.ident)
        second_questions = self._bank.get_questions(second_section.ident)
        self.assertEqual(
            second_questions.available(),
            1
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        self.assertNotIn(item3.ident.identifier, second_questions.next().ident.identifier)

    def test_can_set_section_learning_objective_on_create(self):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                             [ASSESSMENT_SECTION_WITH_OBJECTIVE])
        form.display_name = 'part 1'
        lo = 'mc3-objective%3A9729%40MIT-OEIT'
        form.set_learning_objective_id(lo)
        part = self._bank.create_assessment_part_for_assessment(form)
        self.assertEqual(
            part.learning_objective_id,
            lo
        )

        # make sure this data still shows up when taking the assessment
        taken = self.create_taken_for_assessment(assessment)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section._assessment_part.learning_objective_id,
            lo
        )
        self.assertEqual(
            section_map['learningObjectiveId'],
            lo
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )

    def test_can_update_section_items(self):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        item3 = self.create_mc_item()

        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident, [])
        form.display_name = 'part'
        part = self._bank.create_assessment_part_for_assessment(form)

        self._bank.add_item(item1.ident, part.ident)
        self._bank.add_item(item2.ident, part.ident)

        assessment = self._bank.get_assessment(assessment.ident)

        next_part_id = assessment.get_next_assessment_part_id()
        self.assertEqual(
            str(next_part_id),
            str(part.ident)
        )
        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            2
        )
        self.assertEqual(
            str(items.next().ident),
            str(item1.ident)
        )
        self.assertEqual(
            str(items.next().ident),
            str(item2.ident)
        )

        # make sure the right questions come out via the right sections when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_questions = self._bank.get_questions(first_section.ident)
        self.assertEqual(
            first_questions.available(),
            2
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        orig_question_1 = next(first_questions)
        orig_question_2 = next(first_questions)
        self.assertNotIn(item1.ident.identifier, orig_question_1.ident.identifier)
        self.assertNotIn(item2.ident.identifier, orig_question_2.ident.identifier)

        # now let's change the items and make sure a new taken has the new items
        self._bank.remove_item(item1.ident, part.ident)
        self._bank.add_item(item3.ident, part.ident)

        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            2
        )
        self.assertEqual(
            str(items.next().ident),
            str(item2.ident)
        )
        self.assertEqual(
            str(items.next().ident),
            str(item3.ident)
        )

        # make sure the right questions come out via the right sections when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_questions = self._bank.get_questions(first_section.ident)
        self.assertEqual(
            first_questions.available(),
            2
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        round_2_question_1 = next(first_questions)
        round_2_question_2 = next(first_questions)
        self.assertNotIn(item2.ident.identifier, round_2_question_1.ident.identifier)
        self.assertNotIn(item3.ident.identifier, round_2_question_2.ident.identifier)
        self.assertEqual(
            round_2_question_1._my_map['itemId'],
            orig_question_2._my_map['itemId']
        )

        # now let's re-order the items
        self._bank.move_item_ahead(item3.ident, part.ident, item2.ident)
        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            2
        )
        round_3_question_1 = next(items)
        round_3_question_2 = next(items)
        self.assertEqual(
            str(round_3_question_1.ident),
            str(item3.ident)
        )
        self.assertEqual(
            str(round_3_question_2.ident),
            str(item2.ident)
        )
        self.assertEqual(
            round_3_question_1._my_map['question']['itemId'],
            round_2_question_2._my_map['itemId']
        )
        self.assertEqual(
            round_3_question_2._my_map['question']['itemId'],
            round_2_question_1._my_map['itemId']
        )

        # make sure the right questions come out via the right sections when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_questions = self._bank.get_questions(first_section.ident)
        self.assertEqual(
            first_questions.available(),
            2
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        round_4_question_1 = next(first_questions)
        round_4_question_2 = next(first_questions)
        self.assertNotIn(item3.ident.identifier, round_4_question_1.ident.identifier)
        self.assertNotIn(item2.ident.identifier, round_4_question_2.ident.identifier)
        self.assertEqual(
            round_3_question_1._my_map['question']['itemId'],
            round_4_question_1._my_map['itemId']
        )
        self.assertEqual(
            round_3_question_2._my_map['question']['itemId'],
            round_4_question_2._my_map['itemId']
        )

        # and moving behind also works
        self._bank.move_item_behind(item3.ident, part.ident, item2.ident)
        items = self._bank.get_assessment_part_items(next_part_id)
        self.assertEqual(
            items.available(),
            2
        )
        round_5_question_1 = next(items)
        round_5_question_2 = next(items)
        self.assertEqual(
            str(round_5_question_1.ident),
            str(item2.ident)
        )
        self.assertEqual(
            str(round_5_question_2.ident),
            str(item3.ident)
        )
        self.assertEqual(
            round_5_question_1._my_map['question']['itemId'],
            round_4_question_2._my_map['itemId']
        )
        self.assertEqual(
            round_5_question_2._my_map['question']['itemId'],
            round_4_question_1._my_map['itemId']
        )

        # make sure the right questions come out via the right sections when taking
        taken = self.create_taken_for_assessment(assessment)
        first_section = self._bank.get_first_assessment_section(taken.ident)
        first_questions = self._bank.get_questions(first_section.ident)
        self.assertEqual(
            first_questions.available(),
            2
        )
        # magic questions, so just check the original identifier is included
        # Aug 22, 2016: behavior changed -- all question IDs are unique now, so
        # update test to reflect that.
        round_6_question_1 = next(first_questions)
        round_6_question_2 = next(first_questions)
        self.assertNotIn(item2.ident.identifier, round_6_question_1.ident.identifier)
        self.assertNotIn(item3.ident.identifier, round_6_question_2.ident.identifier)
        self.assertEqual(
            round_5_question_1._my_map['question']['itemId'],
            round_6_question_1._my_map['itemId']
        )
        self.assertEqual(
            round_5_question_2._my_map['question']['itemId'],
            round_6_question_2._my_map['itemId']
        )

    def test_can_update_section_learning_objective(self):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                             [ASSESSMENT_SECTION_WITH_OBJECTIVE])
        form.display_name = 'part 1'
        lo_1 = 'mc3-objective%3A9729%40MIT-OEIT'
        lo_2 = 'mc3-objective%3A9730%40MIT-OEIT'
        form.set_learning_objective_id(lo_1)
        part = self._bank.create_assessment_part_for_assessment(form)
        self.assertEqual(
            part.learning_objective_id,
            lo_1
        )

        # make sure this data still shows up when taking the assessment
        taken = self.create_taken_for_assessment(assessment)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section._assessment_part.learning_objective_id,
            lo_1
        )
        self.assertEqual(
            section_map['learningObjectiveId'],
            lo_1
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )

        # now let's change the part LO, see if it changes in the taken
        form = self._bank.get_assessment_part_form_for_update(part.ident)
        form.set_learning_objective_id(lo_2)
        self._bank.update_assessment_part(part.ident, form)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section._assessment_part.learning_objective_id,
            lo_2
        )
        self.assertEqual(
            section_map['learningObjectiveId'],
            lo_2
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )

    def test_can_set_section_minimum_proficiency_on_create(self):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                             [ASSESSMENT_SECTION_WITH_OBJECTIVE])
        form.display_name = 'part 1'
        min_proficiency = Id('grading.Grade%3A2%40MIT-OEIT')
        form.set_minimum_proficiency(min_proficiency)
        part = self._bank.create_assessment_part_for_assessment(form)
        self.assertEqual(
            part.minimum_proficiency,
            str(min_proficiency)
        )

        # make sure this data still shows up when taking the assessment
        taken = self.create_taken_for_assessment(assessment)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section._assessment_part.minimum_proficiency,
            str(min_proficiency)
        )
        self.assertEqual(
            section_map['minimumProficiency'],
            str(min_proficiency)
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )

    def test_can_update_minimum_proficiency(self):
        form = self._bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._bank.create_assessment(form)

        form = self._bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                             [ASSESSMENT_SECTION_WITH_OBJECTIVE])
        form.display_name = 'part 1'
        min_proficiency = Id('grading.Grade%3A2%40MIT-OEIT')
        new_proficiency = Id('grading.Grade%3A3%40MIT-OEIT')
        form.set_minimum_proficiency(min_proficiency)
        part = self._bank.create_assessment_part_for_assessment(form)
        self.assertEqual(
            part.minimum_proficiency,
            str(min_proficiency)
        )

        # make sure this data still shows up when taking the assessment
        taken = self.create_taken_for_assessment(assessment)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section.minimum_proficiency,
            str(min_proficiency)
        )
        self.assertEqual(
            section_map['minimumProficiency'],
            str(min_proficiency)
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )

        # now let's change the part proficiency, see if it changes in the taken
        form = self._bank.get_assessment_part_form_for_update(part.ident)
        form.set_minimum_proficiency(new_proficiency)
        self._bank.update_assessment_part(part.ident, form)

        section = self._bank.get_first_assessment_section(taken.ident)
        section_map = section.object_map
        self.assertEqual(
            section.minimum_proficiency,
            str(new_proficiency)
        )
        self.assertEqual(
            section_map['minimumProficiency'],
            str(new_proficiency)
        )
        self.assertNotEqual(
            section_map['id'],
            str(part.ident)
        )


class ScaffoldDownTests(DLKitTestCase):
    @staticmethod
    def _extract_item_id(id_str):
        # return unquote(Id(id_str).identifier).split('?')[0]
        # since using ._my_map['itemId'], just return it
        return id_str

    def create_mc_item(self, level=None):
        form = self._item_bank.get_item_form_for_create([MC_ITEM_RECORD,  # Take out WRONG_ANSWER_ITEM_RECORD and replace
                                                         SOURCEABLE_RECORD,
                                                         PROVENANCE_ITEM_RECORD,
                                                         MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'FbW MC item'
        if level is not None:
            form.set_learning_objectives([Id('foo%3A{0}%40MIT'.format(level))])
        item = self._item_bank.create_item(form)

        form = self._item_bank.get_question_form_for_create(item.ident,
                                                            [MC_RANDOMIZED_RECORD])

        form.display_name = "my question"
        form.set_text('what is life about? {0}'.format(str(randint(0, 10))))
        for index, choice in enumerate(['1', '42', '81']):
            form.add_choice(choice, 'Choice {0}'.format(str(index)))
        question = self._item_bank.create_question(form)

        choices = question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]

        form = self._item_bank.get_answer_form_for_create(item.ident,
                                                          [MC_ANSWER_RECORD])
        form.add_choice_id(right_answer['id'])
        form.set_genus_type(RIGHT_ANSWER_GENUS)
        form.set_feedback('right!')
        self._item_bank.create_answer(form)

        form = self._item_bank.get_answer_form_for_create(item.ident,
                                                          [MC_ANSWER_RECORD])
        form.add_choice_id(wrong_answer['id'])
        if level is not None:
            lo_identifier = level + 1
        else:
            lo_identifier = 1
        self._confused_lo_id = 'foo%3A{0}%40MIT'.format(str(lo_identifier))  # use this as a proxy for level down
        if level != 2:
            form.set_confused_learning_objective_ids([self._confused_lo_id])
        form.set_genus_type(WRONG_ANSWER_GENUS)
        form.set_feedback('wrong ...')
        self._item_bank.create_answer(form)

        item = self._item_bank.get_item(item.ident)
        return item

    def create_scaffolded_assessment(self, number_waypoints, create_waypoints=True):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        item3 = self.create_mc_item()
        item4 = self.create_mc_item()

        # let's make two parts, each with two items (so really two magic parts, for a total of 4 magic parts)
        form = self._assessment_bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._assessment_bank.create_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 1'
        form.set_minimum_proficiency(Id('foo%3A1%40MIT'))
        form.set_learning_objective_id('foo%3A1%40MIT')
        parent_part_1 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 1'
        form.set_item_ids([item1.ident])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_1 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 2'
        form.set_item_ids([item2.ident])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_2 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        # second "parent" part
        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 2'
        form.set_minimum_proficiency(Id('foo%3A2%40MIT'))
        form.set_learning_objective_id('foo%3A42%40MIT')

        parent_part_2 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 3'
        form.set_item_ids([item3.ident])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_3 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 4'
        form.set_item_ids([item4.ident])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_4 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        self._items = {
            'target': [item1, item2, item3, item4]
        }
        if create_waypoints:
            scaffold_items1 = []
            scaffold_items2 = []
            for i in range(0, number_waypoints):
                scaffold_items1.append(self.create_mc_item(level=1))
                scaffold_items2.append(self.create_mc_item(level=2))
            self._items.update({
                'waypoint1': scaffold_items1,
                'waypoint2': scaffold_items2
            })

        return self._assessment_bank.get_assessment(assessment.ident)

    def create_minimal_scaffolded_assessment(self):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        item3 = self.create_mc_item()
        item4 = self.create_mc_item()

        scaffold_item1_1 = self.create_mc_item(level=1)

        scaffold_item2_1 = self.create_mc_item(level=2)

        # let's make two parts, each with two items (so really two magic parts, for a total of 4 magic parts)
        form = self._assessment_bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._assessment_bank.create_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 1'
        form.set_minimum_proficiency(Id('foo%3A1%40MIT'))
        form.set_learning_objective_id('foo%3A1%40MIT')
        parent_part_1 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 1'
        form.set_item_ids([item1.ident])
        form.set_item_bank_id(self._item_bank.ident)
        magic_part_1 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 2'
        form.set_item_ids([item2.ident])
        form.set_item_bank_id(self._item_bank.ident)
        magic_part_2 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        # second "parent" part
        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 2'
        form.set_minimum_proficiency(Id('foo%3A2%40MIT'))
        form.set_learning_objective_id('foo%3A42%40MIT')

        parent_part_2 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 3'
        form.set_item_ids([item3.ident])
        form.set_item_bank_id(self._item_bank.ident)
        magic_part_3 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 4'
        form.set_item_ids([item4.ident])
        form.set_item_bank_id(self._item_bank.ident)
        magic_part_4 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        self._items = {
            'target': [item1, item2, item3, item4],
            'waypoint1': [scaffold_item1_1],
            'waypoint2': [scaffold_item2_1]
        }

        return self._assessment_bank.get_assessment(assessment.ident)

    def create_taken(self, number_waypoints=4, create_waypoints=True):
        # make sure this data still shows up when taking the assessment
        assessment = self.create_scaffolded_assessment(number_waypoints, create_waypoints)
        offered_form = self._assessment_bank.get_assessment_offered_form_for_create(assessment.ident,
                                                                                    [REVIEWABLE_OFFERED])
        self._offered = self._assessment_bank.create_assessment_offered(offered_form)

        taken_form = self._assessment_bank.get_assessment_taken_form_for_create(self._offered.ident,
                                                                                [REVIEWABLE_TAKEN,
                                                                                 ADVANCED_QUERY_TAKEN])
        return self._assessment_bank.create_assessment_taken(taken_form)

    def create_taken_only(self):
        taken_form = self._assessment_bank.get_assessment_taken_form_for_create(self._offered.ident,
                                                                                [REVIEWABLE_TAKEN,
                                                                                 ADVANCED_QUERY_TAKEN])
        return self._assessment_bank.create_assessment_taken(taken_form)

    def get_questions_for_taken(self, taken_id):
        """gets all questions across all sections"""
        sections = []
        first_section = self._assessment_bank.get_first_assessment_section(taken_id)
        sections.append(first_section)
        try:
            previous_section_id = first_section.ident
            while True:
                next_section = self._assessment_bank.get_next_assessment_section(previous_section_id)
                previous_section_id = next_section.ident
                sections.append(next_section)
        except (StopIteration, errors.IllegalState):
            final_sections = []
            for section in sections:
                new_questions = list(self._assessment_bank.get_questions(section.ident))
                section_map = {
                    'questions': new_questions,
                    'section_id': section.ident
                }

                final_sections.append(section_map)

            return final_sections

    def num_parts(self, val, sequestered=False):
        if sequestered:
            self._assessment_bank.use_unsequestered_assessment_part_view()
        else:
            self._assessment_bank.use_sequestered_assessment_part_view()
        self.assertEqual(
            self._assessment_bank.get_assessment_parts().available(),
            int(val)
        )

    def setUp(self):
        super(ScaffoldDownTests, self).setUp()
        self._item_bank = self._get_test_bank()
        self._assessment_bank = self.create_new_bank(name="bank for assessments")

    def tearDown(self):
        super(ScaffoldDownTests, self).tearDown()

    def validate_number_sections_and_questions(self, sections, expected_tuple):
        expected_num_sections = expected_tuple[0]
        expected_num_q_per_section = expected_tuple[1]
        self.assertEqual(
            len(sections),
            expected_num_sections
        )
        for index, section in enumerate(sections):
            self.assertEqual(
                len(section['questions']),
                expected_num_q_per_section[index]
            )

    def test_getting_answer_right_does_not_generate_more_parts(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)

        self.validate_number_sections_and_questions(sections, (2, (2, 2)))

        questions = []
        for s in sections:
            questions += s['questions']
        for index, target in enumerate(self._items['target']):
            self.assertEqual(str(target.ident), questions[index]._my_map['itemId'])

        section_1 = sections[0]
        choices = section_1['questions'][0].get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       section_1['questions'][0].ident)
        form.add_choice_id(right_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              section_1['questions'][0].ident,
                                              form)

        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)

        response = self._assessment_bank.get_response(section_1['section_id'],
                                                      section_1['questions'][0].ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            right_answer['id']
        )

    def test_getting_wrong_answer_creates_second_level_parts(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_1 = sections[0]
        choices = section_1['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       section_1['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              section_1['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (3, 2)))

        self.num_parts(2, sequestered=False)

        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]

        for index, question_id_str in enumerate(question_id_strs):
            if index == 0:
                self.assertEqual(str(self._items['target'][0].ident),
                                 question_id_str)
            elif index == 1:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))
            else:
                self.assertEqual(str(self._items['target'][index - 1].ident),
                                 question_id_str)

        response = self._assessment_bank.get_response(section_1['section_id'],
                                                      section_1['questions'][0].ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            wrong_answer['id']
        )

    def test_getting_wrong_answer_in_second_section_creates_second_level_parts(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)

        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]

        for index, question_id_str in enumerate(question_id_strs):
            if index < 3:
                self.assertEqual(str(self._items['target'][index].ident),
                                 question_id_str)
            elif index == 3:
                self.assertTrue(any(t.ident.identifier in question_id_str
                                    for t in self._items['waypoint1']))
            else:
                self.assertEqual(str(self._items['target'][index - 1].ident),
                                 question_id_str)

        response = self._assessment_bank.get_response(section_2['section_id'],
                                                      section_2['questions'][0].ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            wrong_answer['id']
        )

    def test_answering_second_level_question_right_returns_to_first_level(self):
        """ basically getting a second level question right does not generate new questions
        :return:
        """
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)

        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # now let's get the new question right
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        choices = new_question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(right_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]
        for index, question_id_str in enumerate(question_id_strs):
            if index < 3:
                self.assertEqual(str(self._items['target'][index].ident),
                                 question_id_str)
            elif index == 3:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))
            else:
                self.assertEqual(str(self._items['target'][index - 1].ident),
                                 question_id_str)

        response = self._assessment_bank.get_response(section_2['section_id'],
                                                      new_question.ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            right_answer['id']
        )

    def test_answering_second_level_part_wrong_goes_to_third_level(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        # because a new question is also generated a the first level, i.e. 1.2
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]

        for index, question_id_str in enumerate(question_id_strs):
            if index < 3:
                self.assertEqual(str(self._items['target'][index].ident),
                                 question_id_str)
            elif index == 3:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))
            elif index == 4:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint2']))
            else:
                self.assertEqual(str(self._items['target'][index - 2].ident),
                                 question_id_str)

        response = self._assessment_bank.get_response(section_2['section_id'],
                                                      new_question.ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            wrong_answer['id']
        )

    def test_lo_on_next_question_matches_wrong_answer_lo_when_moving_down(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A1%40MIT']
        )
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        section_2 = sections[1]
        new_question = section_2['questions'][2]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint2']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A2%40MIT']
        )

    def test_lo_on_next_question_matches_previous_question_when_moving_up(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # let's check the LOs
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A1%40MIT']
        )

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        # as soon as you get this one wrong, it generates 1.1.1
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # let's check the LOs
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A1%40MIT']
        )
        new_question = section_2['questions'][2]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint2']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A2%40MIT']
        )

        # now let's get the second-level waypoint question in the part right
        # this should bump us back up to a 1.2 question
        section_2 = sections[1]
        new_question = section_2['questions'][2]
        choices = new_question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(right_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 5)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # let's check the LOs
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A1%40MIT']
        )
        new_question = section_2['questions'][2]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint2']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A2%40MIT']
        )
        new_question = section_2['questions'][3]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A1%40MIT']
        )

    def test_display_labels_handled_correctly_when_moving_up_and_down(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # let's check the displayLabels
        questions = []
        for s in sections:
            questions += s['questions']

        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '2']
        )

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        # as soon as you get this one wrong, it generates 1.1.1
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '1.1.1', '2']
        )

        # now let's get the second-level waypoint question in the part right
        # this should bump us back up to a 1.2 question
        section_2 = sections[1]
        new_question = section_2['questions'][2]
        choices = new_question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(right_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        # no new questions are generated

        self.validate_number_sections_and_questions(sections, (2, (2, 5)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '1.1.1', '1.2', '2']
        )

    def test_display_label_handled_correctly_for_multiple_levels_of_depth(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # let's check the displayLabels
        questions = []
        for s in sections:
            questions += s['questions']

        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '2']
        )

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint1']))
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '1.1.1', '2']
        )

        # now let's get a second question in the part wrong
        section_1 = sections[0]
        new_question = section_1['questions'][1]
        self.assertTrue(str(self._items['target'][1].ident) == new_question._my_map['itemId'])
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              new_question.ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (3, 4)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '2.1', '1', '1.1', '1.1.1', '2']
        )

    def test_can_skip_around_and_still_get_scaffold_questions(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][1].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][1].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][1].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # now let's get another question wrong
        section_1 = sections[0]
        new_question = section_1['questions'][1]
        self.assertTrue(str(self._items['target'][1].ident) == new_question._my_map['itemId'])
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (3, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]

        for index, question_id_str in enumerate(question_id_strs):
            if index < 2:
                self.assertEqual(str(self._items['target'][index].ident),
                                 question_id_str)
            elif index == 2:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))
            elif index == 3 or index == 4:
                self.assertTrue(str(self._items['target'][index - 1].ident),
                                question_id_str)
            elif index == 5:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))

    def test_skipping_around_in_same_section_does_not_get_same_waypoint(self):
        self.num_parts(0)
        taken = self.create_taken()
        for i in range(0, 10):
            if i > 0:
                taken = self.create_taken_only()
            self.num_parts(2, sequestered=False)
            self.num_parts(6, sequestered=True)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 2)))
            section_2 = sections[1]
            choices = section_2['questions'][1].get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           section_2['questions'][1].ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  section_2['questions'][1].ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            # now let's get another question wrong
            new_question = section_2['questions'][0]
            choices = new_question.get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           new_question.ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  new_question.ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 4)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            questions = []
            for s in sections:
                questions += s['questions']

            question_id_strs = [q._my_map['itemId'] for q in questions]
            first_waypoint_id = ''
            second_waypoint_id = ''

            for index, question_id_str in enumerate(question_id_strs):
                if index < 3:
                    self.assertEqual(str(self._items['target'][index].ident),
                                     question_id_str)
                elif index == 3 or index == 5:
                    self.assertTrue(any(str(t.ident) == question_id_str
                                        for t in self._items['waypoint1']))
                    if index == 3:
                        first_waypoint_id = self._extract_item_id(question_id_str)
                    else:
                        second_waypoint_id = self._extract_item_id(question_id_str)
                elif index == 4:
                    self.assertEqual(str(self._items['target'][index - 1].ident),
                                     question_id_str)
                else:
                    self.assertEqual(str(self._items['target'][index - 2].ident),
                                     question_id_str)

            if first_waypoint_id == second_waypoint_id:
                self.fail('Got an identical waypoint ...')

            # now delete / finish the taken
            self._assessment_bank.delete_assessment_taken(taken.ident)
        # should be different within the same section, if you get another one wrong

    def test_skipping_around_in_different_sections_allows_same_waypoint(self):
        self.num_parts(0)
        number_identical_waypoints = 0
        taken = self.create_taken(number_waypoints=2)
        for i in range(0, 15):
            if i > 0:
                taken = self.create_taken_only()
            self.num_parts(2, sequestered=False)
            self.num_parts(6, sequestered=True)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 2)))
            section_2 = sections[1]
            choices = section_2['questions'][1].get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           section_2['questions'][1].ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  section_2['questions'][1].ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            # now let's get another question wrong
            section_1 = sections[0]
            new_question = section_1['questions'][0]
            choices = new_question.get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                           new_question.ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_1['section_id'],
                                                  new_question.ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (3, 3)))

            # and let's get another one wrong in section 1 -- this should
            # match the ID of the wrong question waypoint in section 2
            section_1 = sections[0]
            new_question = section_1['questions'][2]
            choices = new_question.get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                           new_question.ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_1['section_id'],
                                                  new_question.ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (4, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            questions = []
            for s in sections:
                questions += s['questions']

            question_id_strs = [q._my_map['itemId'] for q in questions]
            first_waypoint_id = ''
            second_waypoint_id = ''
            third_waypoint_id = ''

            for index, question_id_str in enumerate(question_id_strs):
                if index == 0:
                    self.assertEqual(str(self._items['target'][index].ident),
                                     question_id_str)
                elif index == 1 or index == 3 or index == 6:
                    self.assertTrue(any(str(t.ident) == question_id_str
                                        for t in self._items['waypoint1']))
                    if index == 1:
                        first_waypoint_id = self._extract_item_id(question_id_str)
                    elif index == 3:
                        second_waypoint_id = self._extract_item_id(question_id_str)
                    else:
                        third_waypoint_id = self._extract_item_id(question_id_str)
                elif index == 2:
                    self.assertEqual(str(self._items['target'][index - 1].ident),
                                     question_id_str)
                else:
                    self.assertEqual(str(self._items['target'][index - 2].ident),
                                     question_id_str)
            if (third_waypoint_id == second_waypoint_id or
                    third_waypoint_id == first_waypoint_id or
                    first_waypoint_id == second_waypoint_id):
                number_identical_waypoints += 1
                break

            # now delete / finish the taken
            self._assessment_bank.delete_assessment_taken(taken.ident)
        # should be different within the same section, if you get another one wrong
        self.assertTrue(number_identical_waypoints > 0)

    def test_will_repeat_waypoint_items_if_configured_to_allow_it(self):
        self.num_parts(0)
        taken = self.create_taken(number_waypoints=1)
        for i in range(0, 10):
            if i > 0:
                taken = self.create_taken_only()
            self.num_parts(2, sequestered=False)
            self.num_parts(6, sequestered=True)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 2)))
            section_2 = sections[1]
            choices = section_2['questions'][0].get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           section_2['questions'][0].ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  section_2['questions'][0].ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            # now let's get another question wrong
            new_question = section_2['questions'][1]
            choices = new_question.get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           new_question.ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  new_question.ident,
                                                  form)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 4)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            questions = []
            for s in sections:
                questions += s['questions']

            question_id_strs = [q._my_map['itemId'] for q in questions]

            for index, question_id_str in enumerate(question_id_strs):
                if index < 3:
                    self.assertEqual(str(self._items['target'][index].ident),
                                     question_id_str)
                elif index == 3 or index == 5:
                    self.assertTrue(str(self._items['waypoint1'][0].ident) == question_id_str)
                elif index == 4:
                    self.assertEqual(str(self._items['target'][index - 1].ident),
                                     question_id_str)
                else:
                    self.assertEqual(str(self._items['target'][index - 2].ident),
                                     question_id_str)

            # now delete / finish the taken
            self._assessment_bank.delete_assessment_taken(taken.ident)

    def test_bottom_level_waypoints_generate_new_ones_of_same_lo_when_incorrect(self):
        self.num_parts(0)
        taken = self.create_taken(number_waypoints=1)
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))

        self.num_parts(2, sequestered=False)
        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        # now let's get the new question wrong
        section_2 = sections[1]
        new_question = section_2['questions'][1]
        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 4)))

        # this should be a bottom-level waypoint with no confused_los
        # for its wrong answer. Getting it wrong should generate
        # another question with the same confused LO
        section_2 = sections[1]
        new_question = section_2['questions'][2]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint2']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A2%40MIT']
        )

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '1.1.1', '2']
        )

        choices = new_question.get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       new_question.ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              new_question.ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 5)))

        section_2 = sections[1]
        new_question = section_2['questions'][3]
        self.assertTrue(any(str(t.ident) == new_question._my_map['itemId']
                            for t in self._items['waypoint2']))
        self.assertEqual(
            new_question.object_map['learningObjectiveIds'],
            ['foo%3A2%40MIT']
        )

        questions = []
        for s in sections:
            questions += s['questions']

        # let's check the displayLabels
        question_names = [q.display_name.text for q in questions]
        self.assertEqual(
            question_names,
            ['1', '2', '1', '1.1', '1.1.1', '1.1.2', '2']
        )

    def test_waypoint_items_do_not_repeat_across_sections(self):
        self.num_parts(0)
        number_identical_waypoints = 0
        taken = self.create_taken(number_waypoints=2)
        for i in range(0, 15):
            if i > 0:
                taken = self.create_taken_only()
            self.num_parts(2, sequestered=False)
            self.num_parts(6, sequestered=True)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 2)))
            section_2 = sections[1]
            choices = section_2['questions'][1].get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           section_2['questions'][1].ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  section_2['questions'][1].ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            # now let's get another question wrong
            section_1 = sections[0]
            new_question = section_1['questions'][0]
            choices = new_question.get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                           new_question.ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_1['section_id'],
                                                  new_question.ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (3, 3)))

            self.num_parts(2, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(6, sequestered=True)

            questions = []
            for s in sections:
                questions += s['questions']

            question_id_strs = [q._my_map['itemId'] for q in questions]
            first_waypoint_id = ''
            second_waypoint_id = ''

            for index, question_id_str in enumerate(question_id_strs):
                if index == 0:
                    self.assertEqual(str(self._items['target'][index].ident),
                                     question_id_str)
                elif index == 1 or index == 5:
                    self.assertTrue(any(str(t.ident) == question_id_str
                                        for t in self._items['waypoint1']))
                    if index == 1:
                        first_waypoint_id = self._extract_item_id(question_id_str)
                    else:
                        second_waypoint_id = self._extract_item_id(question_id_str)
                else:
                    self.assertEqual(str(self._items['target'][index - 1].ident),
                                     question_id_str)

            if first_waypoint_id == second_waypoint_id:
                number_identical_waypoints += 1
                break

            # now delete / finish the taken
            self._assessment_bank.delete_assessment_taken(taken.ident)
        # should not get any duplicates across sections
        self.assertFalse(number_identical_waypoints > 0)

    def test_target_items_do_not_repeat_across_assessments(self):
        self.num_parts(0)
        number_identical_waypoints = 0
        taken = self.create_taken(number_waypoints=2)
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_2 = sections[1]
        choices = section_2['questions'][1].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                       section_2['questions'][1].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_2['section_id'],
                                              section_2['questions'][1].ident,
                                              form)
        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (2, 3)))
        inserted_waypoint_id = sections[1]['questions'][2]._my_map['itemId']

        original_waypoints = self._items['waypoint1']

        taken2 = self.create_taken(number_waypoints=2, create_waypoints=False)

        self.num_parts(4, sequestered=False)
        self.num_parts(12, sequestered=True)

        for i in range(0, 15):
            if i > 0:
                taken = self.create_taken_only()
            else:
                taken = taken2
            self.num_parts(4, sequestered=False)
            self.num_parts(12, sequestered=True)
            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 2)))
            section_2 = sections[1]
            choices = section_2['questions'][1].get_choices()
            wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
            form = self._assessment_bank.get_response_form(section_2['section_id'],
                                                           section_2['questions'][1].ident)
            form.add_choice_id(wrong_answer['id'])
            self._assessment_bank.submit_response(section_2['section_id'],
                                                  section_2['questions'][1].ident,
                                                  form)

            sections = self.get_questions_for_taken(taken.ident)
            self.validate_number_sections_and_questions(sections, (2, (2, 3)))

            self.num_parts(4, sequestered=False)
            # magic parts are not saved to disk ...
            self.num_parts(12, sequestered=True)

            questions = []
            for s in sections:
                questions += s['questions']

            question_id_strs = [q._my_map['itemId'] for q in questions]
            new_inserted_waypoint_id = ''

            for index, question_id_str in enumerate(question_id_strs):
                if index == 4:
                    self.assertTrue(any(str(t.ident) == question_id_str
                                        for t in original_waypoints))
                    new_inserted_waypoint_id = self._extract_item_id(question_id_str)
                else:
                    self.assertEqual(str(self._items['target'][index].ident),
                                     question_id_str)

            if inserted_waypoint_id == new_inserted_waypoint_id:
                number_identical_waypoints += 1
                break

            # now delete / finish the taken
            self._assessment_bank.delete_assessment_taken(taken.ident)
        # should not get any duplicates across assessments
        self.assertFalse(number_identical_waypoints > 0)


class MultiLanguageBaseTestCase(DLKitTestCase):
    def _english(self):
        return DisplayText(display_text_map={
            'text': self._english_text,
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

    def _hindi(self):
        return DisplayText(display_text_map={
            'text': self._hindi_text,
            'languageTypeId': '639-2%3AHIN%40ISO',
            'scriptTypeId': '15924%3ADEVA%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

    def _telugu(self):
        return DisplayText({
            'text': self._telugu_text,
            'languageTypeId': '639-2%3ATEL%40ISO',
            'scriptTypeId': '15924%3ATELU%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

    @staticmethod
    def _str_txt(display_text):
        return {
            'text': display_text.text,
            'languageTypeId': str(display_text.language_type),
            'scriptTypeId': str(display_text.script_type),
            'formatTypeId': str(display_text.format_type)
        }

    def get_bank_with_proxy_set_to_locale(self, locale_code):
        # expects eng, hin, tel as code
        locale = InitializableLocale(language_type_identifier=locale_code)

        condition = PROXY_SESSION.get_proxy_condition()
        condition.set_http_request(self.instructor_req)
        condition.set_locale(locale)
        proxy = PROXY_SESSION.get_proxy(condition)
        am = RUNTIME.get_service_manager('ASSESSMENT',
                                         proxy=proxy)
        return am.get_bank(self._bank.ident)

    def setUp(self):
        super(MultiLanguageBaseTestCase, self).setUp()
        self._bank = self._get_test_bank()
        self._english_text = 'english'
        self._hindi_text = 'हिंदी'
        self._telugu_text = 'తెలుగు'

    def tearDown(self):
        super(MultiLanguageBaseTestCase, self).tearDown()


class MultiLanguageItemTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageItemTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageItemTests, self).tearDown()

    def test_can_set_multiple_display_texts(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._hindi())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])
        self.assertEqual(
            item.description.text,
            ''
        )
        self.assertEqual(
            item.display_name.text,
            self._english_text
        )

    def test_can_set_multiple_descriptions(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._hindi())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])
        self.assertEqual(
            item.display_name.text,
            ''
        )
        self.assertEqual(
            item.description.text,
            self._english_text
        )

    def test_can_clear_display_names(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._hindi())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])

        form = self._bank.get_item_form_for_update(item.ident)
        form.clear_display_names()
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            0
        )
        self.assertEqual(
            item.description.text,
            ''
        )
        self.assertEqual(
            item.display_name.text,
            ''
        )

    def test_can_clear_descriptions(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._hindi())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])

        form = self._bank.get_item_form_for_update(item.ident)
        form.clear_descriptions()
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            0
        )

        self.assertEqual(
            item.display_name.text,
            ''
        )
        self.assertEqual(
            item.description.text,
            ''
        )

    def test_can_remove_a_display_name(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._hindi())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])

        form = self._bank.get_item_form_for_update(item.ident)
        form.remove_display_name_by_language(self._english().language_type)
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])

        self.assertEqual(
            item.description.text,
            ''
        )
        self.assertEqual(
            item.display_name.text,
            self._hindi_text
        )

    def test_can_remove_a_description(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._hindi())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])

        form = self._bank.get_item_form_for_update(item.ident)
        form.remove_description_by_language(self._english().language_type)
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])

        self.assertEqual(
            item.display_name.text,
            ''
        )
        self.assertEqual(
            item.description.text,
            self._hindi_text
        )

    def test_can_replace_a_display_name(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._hindi())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])

        form = self._bank.get_item_form_for_update(item.ident)
        new_display_name = {
            'text': self._telugu().text,
            'languageTypeId': str(self._english().language_type),
            'formatTypeId': str(self._english().format_type),
            'scriptTypeId': str(self._english().script_type)
        }
        form.edit_display_name(DisplayText(display_text_map=new_display_name))
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['displayNames']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['displayNames'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['displayNames'])
        self.assertNotIn(self._str_txt(self._english()), item._my_map['displayNames'])

        self.assertEqual(
            item.description.text,
            ''
        )
        self.assertEqual(
            item.display_name.text,
            self._telugu_text
        )

    def test_can_replace_a_description(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._hindi())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])

        form = self._bank.get_item_form_for_update(item.ident)
        new_description = {
            'text': self._telugu().text,
            'languageTypeId': str(self._english().language_type),
            'formatTypeId': str(self._english().format_type),
            'scriptTypeId': str(self._english().script_type)
        }
        form.edit_description(DisplayText(display_text_map=new_description))
        item = self._bank.update_item(form)
        self.assertEqual(
            len(item._my_map['descriptions']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['descriptions'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['descriptions'])
        self.assertNotIn(self._str_txt(self._english()), item._my_map['descriptions'])

        self.assertEqual(
            item.display_name.text,
            ''
        )
        self.assertEqual(
            item.description.text,
            self._telugu_text
        )

    def test_setting_proxy_locale_gets_item_display_name_in_specified_language(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._hindi())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.display_name.text,
            self._hindi_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.display_name.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.display_name.text,
            self._telugu_text
        )

    def test_english_default_display_name_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._english())
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.display_name.text,
            self._english_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.display_name.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.display_name.text,
            self._telugu_text
        )

    def test_first_available_display_name_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_display_name(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.display_name.text,
            self._telugu_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.display_name.text,
            self._telugu_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.display_name.text,
            self._telugu_text
        )

    def test_setting_proxy_locale_gets_item_description_in_specified_language(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._hindi())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.description.text,
            self._hindi_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.description.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.description.text,
            self._telugu_text
        )

    def test_english_default_description_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._english())
        form.add_description(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.description.text,
            self._english_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.description.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.description.text,
            self._telugu_text
        )

    def test_first_available_description_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([MULTI_LANGUAGE_OBJECT_RECORD])
        form.add_description(self._telugu())
        item = self._bank.create_item(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.description.text,
            self._telugu_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.description.text,
            self._telugu_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.description.text,
            self._telugu_text
        )


class MultiLanguageQuestionTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageQuestionTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageQuestionTests, self).tearDown()

    def test_can_set_multiple_question_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._english_text
        )

    def test_can_clear_question_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._english_text
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_texts()
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            0
        )
        self.assertEqual(
            item.get_question().get_text().text,
            ''
        )

    def test_can_remove_a_question_text_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )

        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        form = self._bank.get_question_form_for_update(question.ident)
        form.remove_text_language(self._english().language_type)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['question']['texts']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._hindi_text
        )

    def test_can_replace_a_question_text(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )

        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_question_form_for_update(question.ident)
        form.edit_text(new_english_feedback)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            'foo'
        )

    def test_setting_proxy_locale_gets_question_text_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._hindi_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )

    def test_english_default_question_text_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._english_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )

    def test_first_available_question_text_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._telugu_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._telugu_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )


class MultiLanguageMultipleChoiceQuestionTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageMultipleChoiceQuestionTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageMultipleChoiceQuestionTests, self).tearDown()

    def test_can_set_multiple_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

    def test_can_clear_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_choice_texts(choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': '',
                'name': ''
            }]
        )

    def test_can_clear_choices(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_choices()
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            0
        )
        self.assertEqual(
            item.get_question().get_choices(),
            []
        )

    def test_can_remove_a_choice_text_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.remove_choice_language(self._english().language_type, choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._hindi_text,
                'name': ''
            }]
        )

    def test_can_replace_a_choice_text(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_question_form_for_update(question.ident)
        form.edit_choice(new_english_feedback, choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': 'foo',
                'name': ''
            }]
        )

    def test_setting_proxy_locale_gets_choice_text_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._hindi_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_english_default_choice_text_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_first_available_choice_text_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_multi_language_plays_well_with_randomized_order(self):
        form = self._bank.get_item_form_for_create([MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MC_RANDOMIZED_RECORD,
                                                                    MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD])
        form.add_choice(self._english(), identifier='1')
        form.add_choice(self._hindi(), identifier='1')
        form.add_choice(self._telugu(), identifier='1')

        form.add_choice(self._english(), identifier='2')
        form.add_choice(self._hindi(), identifier='2')
        form.add_choice(self._telugu(), identifier='2')

        form.add_choice(self._english(), identifier='3')
        form.add_choice(self._hindi(), identifier='3')
        form.add_choice(self._telugu(), identifier='3')

        self._bank.create_question(form)

        different_hindi_order = 0
        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = hi_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_hindi_order += 1
            self.assertEqual(
                choice_texts,
                [self._hindi_text, self._hindi_text, self._hindi_text]
            )
        self.assertTrue(different_hindi_order > 0)

        different_english_order = 0
        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = en_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_english_order += 1
            self.assertEqual(
                choice_texts,
                [self._english_text, self._english_text, self._english_text]
            )
        self.assertTrue(different_english_order > 0)

        different_telugu_order = 0
        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = te_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_telugu_order += 1
            self.assertEqual(
                choice_texts,
                [self._telugu_text, self._telugu_text, self._telugu_text]
            )
        self.assertTrue(different_telugu_order > 0)


class MultiLanguageOrderedChoiceQuestionTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageOrderedChoiceQuestionTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageOrderedChoiceQuestionTests, self).tearDown()

    def test_can_set_multiple_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

    def test_can_clear_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_choice_texts(choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': '',
                'name': ''
            }]
        )

    def test_can_clear_choices(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_choices()
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            0
        )
        self.assertEqual(
            item.get_question().get_choices(),
            []
        )

    def test_can_remove_a_choice_text_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.remove_choice_language(self._english().language_type, choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._hindi_text,
                'name': ''
            }]
        )

    def test_can_replace_a_choice_text(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices']),
            1
        )
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_question_form_for_update(question.ident)
        form.edit_choice(new_english_feedback, choice_identifier)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices'][0]['texts']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][0]['texts'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['question']['choices'][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': 'foo',
                'name': ''
            }]
        )

    def test_setting_proxy_locale_gets_choice_text_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._hindi(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._hindi_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_english_default_choice_text_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._english(), identifier=choice_identifier)
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._english_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_first_available_choice_text_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        choice_identifier = 'foobar'
        form.add_choice(self._telugu(), identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            [{
                'id': choice_identifier,
                'text': self._telugu_text,
                'name': ''
            }]
        )

    def test_multi_language_plays_well_with_randomized_order(self):
        form = self._bank.get_item_form_for_create([MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MC_RANDOMIZED_RECORD,
                                                                    MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD])
        form.add_choice(self._english(), identifier='1')
        form.add_choice(self._hindi(), identifier='1')
        form.add_choice(self._telugu(), identifier='1')

        form.add_choice(self._english(), identifier='2')
        form.add_choice(self._hindi(), identifier='2')
        form.add_choice(self._telugu(), identifier='2')

        form.add_choice(self._english(), identifier='3')
        form.add_choice(self._hindi(), identifier='3')
        form.add_choice(self._telugu(), identifier='3')

        self._bank.create_question(form)

        different_hindi_order = 0
        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = hi_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_hindi_order += 1
            self.assertEqual(
                choice_texts,
                [self._hindi_text, self._hindi_text, self._hindi_text]
            )
        self.assertTrue(different_hindi_order > 0)

        different_english_order = 0
        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = en_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_english_order += 1
            self.assertEqual(
                choice_texts,
                [self._english_text, self._english_text, self._english_text]
            )
        self.assertTrue(different_english_order > 0)

        different_telugu_order = 0
        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = te_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices]
            choice_texts = [c['text'] for c in choices]
            if choice_order != ['1', '2', '3']:
                different_telugu_order += 1
            self.assertEqual(
                choice_texts,
                [self._telugu_text, self._telugu_text, self._telugu_text]
            )
        self.assertTrue(different_telugu_order > 0)


class MultiLanguageInlineChoiceQuestionTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageInlineChoiceQuestionTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageInlineChoiceQuestionTests, self).tearDown()

    def test_can_set_multiple_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 3 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][region_name][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

    def test_can_clear_choice_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 3 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][region_name][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        form = self._bank.get_question_form_for_update(item.ident)
        form.clear_choice_texts(choice_identifier, region_name)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 0 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            0
        )
        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': '',
                    'name': ''
                }]
            }
        )

    def test_can_clear_choices(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 3 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][region_name][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        form = self._bank.get_question_form_for_update(item.ident)
        form.clear_choices(region_name)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            0
        )
        self.assertEqual(
            item.get_question().get_choices(),
            {region_name: []}
        )

    def test_can_remove_a_choice_text_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 3 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][region_name][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        form = self._bank.get_question_form_for_update(item.ident)
        form.remove_choice_language(self._english().language_type, choice_identifier, region_name)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._hindi_text,
                    'name': ''
                }]
            }
        )

    def test_can_replace_a_choice_text(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        # 1 region
        self.assertEqual(
            len(list(item._my_map['question']['choices'].keys())),
            1
        )
        # 1 choice in this region
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name]),
            1
        )
        # 3 texts for the choice
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertEqual(
            item._my_map['question']['choices'][region_name][0]['id'],
            choice_identifier
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_question_form_for_update(item.ident)
        form.edit_choice(new_english_feedback, choice_identifier, region_name)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['choices'][region_name][0]['texts']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['choices'][region_name][0]['texts'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['question']['choices'][region_name][0]['texts'])

        self.assertEqual(
            item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': 'foo',
                    'name': ''
                }]
            }
        )

    def test_setting_proxy_locale_gets_choice_text_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._hindi(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._hindi_text,
                    'name': ''
                }]
            }
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._telugu_text,
                    'name': ''
                }]
            }
        )

    def test_english_default_choice_text_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._english(), region_name, identifier=choice_identifier)
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._english_text,
                    'name': ''
                }]
            }
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._telugu_text,
                    'name': ''
                }]
            }
        )

    def test_first_available_choice_text_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        choice_identifier = 'foobar'
        form.add_choice(self._telugu(), region_name, identifier=choice_identifier)
        self._bank.create_question(form)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._telugu_text,
                    'name': ''
                }]
            }
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._telugu_text,
                    'name': ''
                }]
            }
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_choices(),
            {
                region_name: [{
                    'id': choice_identifier,
                    'text': self._telugu_text,
                    'name': ''
                }]
            }
        )

    def test_multi_language_plays_well_with_randomized_order(self):
        form = self._bank.get_item_form_for_create([RANDOMIZED_INLINE_CHOICE_ITEM_RECORD])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [QTI_QUESTION_RECORD,
                                                                    MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD])
        region_name = 'REGION_1'

        form.add_inline_region(region_name)
        form.add_choice(self._english(), region_name, identifier='1')
        form.add_choice(self._hindi(), region_name, identifier='1')
        form.add_choice(self._telugu(), region_name, identifier='1')

        form.add_choice(self._english(), region_name, identifier='2')
        form.add_choice(self._hindi(), region_name, identifier='2')
        form.add_choice(self._telugu(), region_name, identifier='2')

        form.add_choice(self._english(), region_name, identifier='3')
        form.add_choice(self._hindi(), region_name, identifier='3')
        form.add_choice(self._telugu(), region_name, identifier='3')

        self._bank.create_question(form)

        different_hindi_order = 0
        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = hi_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices[region_name]]
            choice_texts = [c['text'] for c in choices[region_name]]
            if choice_order != ['1', '2', '3']:
                different_hindi_order += 1
            self.assertEqual(
                choice_texts,
                [self._hindi_text, self._hindi_text, self._hindi_text]
            )
        self.assertTrue(different_hindi_order > 0)

        different_english_order = 0
        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = en_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices[region_name]]
            choice_texts = [c['text'] for c in choices[region_name]]
            if choice_order != ['1', '2', '3']:
                different_english_order += 1
            self.assertEqual(
                choice_texts,
                [self._english_text, self._english_text, self._english_text]
            )
        self.assertTrue(different_english_order > 0)

        different_telugu_order = 0
        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)

        for i in range(0, 10):
            choices = te_item.get_question().get_choices()
            choice_order = [c['id'] for c in choices[region_name]]
            choice_texts = [c['text'] for c in choices[region_name]]
            if choice_order != ['1', '2', '3']:
                different_telugu_order += 1
            self.assertEqual(
                choice_texts,
                [self._telugu_text, self._telugu_text, self._telugu_text]
            )
        self.assertTrue(different_telugu_order > 0)


class MultiLanguageAnswerFeedbackTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageAnswerFeedbackTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageAnswerFeedbackTests, self).tearDown()

    def test_can_set_multiple_answer_feedbacks(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._hindi())
        form.add_feedback(self._telugu())
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            self._english_text
        )

    def test_can_clear_answer_feedbacks(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._hindi())
        form.add_feedback(self._telugu())
        answer = self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            self._english_text
        )

        form = self._bank.get_answer_form_for_update(answer.ident)
        form.clear_feedbacks()
        self._bank.update_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            0
        )
        self.assertEqual(
            item.get_answers().next().feedback.text,
            ''
        )

    def test_can_remove_an_answer_feedback_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._hindi())
        form.add_feedback(self._telugu())
        answer = self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            self._english_text
        )

        form = self._bank.get_answer_form_for_update(answer.ident)
        form.remove_feedback_language(self._english().language_type)
        self._bank.update_answer(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            self._hindi_text
        )

    def test_can_replace_an_answer_feedback(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._hindi())
        form.add_feedback(self._telugu())
        answer = self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            self._english_text
        )
        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_answer_form_for_update(answer.ident)
        form.edit_feedback(new_english_feedback)
        self._bank.update_answer(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['answers'][0]['feedbacks']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['answers'][0]['feedbacks'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['answers'][0]['feedbacks'])

        self.assertEqual(
            item.get_answers().next().feedback.text,
            'foo'
        )

    def test_setting_proxy_locale_gets_answer_feedback_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._hindi())
        form.add_feedback(self._telugu())
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_answers().next().feedback.text,
            self._hindi_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_answers().next().feedback.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_answers().next().feedback.text,
            self._telugu_text
        )

    def test_english_default_answer_feedback_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._english())
        form.add_feedback(self._telugu())
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_answers().next().feedback.text,
            self._english_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_answers().next().feedback.text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_answers().next().feedback.text,
            self._telugu_text
        )

    def test_first_available_answer_feedback_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_answer_form_for_create(item.ident, [MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD])
        form.add_feedback(self._telugu())
        self._bank.create_answer(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_answers().next().feedback.text,
            self._telugu_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_answers().next().feedback.text,
            self._telugu_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_answers().next().feedback.text,
            self._telugu_text
        )


class MultiLanguageTextInteractionTests(MultiLanguageBaseTestCase):
    def setUp(self):
        super(MultiLanguageTextInteractionTests, self).setUp()

    def tearDown(self):
        super(MultiLanguageTextInteractionTests, self).tearDown()

    def test_can_set_multiple_question_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_TEXT_INTERACTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._english_text
        )

    def test_can_clear_question_texts(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._english_text
        )

        form = self._bank.get_question_form_for_update(question.ident)
        form.clear_texts()
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            0
        )
        self.assertEqual(
            item.get_question().get_text().text,
            ''
        )

    def test_can_remove_a_question_text_by_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )

        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        form = self._bank.get_question_form_for_update(question.ident)
        form.remove_text_language(self._english().language_type)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)

        self.assertEqual(
            len(item._my_map['question']['texts']),
            2
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            self._hindi_text
        )

    def test_can_replace_a_question_text(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        question = self._bank.create_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )

        self.assertIn(self._str_txt(self._english()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])

        new_english_feedback = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AENG%40ISO',
            'scriptTypeId': '15924%3ALATN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net'
        })

        form = self._bank.get_question_form_for_update(question.ident)
        form.edit_text(new_english_feedback)
        self._bank.update_question(form)

        item = self._bank.get_item(item.ident)
        self.assertEqual(
            len(item._my_map['question']['texts']),
            3
        )
        self.assertIn(self._str_txt(self._hindi()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(self._telugu()), item._my_map['question']['texts'])
        self.assertIn(self._str_txt(new_english_feedback), item._my_map['question']['texts'])

        self.assertEqual(
            item.get_question().get_text().text,
            'foo'
        )

    def test_setting_proxy_locale_gets_question_text_in_specified_language(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._hindi())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._hindi_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )

    def test_english_default_question_text_if_locale_code_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._english())
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._english_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._english_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )

    def test_first_available_question_text_if_locale_code_and_english_not_available(self):
        form = self._bank.get_item_form_for_create([])
        form.display_name = 'testing for question text'
        item = self._bank.create_item(form)

        form = self._bank.get_question_form_for_create(item.ident, [MULTI_LANGUAGE_QUESTION_RECORD])
        form.add_text(self._telugu())
        self._bank.create_question(form)

        item = self._bank.get_item(item.ident)

        hi_bank = self.get_bank_with_proxy_set_to_locale('HIN')
        hi_item = hi_bank.get_item(item.ident)
        self.assertEqual(
            hi_item.get_question().get_text().text,
            self._telugu_text
        )

        en_bank = self.get_bank_with_proxy_set_to_locale('ENG')
        en_item = en_bank.get_item(item.ident)
        self.assertEqual(
            en_item.get_question().get_text().text,
            self._telugu_text
        )

        te_bank = self.get_bank_with_proxy_set_to_locale('TEL')
        te_item = te_bank.get_item(item.ident)
        self.assertEqual(
            te_item.get_question().get_text().text,
            self._telugu_text
        )


class LOScaffoldDownTests(DLKitTestCase):
    """Specify only the LO, but scaffold down
    """
    @staticmethod
    def _extract_item_id(id_str):
        # return unquote(Id(id_str).identifier).split('?')[0]
        # since using ._my_map['itemId'], just return it
        return id_str

    def create_mc_item(self, level=None):
        form = self._item_bank.get_item_form_for_create([MC_ITEM_RECORD,  # Take out WRONG_ANSWER_ITEM_RECORD and replace
                                                         SOURCEABLE_RECORD,
                                                         PROVENANCE_ITEM_RECORD,
                                                         MC_RANDOMIZED_ITEM_RECORD])
        form.display_name = 'FbW MC item'
        if level is not None:
            form.set_learning_objectives([Id('foo%3A{0}%40MIT'.format(level))])
        else:
            form.set_learning_objectives([Id('foo%3A{0}%40MIT'.format('0'))])
        item = self._item_bank.create_item(form)

        form = self._item_bank.get_question_form_for_create(item.ident,
                                                            [MC_RANDOMIZED_RECORD])

        form.display_name = "my question"
        form.set_text('what is life about? {0}'.format(str(randint(0, 10))))
        for index, choice in enumerate(['1', '42', '81']):
            form.add_choice(choice, 'Choice {0}'.format(str(index)))
        question = self._item_bank.create_question(form)

        choices = question.get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]

        form = self._item_bank.get_answer_form_for_create(item.ident,
                                                          [MC_ANSWER_RECORD])
        form.add_choice_id(right_answer['id'])
        form.set_genus_type(RIGHT_ANSWER_GENUS)
        form.set_feedback('right!')
        self._item_bank.create_answer(form)

        form = self._item_bank.get_answer_form_for_create(item.ident,
                                                          [MC_ANSWER_RECORD])
        form.add_choice_id(wrong_answer['id'])
        if level is not None:
            lo_identifier = level + 1
        else:
            lo_identifier = 1
        self._confused_lo_id = 'foo%3A{0}%40MIT'.format(str(lo_identifier))  # use this as a proxy for level down
        if level != 2:
            form.set_confused_learning_objective_ids([self._confused_lo_id])
        form.set_genus_type(WRONG_ANSWER_GENUS)
        form.set_feedback('wrong ...')
        self._item_bank.create_answer(form)

        item = self._item_bank.get_item(item.ident)
        return item

    def create_scaffolded_assessment(self, number_waypoints):
        item1 = self.create_mc_item()
        item2 = self.create_mc_item()
        item3 = self.create_mc_item()

        scaffold_items1 = []
        scaffold_items2 = []
        for i in range(0, number_waypoints):
            scaffold_items1.append(self.create_mc_item(level=1))
            scaffold_items2.append(self.create_mc_item(level=2))

        # let's make two parts, each with two items (so really two magic parts, for a total of 4 magic parts)
        form = self._assessment_bank.get_assessment_form_for_create([SIMPLE_SEQUENCE_ASSESSMENT_RECORD])
        form.display_name = "for testing"
        assessment = self._assessment_bank.create_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 1'
        form.set_minimum_proficiency(Id('foo%3A1%40MIT'))
        form.set_learning_objective_id('foo%3A1%40MIT')
        parent_part_1 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 1'
        form.set_learning_objective_ids([Id('foo%3A0%40MIT')])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_1 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_1.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 2'
        form.set_learning_objective_ids([Id('foo%3A0%40MIT')])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_2 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        # second "parent" part
        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment(assessment.ident,
                                                                                        [ASSESSMENT_SECTION_WITH_OBJECTIVE,
                                                                                         SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'parent part 2'
        form.set_minimum_proficiency(Id('foo%3A2%40MIT'))
        form.set_learning_objective_id('foo%3A42%40MIT')

        parent_part_2 = self._assessment_bank.create_assessment_part_for_assessment(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 3'
        form.set_learning_objective_ids([Id('foo%3A0%40MIT')])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_3 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        form = self._assessment_bank.get_assessment_part_form_for_create_for_assessment_part(parent_part_2.ident,
                                                                                             [MAGIC_ASSESSMENT_PART_FOR_SCAFFOLDING,
                                                                                              SIMPLE_SEQUENCE_PART_RECORD_TYPE])
        form.display_name = 'magic part 4'
        form.set_learning_objective_ids([Id('foo%3A0%40MIT')])
        form.set_item_bank_id(self._item_bank.ident)
        form.set_waypoint_quota(1)
        magic_part_4 = self._assessment_bank.create_assessment_part_for_assessment_part(form)

        self._items = {
            'target': [item1, item2, item3],
            'waypoint1': scaffold_items1,
            'waypoint2': scaffold_items2
        }
        self.target_item_ids = [str(t.ident) for t in self._items['target']]

        return self._assessment_bank.get_assessment(assessment.ident)

    def create_taken(self, number_waypoints=4):
        # make sure this data still shows up when taking the assessment
        assessment = self.create_scaffolded_assessment(number_waypoints)
        offered_form = self._assessment_bank.get_assessment_offered_form_for_create(assessment.ident,
                                                                                    [REVIEWABLE_OFFERED])
        self._offered = self._assessment_bank.create_assessment_offered(offered_form)

        taken_form = self._assessment_bank.get_assessment_taken_form_for_create(self._offered.ident,
                                                                                [REVIEWABLE_TAKEN,
                                                                                 ADVANCED_QUERY_TAKEN])
        return self._assessment_bank.create_assessment_taken(taken_form)

    def create_taken_only(self):
        taken_form = self._assessment_bank.get_assessment_taken_form_for_create(self._offered.ident,
                                                                                [REVIEWABLE_TAKEN,
                                                                                 ADVANCED_QUERY_TAKEN])
        return self._assessment_bank.create_assessment_taken(taken_form)

    def get_questions_for_taken(self, taken_id):
        """gets all questions across all sections"""
        sections = []
        first_section = self._assessment_bank.get_first_assessment_section(taken_id)
        sections.append(first_section)
        try:
            previous_section_id = first_section.ident
            while True:
                next_section = self._assessment_bank.get_next_assessment_section(previous_section_id)
                previous_section_id = next_section.ident
                sections.append(next_section)
        except (StopIteration, errors.IllegalState):
            final_sections = []
            for section in sections:
                new_questions = list(self._assessment_bank.get_questions(section.ident))
                section_map = {
                    'questions': new_questions,
                    'section_id': section.ident
                }

                final_sections.append(section_map)

            return final_sections

    def num_parts(self, val, sequestered=False):
        if sequestered:
            self._assessment_bank.use_unsequestered_assessment_part_view()
        else:
            self._assessment_bank.use_sequestered_assessment_part_view()
        self.assertEqual(
            self._assessment_bank.get_assessment_parts().available(),
            int(val)
        )

    def setUp(self):
        super(LOScaffoldDownTests, self).setUp()
        self._item_bank = self._get_test_bank()
        self._assessment_bank = self.create_new_bank(name="bank for assessments")

    def tearDown(self):
        super(LOScaffoldDownTests, self).tearDown()

    def validate_number_sections_and_questions(self, sections, expected_tuple):
        expected_num_sections = expected_tuple[0]
        expected_num_q_per_section = expected_tuple[1]
        self.assertEqual(
            len(sections),
            expected_num_sections
        )
        for index, section in enumerate(sections):
            self.assertEqual(
                len(section['questions']),
                expected_num_q_per_section[index]
            )

    def test_initial_magic_part_will_pick_from_right_items_when_only_lo_specified(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)

        self.validate_number_sections_and_questions(sections, (2, (2, 2)))

        questions = []
        for s in sections:
            questions += s['questions']
        for question in questions:
            self.assertTrue(question._my_map['itemId'] in self.target_item_ids)
        # also, the first three should be unique, and the last one should
        # be a duplicate of one of the first three
        self.assertNotEqual(questions[0]._my_map['itemId'], questions[1]._my_map['itemId'])
        self.assertNotEqual(questions[1]._my_map['itemId'], questions[2]._my_map['itemId'])

        question_ids = [q._my_map['itemId'] for q in questions[0:3]]
        self.assertIn(questions[3]._my_map['itemId'], question_ids)

    def test_getting_first_level_magic_part_wrong_still_scaffolds_correctly(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)

        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_1 = sections[0]

        choices = section_1['questions'][0].get_choices()
        wrong_answer = [c for c in choices if c['name'] == 'Choice 1'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       section_1['questions'][0].ident)
        form.add_choice_id(wrong_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              section_1['questions'][0].ident,
                                              form)

        sections = self.get_questions_for_taken(taken.ident)
        self.validate_number_sections_and_questions(sections, (2, (3, 2)))

        self.num_parts(2, sequestered=False)

        # magic parts are not saved to disk ...
        self.num_parts(6, sequestered=True)

        questions = []
        for s in sections:
            questions += s['questions']

        question_id_strs = [q._my_map['itemId'] for q in questions]

        for index, question_id_str in enumerate(question_id_strs):
            if index == 0:
                self.assertIn(question_id_str, self.target_item_ids)
            elif index == 1:
                self.assertTrue(any(str(t.ident) == question_id_str
                                    for t in self._items['waypoint1']))
            else:
                self.assertIn(question_id_str, self.target_item_ids)

        response = self._assessment_bank.get_response(section_1['section_id'],
                                                      section_1['questions'][0].ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            wrong_answer['id']
        )

    def test_getting_first_level_magic_part_right_does_not_scaffold(self):
        self.num_parts(0)
        taken = self.create_taken()
        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)
        sections = self.get_questions_for_taken(taken.ident)

        self.validate_number_sections_and_questions(sections, (2, (2, 2)))
        section_1 = sections[0]
        choices = section_1['questions'][0].get_choices()
        right_answer = [c for c in choices if c['name'] == 'Choice 0'][0]
        form = self._assessment_bank.get_response_form(section_1['section_id'],
                                                       section_1['questions'][0].ident)
        form.add_choice_id(right_answer['id'])
        self._assessment_bank.submit_response(section_1['section_id'],
                                              section_1['questions'][0].ident,
                                              form)

        self.num_parts(2, sequestered=False)
        self.num_parts(6, sequestered=True)

        response = self._assessment_bank.get_response(section_1['section_id'],
                                                      section_1['questions'][0].ident)
        self.assertEqual(
            response.get_choice_ids().available(),
            1
        )
        self.assertEqual(
            str(next(response.get_choice_ids())),
            right_answer['id']
        )


class FbWSpawnableAssessmentTests(DLKitTestCase):
    def setUp(self):
        super(FbWSpawnableAssessmentTests, self).setUp()
        self._bank = self._get_test_bank()

    def tearDown(self):
        super(FbWSpawnableAssessmentTests, self).tearDown()

    def test_can_set_spawned_flag_to_true(self):
        form = self._bank.get_assessment_form_for_create([FBW_PHASE_I_ASSESSMENT_RECORD])
        assessment = self._bank.create_assessment(form)
        self.assertFalse(assessment.spawned)
        self.assertFalse(assessment.object_map['hasSpawnedFollowOnPhase'])

        form = self._bank.get_assessment_form_for_update(assessment.ident)
        form.set_follow_on_phase_state(True)
        assessment = self._bank.update_assessment(form)
        self.assertTrue(assessment.spawned)
        self.assertTrue(assessment.object_map['hasSpawnedFollowOnPhase'])

    def test_can_set_source_taken_id(self):
        fake_taken_id = 'assessment.AssessmentTaken%3A123%40ODL.MIT.EDU'
        form = self._bank.get_assessment_form_for_create([FBW_PHASE_II_ASSESSMENT_RECORD])
        assessment = self._bank.create_assessment(form)
        self.assertEqual(str(assessment.source_assessment_taken_id), '')
        self.assertEqual(assessment.object_map['sourceAssessmentTakenId'], '')

        form = self._bank.get_assessment_form_for_update(assessment.ident)
        form.set_source_assessment_taken_id(Id(fake_taken_id))
        assessment = self._bank.update_assessment(form)
        self.assertEqual(str(assessment.source_assessment_taken_id), fake_taken_id)
        self.assertEqual(assessment.object_map['sourceAssessmentTakenId'], fake_taken_id)

    def test_can_query_on_source_taken_id(self):
        bad_taken_id = 'foo%3A1%40ODL.MIT.EDU'
        fake_taken_id_1 = 'assessment.AssessmentTaken%3A123%40ODL.MIT.EDU'
        fake_taken_id_2 = 'assessment.AssessmentTaken%3A987%40ODL.MIT.EDU'
        form = self._bank.get_assessment_form_for_create([FBW_PHASE_II_ASSESSMENT_RECORD])
        form.set_source_assessment_taken_id(Id(fake_taken_id_1))
        assessment_1 = self._bank.create_assessment(form)

        form = self._bank.get_assessment_form_for_create([FBW_PHASE_II_ASSESSMENT_RECORD])
        form.set_source_assessment_taken_id(Id(fake_taken_id_2))
        assessment_2 = self._bank.create_assessment(form)

        querier = self._bank.get_assessment_query()
        querier.match_source_assessment_taken_id(Id(bad_taken_id), True)
        results = self._bank.get_assessments_by_query(querier)
        self.assertEqual(results.available(), 0)

        querier = self._bank.get_assessment_query()
        querier.match_source_assessment_taken_id(Id(fake_taken_id_1), True)
        results = self._bank.get_assessments_by_query(querier)
        self.assertEqual(results.available(), 1)
        self.assertEqual(str(results.next().ident), str(assessment_1.ident))

        querier = self._bank.get_assessment_query()
        querier.match_source_assessment_taken_id(Id(fake_taken_id_1), True)
        querier.match_source_assessment_taken_id(Id(fake_taken_id_2), True)
        results = self._bank.get_assessments_by_query(querier)
        self.assertEqual(results.available(), 2)
        self.assertEqual(str(results.next().ident), str(assessment_2.ident))
        self.assertEqual(str(results.next().ident), str(assessment_1.ident))
