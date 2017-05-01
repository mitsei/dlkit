"""Unit tests of osid base_records."""

import datetime
import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.records.osid.base_records import *
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.metadata import Metadata

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
