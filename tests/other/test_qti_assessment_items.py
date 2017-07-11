"""Unit tests of QTI item type functionality."""


import unittest
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime import Runtime
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type

REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)


QTI_TEST_ITEM = """<?xml version="1.0" encoding="UTF-8"?>
<assessmentItem xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1p1.xsd http://www.w3.org/1998/Math/MathML http://www.w3.org/Math/XMLSchema/mathml2/mathml2.xsd" identifier="idee9de674-4216-4300-b514-cf891e9a90c4" title="Jeff Test Question" adaptive="false" timeDependent="false">
    <responseDeclaration identifier="RESPONSE_1" cardinality="single" baseType="identifier">
        <correctResponse>
            <value>id9338b0ad-2bfe-45f2-9b8e-357f5cd10732</value>
        </correctResponse>
    </responseDeclaration>
    <outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">
        <defaultValue>
            <value>0</value>
        </defaultValue>
    </outcomeDeclaration>
    <outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">
        <defaultValue>
            <value>1</value>
        </defaultValue>
    </outcomeDeclaration>
    <outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier">
        <defaultValue>
            <value>empty</value>
        </defaultValue>
    </outcomeDeclaration>
    <outcomeDeclaration identifier="MINSCORE" cardinality="single" baseType="float" view="testConstructor">
        <defaultValue>
            <value>0</value>
        </defaultValue>
    </outcomeDeclaration>
    <itemBody>
        <p>What color is the sky?</p>
        <choiceInteraction responseIdentifier="RESPONSE_1" shuffle="true" maxChoices="1">
            <simpleChoice identifier="id9338b0ad-2bfe-45f2-9b8e-357f5cd10732">
                <p>Blue</p>
            </simpleChoice>
            <simpleChoice identifier="id7900c5e3-455b-480d-b84e-0a5e709ca0f3">
                <p>Brown</p>
            </simpleChoice>
            <simpleChoice identifier="idaea7bf89-d7f6-4992-931d-df43cfb74efd">
                <p>Red</p>
            </simpleChoice>
            <simpleChoice identifier="idac4ef710-cfca-41a9-a664-212bb313b825">
                <p>Purple</p>
            </simpleChoice>
        </choiceInteraction>
    </itemBody>
    <responseProcessing>
        <responseCondition>
            <responseIf>
                <isNull>
                    <variable identifier="RESPONSE_1"/>
                </isNull>
                <setOutcomeValue identifier="FEEDBACKBASIC">
                    <baseValue baseType="identifier">empty</baseValue>
                </setOutcomeValue>
            </responseIf>
            <responseElseIf>
                <match>
                    <variable identifier="RESPONSE_1"/>
                    <correct identifier="RESPONSE_1"/>
                </match>
                <setOutcomeValue identifier="SCORE">
                    <sum>
                        <variable identifier="SCORE"/>
                        <variable identifier="MAXSCORE"/>
                    </sum>
                </setOutcomeValue>
                <setOutcomeValue identifier="FEEDBACKBASIC">
                    <baseValue baseType="identifier">correct</baseValue>
                </setOutcomeValue>
            </responseElseIf>
            <responseElse>
                <setOutcomeValue identifier="FEEDBACKBASIC">
                    <baseValue baseType="identifier">incorrect</baseValue>
                </setOutcomeValue>
            </responseElse>
        </responseCondition>
        <responseCondition>
            <responseIf>
                <gt>
                    <variable identifier="SCORE"/>
                    <variable identifier="MAXSCORE"/>
                </gt>
                <setOutcomeValue identifier="SCORE">
                    <variable identifier="MAXSCORE"/>
                </setOutcomeValue>
            </responseIf>
        </responseCondition>
        <responseCondition>
            <responseIf>
                <lt>
                    <variable identifier="SCORE"/>
                    <variable identifier="MINSCORE"/>
                </lt>
                <setOutcomeValue identifier="SCORE">
                    <variable identifier="MINSCORE"/>
                </setOutcomeValue>
            </responseIf>
        </responseCondition>
    </responseProcessing>
</assessmentItem>
"""

QTI_QUESTION_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'question-record-type',
    'identifier': 'qti',
})

QTI_ANSWER_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'answer-record-type',
    'identifier': 'qti',
})

FEEDBACK_ANSWER_RECORD = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'answer-record-type',
    'identifier': 'answer-with-feedback',
})


class TestQTILoading(unittest.TestCase):
    """Tests qti item records"""

    @classmethod
    def setUpClass(cls):
        # cls.asset_list = list()
        # cls.asset_ids = list()
        cls.assess_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.assess_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for QTI Item tests'
        cls.bank = cls.assess_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for bank in cls.assess_mgr.get_banks():
            for obj in bank.get_items():
                bank.delete_item(obj.ident)
            cls.assess_mgr.delete_bank(bank.ident)

    def test_create_item_with_qti(self):
        """Tests creating an item loaded from a qti document"""
        create_form = self.bank.get_item_form_for_create([])
        create_form.display_name = "QTI Test Item"
        create_form.description = "Item for testing QTI loading"
        test_item = self.bank.create_item(create_form)
        create_form = self.bank.get_question_form_for_create(
            test_item.ident,
            [QTI_QUESTION_RECORD])
        create_form.load_from_qti_item(QTI_TEST_ITEM)
        self.bank.create_question(create_form)
        create_form = self.bank.get_answer_form_for_create(
            test_item.ident,
            [QTI_ANSWER_RECORD, FEEDBACK_ANSWER_RECORD])
        create_form.load_from_qti_item(QTI_TEST_ITEM)
        self.bank.create_answer(create_form)
