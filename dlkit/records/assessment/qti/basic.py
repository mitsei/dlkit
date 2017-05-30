"""
records.qti.basic
"""
from __future__ import unicode_literals

import json
import os
import re

from bs4 import BeautifulSoup, Tag

from dlkit.json_ import types
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.id.objects import IdList

from dlkit.abstract_osid.osid.errors import IllegalState, OperationFailed,\
    InvalidArgument, NotFound
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.transport.objects import DataInputStream
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.locale.objects import InitializableLocale

from .ordered_choice_records import OrderedChoiceItemRecord
from .inline_choice_records import MagicRandomizedInlineChoiceItemRecord
from .numeric_response_records import CalculationInteractionItemRecord
from ..basic.multi_choice_records import MultiChoiceItemRecord
from ...osid.base_records import ObjectInitRecord
from ... import registry
from ...repository import registry as repository_registry

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))

FEEDBACK_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['answer-with-feedback'])
FILE_SUBMISSION_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['file-submission'])
FILE_SUBMISSION_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['file-submission'])
FILES_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['files'])
FILES_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['files'])
INLINE_CHOICE_ITEM_RECORD = Type(**registry.ITEM_RECORD_TYPES['qti-inline-choice'])
MULTI_CHOICE_TEXT_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-choice-text'])
MULTI_CHOICE_TEXT_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['multi-choice-with-files-and-feedback'])
RANDOMIZED_MULTI_CHOICE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-choice-randomized'])
RANDOMIZED_MULTI_CHOICE_ITEM_RECORD = Type(**registry.ITEM_RECORD_TYPES['multi-choice-randomized'])
CHOICE_INTERACTION_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-choice-interaction'])
CHOICE_INTERACTION_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-choice-interaction'])
CHOICE_INTERACTION_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-choice-interaction'])
CHOICE_INTERACTION_MULTI_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-choice-interaction-multi-select'])
CHOICE_INTERACTION_MULTI_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-choice-interaction-multi-select'])
CHOICE_INTERACTION_MULTI_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-choice-interaction-multi-select'])
CHOICE_INTERACTION_SURVEY_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-choice-interaction-survey'])
CHOICE_INTERACTION_SURVEY_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-choice-interaction-survey'])
CHOICE_INTERACTION_MULTI_SELECT_SURVEY_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-choice-interaction-multi-select-survey'])
CHOICE_INTERACTION_MULTI_SELECT_SURVEY_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-choice-interaction-multi-select-survey'])

UPLOAD_INTERACTION_AUDIO_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-upload-interaction-audio'])
UPLOAD_INTERACTION_AUDIO_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-upload-interaction-audio'])
UPLOAD_INTERACTION_AUDIO_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-upload-interaction-audio'])
UPLOAD_INTERACTION_GENERIC_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-upload-interaction-generic'])
UPLOAD_INTERACTION_GENERIC_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-upload-interaction-generic'])
UPLOAD_INTERACTION_GENERIC_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-upload-interaction-generic'])

ORDER_INTERACTION_MW_SENTENCE_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-order-interaction-mw-sentence'])
ORDER_INTERACTION_MW_SENTENCE_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-order-interaction-mw-sentence'])
ORDER_INTERACTION_MW_SENTENCE_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-order-interaction-mw-sentence'])
ORDERED_CHOICE_TEXT_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['ordered-choice-text'])
ORDERED_CHOICE_TEXT_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['ordered-choice-with-files-and-feedback'])
ORDER_INTERACTION_MW_SANDBOX_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-order-interaction-mw-sandbox'])
ORDER_INTERACTION_MW_SANDBOX_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-order-interaction-mw-sandbox'])
ORDER_INTERACTION_MW_SANDBOX_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-order-interaction-mw-sandbox'])
ORDER_INTERACTION_OBJECT_MANIPULATION_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-order-interaction-object-manipulation'])
ORDER_INTERACTION_OBJECT_MANIPULATION_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-order-interaction-object-manipulation'])
ORDER_INTERACTION_OBJECT_MANIPULATION_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-order-interaction-object-manipulation'])

EXTENDED_TEXT_INTERACTION_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-extended-text-interaction'])
EXTENDED_TEXT_INTERACTION_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['extended-text-answer'])
EXTENDED_TEXT_INTERACTION_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-extended-text-interaction'])
EXTENDED_TEXT_INTERACTION_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-extended-text-interaction'])
EXTENDED_TEXT_INTERACTION_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['qti-extended-text-interaction'])
INLINE_CHOICE_MW_FITB_INTERACTION_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-inline-choice-interaction-mw-fill-in-the-blank'])
INLINE_CHOICE_MW_FITB_INTERACTION_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['qti-inline-choice-with-files-and-feedback'])
INLINE_CHOICE_MW_FITB_INTERACTION_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-inline-choice-interaction-mw-fill-in-the-blank'])
INLINE_CHOICE_MW_FITB_INTERACTION_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-inline-choice-interaction-mw-fill-in-the-blank'])
INLINE_CHOICE_MW_FITB_INTERACTION_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['qti-inline-choice-text'])

NUMERIC_RESPONSE_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['qti-numeric-response'])
NUMERIC_RESPONSE_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['qti-numeric-response-with-files-and-feedback'])
NUMERIC_RESPONSE_GENUS = Type(**registry.ITEM_GENUS_TYPES['qti-numeric-response'])
NUMERIC_RESPONSE_RECORD = Type(**registry.ITEM_RECORD_TYPES['qti-numeric-response'])
NUMERIC_RESPONSE_QUESTION_GENUS = Type(**registry.QUESTION_GENUS_TYPES['qti-numeric-response'])
NUMERIC_RESPONSE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['qti-numeric-response'])

MULTI_LANGUAGE_QUESTION_STRING_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-question-string'])
MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-multiple-choice'])
MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-ordered-choice'])
MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-inline-choice'])
MULTI_LANGUAGE_EXTENDED_TEXT_INTERACTION_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-text-interaction'])
MULTI_LANGUAGE_FILE_UPLOAD_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-file-submission'])
MULTI_LANGUAGE_NUMERIC_RESPONSE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-numeric-response'])

MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['multi-language-answer-with-feedback'])
SIMPLE_INLINE_CHOICE_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['inline-choice-answer'])
SIMPLE_MULTIPLE_CHOICE_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['multi-choice-answer'])
MULTI_LANGUAGE_NUMERIC_RESPONSE_ANSWER_RECORD = Type(**registry.ANSWER_RECORD_TYPES['multi-language-numeric-response-with-feedback'])

MULTI_LANGUAGE_ASSET_CONTENTS = Type(**registry.ASSET_CONTENT_RECORD_TYPES['multi-language'])

RIGHT_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['right-answer'])
WRONG_ANSWER_GENUS = Type(**registry.ANSWER_GENUS_TYPES['wrong-answer'])

AUDIO_ASSET_GENUS_TYPE = Type(**repository_registry.ASSET_GENUS_TYPES['audio'])
IMAGE_ASSET_GENUS_TYPE = Type(**repository_registry.ASSET_GENUS_TYPES['image'])
JPG_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['jpg'])
GENERIC_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['generic'])
MP3_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['mp3'])
PNG_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['png'])
SVG_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['svg'])
WAV_ASSET_CONTENT_GENUS_TYPE = Type(**repository_registry.ASSET_CONTENT_GENUS_TYPES['wav'])


def _stringify(soup_tag, contents=False):
    if contents:
        result = ''
        try:
            num_contents = len(soup_tag.contents)
            for index, child in enumerate(soup_tag.contents):
                try:
                    result += '{0}'.format(child)
                except TypeError:
                    result += soup_tag.prettify()
                if (index + 1) != num_contents:
                    result += '\n'
            return result
        except AttributeError:
            # might just be a string!
            return soup_tag
    else:
        try:
            # python 2
            return unicode(soup_tag)
        except NameError:
            # python 3
            return str(soup_tag)


def create_display_text(text_string, language_code=None):
    if language_code is None:
        return DisplayText(display_text_map={
            'text': text_string,
            'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
            'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            'scriptTypeId': str(DEFAULT_SCRIPT_TYPE)
        })
    else:
        language_code = language_code.lower()
        if language_code in ['en', 'hi', 'te']:
            if language_code == 'en':
                language_code = 'ENG'
                script_code = 'LATN'
            elif language_code == 'hi':
                language_code = 'HIN'
                script_code = 'DEVA'
            else:
                language_code = 'TEL'
                script_code = 'TELU'
            locale = InitializableLocale(language_type_identifier=language_code,
                                         script_type_identifier=script_code)
            language_type_id = locale.language_type
            script_type_id = locale.script_type
        else:
            language_type_id = DEFAULT_LANGUAGE_TYPE
            script_type_id = DEFAULT_SCRIPT_TYPE

        return DisplayText(display_text_map={
            'text': text_string,
            'languageTypeId': str(language_type_id),
            'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            'scriptTypeId': str(script_type_id)
        })


class QTIFormWithMediaFiles(object):
    def _get_asset_content_genus_type(self, file_name):
        extension = self._get_file_extension(file_name).lower()
        if 'png' in extension:
            ac_genus_type = PNG_ASSET_CONTENT_GENUS_TYPE
        elif 'jpg' in extension or 'jpeg' in extension:
            ac_genus_type = JPG_ASSET_CONTENT_GENUS_TYPE
        elif 'svg' in extension:
            ac_genus_type = SVG_ASSET_CONTENT_GENUS_TYPE
        elif 'mp3' in extension:
            ac_genus_type = MP3_ASSET_CONTENT_GENUS_TYPE
        elif 'wav' in extension:
            ac_genus_type = WAV_ASSET_CONTENT_GENUS_TYPE
        else:
            # since this is used for the extension, let's derive it
            # more gracefully
            ac_genus_type = Type(identifier=extension,
                                 namespace='asset-content-genus-type',
                                 authority='ODL.MIT.EDU')
            # ac_genus_type = GENERIC_ASSET_CONTENT_GENUS_TYPE
        return ac_genus_type

    @staticmethod
    def _get_file_extension(file_name):
        return os.path.splitext(os.path.basename(file_name))[-1]

    def _add_media_files(self, soup, media_files):
        qti_media_regex = re.compile('(media)')
        media_file_elements = soup.find_all(src=qti_media_regex)
        media_file_data_elements = soup.find_all(data=qti_media_regex)
        media_file_elements += media_file_data_elements
        if len(media_file_elements) > 0 and media_files is not None:
            if 'Question' in self.my_osid_object_form._namespace:
                self.my_osid_object_form.get_question_form_record(FILES_QUESTION_RECORD)
            else:
                self.my_osid_object_form.get_answer_form_record(FILES_ANSWER_RECORD)

            for media_file_element in media_file_elements:
                if 'src' in media_file_element.attrs:
                    key = 'src'
                    asset_type = IMAGE_ASSET_GENUS_TYPE
                else:
                    key = 'data'
                    asset_type = AUDIO_ASSET_GENUS_TYPE

                media_file_url = media_file_element[key]

                ac_genus_type = self._get_asset_content_genus_type(media_file_url)
                media_file_id = media_file_url.split('%2F')[-1]
                media_file_name = media_file_id.replace('.', '_')

                # TODO: How do we add / check alias IDs for media files?
                # match on displayName? Probably not necessary because
                # they are all unique from Onyx...
                if media_file_name in media_files:
                    self.my_osid_object_form.add_file(DataInputStream(media_files[media_file_name]),
                                                      label=media_file_name,
                                                      asset_type=asset_type,
                                                      asset_content_type=ac_genus_type,
                                                      asset_content_record_types=[MULTI_LANGUAGE_ASSET_CONTENTS],
                                                      asset_name=media_file_id,
                                                      asset_description='QTI media file')

                    media_file_element[key] = 'AssetContent:{0}'.format(media_file_name)


class QTITypeRecordMixin(object):
    """Helper mixing to detect item / question type based on genusTypeId"""
    def _is_multiple_choice(self):
        return str(self.my_osid_object.genus_type) in [str(CHOICE_INTERACTION_QUESTION_GENUS),
                                                       str(CHOICE_INTERACTION_MULTI_QUESTION_GENUS),
                                                       str(CHOICE_INTERACTION_GENUS),
                                                       str(CHOICE_INTERACTION_MULTI_GENUS)]

    def _is_reflection(self):
        return str(self.my_osid_object.genus_type) in [str(CHOICE_INTERACTION_SURVEY_GENUS),
                                                       str(CHOICE_INTERACTION_MULTI_SELECT_SURVEY_GENUS),
                                                       str(CHOICE_INTERACTION_SURVEY_QUESTION_GENUS),
                                                       str(CHOICE_INTERACTION_MULTI_SELECT_SURVEY_QUESTION_GENUS)]

    def _is_file_upload(self):
        return str(self.my_osid_object.genus_type) in [str(UPLOAD_INTERACTION_GENERIC_GENUS),
                                                       str(UPLOAD_INTERACTION_GENERIC_QUESTION_GENUS)]

    def _is_audio_record(self):
        # excludes MW sandbox
        return str(self.my_osid_object.genus_type) in [str(UPLOAD_INTERACTION_AUDIO_QUESTION_GENUS),
                                                       str(UPLOAD_INTERACTION_AUDIO_GENUS)]

    def _is_image_sequence(self):
        return str(self.my_osid_object.genus_type) in [str(ORDER_INTERACTION_OBJECT_MANIPULATION_GENUS),
                                                       str(ORDER_INTERACTION_OBJECT_MANIPULATION_QUESTION_GENUS)]

    def _is_mw_sentence(self):
        return str(self.my_osid_object.genus_type) in [str(ORDER_INTERACTION_MW_SENTENCE_QUESTION_GENUS),
                                                       str(ORDER_INTERACTION_MW_SENTENCE_GENUS)]

    def _is_mw_sandbox(self):
        return str(self.my_osid_object.genus_type) in [str(ORDER_INTERACTION_MW_SANDBOX_GENUS),
                                                       str(ORDER_INTERACTION_MW_SANDBOX_QUESTION_GENUS)]

    def _is_fitb(self):
        return str(self.my_osid_object.genus_type) in [str(INLINE_CHOICE_MW_FITB_INTERACTION_QUESTION_GENUS),
                                                       str(INLINE_CHOICE_MW_FITB_INTERACTION_GENUS)]

    def _is_numeric_response(self):
        return str(self.my_osid_object.genus_type) in [str(NUMERIC_RESPONSE_QUESTION_GENUS),
                                                       str(NUMERIC_RESPONSE_GENUS)]

    def _is_short_answer(self):
        return str(self.my_osid_object.genus_type) in [str(EXTENDED_TEXT_INTERACTION_QUESTION_GENUS),
                                                       str(EXTENDED_TEXT_INTERACTION_GENUS)]

    def _only_generic_right_feedback(self):
        return (self._is_file_upload() or
                self._is_audio_record() or
                self._is_reflection() or
                self._is_mw_sandbox() or
                self._is_short_answer())


class QTIQuestionRecord(QTITypeRecordMixin, ObjectInitRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    @staticmethod
    def _wrap_xml(text, tag):
        bracketed_tag = '<{0}'.format(tag)
        if bracketed_tag not in text:
            return '<{0}>{1}</{0}>'.format(tag, text)
        return text

    @property
    def shuffle(self):
        try:
            return json.dumps(self.my_osid_object._my_map['shuffle'])
        except KeyError:
            # add this in for legacy data
            self.my_osid_object._my_map['shuffle'] = True
            return self.my_osid_object._my_map['shuffle']

    def get_qti_xml(self, media_file_root_path=''):
        qti = BeautifulSoup('<assessmentItem></assessmentItem>', 'xml')

        item = qti.assessmentItem

        try:
            item['identifier'] = self.my_osid_object._my_map['qti_id']
        except (AttributeError, KeyError):
            item['identifier'] = str(self.my_osid_object.ident)

        item['xml_ns'] = "http://www.imsglobal.org/xsd/imsqti_v2p1"
        item['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
        item['xsi:schemaLocation'] = "http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1p1.xsd http://www.w3.org/1998/Math/MathML http://www.w3.org/Math/XMLSchema/mathml2/mathml2.xsd"
        item['title'] = self.my_osid_object.display_name.text
        item['adaptive'] = False
        item['timeDependent'] = False

        original_choice_order = None
        try:
            original_choice_order = self.my_osid_object.get_unordered_choices()
        except AttributeError:
            pass

        object_map = self.my_osid_object.object_map

        if self._is_multiple_choice() or self._is_reflection():
            # scoring values
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            feedback_declaration = ('<outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">'
                                    '<defaultValue>'
                                    '<value>empty</value>'
                                    '</defaultValue>'
                                    '</outcomeDeclaration>')
            item.append(BeautifulSoup(feedback_declaration, 'xml').outcomeDeclaration)

            # item_body = qti.new_tag('itemBody')
            # don't use html.parser here because it lower cases all internal tags
            # i.e. inlineChoiceInteraction => inlinechoiceinteraction
            # assume this is one content?
            # for c in BeautifulSoup(self.my_osid_object.get_text().text, 'xml').contents:
            #     item_body.append(c)
            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody

            choice_interaction = qti.new_tag('choiceInteraction')
            choice_interaction['responseIdentifier'] = 'RESPONSE_1'
            choice_interaction['shuffle'] = self.my_osid_object.shuffle
            if str(self.my_osid_object.genus_type) in [str(CHOICE_INTERACTION_QUESTION_GENUS),
                                                       str(CHOICE_INTERACTION_SURVEY_QUESTION_GENUS)]:
                choice_interaction['maxChoices'] = '1'
            else:
                choice_interaction['maxChoices'] = '0'

            if json.loads(self.my_osid_object.shuffle):
                choices_list = object_map['choices']
            else:
                choices_list = object_map['choices']
                if original_choice_order is not None:
                    # need to verify this works
                    # it may not, because we've called .object_map
                    choices_list = original_choice_order
                    # need to replace the text, in case there was an image or media URL
                    # generated by .object_map
                    for choice in choices_list:
                        matching_choice = [c
                                           for c in object_map['choices']
                                           if c['id'] == choice['id']][0]
                        choice['text'] = matching_choice['text']

            for choice in choices_list:
                if 'text' in choice:
                    choice_text = self._wrap_xml(choice['text'], 'simpleChoice')
                else:
                    choice_text = self._wrap_xml(self.my_osid_object.get_matching_language_value('texts',
                                                                                                 dictionary=choice).text,
                                                 'simpleChoice')
                choice_tag = BeautifulSoup(choice_text,
                                           'xml').simpleChoice
                # especially for multi-language, need to replace the ID in the XML
                # with the choice['id']
                choice_tag['identifier'] = choice['id']
                choice_interaction.append(choice_tag)

            item_body.append(choice_interaction)
            item.append(item_body)
        elif self._is_audio_record() or self._is_file_upload():
            # scoring values
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody

            upload_interaction = qti.new_tag('uploadInteraction')
            upload_interaction['responseIdentifier'] = 'RESPONSE_1'
            item_body.append(upload_interaction)
            item.append(item_body)
        elif self._is_mw_sandbox() or self._is_mw_sentence() or self._is_image_sequence():
            # scoring values
            # we're not capturing score on create, so it is irrelevant here ...
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            feedback_declaration = ('<outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">'
                                    '<defaultValue>'
                                    '<value>empty</value>'
                                    '</defaultValue>'
                                    '</outcomeDeclaration>')
            item.append(BeautifulSoup(feedback_declaration, 'xml').outcomeDeclaration)
            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody

            order_interaction = qti.new_tag('orderInteraction')
            order_interaction['responseIdentifier'] = 'RESPONSE_1'
            order_interaction['shuffle'] = self.my_osid_object.shuffle
            for choice in object_map['choices']:
                if 'text' in choice:
                    choice_text = self._wrap_xml(choice['text'], 'simpleChoice')
                else:
                    choice_text = self._wrap_xml(self.my_osid_object.get_matching_language_value('texts',
                                                                                                 dictionary=choice).text,
                                                 'simpleChoice')
                choice_tag = BeautifulSoup(choice_text, 'xml').simpleChoice
                choice_tag['identifier'] = choice['id']
                order_interaction.append(choice_tag)

            item_body.append(order_interaction)
            item.append(item_body)
        elif self._is_short_answer():
            # scoring values
            # we're not capturing score on create, so it is irrelevant here ...
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            feedback_declaration = ('<outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">'
                                    '<defaultValue>'
                                    '<value>empty</value>'
                                    '</defaultValue>'
                                    '</outcomeDeclaration>')
            item.append(BeautifulSoup(feedback_declaration, 'xml').outcomeDeclaration)

            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody

            text_interaction = qti.new_tag('extendedTextInteraction')
            text_interaction['responseIdentifier'] = 'RESPONSE_1'
            text_interaction['maxStrings'] = self.my_osid_object.max_strings
            text_interaction['expectedLength'] = self.my_osid_object.expected_length
            text_interaction['expectedLines'] = self.my_osid_object.expected_lines
            item_body.append(text_interaction)
            item.append(item_body)
        elif self._is_fitb():
            # scoring values
            # we're not capturing score on create, so it is irrelevant here ...
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            feedback_declaration = ('<outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">'
                                    '<defaultValue>'
                                    '<value>empty</value>'
                                    '</defaultValue>'
                                    '</outcomeDeclaration>')
            item.append(BeautifulSoup(feedback_declaration, 'xml').outcomeDeclaration)
            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody

            choice_region_map = object_map['choices']

            for inline_choice_interaction in item_body.find_all('inlineChoiceInteraction'):
                inline_identifier = inline_choice_interaction['responseIdentifier']
                for choice in choice_region_map[inline_identifier]:
                    if 'text' in choice:
                        choice_text = self._wrap_xml(choice['text'], 'inlineChoice')
                    else:
                        choice_text = self._wrap_xml(self.my_osid_object.get_matching_language_value('texts',
                                                                                                     dictionary=choice).text,
                                                     'inlineChoice')

                    inline_choice = BeautifulSoup(choice_text, 'xml').inlineChoice
                    inline_choice['identifier'] = choice['id']
                    inline_choice_interaction.append(inline_choice)
            item.append(item_body)
        elif self._is_numeric_response():
            # scoring values
            # we're not capturing score on create, so it is irrelevant here ...
            score_declaration = ('<outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">'
                                 '<defaultValue>'
                                 '<value>0</value>'
                                 '</defaultValue>'
                                 '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_declaration, 'xml').outcomeDeclaration)
            max_score_declaration = ('<outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">'
                                     '<defaultValue>'
                                     '<value>1</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_declaration, 'xml').outcomeDeclaration)
            min_score_declaration = ('<outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">'
                                     '<defaultValue>'
                                     '<value>0</value>'
                                     '</defaultValue>'
                                     '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_declaration, 'xml').outcomeDeclaration)
            feedback_declaration = ('<outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">'
                                    '<defaultValue>'
                                    '<value>empty</value>'
                                    '</defaultValue>'
                                    '</outcomeDeclaration>')
            item.append(BeautifulSoup(feedback_declaration, 'xml').outcomeDeclaration)
            max_score_response_declaration = ('<outcomeDeclaration identifier="MAXSCORE_RESPONSE_1" cardinality="single" baseType="float" view="testConstructor">'
                                              '<defaultValue>'
                                              '<value>1</value>'
                                              '</defaultValue>'
                                              '</outcomeDeclaration>')
            item.append(BeautifulSoup(max_score_response_declaration, 'xml').outcomeDeclaration)
            min_score_response_declaration = ('<outcomeDeclaration identifier="MINSCORE_RESPONSE_1" cardinality="single" baseType="float" view="testConstructor">'
                                              '<defaultValue>'
                                              '<value>0</value>'
                                              '</defaultValue>'
                                              '</outcomeDeclaration>')
            item.append(BeautifulSoup(min_score_response_declaration, 'xml').outcomeDeclaration)
            score_response_declaration = ('<outcomeDeclaration identifier="SCORE_RESPONSE_1" cardinality="single" baseType="float" view="testConstructor">'
                                          '<defaultValue>'
                                          '<value>0</value>'
                                          '</defaultValue>'
                                          '</outcomeDeclaration>')
            item.append(BeautifulSoup(score_response_declaration, 'xml').outcomeDeclaration)

            # ignore the template declarations here, because not needed for client-side
            my_text = self._wrap_xml(object_map['text']['text'], 'itemBody')
            item_body = BeautifulSoup(my_text, 'xml').itemBody
            item.append(item_body)

        return qti.prettify()


class QTIQuestionFormRecord(QTIFormWithMediaFiles, osid_records.OsidRecord):
    """A record for an ``ItemForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(QTIQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['shuffle'] = \
            bool(self._shuffle_metadata['default_boolean_values'][0])

    def _init_metadata(self):
        """stub"""
        self._shuffle_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'shuffle'),
            'element_label': 'Shuffle',
            'instructions': 'Shuffle parameters',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }

    def get_shuffle_metadata(self):
        """stub"""
        return Metadata(**self._shuffle_metadata)

    def set_shuffle(self, shuffle):
        """stub"""
        if not self.my_osid_object_form._is_valid_boolean(
                shuffle):
            raise InvalidArgument('shuffle')
        self.my_osid_object_form._my_map['shuffle'] = shuffle

    def clear_shuffle(self):
        """stub"""
        self.my_osid_object_form._my_map['shuffle'] = \
            bool(self._shuffle_metadata['default_boolean_values'][0])

    @staticmethod
    def _wrap_mw_words(soup_tag):
        # need to parse out the "type of word" here
        # [the bus]<noun> should become => <p class="noun">the bus</p>
        word_type_regex = re.compile('{(.*)}')
        choice_regex = re.compile(r'\[(.*)\]')
        choice_text = choice_regex.findall(_stringify(soup_tag, contents=True))
        if len(choice_text) > 0:
            choice_text = choice_text[0]
        else:
            choice_text = _stringify(soup_tag)
        word_type = word_type_regex.findall(_stringify(soup_tag, contents=True))
        if len(word_type) > 0:
            word_type = word_type[0]
        else:
            word_type = ""
        wrapped_choice = BeautifulSoup('<p class="{0}">{1}</p>'.format(word_type,
                                                                       choice_text), 'xml').p
        return wrapped_choice

    def _recursively_wrap_words_in_item_body(self, soup_tag):
        def clean_list_content(content_list):
            is_clean = True
            content_list = [c for c in content_list if c != '']

            for c in content_list:
                if not (c.startswith('[') and c.endswith('}')):
                    is_clean = False
                    break
            if not is_clean:
                clean_content = []
                indices_to_delete = []
                for index_c, content_ in enumerate(content_list):
                    if not content_.startswith('['):
                        clean_content.append('{0} {1}'.format(clean_content[index_c - 1],
                                                              content_))
                        indices_to_delete.append(index_c - 1)
                    else:
                        clean_content.append(content_)
                indices_to_delete.reverse()
                for index_d in indices_to_delete:
                    del clean_content[index_d]
                return clean_list_content(clean_content)
            else:
                return content_list
        for index, content in enumerate(soup_tag.contents):
            if isinstance(content, Tag):
                self._recursively_wrap_words_in_item_body(content)
            else:
                content = content.strip()

                if '[' in content and '{' in content:  # otherwise just a string
                    has_ending_punctuation = None
                    ending_symbols = ['.', '?', '!']
                    if any(content.endswith(symbol) for symbol in ending_symbols):
                        has_ending_punctuation = content[-1]
                        for symbol in ending_symbols:
                            content = content.replace(symbol, '')
                    # separated_content = content.strip().split(' ').split('\xa0')
                    split_contents = re.split(r'(\[.*?})', content.strip())
                    separated_content = [item for item in split_contents
                                         if item not in ['', ' ', '\xa0']]
                    # let's clean this up, because some of the words will break
                    # like [the bus]{noun}
                    cleaned_content = clean_list_content(separated_content)
                    new_tag = BeautifulSoup('<p></p>', 'xml').p
                    for pair in cleaned_content:
                        new_tag.append(self._wrap_mw_words(pair.strip()))

                    if has_ending_punctuation is not None:
                        new_tag.append(has_ending_punctuation)
                    soup_tag.contents[index].replace_with(new_tag)

    def load_from_qti_item(self, qti_item, media_files=None, keywords=()):
        my_qti_record_identifiers = [Id(i).get_identifier()
                                     for i in self.my_osid_object_form._my_map['recordTypeIds']
                                     if Id(i).get_identifier() == 'qti']
        if len(my_qti_record_identifiers) > 1:
            raise IllegalState('Can not load QTI item more than once')

        soup = BeautifulSoup(qti_item, 'xml')

        # for all embedded audio elements, change them to <audio> tags
        # instead of the Onyx <object> tags, and only autoplay the first one
        # (in the itemBody). Anything in a choice should be autoplay false
        # by default.
        first_object = True
        for object_ in soup.find_all('object'):
            if first_object:
                first_object = False
                is_choice = False
                for parent in object_.parents:
                    if parent.name in ['simpleChoice', 'inlineChoice']:
                        is_choice = True
                        # param = soup.new_tag('param')
                        # param['name'] = 'autoplay'
                        # param['value'] = 'false'
                        # object_.append(param)
                        # object_['autoplay'] = 'false'
                        break
                audio = soup.new_tag('audio')
                audio['controls'] = 'controls'
                audio['style'] = 'width: 125px'
                source = soup.new_tag('source')
                source['type'] = 'audio/mpeg'
                source['src'] = object_['data']
                if is_choice:
                    pass  # no autoplay
                else:
                    audio['autoplay'] = 'autoplay'
                audio.append(source)
                object_.replace_with(audio)
            else:
                audio = soup.new_tag('audio')
                audio['controls'] = 'controls'
                audio['style'] = 'width: 125px'
                source = soup.new_tag('source')
                source['type'] = 'audio/mpeg'
                source['src'] = object_['data']
                audio.append(source)
                object_.replace_with(audio)

        # Pull in the randomized records here.
        # need to do this before any choices get assigned and files added, otherwise they will get
        # reset to []
        if (soup.itemBody.choiceInteraction or
                soup.itemBody.orderInteraction):
            if soup.itemBody.choiceInteraction:
                interaction = soup.itemBody.choiceInteraction
            else:
                interaction = soup.itemBody.orderInteraction
            if ('shuffle' not in interaction.attrs or
                    json.loads(interaction['shuffle'])):
                self.my_osid_object_form.get_question_form_record(RANDOMIZED_MULTI_CHOICE_QUESTION_RECORD)
                self.my_osid_object_form.set_shuffle(True)
            else:
                self.my_osid_object_form.set_shuffle(False)
            # default is True
        elif soup.itemBody.inlineChoiceInteraction:
            # doesn't use that MC randomized record
            interaction = soup.itemBody.inlineChoiceInteraction
            if ('shuffle' not in interaction.attrs or
                    json.loads(interaction['shuffle'])):
                self.my_osid_object_form.set_shuffle(True)
            else:
                self.my_osid_object_form.set_shuffle(False)

        self._add_media_files(soup, media_files)

        item_name = soup.assessmentItem['title']
        language_code = None
        if any(lang_code in item_name for lang_code in ['en', 'hi', 'te']):
            language_code = item_name.split('_')[-1]
            item_name = '_'.join(item_name.split('_')[0:-1])

        display_name = create_display_text(item_name, language_code)
        description = create_display_text(item_name, language_code)

        if soup.itemBody.choiceInteraction:
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_MULTIPLE_CHOICE_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?
            choice_interaction = soup.itemBody.choiceInteraction.extract()

            self.my_osid_object_form.add_text(create_display_text(_stringify(soup.itemBody),
                                                                  language_code))
            for choice in choice_interaction.find_all('simpleChoice'):
                choice_text = create_display_text(_stringify(choice),
                                                  language_code)
                self.my_osid_object_form.add_choice(
                    choice_text, name='', identifier=choice['identifier'])

            if len(keywords) > 0 and 'mcreflect' in [k.lower() for k in keywords]:
                if choice_interaction['maxChoices'] == '0':
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_MULTI_SELECT_SURVEY_QUESTION_GENUS)
                else:
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_SURVEY_QUESTION_GENUS)
            else:
                if choice_interaction['maxChoices'] == '1':
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_QUESTION_GENUS)
                else:
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_MULTI_QUESTION_GENUS)

        elif soup.itemBody.uploadInteraction:
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_FILE_UPLOAD_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?
            upload_interaction = soup.itemBody.uploadInteraction.extract()
            self.my_osid_object_form.add_text(create_display_text(_stringify(soup.itemBody),
                                                                  language_code))
            # now check the keywords for the specific upload type
            # out of band agreement
            if len(keywords) > 0 and 'audiort' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(UPLOAD_INTERACTION_AUDIO_QUESTION_GENUS)
            else:
                self.my_osid_object_form.set_genus_type(UPLOAD_INTERACTION_GENERIC_QUESTION_GENUS)
        elif soup.itemBody.orderInteraction:
            # the main difference here (MW Sentence) will be that
            # the answer has multiple choices used, not a single choice
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?
            order_interaction = soup.itemBody.orderInteraction.extract()
            self.my_osid_object_form.add_text(create_display_text(_stringify(soup.itemBody),
                                                                  language_code))

            is_object_manipulation = False
            if len(keywords) > 0 and 'mwsentence' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_MW_SENTENCE_QUESTION_GENUS)
            elif len(keywords) > 0 and 'mwsandbox' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_MW_SANDBOX_QUESTION_GENUS)
            elif len(keywords) > 0 and 'objmsequence' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_OBJECT_MANIPULATION_QUESTION_GENUS)
                is_object_manipulation = True

            # only wrap the words if it is not object manipulation
            for choice in order_interaction.find_all('simpleChoice'):
                # assumes simple text words only??
                if not is_object_manipulation:
                    choice.contents[0].replace_with(self._wrap_mw_words(choice))
                choice_text = create_display_text(str(choice),
                                                  language_code)
                self.my_osid_object_form.add_choice(
                    choice_text, name='', identifier=choice['identifier'])
        elif soup.itemBody.extendedTextInteraction:
            # do the multi language one second so that the texts fields and metadata
            # do not get wiped out
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_EXTENDED_TEXT_INTERACTION_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?
            text_interaction = soup.itemBody.extendedTextInteraction.extract()
            self.my_osid_object_form.add_text(create_display_text(_stringify(soup.itemBody),
                                                                  language_code))

            # capture the metadata values for extended text interaction
            if 'maxStrings' in text_interaction.attrs:
                self.my_osid_object_form.set_max_strings(int(text_interaction['maxStrings']))
            if 'expectedLength' in text_interaction.attrs:
                self.my_osid_object_form.set_expected_length(int(text_interaction['expectedLength']))
            if 'expectedLines' in text_interaction.attrs:
                self.my_osid_object_form.set_expected_lines(int(text_interaction['expectedLines']))
            self.my_osid_object_form.set_genus_type(EXTENDED_TEXT_INTERACTION_QUESTION_GENUS)
        elif soup.itemBody.inlineChoiceInteraction:
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_INLINE_CHOICE_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?

            for inline_choice_interaction in soup.itemBody.find_all('inlineChoiceInteraction'):
                region_identifier = inline_choice_interaction['responseIdentifier']
                self.my_osid_object_form.add_inline_region(region_identifier)
                self.my_osid_object_form.set_shuffle(json.loads(inline_choice_interaction['shuffle']))
                for choice in inline_choice_interaction.find_all('inlineChoice'):
                    choice.contents[0].replace_with(self._wrap_mw_words(choice))
                    choice_text = create_display_text(str(choice),
                                                      language_code)
                    self.my_osid_object_form.add_choice(choice_text,
                                                        region_identifier,
                                                        identifier=choice['identifier'])
                    choice.extract()

            # now try to wrap the words in the itemBody ...
            self._recursively_wrap_words_in_item_body(soup.itemBody)

            self.my_osid_object_form.add_text(create_display_text(_stringify(soup.itemBody),
                                                                  language_code))
            self.my_osid_object_form.set_genus_type(INLINE_CHOICE_MW_FITB_INTERACTION_QUESTION_GENUS)
        elif soup.itemBody.textEntryInteraction and soup.templateDeclaration:
            self.my_osid_object_form.get_question_form_record(MULTI_LANGUAGE_NUMERIC_RESPONSE_QUESTION_RECORD)
            self.my_osid_object_form.add_display_name(display_name)
            self.my_osid_object_form.add_description(description)  # Is there a description in QTI?
            self.my_osid_object_form.set_genus_type(NUMERIC_RESPONSE_QUESTION_GENUS)

            soup.itemBody.textEntryInteraction['responseIdentifier'] = 'RESPONSE_1'  # let's standardize ...
            original_item_body = _stringify(soup.itemBody)
            if soup.itemBody.printedVariable:
                for printed_var in soup.itemBody.find_all('printedVariable'):
                    var_id = printed_var['identifier']
                    printed_var.replace_with('{{{0}}}'.format(var_id))

            # used simple form, should be like {var1} + {var2}
            # item_body_str = _stringify(soup.itemBody)
            # expression = item_body_str[item_body_str.index(':') + 1:item_body_str.index('=')].strip()
            numeric_choice_wrapper = None
            interaction = soup.itemBody.textEntryInteraction
            for parent in interaction.parents:
                if parent.name == 'p':
                    numeric_choice_wrapper = parent
                    break

            numeric_choice_line_str = _stringify(numeric_choice_wrapper)
            expression = numeric_choice_line_str[3:numeric_choice_line_str.index('=')].strip()  # skip the opening <p> tag
            self.my_osid_object_form.set_expression(expression)

            self.my_osid_object_form.add_text(create_display_text(original_item_body,
                                                                  language_code))

            variables = {}
            for var in soup.find_all('templateDeclaration'):
                var_name = var['identifier']
                if var_name != 'solution':
                    var_type = var['baseType']
                    variables[var_name] = {
                        'type': var_type
                    }
                    if 'format' in var.attrs:
                        variables[var_name]['format'] = var['format']
            for var_params in soup.find_all('setTemplateValue'):
                var_name = var_params['identifier']
                if var_name in variables:
                    if variables[var_name]['type'] == 'integer':
                        variables[var_name]['min'] = var_params.randomInteger['min']
                        variables[var_name]['max'] = var_params.randomInteger['max']
                        variables[var_name]['step'] = 1
                    elif variables[var_name]['type'] == 'float':
                        variables[var_name]['min'] = float(var_params.randomFloat['min'])
                        variables[var_name]['max'] = float(var_params.randomFloat['max'])
                    else:
                        # don't know what to do with things like "solution" or "RESPONSE_1"
                        pass

            for var_name, var_data in variables.items():
                if 'format'in var_data:
                    var_format = var_data['format']
                else:
                    var_format = ''
                if 'step' in var_data:
                    step = var_data['step']
                else:
                    step = 1
                self.my_osid_object_form.add_variable(var_name.lower(),  # why does it lowercase? see the simple_numeric_response_test_file
                                                      var_data['type'],
                                                      var_data['min'],
                                                      var_data['max'],
                                                      var_step=step,
                                                      format=var_format)
        else:
            raise OperationFailed('Item type not supported or unrecognized')


class QTIAnswerRecord(ObjectInitRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def get_qti_xml(self, media_file_root_path=''):
        try:
            if '<modalFeedback' not in self.my_osid_object.feedback.text:
                qti = BeautifulSoup('<modalFeedback></modalFeedback>', 'xml')
                feedback = qti.modalFeedback
                feedback['identifier'] = str(self.my_osid_object.ident)
                feedback['outcomeIdentifier'] = "FEEDBACKMODAL"
                feedback['showHide'] = "show"
                feedback_wrapped = '<div>{0}</div>'.format(self.my_osid_object.feedback.text)
                feedback_soup = BeautifulSoup(feedback_wrapped, 'xml').div
                feedback.append(feedback_soup)
            else:
                qti = BeautifulSoup(self.my_osid_object.feedback.text, 'xml')
        except AttributeError:
            qti = BeautifulSoup('<modalFeedback></modalFeedback>', 'xml')
            feedback = qti.modalFeedback
            feedback['identifier'] = str(self.my_osid_object.ident)
            feedback['outcomeIdentifier'] = "FEEDBACKMODAL"
            feedback['showHide'] = "show"

        return qti.prettify()


class QTIAnswerFormRecord(QTIFormWithMediaFiles, osid_records.OsidRecord):
    """A record for an ``AnswerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form

    def _set_feedback(self, soup, correct, feedback_choice_id, submitted=False, media_files=None):
        # add media files here, otherwise getting the other records might over-write fileIds
        empty_modal = create_display_text("""<modalFeedback  identifier="Feedback" outcomeIdentifier="FEEDBACKMODAL" showHide="show">
<p></p>
</modalFeedback>""")
        response_processing = soup.assessmentItem.responseProcessing
        if not response_processing:
            if correct:
                if submitted:
                    self.my_osid_object_form.add_feedback(empty_modal)
                else:
                    self.my_osid_object_form.set_feedback(empty_modal)
            else:
                self.my_osid_object_form.set_feedback(empty_modal)
        else:
            matches = response_processing.find_all('match')
            found_direct_feedback = False
            for match in matches:
                if feedback_choice_id != '' and match.find(string=feedback_choice_id):
                    for parent in match.parents:
                        if parent.name == 'responseIf':
                            feedback_id = parent.setOutcomeValue.baseValue.string
                            if feedback_id != 'FEEDBACKBASIC':
                                feedback = soup.find('modalFeedback', identifier=feedback_id)
                                if feedback:
                                    self._add_media_files(feedback, media_files)
                                    self.my_osid_object_form.add_feedback(create_display_text(_stringify(feedback)))
                                    found_direct_feedback = True
                            break
                    break
                else:
                    try:
                        match_value = match.baseValue.string.strip()
                        if (match_value == 'empty' or match_value == 'correct') and correct:
                            for parent in match.parents:
                                if parent.name == 'responseIf':
                                    feedback_id = parent.setOutcomeValue.baseValue.string.strip()
                                    if feedback_id != 'FEEDBACKBASIC':
                                        feedback = soup.find('modalFeedback', identifier=feedback_id)
                                        if feedback:
                                            self._add_media_files(feedback, media_files)
                                            self.my_osid_object_form.add_feedback(create_display_text(_stringify(feedback)))
                                            found_direct_feedback = True
                                            break
                    except AttributeError:
                        pass

            if not found_direct_feedback and correct:
                if submitted:
                    self.my_osid_object_form.add_feedback(empty_modal)
                else:
                    self.my_osid_object_form.add_feedback(empty_modal)
            if not found_direct_feedback and not correct:
                feedback_found = False
                for match in matches:
                    if match.find(string='incorrect'):
                        for parent in match.parents:
                            if parent.name == 'responseIf':
                                feedback_id = parent.setOutcomeValue.baseValue.string

                                feedback = soup.find('modalFeedback', identifier=feedback_id)
                                if feedback:
                                    self._add_media_files(feedback, media_files)
                                    feedback_found = True
                                    self.my_osid_object_form.add_feedback(create_display_text(_stringify(feedback)))
                                    break
                if not feedback_found:
                    self.my_osid_object_form.add_feedback(empty_modal)

    def load_from_qti_item(self, qti_item, keywords=(), correct=False, feedback_choice_id='', media_files=None):
        my_qti_record_identifiers = [Id(i).get_identifier()
                                     for i in self.my_osid_object_form._my_map['recordTypeIds']
                                     if Id(i).get_identifier() == 'qti']
        if len(my_qti_record_identifiers) > 1:
            raise IllegalState('Can not load QTI item more than once')
        soup = BeautifulSoup(qti_item, 'xml')
        if correct:
            answer_genus = RIGHT_ANSWER_GENUS
        else:
            answer_genus = WRONG_ANSWER_GENUS

        if soup.itemBody.choiceInteraction:
            self.my_osid_object_form.get_answer_form_record(SIMPLE_MULTIPLE_CHOICE_ANSWER_RECORD)

            # self.my_osid_object_form.display_name = soup.assessmentItem['title']
            # self.my_osid_object_form.description = soup.assessmentItem['title'] # Is there a description in QTI?

            if correct:
                for value in soup.responseDeclaration.correctResponse.find_all('value'):
                    self.my_osid_object_form.add_choice_id(value.string)
            else:
                if feedback_choice_id == 'incorrect' or feedback_choice_id == '':
                    self.my_osid_object_form.add_choice_id(None)
                else:
                    self.my_osid_object_form.add_choice_id(feedback_choice_id)
            self.my_osid_object_form.set_genus_type(answer_genus)

            if len(keywords) > 0 and 'mcreflect' in [k.lower() for k in keywords]:
                # because we'll want the standard "correct" feedback, if provided
                # this should work for both single and multi-select survey questions
                self.my_osid_object_form.set_genus_type(RIGHT_ANSWER_GENUS)
                self._set_feedback(soup, True, 'correct', media_files=media_files)
            else:
                # get the feedback for the passed in feedback_choice_id
                self._set_feedback(soup, correct, feedback_choice_id, media_files=media_files)
        elif soup.itemBody.uploadInteraction:
            self.my_osid_object_form.get_answer_form_record(FILE_SUBMISSION_ANSWER_RECORD)
            # self.my_osid_object_form.display_name = soup.assessmentItem['title']
            # self.my_osid_object_form.description = soup.assessmentItem['title'] # Is there a description in QTI?
            # now check the keywords for the specific upload type
            # out of band agreement
            if len(keywords) > 0 and 'audiort' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(answer_genus)
            else:
                self.my_osid_object_form.set_genus_type(answer_genus)

            if correct:
                # self.my_osid_object_form.get_answer_form_record(MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD)
                self._set_feedback(soup, correct, feedback_choice_id, submitted=True, media_files=media_files)
        elif soup.itemBody.orderInteraction:
            if 'mwsandbox' in [k.lower() for k in keywords]:
                sandbox = True
                self.my_osid_object_form.get_answer_form_record(FILE_SUBMISSION_ANSWER_RECORD)
            else:
                sandbox = False
                self.my_osid_object_form.get_answer_form_record(SIMPLE_MULTIPLE_CHOICE_ANSWER_RECORD)

            # self.my_osid_object_form.display_name = soup.assessmentItem['title']
            # self.my_osid_object_form.description = soup.assessmentItem['title'] # Is there a description in QTI?

            if not sandbox:
                if correct:
                    for value in soup.responseDeclaration.correctResponse:
                        self.my_osid_object_form.add_choice_id(value.string)
                else:
                    # all other choice orders ...
                    self.my_osid_object_form.add_choice_id(None)
            self.my_osid_object_form.set_genus_type(answer_genus)

            if correct and sandbox:
                # self.my_osid_object_form.get_answer_form_record(MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD)
                self._set_feedback(soup, correct, feedback_choice_id, submitted=True, media_files=media_files)
            else:
                # get the feedback for the passed in feedback_choice_id
                self._set_feedback(soup, correct, feedback_choice_id, media_files=media_files)
        elif soup.itemBody.extendedTextInteraction:
            self.my_osid_object_form.get_answer_form_record(EXTENDED_TEXT_INTERACTION_ANSWER_RECORD)
            self.my_osid_object_form.set_genus_type(answer_genus)

            if correct:
                # self.my_osid_object_form.get_answer_form_record(MULTI_LANGUAGE_FEEDBACK_ANSWER_RECORD)
                self._set_feedback(soup, correct, feedback_choice_id, submitted=True, media_files=media_files)
        elif soup.itemBody.inlineChoiceInteraction:
            self.my_osid_object_form.get_answer_form_record(SIMPLE_INLINE_CHOICE_ANSWER_RECORD)
            # self.my_osid_object_form.display_name = soup.assessmentItem['title']
            # self.my_osid_object_form.description = soup.assessmentItem['title'] # Is there a description in QTI?

            if correct:
                # Submit the IDs against the order of IDs in
                # the itemBody
                response_ids_list = []
                for interaction in soup.itemBody.find_all('inlineChoiceInteraction'):
                    response_id = interaction['responseIdentifier']
                    self.my_osid_object_form.add_inline_region(response_id)
                    response_ids_list.append(response_id)

                for response_id in response_ids_list:
                    response = soup.find('responseDeclaration', identifier=response_id)
                    for value in response.correctResponse.find_all('value'):
                        self.my_osid_object_form.add_choice_id(value.string, response_id)
            else:
                # all other choice orders ...
                pass
            self.my_osid_object_form.set_genus_type(answer_genus)

            # get the feedback for the passed in feedback_choice_id
            self._set_feedback(soup, correct, feedback_choice_id, media_files=media_files)
        elif soup.itemBody.textEntryInteraction and soup.templateDeclaration:
            # only store the tolerance information here?
            self.my_osid_object_form.get_answer_form_record(MULTI_LANGUAGE_NUMERIC_RESPONSE_ANSWER_RECORD)
            # self.my_osid_object_form.display_name = soup.assessmentItem['title']
            # self.my_osid_object_form.description = soup.assessmentItem['title'] # Is there a description in QTI?

            if correct:
                for response_condition in soup.find_all('responseCondition'):
                    if response_condition.responseIf.equal:
                        self.my_osid_object_form.set_tolerance_mode(response_condition.responseIf.equal['toleranceMode'])
                        break
                        # should also take care of other settings here?
            else:
                # all other choice orders ...
                pass
            self.my_osid_object_form.set_genus_type(answer_genus)

            # get the feedback for the passed in feedback_choice_id
            self._set_feedback(soup, correct, feedback_choice_id, media_files=media_files)
        else:
            raise OperationFailed('Item type not supported or unrecognized')


class QTIItemRecord(QTITypeRecordMixin, MultiChoiceItemRecord, OrderedChoiceItemRecord,
                    CalculationInteractionItemRecord, MagicRandomizedInlineChoiceItemRecord,
                    ObjectInitRecord):
    """A record for an ``Item``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def _is_match(self, response, answer):
        """For MC, can call through to MultiChoice Item Record?"""
        # TODO: this varies depending on question type
        if self._only_generic_right_feedback():
            return str(answer.genus_type) == str(RIGHT_ANSWER_GENUS)
        elif self._is_multiple_choice():
            return MultiChoiceItemRecord._is_match(self, response, answer)
        elif self._is_image_sequence() or self._is_mw_sentence():
            return OrderedChoiceItemRecord._is_match(self, response, answer)
        elif self._is_numeric_response():
            return CalculationInteractionItemRecord._is_match(self, response, answer)
        elif self._is_fitb():
            return MagicRandomizedInlineChoiceItemRecord._is_match(self, response, answer)
        return False

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular response"""
        return True

    def is_response_correct(self, response):
        """returns True if response evaluates to an Item Answer that is 100 percent correct"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return True
        return False

    def get_correctness_for_response(self, response):
        """get measure of correctness available for a particular response"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 100
        for answer in self.my_osid_object.get_wrong_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 0
        return 0

    def get_answer_for_response(self, response):
        # TODO: for certain QTI question types, need to find
        # a generic right-answer (file upload, ART, reflection)
        if self._only_generic_right_feedback():
            for answer in self.my_osid_object.get_answers():
                if self._is_match(response, answer):
                    return answer

            try:
                wrong_answers = list(self.my_osid_object.get_wrong_answers())
            except AttributeError:
                pass
            else:
                for answer in wrong_answers:
                    if self._is_match(response, answer):
                        return answer
        elif self._is_multiple_choice():
            return MultiChoiceItemRecord.get_answer_for_response(self, response)
        elif self._is_image_sequence() or self._is_mw_sentence():
            return OrderedChoiceItemRecord.get_answer_for_response(self, response)
        elif self._is_numeric_response():
            return CalculationInteractionItemRecord.get_answer_for_response(self, response)
        elif self._is_fitb():
            return MagicRandomizedInlineChoiceItemRecord.get_answer_for_response(self, response)

        raise NotFound('no matching answer found for response')

    def is_feedback_available_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            return False
        try:
            return answer.has_feedback()
        except AttributeError:
            return False

    def get_feedback_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        answer.object_map  # this will generate any source URLs from the adapter...kind of a hack
        return answer.get_feedback()  # raises IllegalState

    def get_confused_learning_objective_ids_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        try:
            return answer.get_confused_learning_objective_ids()
        except AttributeError:
            return IdList([])

    def get_qti_xml(self, media_file_root_path=''):
        try:
            qti = BeautifulSoup(
                self.my_osid_object.get_question().get_qti_xml(
                    media_file_root_path=media_file_root_path),
                'xml')
        except (TypeError, AttributeError):
            # no question?? or not a QTI question?
            return ''

        item = qti.assessmentItem
        if str(self.my_osid_object.genus_type) in [str(CHOICE_INTERACTION_GENUS),
                                                   str(CHOICE_INTERACTION_MULTI_GENUS)]:

            # TODO: this is a big assumption...that only one correct answer exists?
            try:
                correct_answer = next(self.my_osid_object.get_answers())
            except StopIteration:
                # no correct answers
                pass
            else:
                response = qti.new_tag('responseDeclaration')
                response['identifier'] = 'RESPONSE_1'
                response['cardinality'] = 'single'
                response['baseType'] = 'identifier'

                correct_response = qti.new_tag('correctResponse')
                value = qti.new_tag('value')
                value.string = correct_answer.object_map['choiceIds'][0]
                correct_response.append(value)
                response.append(correct_response)

                item.append(response)

                # responseProcessing
                response_processing = qti.new_tag('responseProcessing')
                response_condition = qti.new_tag('responseCondition')
                response_if = qti.new_tag('responseIf')
                is_null = qti.new_tag('isNull')
                variable = qti.new_tag('variable')
                variable['identifier'] = 'RESPONSE_1'
                is_null.append(variable)
                response_if.append(is_null)
                set_outcome_value = qti.new_tag('setOutcomeValue')
                set_outcome_value['identifier'] = 'FEEDBACKBASIC'
                base_value = qti.new_tag('baseValue')
                base_value['baseType'] = 'identifier'
                base_value.string = 'empty'
                set_outcome_value.append(base_value)
                response_if.append(set_outcome_value)

                response_else_if = qti.new_tag('responseElseIf')
                match = qti.new_tag('match')
                variable = qti.new_tag('variable')
                variable['identifier'] = 'RESPONSE_1'
                match.append(variable)
                response_else_if.append(match)
                set_outcome_value = qti.new_tag('setOutcomeValue')
                set_outcome_value['identifier'] = 'SCORE'
                sum = qti.new_tag('sum')
                for var in ['SCORE', 'MAXSCORE']:
                    variable = qti.new_tag('variable')
                    variable['identifier'] = var
                    sum.append(variable)
                set_outcome_value.append(sum)
                response_else_if.append(set_outcome_value)
                set_outcome_value = qti.new_tag('setOutcomeValue')
                set_outcome_value['identifier'] = 'FEEDBACKBASIC'
                base_value = qti.new_tag('baseValue')
                base_value['baseType'] = 'identifier'
                base_value.string = 'correct'
                set_outcome_value.append(base_value)
                response_else_if.append(set_outcome_value)

                response_else = qti.new_tag('responseElse')
                set_outcome_value = qti.new_tag('setOutcomeValue')
                set_outcome_value['identifier'] = 'FEEDBACKBASIC'
                base_value = qti.new_tag('baseValue')
                base_value['baseType'] = 'identifier'
                base_value.string = 'incorrect'
                set_outcome_value.append(base_value)
                response_else.append(set_outcome_value)

                response_condition.append(response_if)
                response_condition.append(response_else_if)
                response_condition.append(response_else)
                response_processing.append(response_condition)
                item.append(response_processing)
        elif str(self.my_osid_object.genus_type) in [str(UPLOAD_INTERACTION_AUDIO_GENUS),
                                                     str(UPLOAD_INTERACTION_AUDIO_GENUS)]:

            # TODO: this is a big assumption...that only one correct answer exists?
            try:
                correct_answer = next(self.my_osid_object.get_answers())
            except StopIteration:
                # no correct answers
                pass
            else:
                response = qti.new_tag('responseDeclaration')
                response['identifier'] = 'RESPONSE_1'
                response['cardinality'] = 'single'
                response['baseType'] = 'file'

                item.append(response)
        elif str(self.my_osid_object.genus_type) in [str(ORDER_INTERACTION_MW_SENTENCE_GENUS),
                                                     str(ORDER_INTERACTION_MW_SANDBOX_GENUS),
                                                     str(ORDER_INTERACTION_OBJECT_MANIPULATION_GENUS)]:
            response = qti.new_tag('responseDeclaration')
            response['identifier'] = 'RESPONSE_1'
            response['cardinality'] = 'ordered'
            response['baseType'] = 'identifier'
            correct_response = qti.new_tag('correctResponse')
            append_response = False
            if str(self.my_osid_object.genus_type) != str(ORDER_INTERACTION_MW_SANDBOX_GENUS):
                try:
                    correct_answer = next(self.my_osid_object.get_answers())
                except StopIteration:
                    pass
                else:
                    append_response = True
                    for choice_id in correct_answer.get_choice_ids():
                        value = qti.new_tag('value')
                        value.string = str(choice_id)
                        correct_response.append(value)
            if str(self.my_osid_object.genus_type) == str(ORDER_INTERACTION_MW_SANDBOX_GENUS):
                append_response = True

            response.append(correct_response)
            if append_response:
                item.append(response)
        elif str(self.my_osid_object.genus_type) == str(EXTENDED_TEXT_INTERACTION_GENUS):
            response = qti.new_tag('responseDeclaration')
            response['identifier'] = 'RESPONSE_1'
            response['cardinality'] = 'single'
            response['baseType'] = 'string'
            item.append(response)
        elif str(self.my_osid_object.genus_type) == str(INLINE_CHOICE_MW_FITB_INTERACTION_GENUS):
            for answer in self.my_osid_object.get_answers():
                if str(answer.genus_type) == str(RIGHT_ANSWER_GENUS):
                    for response_id, data in answer.get_inline_choice_ids().items():
                        response = qti.new_tag('responseDeclaration')
                        response['identifier'] = response_id
                        response['cardinality'] = 'single'
                        response['baseType'] = 'identifier'
                        correct_response = qti.new_tag('correctResponse')

                        # should only have one choice per answer, for inline choice
                        for choice_id in data['choiceIds']:
                            value = qti.new_tag('value')
                            value.string = str(choice_id)
                            correct_response.append(value)
                        response.append(correct_response)
                        item.append(response)
        elif str(self.my_osid_object.genus_type) == str(NUMERIC_RESPONSE_GENUS):
            response = qti.new_tag('responseDeclaration')
            response['identifier'] = 'RESPONSE_1'
            response['cardinality'] = 'single'
            response['baseType'] = 'float'

            correct_response = qti.new_tag('correctResponse')
            correct_value = qti.new_tag('value')
            correct_value.string = '0'
            correct_response.append(correct_value)
            response.append(correct_response)

            item.append(response)
        else:
            pass

        return qti.prettify()


class QTIItemFormRecord(osid_records.OsidRecord):
    """A record for an ``ItemForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form

    def load_from_qti_item(self, qti_item, keywords=()):
        my_qti_record_identifiers = [Id(i).get_identifier()
                                     for i in self.my_osid_object_form._my_map['recordTypeIds']
                                     if Id(i).get_identifier() == 'qti']
        if len(my_qti_record_identifiers) > 1:
            raise IllegalState('Can not load QTI item more than once')
        soup = BeautifulSoup(qti_item, 'xml')

        if soup.itemBody.choiceInteraction:
            if len(keywords) > 0 and 'mcreflect' in [k.lower() for k in keywords]:
                if soup.itemBody.choiceInteraction['maxChoices'] == '0':
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_MULTI_SELECT_SURVEY_GENUS)
                else:
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_SURVEY_GENUS)
            else:
                if soup.itemBody.choiceInteraction['maxChoices'] == '1':
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_GENUS)
                else:
                    self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_MULTI_GENUS)
            if ('shuffle' not in soup.itemBody.choiceInteraction.attrs or
                    json.loads(soup.itemBody.choiceInteraction['shuffle'])):
                self.my_osid_object_form.get_item_form_record(RANDOMIZED_MULTI_CHOICE_ITEM_RECORD)
        elif soup.itemBody.uploadInteraction:
            # now check the keywords for the specific upload type
            # out of band agreement
            if len(keywords) > 0 and 'audiort' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(UPLOAD_INTERACTION_AUDIO_GENUS)
            else:
                self.my_osid_object_form.set_genus_type(UPLOAD_INTERACTION_GENERIC_GENUS)
        elif soup.itemBody.orderInteraction:
            if len(keywords) > 0 and 'mwsentence' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_MW_SENTENCE_GENUS)
            elif len(keywords) > 0 and 'mwsandbox' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_MW_SANDBOX_GENUS)
            elif len(keywords) > 0 and 'objmsequence' in [k.lower() for k in keywords]:
                self.my_osid_object_form.set_genus_type(ORDER_INTERACTION_OBJECT_MANIPULATION_GENUS)

            if ('shuffle' not in soup.itemBody.orderInteraction.attrs or
                    json.loads(soup.itemBody.orderInteraction['shuffle'])):
                self.my_osid_object_form.get_item_form_record(RANDOMIZED_MULTI_CHOICE_ITEM_RECORD)
        elif soup.itemBody.extendedTextInteraction:
            self.my_osid_object_form.set_genus_type(EXTENDED_TEXT_INTERACTION_GENUS)
        elif soup.itemBody.inlineChoiceInteraction:
            self.my_osid_object_form.set_genus_type(INLINE_CHOICE_MW_FITB_INTERACTION_GENUS)

            # need to always add this
            self.my_osid_object_form.get_item_form_record(INLINE_CHOICE_ITEM_RECORD)
        elif soup.itemBody.textEntryInteraction and soup.templateDeclaration:
            self.my_osid_object_form.set_genus_type(NUMERIC_RESPONSE_GENUS)
            self.my_osid_object_form.get_item_form_record(NUMERIC_RESPONSE_RECORD)
        else:
            raise OperationFailed('Item type not supported or unrecognized')


class QTIAssessmentRecord(ObjectInitRecord):
    """A record for an ``Assessment``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def get_qti_xml(self, media_file_root_path=''):
        qti = BeautifulSoup(
            self.my_osid_object.get_question().get_qti_xml(
                media_file_root_path=media_file_root_path),
            'xml')
        item = qti.assessmentItem

        if str(self.my_osid_object.genus_type) == str(CHOICE_INTERACTION_GENUS):

            # TODO: this is a big assumption...that only one correct answer exists?
            correct_answer = next(self.my_osid_object.get_answers())
            response = qti.new_tag('responseDeclaration')
            response['identifier'] = 'RESPONSE_1'
            response['cardinality'] = 'single'
            response['baseType'] = 'identifier'

            correct_response = qti.new_tag('correctResponse')
            value = qti.new_tag('value')
            value.string = correct_answer.object_map['choiceIds'][0]
            correct_response.append(value)
            response.append(correct_response)

            item.append(response)

            # responseProcessing
            response_processing = qti.new_tag('responseProcessing')
            response_condition = qti.new_tag('responseCondition')
            response_if = qti.new_tag('responseIf')
            is_null = qti.new_tag('isNull')
            variable = qti.new_tag('variable')
            variable['identifier'] = 'RESPONSE_1'
            is_null.append(variable)
            response_if.append(is_null)
            set_outcome_value = qti.new_tag('setOutcomeValue')
            set_outcome_value['identifier'] = 'FEEDBACKBASIC'
            base_value = qti.new_tag('baseValue')
            base_value['baseType'] = 'identifier'
            base_value.string = 'empty'
            set_outcome_value.append(base_value)
            response_if.append(set_outcome_value)

            response_else_if = qti.new_tag('responseElseIf')
            match = qti.new_tag('match')
            variable = qti.new_tag('variable')
            variable['identifier'] = 'RESPONSE_1'
            match.append(variable)
            response_else_if.append(match)
            set_outcome_value = qti.new_tag('setOutcomeValue')
            set_outcome_value['identifier'] = 'SCORE'
            sum = qti.new_tag('sum')
            for var in ['SCORE', 'MAXSCORE']:
                variable = qti.new_tag('variable')
                variable['identifier'] = var
                sum.append(variable)
            set_outcome_value.append(sum)
            response_else_if.append(set_outcome_value)
            set_outcome_value = qti.new_tag('setOutcomeValue')
            set_outcome_value['identifier'] = 'FEEDBACKBASIC'
            base_value = qti.new_tag('baseValue')
            base_value['baseType'] = 'identifier'
            base_value.string = 'correct'
            set_outcome_value.append(base_value)
            response_else_if.append(set_outcome_value)

            response_else = qti.new_tag('responseElse')
            set_outcome_value = qti.new_tag('setOutcomeValue')
            set_outcome_value['identifier'] = 'FEEDBACKBASIC'
            base_value = qti.new_tag('baseValue')
            base_value['baseType'] = 'identifier'
            base_value.string = 'incorrect'
            set_outcome_value.append(base_value)
            response_else.append(set_outcome_value)

            response_condition.append(response_if)
            response_condition.append(response_else_if)
            response_condition.append(response_else)
            response_processing.append(response_condition)
            item.append(response_processing)
        else:
            pass

        return qti.prettify()


class QTIAssessmentFormRecord(osid_records.OsidRecord):
    """A record for an ``AssessmentForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'qti'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form

    def load_from_qti_assessment(self, qti_assessment):
        my_qti_record_identifiers = [Id(i).get_identifier()
                                     for i in self.my_osid_object_form._my_map['recordTypeIds']
                                     if Id(i).get_identifier() == 'qti']
        if len(my_qti_record_identifiers) > 1:
            raise IllegalState('Can not load QTI item more than once')
        soup = BeautifulSoup(qti_assessment, 'xml')

        if soup.itemBody.choiceInteraction:
            self.my_osid_object_form.set_genus_type(CHOICE_INTERACTION_GENUS)
        else:
            raise OperationFailed('Item type not supported or unrecognized')
