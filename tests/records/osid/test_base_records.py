"""Unit tests of osid base_records."""

import datetime
import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.transport.objects import DataInputStream
from dlkit.records.osid.base_records import *

from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.metadata import Metadata
from dlkit.runtime import configs
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))

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


def get_repository_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('REPOSITORY',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


class TestProvenanceFormRecord(unittest.TestCase):
    """Tests for ProvenanceFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_provenance(self):
        """Tests set_provenance"""
        form = ProvenanceFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         '')
        form.set_provenance('foo')
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         'foo')

    def test_cannot_send_non_string(self):
        form = ProvenanceFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_provenance(123)

    def test_can_update_provenance(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['provenanceId'] = 'test1'
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = ProvenanceFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         'test1')
        form.set_provenance('test2')
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         'test2')

    def test_can_clear_provenance(self):
        form = ProvenanceFormRecord(self.osid_object_form)
        form.set_provenance('foo')
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         'foo')
        form.clear_provenance()
        self.assertEqual(form.my_osid_object_form._my_map['provenanceId'],
                         '')

    def test_can_get_provenance_metadata(self):
        form = ProvenanceFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_provenance_metadata(), Metadata))


class TestProvenanceRecord(unittest.TestCase):
    """Tests for ProvenanceRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['creatorId'] = 'foo%3Acreator%40ODL.MIT.EDU'
        cls.now = datetime.datetime.utcnow()
        obj_map['creationTime'] = cls.now
        obj_map['provenanceId'] = 'provenance'
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.provenance_object = ProvenanceRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_creator_id(self):
        self.assertTrue(isinstance(self.provenance_object.creator_id, Id))
        self.assertEqual(str(self.provenance_object.creator_id),
                         'foo%3Acreator%40ODL.MIT.EDU')

    def test_can_get_creation_time(self):
        creation_time = self.provenance_object.create_time
        properties = ['year', 'month', 'day', 'hour',
                      'minute', 'second', 'microsecond']
        for prop in properties:
            self.assertEqual(getattr(self.now, prop),
                             getattr(creation_time, prop))

    def test_can_get_provider_id(self):
        self.assertEqual(self.provenance_object.provenance, 'provenance')

    def test_can_check_provenance(self):
        self.assertTrue(self.provenance_object.has_provenance())

    def test_getting_provenance_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['creatorId'] = 'creator'
        obj_map['creationTime'] = datetime.datetime.utcnow()
        obj_map['provenanceId'] = ''
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        provenance_object = ProvenanceRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            provenance_object.provenance


class TestResourceFormRecord(unittest.TestCase):
    """Tests for ResourceFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_resource_id(self):
        """Tests set_resource_id"""
        form = ResourceFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['resourceId'],
                         '')
        form.set_resource_id(Id('foo%3Afoo%40foo'))
        self.assertEqual(str(form.my_osid_object_form._my_map['resourceId']),
                         'foo%3Afoo%40foo')

    def test_cannot_send_none_as_resource_id(self):
        form = ResourceFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_resource_id()

    def test_cannot_send_non_id_as_resource_id(self):
        form = ResourceFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_resource_id('foo%3Afoo%40foo')

    def test_can_update_resource_id(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['resourceId'] = 'test1%3Atest1%40test1'
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = ResourceFormRecord(osid_object_form)
        self.assertEqual(str(form.my_osid_object_form._my_map['resourceId']),
                         'test1%3Atest1%40test1')
        form.set_resource_id(Id('test2%3Atest2%40test2'))
        self.assertEqual(str(form.my_osid_object_form._my_map['resourceId']),
                         'test2%3Atest2%40test2')

    def test_can_clear_resource_id(self):
        form = ResourceFormRecord(self.osid_object_form)
        form.set_resource_id(Id('foo%3Afoo%40foo'))
        self.assertEqual(str(form.my_osid_object_form._my_map['resourceId']),
                         'foo%3Afoo%40foo')
        form.clear_resource_id()
        self.assertEqual(form.my_osid_object_form._my_map['resourceId'],
                         '')

    def test_can_get_resource_id_metadata(self):
        form = ResourceFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_resource_id_metadata(), Metadata))


class TestResourceIdRecord(unittest.TestCase):
    """Tests for ResourceIdRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['resourceId'] = 'foo%3Aresource%40ODL.MIT.EDU'
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.resource_id_object = ResourceIdRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_resource_id(self):
        self.assertTrue(isinstance(self.resource_id_object.resource_id, Id))
        self.assertEqual(str(self.resource_id_object.resource_id),
                         'foo%3Aresource%40ODL.MIT.EDU')

    def test_can_check_resource_id(self):
        self.assertTrue(self.resource_id_object.has_resource_id())

    def test_getting_resource_id_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['resourceId'] = ''
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        resource_id_object = ResourceIdRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            resource_id_object.resource_id


class TestTextFormRecord(unittest.TestCase):
    """Tests for TextFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_text(self):
        """Tests set_text"""
        form = TextFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         '')
        form.set_text('foo')
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         'foo')

    def test_cannot_send_none_as_text(self):
        form = TextFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_text()

    def test_cannot_send_non_string(self):
        form = TextFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_text(123)

    def test_can_update_text(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': 'test1'
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = TextFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         'test1')
        form.set_text('test2')
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         'test2')

    def test_can_clear_text(self):
        form = TextFormRecord(self.osid_object_form)
        form.set_text('foo')
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         'foo')
        form.clear_text()
        self.assertEqual(form.my_osid_object_form._my_map['text']['text'],
                         '')

    def test_can_get_text_metadata(self):
        form = TextFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_text_metadata(), Metadata))


class TestTextRecord(unittest.TestCase):
    """Tests for TextRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': 'silly',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.text_object = TextRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_text(self):
        self.assertTrue(isinstance(self.text_object.text, DisplayText))
        self.assertEqual(self.text_object.text.text,
                         'silly')

    def test_can_check_text(self):
        self.assertTrue(self.text_object.has_text())

    def test_getting_text_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': '',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        text_object = TextRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            text_object.text


class TestIntegerValueFormRecord(unittest.TestCase):
    """Tests for IntegerValueFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_integer_value(self):
        """Tests set_integer_value"""
        form = IntegerValueFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         None)
        form.set_integer_value(-1)
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         -1)

    def test_cannot_send_none(self):
        form = IntegerValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_integer_value()

    def test_cannot_send_non_integer(self):
        form = IntegerValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_integer_value('1')

    def test_can_update_integer_value(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValue'] = 29
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = IntegerValueFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         29)
        form.set_integer_value(21)
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         21)

    def test_can_clear_integer_value(self):
        form = IntegerValueFormRecord(self.osid_object_form)
        form.set_integer_value(23)
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         23)
        form.clear_integer_value()
        self.assertEqual(form.my_osid_object_form._my_map['integerValue'],
                         None)

    def test_can_get_integer_metadata(self):
        form = IntegerValueFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_integer_value_metadata(), Metadata))


class TestIntegerValueRecord(unittest.TestCase):
    """Tests for IntegerValueRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValue'] = 42
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.integer_object = IntegerValueRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_integer_value(self):
        self.assertTrue(isinstance(self.integer_object.integer, int))
        self.assertEqual(self.integer_object.integer,
                         42)

    def test_can_check_integer(self):
        self.assertTrue(self.integer_object.has_integer())

    def test_getting_integer_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        integer_object = IntegerValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            integer_object.integer

    def test_zero_returns_as_valid_integer(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValue'] = 0
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        integer_object = IntegerValueRecord(osid_object)
        self.assertTrue(self.integer_object.has_integer())


class TestDecimalValueFormRecord(unittest.TestCase):
    """Tests for DecimalValueFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_decimal_value(self):
        """Tests set_decimal_value"""
        form = DecimalValueFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         None)
        form.set_decimal_value(-1.1)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         -1.1)

    def test_cannot_send_none(self):
        form = DecimalValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_decimal_value()

    def test_cannot_send_non_decimal(self):
        form = DecimalValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_decimal_value(1)

    def test_can_update_decimal_value(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValue'] = 29.25
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = DecimalValueFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         29.25)
        form.set_decimal_value(21.3)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         21.3)

    def test_can_clear_decimal_value(self):
        form = DecimalValueFormRecord(self.osid_object_form)
        form.set_decimal_value(23.4)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         23.4)
        form.clear_decimal_value()
        self.assertEqual(form.my_osid_object_form._my_map['decimalValue'],
                         None)

    def test_can_get_decimal_metadata(self):
        form = DecimalValueFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_decimal_value_metadata(), Metadata))


class TestDecimalValueRecord(unittest.TestCase):
    """Tests for DecimalValueRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValue'] = 42.12
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.decimal_object = DecimalValueRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_decimal_value(self):
        self.assertTrue(isinstance(self.decimal_object.decimal, float))
        self.assertEqual(self.decimal_object.decimal,
                         42.12)

    def test_can_check_decimal(self):
        self.assertTrue(self.decimal_object.has_decimal())

    def test_getting_decimal_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        decimal_object = DecimalValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            decimal_object.decimal

    def test_zero_returns_as_valid_decimal(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValue'] = 0.0
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        decimal_object = DecimalValueRecord(osid_object)
        self.assertTrue(self.decimal_object.has_decimal())


class TestTextsFormRecord(unittest.TestCase):
    """Tests for TextsFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_text_with_string(self):
        """Tests set_text"""
        form = TextsFormRecord(self.osid_object_form)
        self.assertNotIn('foo', form.my_osid_object_form._my_map['texts'])
        form.add_text('bar', label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bar')

    def test_can_set_text_with_display_text(self):
        """Tests set_text"""
        form = TextsFormRecord(self.osid_object_form)
        self.assertNotIn('foo', form.my_osid_object_form._my_map['texts'])
        display_text = DisplayText(display_text_map={
            'text': 'bar',
            'languageTypeId': '639-2%3AHIN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ADEVA%40ISO'
        })
        form.add_text(display_text, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bar')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['languageTypeId'],
                         str(display_text.language_type))
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['scriptTypeId'],
                         str(display_text.script_type))

    def test_label_generated_if_not_provided(self):
        form = TextsFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['texts'], {})
        form.add_text('bar')
        self.assertEqual(len(form.my_osid_object_form._my_map['texts'].keys()), 1)
        label = form.my_osid_object_form._my_map['texts'].keys()[0]
        self.assertEqual(len(label), 24)
        self.assertEqual(form.my_osid_object_form._my_map['texts'][label]['text'],
                         'bar')

    def test_can_add_multiple_labels(self):
        form = TextsFormRecord(self.osid_object_form)
        form.add_text('bink', label='foo')
        form.add_text('zing', label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bink')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['bonk']['text'],
                         'zing')

    def test_cannot_add_label_with_period(self):
        form = TextsFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_text('boo', label='1.23')

    def test_cannot_send_none(self):
        form = TextsFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_text(None, label='foo')

    def test_cannot_send_non_string_non_display_text(self):
        form = TextsFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_text(1, label='foo')

    def test_can_update_text(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['texts'] = {
            'foo': {
                'text': 'bar',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = TextsFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bar')
        form.add_text('bim', label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bim')

    def test_can_clear_texts(self):
        form = TextsFormRecord(self.osid_object_form)
        form.add_text('bink', label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bink')
        form.clear_texts()
        self.assertEqual(form.my_osid_object_form._my_map['texts'], {})

    def test_can_clear_text(self):
        form = TextsFormRecord(self.osid_object_form)
        form.add_text('bink', label='foo')
        form.add_text('zing', label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['foo']['text'],
                         'bink')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['bonk']['text'],
                         'zing')
        form.clear_text('foo')
        self.assertNotIn('foo', form.my_osid_object_form._my_map['texts'])
        self.assertEqual(form.my_osid_object_form._my_map['texts']['bonk']['text'],
                         'zing')

    def test_clearing_non_existent_label_throws_exception(self):
        form = TextsFormRecord(self.osid_object_form)
        form.add_text('bink', label='foo')
        with self.assertRaises(errors.NotFound):
            form.clear_text('zoom')

    def test_can_get_texts_metadata(self):
        form = TextsFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_texts_metadata(), Metadata))

    def test_can_get_text_metadata(self):
        form = TextsFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_text_metadata(), Metadata))

    def test_can_get_label_metadata(self):
        form = TextsFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_label_metadata(), Metadata))


class TestTextsRecord(unittest.TestCase):
    """Tests for TextsRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['texts'] = {
            'foo': {
                'text': 'bar',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.texts_object = TextsRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_texts_map(self):
        texts_map = self.texts_object.texts_map
        self.assertTrue(isinstance(texts_map, dict))
        self.assertEqual(texts_map, {
            'foo': {
                'text': 'bar',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        })

    def test_can_get_text_value(self):
        self.assertTrue(isinstance(self.texts_object.get_text('foo'),
                                   DisplayText))
        self.assertEqual(self.texts_object.get_text('foo').text,
                         'bar')

    def test_can_check_texts(self):
        self.assertTrue(self.texts_object.has_texts())

    def test_can_check_text(self):
        self.assertTrue(self.texts_object.has_text('foo'))

    def test_getting_text_map_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        texts_object = TextsRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            texts_object.texts_map

    def test_getting_non_existent_label_throws_exception(self):
        with self.assertRaises(errors.IllegalState):
            self.texts_object.get_text('bim')


class TestIntegerValuesFormRecord(unittest.TestCase):
    """Tests for IntegerValuesFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_integer_value(self):
        """Tests set_integer_value"""
        form = IntegerValuesFormRecord(self.osid_object_form)
        self.assertNotIn('foo', form.my_osid_object_form._my_map['integerValues'])
        form.add_integer_value(0, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         0)

    def test_label_generated_if_not_provided(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['integerValues'], {})
        form.add_integer_value(23)
        self.assertEqual(len(form.my_osid_object_form._my_map['integerValues'].keys()), 1)
        label = form.my_osid_object_form._my_map['integerValues'].keys()[0]
        self.assertEqual(len(label), 24)
        self.assertEqual(form.my_osid_object_form._my_map['integerValues'][label],
                         23)

    def test_can_add_multiple_labels(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        form.add_integer_value(123, label='foo')
        form.add_integer_value(321, label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         123)
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['bonk'],
                         321)

    def test_cannot_add_label_with_period(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_integer_value('boo', label='1.23')

    def test_cannot_send_none(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_integer_value(None, label='foo')

    def test_cannot_send_non_integer(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_integer_value(1.1, label='foo')

    def test_can_update_integer(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValues'] = {
            'foo': 0
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = IntegerValuesFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         0)
        form.add_integer_value(-1, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         -1)

    def test_can_clear_integer_values(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        form.add_integer_value(0, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         0)
        form.clear_integer_values()
        self.assertEqual(form.my_osid_object_form._my_map['integerValues'], {})

    def test_can_clear_integer_value(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        form.add_integer_value(0, label='foo')
        form.add_integer_value(23, label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['foo'],
                         0)
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['bonk'],
                         23)
        form.clear_integer_value('foo')
        self.assertNotIn('foo', form.my_osid_object_form._my_map['integerValues'])
        self.assertEqual(form.my_osid_object_form._my_map['integerValues']['bonk'],
                         23)

    def test_clearing_non_existent_label_throws_exception(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        form.add_integer_value(123, label='foo')
        with self.assertRaises(errors.NotFound):
            form.clear_integer_value('zoom')

    def test_can_get_integer_values_metadata(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_integer_values_metadata(), Metadata))

    def test_can_get_integer_value_metadata(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_integer_value_metadata(), Metadata))

    def test_can_get_label_metadata(self):
        form = IntegerValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_label_metadata(), Metadata))


class TestIntegerValuesRecord(unittest.TestCase):
    """Tests for IntegerValuesRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValues'] = {
            'foo': 123
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.integer_values_object = IntegerValuesRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_integer_values_map(self):
        integer_values_map = self.integer_values_object.integer_values_map
        self.assertTrue(isinstance(integer_values_map, dict))
        self.assertEqual(integer_values_map, {
            'foo': 123
        })

    def test_can_get_integer_value(self):
        self.assertTrue(isinstance(self.integer_values_object.get_integer_value('foo'),
                                   int))
        self.assertEqual(self.integer_values_object.get_integer_value('foo'),
                         123)

    def test_can_check_integer_values(self):
        self.assertTrue(self.integer_values_object.has_integer_values())

    def test_can_check_integer_value(self):
        self.assertTrue(self.integer_values_object.has_integer_value('foo'))

    def test_getting_integer_values_map_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['integerValues'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        integer_values_object = IntegerValuesRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            integer_values_object.integer_values_map

    def test_getting_non_existent_label_throws_exception(self):
        with self.assertRaises(errors.IllegalState):
            self.integer_values_object.get_integer_value('bim')


class TestDecimalValuesFormRecord(unittest.TestCase):
    """Tests for DecimalValuesFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_decimal_value(self):
        """Tests set_decimal_value"""
        form = DecimalValuesFormRecord(self.osid_object_form)
        self.assertNotIn('foo', form.my_osid_object_form._my_map['decimalValues'])
        form.add_decimal_value(0.9, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         0.9)

    def test_label_generated_if_not_provided(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues'], {})
        form.add_decimal_value(2.3)
        self.assertEqual(len(form.my_osid_object_form._my_map['decimalValues'].keys()), 1)
        label = form.my_osid_object_form._my_map['decimalValues'].keys()[0]
        self.assertEqual(len(label), 24)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues'][label],
                         2.3)

    def test_can_add_multiple_labels(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        form.add_decimal_value(1.23, label='foo')
        form.add_decimal_value(3.21, label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         1.23)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['bonk'],
                         3.21)

    def test_cannot_add_label_with_period(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_decimal_value(1.1, label='1.23')

    def test_cannot_send_none(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_decimal_value(None, label='foo')

    def test_cannot_send_non_decimal(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_decimal_value(1, label='foo')

    def test_can_update_decimal(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValues'] = {
            'foo': 0.3
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = DecimalValuesFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         0.3)
        form.add_decimal_value(-1.5, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         -1.5)

    def test_can_clear_decimal_values(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        form.add_decimal_value(0.1, label='foo')
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         0.1)
        form.clear_decimal_values()
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues'], {})

    def test_can_clear_decimal_value(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        form.add_decimal_value(1.0, label='foo')
        form.add_decimal_value(-2.3, label='bonk')
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['foo'],
                         1.0)
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['bonk'],
                         -2.3)
        form.clear_decimal_value('foo')
        self.assertNotIn('foo', form.my_osid_object_form._my_map['decimalValues'])
        self.assertEqual(form.my_osid_object_form._my_map['decimalValues']['bonk'],
                         -2.3)

    def test_clearing_non_existent_label_throws_exception(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        form.add_decimal_value(1.23, label='foo')
        with self.assertRaises(errors.NotFound):
            form.clear_decimal_value('zoom')

    def test_can_get_decimal_values_metadata(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_decimal_values_metadata(), Metadata))

    def test_can_get_decimal_value_metadata(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_decimal_value_metadata(), Metadata))

    def test_can_get_label_metadata(self):
        form = DecimalValuesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_label_metadata(), Metadata))


class TestDecimalValuesRecord(unittest.TestCase):
    """Tests for DecimalValuesRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValues'] = {
            'foo': 123.45
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.decimal_values_object = DecimalValuesRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_decimal_values_map(self):
        decimal_values_map = self.decimal_values_object.decimal_values_map
        self.assertTrue(isinstance(decimal_values_map, dict))
        self.assertEqual(decimal_values_map, {
            'foo': 123.45
        })

    def test_can_get_decimal_value(self):
        self.assertTrue(isinstance(self.decimal_values_object.get_decimal_value('foo'),
                                   float))
        self.assertEqual(self.decimal_values_object.get_decimal_value('foo'),
                         123.45)

    def test_can_check_integer_values(self):
        self.assertTrue(self.decimal_values_object.has_decimal_values())

    def test_can_check_integer_value(self):
        self.assertTrue(self.decimal_values_object.has_decimal_value('foo'))

    def test_getting_integer_values_map_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['decimalValues'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        decimal_values_object = DecimalValuesRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            decimal_values_object.decimal_values_map

    def test_getting_non_existent_label_throws_exception(self):
        with self.assertRaises(errors.IllegalState):
            self.decimal_values_object.get_decimal_value('bim')


class TestedXBaseFormRecord(unittest.TestCase):
    """Tests for edXBaseFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_attempts(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertNotEqual(2, form.my_osid_object_form._my_map['attempts'])
        form.add_attempts(2)
        self.assertEqual(form.my_osid_object_form._my_map['attempts'],
                         2)

    def test_can_set_weight(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertNotEqual(2.1, form.my_osid_object_form._my_map['weight'])
        form.add_weight(2.1)
        self.assertEqual(form.my_osid_object_form._my_map['weight'],
                         2.1)

    def test_can_set_showanswer(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertNotEqual('never', form.my_osid_object_form._my_map['showanswer'])
        form.add_showanswer('never')
        self.assertEqual(form.my_osid_object_form._my_map['showanswer'],
                         'never')

    def test_can_set_markdown(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertNotEqual('<what />', form.my_osid_object_form._my_map['markdown'])
        form.add_markdown('<what />')
        self.assertEqual(form.my_osid_object_form._my_map['markdown'],
                         '<what />')

    def test_cannot_send_none_to_attempts(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_attempts(None)

    def test_cannot_send_non_integer_to_attempts(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_attempts(1.0)

    def test_can_update_attempts(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['attempts'] = 3
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = edXBaseFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['attempts'],
                         3)
        form.add_attempts(1)
        self.assertEqual(form.my_osid_object_form._my_map['attempts'],
                         1)

    def test_cannot_send_none_to_weight(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_weight(None)

    def test_cannot_send_non_float_to_weight(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_weight(1)

    def test_can_update_weight(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['weight'] = 1.23
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = edXBaseFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['weight'],
                         1.23)
        form.add_weight(0.15)
        self.assertEqual(form.my_osid_object_form._my_map['weight'],
                         0.15)

    def test_cannot_send_none_to_showanswer(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_showanswer(None)

    def test_cannot_send_non_string_to_showanswer(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_showanswer(1)

    def test_can_update_showanswer(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['showanswer'] = 'always'
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = edXBaseFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['showanswer'],
                         'always')
        form.add_showanswer('sometimes')
        self.assertEqual(form.my_osid_object_form._my_map['showanswer'],
                         'sometimes')

    def test_cannot_send_none_for_markdown(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_markdown(None)

    def test_cannot_send_non_string_to_markdown(self):
        form = edXBaseFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_markdown(1)

    def test_can_update_markdown(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['markdown'] = '<here />'
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = edXBaseFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['markdown'],
                         '<here />')
        form.add_markdown('<there />')
        self.assertEqual(form.my_osid_object_form._my_map['markdown'],
                         '<there />')

    def test_can_clear_attempts(self):
        form = edXBaseFormRecord(self.osid_object_form)
        form.add_attempts(5)
        self.assertEqual(form.my_osid_object_form._my_map['attempts'],
                         5)
        form.clear_attempts()
        self.assertEqual(form.my_osid_object_form._my_map['attempts'], 0)

    def test_can_clear_weight(self):
        form = edXBaseFormRecord(self.osid_object_form)
        form.add_weight(0.2)
        self.assertEqual(form.my_osid_object_form._my_map['weight'],
                         0.2)
        form.clear_weight()
        self.assertEqual(form.my_osid_object_form._my_map['weight'], 1.0)

    def test_can_clear_showanswer(self):
        form = edXBaseFormRecord(self.osid_object_form)
        form.add_showanswer('always')
        self.assertEqual(form.my_osid_object_form._my_map['showanswer'],
                         'always')
        form.clear_showanswer()
        self.assertEqual(form.my_osid_object_form._my_map['showanswer'],
                         'closed')

    def test_can_clear_markdown(self):
        form = edXBaseFormRecord(self.osid_object_form)
        form.add_markdown('# Title')
        self.assertEqual(form.my_osid_object_form._my_map['markdown'],
                         '# Title')
        form.clear_markdown()
        self.assertEqual(form.my_osid_object_form._my_map['markdown'],
                         '')

    def test_can_get_attempts_metadata(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_attempts_metadata(), Metadata))

    def test_can_get_weight_metadata(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_weight_metadata(), Metadata))

    def test_can_get_showanwer_metadata(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_showanswer_metadata(), Metadata))

    def test_can_get_markdown_metadata(self):
        form = edXBaseFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_markdown_metadata(), Metadata))


class TestedXBaseRecord(unittest.TestCase):
    """Tests for edXBaseRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['attempts'] = 2
        obj_map['weight'] = 0.75
        obj_map['showanswer'] = 'always'
        obj_map['markdown'] = '<here />'
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.edx_base_object = edXBaseRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_attempts(self):
        self.assertTrue(isinstance(self.edx_base_object.attempts, int))
        self.assertEqual(self.edx_base_object.attempts, 2)

    def test_can_get_weight(self):
        self.assertTrue(isinstance(self.edx_base_object.weight, float))
        self.assertEqual(self.edx_base_object.weight, 0.75)

    def test_can_get_showanswer(self):
        self.assertTrue(isinstance(self.edx_base_object.showanswer,
                                   basestring))
        self.assertEqual(self.edx_base_object.showanswer, 'always')

    def test_can_get_markdown(self):
        self.assertTrue(isinstance(self.edx_base_object.markdown,
                                   basestring))
        self.assertEqual(self.edx_base_object.markdown, '<here />')

    def test_can_check_attempts(self):
        self.assertTrue(self.edx_base_object.has_attempts())

    def test_can_check_weight(self):
        self.assertTrue(self.edx_base_object.has_weight())

    def test_can_check_showanswer(self):
        self.assertTrue(self.edx_base_object.has_showanswer())

    def test_can_check_markdown(self):
        self.assertTrue(self.edx_base_object.has_markdown())

    def test_getting_attempts_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['attempts'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.attempts

    def test_getting_weight_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['weight'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.weight

    def test_getting_showanswer_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['showanswer'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.showanswer

    def test_getting_markdown_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['markdown'] = ''
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.markdown


class TestTimeValueFormRecord(unittest.TestCase):
    """Tests for TimeValueFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_time_value_with_string(self):
        form = TimeValueFormRecord(self.osid_object_form)
        self.assertNotEqual({
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        }, form.my_osid_object_form._my_map['timeValue'])
        form.set_time_value('05:05:05')
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        })

    def test_can_set_time_value_with_duration(self):
        form = TimeValueFormRecord(self.osid_object_form)
        test_duration = Duration(seconds=5 * 60 * 60 + 5 * 60 + 5)
        self.assertNotEqual({
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        }, form.my_osid_object_form._my_map['timeValue'])
        form.set_time_value(test_duration)
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        })

    def test_cannot_send_none_to_time_value(self):
        form = TimeValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_time_value(None)

    def test_cannot_send_non_duration_non_string_to_time_value(self):
        form = TimeValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_time_value(1)

    def test_cannot_send_incorrectly_formatted_time_string(self):
        form = TimeValueFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_time_value('ninety')

    def test_can_update_time_value(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['timeValue'] = {
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'

        form = TimeValueFormRecord(osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 5,
            'minutes': 5,
            'seconds': 5
        })
        form.set_time_value('01:02:03')
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 1,
            'minutes': 2,
            'seconds': 3
        })

    def test_can_clear_time_value(self):
        form = TimeValueFormRecord(self.osid_object_form)
        form.set_time_value('01:02:03')
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 1,
            'minutes': 2,
            'seconds': 3
        })
        form.clear_time_value()
        self.assertEqual(form.my_osid_object_form._my_map['timeValue'], {
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        })

    def test_can_get_time_value_metadata(self):
        form = TimeValueFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_time_value_metadata(), Metadata))


class TestTimeValueRecord(unittest.TestCase):
    """Tests for TimeValueRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['timeValue'] = {
            'hours': 1,
            'minutes': 2,
            'seconds': 3
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.time_value_object = TimeValueRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_time_value(self):
        self.assertTrue(isinstance(self.time_value_object.time, dict))
        self.assertEqual(self.time_value_object.time, {
            'hours': 1,
            'minutes': 2,
            'seconds': 3
        })

    def test_can_check_time_value(self):
        self.assertTrue(self.time_value_object.has_time())

    def test_getting_time_value_when_has_none_throws_exception(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['timeValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        time_value_object = TimeValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            time_value_object.time

    def test_can_get_time_string(self):
        self.assertTrue(isinstance(self.time_value_object.time_str,
                                   basestring))
        self.assertEqual(self.time_value_object.time_str, '01:02:03')


class TestFilesFormRecord(unittest.TestCase):
    """Tests for FilesFormRecord"""

    @classmethod
    def setUpClass(cls):
        # Create a test repository for file creation
        #   all of the OsidObjectForm maps need to have
        #   ``assignedRepositoryIds[<test repository id>]``
        mgr = get_repository_manager()
        form = mgr.get_repository_form_for_create([])
        form.display_name = 'Test repository'
        cls.repo = mgr.create_repository(form)

        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                              runtime=mgr._runtime)
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'
        cls.osid_object_form._my_map['assignedRepositoryIds'] = [str(cls.repo.ident)]
        cls.test_file = open(os.path.join(ABS_PATH, 'files', 'test_image.png'), 'r')

    @classmethod
    def tearDownClass(cls):
        # NOTE: make sure to call form.clear_files() after any tests that
        #   adds a file to the form -- that will also delete the
        #   asset.
        cls.test_file.close()
        # Delete the test repository (used for file creation)
        mgr = get_repository_manager()
        mgr.delete_repository(cls.repo.ident)

    def test_can_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file),
                      label='test_file',
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_record_types=[],
                      asset_name='Test asset',
                      asset_description='Test asset description')
        self.assertIn('test_file',
                      form.my_osid_object_form._my_map['fileIds'])
        for key in ['assetId', 'assetContentId', 'assetContentTypeId']:
            self.assertIn(key,
                          form.my_osid_object_form._my_map['fileIds']['test_file'])
        form.clear_files()

    def test_can_add_existing_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        asset_id = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        asset_content_id = Id('repository.AssetContent%3A2%40ODL.MIT.EDU')
        asset_content_type = Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU')
        form.add_asset(asset_id,
                       label='test_file',
                       asset_content_id=asset_content_id,
                       asset_content_type=asset_content_type)
        self.assertIn('test_file',
                      form.my_osid_object_form._my_map['fileIds'])
        for key in ['assetId', 'assetContentId', 'assetContentTypeId']:
            self.assertIn(key,
                          form.my_osid_object_form._my_map['fileIds']['test_file'])
        self.assertEqual(str(asset_id),
                         form.my_osid_object_form._my_map['fileIds']['test_file']['assetId'])
        self.assertEqual(str(asset_content_id),
                         form.my_osid_object_form._my_map['fileIds']['test_file']['assetContentId'])
        self.assertEqual(str(asset_content_type),
                         form.my_osid_object_form._my_map['fileIds']['test_file']['assetContentTypeId'])

    def test_cannot_send_none_to_add_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_asset(None)

    def test_cannot_send_none_to_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_file(None)

    def test_cannot_send_non_data_stream_to_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(self.test_file)

    def test_cannot_send_non_id_to_add_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_asset('repository.Asset%3A1%40ODL.MIT.EDU')

    def test_cannot_send_label_with_period_in_name_to_add_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_asset(Id('repository.Asset%3A1%40ODL.MIT.EDU'),
                           label='foo.bar')

    def test_cannot_send_label_with_period_in_name_to_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(DataInputStream(self.test_file),
                          label='foo.bar')

    def test_label_auto_generated_if_not_sent_to_add_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        asset_id = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        form.add_asset(asset_id)
        self.assertTrue(len(form.my_osid_object_form._my_map['fileIds'].keys()) == 1)
        label = form.my_osid_object_form._my_map['fileIds'].keys()[0]
        self.assertTrue(len(label), 24)

    def test_label_auto_generated_if_not_sent_to_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file))
        self.assertTrue(len(form.my_osid_object_form._my_map['fileIds'].keys()) == 1)
        label = form.my_osid_object_form._my_map['fileIds'].keys()[0]
        self.assertTrue(len(label), 24)
        form.clear_files()

    def test_asset_content_id_must_be_id(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        asset_id = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        asset_content_type = Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            form.add_asset(asset_id,
                           label='test_file',
                           asset_content_id='foo',
                           asset_content_type=asset_content_type)

    def test_asset_content_type_must_be_type_for_add_asset(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        asset_id = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        asset_content_id = Id('repository.AssetContent%3A2%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            form.add_asset(asset_id,
                           label='test_file',
                           asset_content_id=asset_content_id,
                           asset_content_type='foo')

    def test_asset_type_must_be_type(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(DataInputStream(self.test_file),
                          label='test_file',
                          asset_type='repository.Asset%3Amy-type%40ODL.MIT.EDU',
                          asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_record_types=[],
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_content_type_must_be_type_for_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(DataInputStream(self.test_file),
                          label='test_file',
                          asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_type='repository.AssetContent%3Amy-type%40ODL.MIT.EDU',
                          asset_content_record_types=[],
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_content_record_types_must_be_list(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(DataInputStream(self.test_file),
                          label='test_file',
                          asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_record_types='one',
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_content_record_types_must_be_types(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        with self.assertRaises(errors.InvalidArgument):
            form.add_file(DataInputStream(self.test_file),
                          label='test_file',
                          asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_record_types=['one'],
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_can_update_file(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['fileIds'] = {}
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map,
                                          runtime=self.repo._runtime)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'
        self.test_file.seek(0)
        form = FilesFormRecord(osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file),
                      label='foo')
        self.assertIn('foo', form.my_osid_object_form._my_map['fileIds'])
        asset_id_str = form.my_osid_object_form._my_map['fileIds']['foo']['assetId']
        asset = self.repo.get_asset(Id(asset_id_str))
        asset_content = asset.get_asset_contents().next()
        self.test_file.seek(0)
        self.assertEqual(asset_content.get_data().read(),
                         self.test_file.read())
        form.clear_files()

    def test_can_update_asset(self):
        obj_map = deepcopy(TEST_OBJECT_MAP)
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['fileIds'] = {
            'foo': {
                'assetId': 'repository.Asset%3Aold-id%40ODL.MIT.EDU',
                'assetContentId': 'repository.AssetContent%3Aold-ac-id%40ODL.MIT.EDU',
                'assetContentTypeId': 'repository.AssetContent%3Aold-type%40ODL.MIT.EDU'
            }
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map,
                                          runtime=self.repo._runtime)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'
        form = FilesFormRecord(osid_object_form)
        self.assertIn('old-id',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetId'])
        self.assertIn('old-ac-id',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetContentId'])
        self.assertIn('old-type',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetContentTypeId'])

        form.add_asset(Id('repository.Asset%3Anew-id%40ODL.MIT.EDU'),
                       label='foo',
                       asset_content_id=Id('repository.AssetContent%3Anew-ac-id%40ODL.MIT.EDU'),
                       asset_content_type=Type('repository.AssetContent%3Anew-type%40ODL.MIT.EDU'))
        self.assertTrue(len(form.my_osid_object_form._my_map['fileIds']['foo'].keys()), 1)
        self.assertIn('new-id',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetId'])
        self.assertIn('new-ac-id',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetContentId'])
        self.assertIn('new-type',
                      form.my_osid_object_form._my_map['fileIds']['foo']['assetContentTypeId'])

    def test_can_clear_file(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file),
                      label='test_file',
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_record_types=[],
                      asset_name='Test asset',
                      asset_description='Test asset description')
        self.assertIn('test_file',
                      form.my_osid_object_form._my_map['fileIds'])
        form.clear_file('test_file')
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])

    def test_clearing_non_existent_label_throws_exception(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file),
                      label='test_file',
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_record_types=[],
                      asset_name='Test asset',
                      asset_description='Test asset description')
        self.assertIn('test_file',
                      form.my_osid_object_form._my_map['fileIds'])
        with self.assertRaises(errors.NotFound):
            form.clear_file('foo')
        form.clear_files()

    def test_can_clear_files(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file),
                      label='test_file',
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_record_types=[],
                      asset_name='Test asset',
                      asset_description='Test asset description')
        self.assertIn('test_file',
                      form.my_osid_object_form._my_map['fileIds'])
        form.clear_files()
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])

    def test_can_get_file_metadata(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_file_metadata(), Metadata))

    def test_can_get_label_metadata(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_label_metadata(), Metadata))
