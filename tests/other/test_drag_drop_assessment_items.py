"""Unit tests of drag and drop assessment item functionality."""

import unittest

from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime import Runtime
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate
from dlkit.primordium.mapping.spatial_units import RectangularSpatialUnit
from dlkit.primordium.locale.types import language, format, script

REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DRAG_DROP_ITEM_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'item-record-type',
    'identifier': 'drag-and-drop',
})

MULTI_LANG_DRAG_DROP_QUESTION_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'question-record-type',
    'identifier': 'multi-language-drag-and-drop',
})

DRAG_AND_DROP_ANSWER_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'answer-record-type',
    'identifier': 'drag-and-drop',
})


def get_display_text(text, language_code='ENG', format_code='PLAIN', script_code='LATN'):
    return DisplayText(
        **{'text': text,
           'language_type': Type(**language.get_type_data(language_code)),
           'format_type': Type(**format.get_type_data(format_code)),
           'script_type': Type(**script.get_type_data(script_code))})


class TestDragDropAuthoring(unittest.TestCase):
    """Tests qti item records"""

    @classmethod
    def setUpClass(cls):
        # cls.asset_list = list()
        # cls.asset_ids = list()
        cls.assess_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.assess_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for Drag and Drop Item tests'
        cls.bank = cls.assess_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for bank in cls.assess_mgr.get_banks():
            for obj in bank.get_items():
                bank.delete_item(obj.ident)
            cls.assess_mgr.delete_bank(bank.ident)

    def test_drag_drop_item(self):
        """Tests creating a Drag and Drop Item"""
        create_form = self.bank.get_item_form_for_create([DRAG_DROP_ITEM_RECORD])
        create_form.display_name = "Drag and Drop Test Item"
        create_form.description = "Item for testing Drag and Drop"
        test_item = self.bank.create_item(create_form)

        create_form = self.bank.get_question_form_for_create(test_item.ident, [MULTI_LANG_DRAG_DROP_QUESTION_RECORD])
        droppable_1 = create_form.add_droppable(get_display_text('This is a Droppable'), 'Droppable 1')
        droppable_2 = create_form.add_droppable(get_display_text('This is another Droppable'), 'Droppable 2')
        droppable_3 = create_form.add_droppable(get_display_text('This is an unused Droppable'), 'Droppable 3')
        target = create_form.add_target(get_display_text('This is the Target'))
        corner_coordinate_10 = BasicCoordinate([10, 10])
        corner_coordinate_12 = BasicCoordinate([20, 20])
        corner_coordinate_20 = BasicCoordinate([50, 50])
        corner_coordinate_22 = BasicCoordinate([70, 70])
        corner_coordinate_30 = BasicCoordinate([68, 68])
        spatial_unit_1 = RectangularSpatialUnit(coordinate=corner_coordinate_10, width=10, height=10)
        spatial_unit_2 = RectangularSpatialUnit(coordinate=corner_coordinate_20, width=20, height=20)
        zone_A = create_form.add_zone(
            spatial_unit_1,
            target['id'],
            'Zone A')
        zone_B = create_form.add_zone(
            spatial_unit_2,
            target['id'],
            'Zone B')
        question = self.bank.create_question(create_form)
        # print question.object_map
        # print zone_A

        create_form = self.bank.get_answer_form_for_create(test_item.ident, [DRAG_AND_DROP_ANSWER_RECORD])
        create_form.add_zone_condition(droppable_1['id'], zone_A['id'])
        create_form.add_zone_condition(droppable_2['id'], zone_B['id'])
        correct_answer = self.bank.create_answer(create_form)
        # print correct_answer.object_map
        test_item = self.bank.get_item(test_item.ident)

        create_form = self.bank.get_item_form_for_create([DRAG_DROP_ITEM_RECORD])
        create_form.display_name = "Drag and Drop Item for Testing Response"
        create_form.description = "Item for testing Drag and Drop Response Evaluation"
        response_item = self.bank.create_item(create_form)

        # Create correct answer for response testing
        create_form = self.bank.get_answer_form_for_create(response_item.ident, [DRAG_AND_DROP_ANSWER_RECORD])
        create_form.add_coordinate_condition(droppable_1['id'], target['id'], BasicCoordinate([11, 18]))
        create_form.add_coordinate_condition(droppable_2['id'], target['id'], BasicCoordinate([55, 60]))
        correct_response = self.bank.create_answer(create_form)

        # Create incorrect answers for response testing
        create_form = self.bank.get_answer_form_for_create(response_item.ident, [DRAG_AND_DROP_ANSWER_RECORD])
        create_form.add_coordinate_condition(droppable_1['id'], target['id'], BasicCoordinate([10, 18]))
        incorrect_response_1 = self.bank.create_answer(create_form)

        create_form = self.bank.get_answer_form_for_create(response_item.ident, [DRAG_AND_DROP_ANSWER_RECORD])
        create_form.add_coordinate_condition(droppable_3['id'], target['id'], BasicCoordinate([12, 18]))
        incorrect_response_2 = self.bank.create_answer(create_form)

        create_form = self.bank.get_answer_form_for_create(response_item.ident, [DRAG_AND_DROP_ANSWER_RECORD])
        create_form.add_coordinate_condition(droppable_1['id'], target['id'], BasicCoordinate([11, 18]))
        create_form.add_coordinate_condition(droppable_2['id'], target['id'], BasicCoordinate([55, 60]))
        create_form.add_coordinate_condition(droppable_3['id'], target['id'], BasicCoordinate([12, 18]))
        incorrect_response_3 = self.bank.create_answer(create_form)

        response_item = self.bank.get_item(response_item.ident)

        assert BasicCoordinate([11, 18]) in spatial_unit_1
        assert BasicCoordinate([55, 60]) in spatial_unit_2

        assert test_item.is_response_correct(correct_response)
        assert not test_item.is_response_correct(incorrect_response_1)
        assert not test_item.is_response_correct(incorrect_response_2)
        assert not test_item.is_response_correct(incorrect_response_3)
