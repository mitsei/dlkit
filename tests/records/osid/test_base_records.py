"""Unit tests of osid base_records."""
from __future__ import unicode_literals

import os

import datetime
import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.repository.objects import AssetList
from dlkit.abstract_osid.resource.objects import Resource
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.transport.objects import DataInputStream
from dlkit.primordium.mapping.color_primitives import RGBColorCoordinate
from dlkit.records.osid.base_records import *

from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.queries import OsidObjectQuery
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.id.objects import IdList
from dlkit.json_.utilities import is_string
from dlkit.runtime import configs
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.primitives import InitializableLocale
from dlkit.runtime.proxy_example import SimpleRequest

from .. import utilities

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


def get_repository_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('REPOSITORY',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


def get_resource_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('RESOURCE',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


def get_proxy(with_locale=None):
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    if with_locale is not None and with_locale in ['en', 'hi', 'te']:
        if with_locale == 'en':
            language_code = 'ENG'
            script_code = 'LATN'
        elif with_locale == 'hi':
            language_code = 'HIN'
            script_code = 'DEVA'
        else:
            language_code = 'TEL'
            script_code = 'TELU'

        locale = InitializableLocale(language_type_identifier=language_code,
                                     script_type_identifier=script_code)

        condition.set_locale(locale)
    return PROXY_SESSION.get_proxy(condition)


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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['integerValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        integer_object = IntegerValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            integer_object.integer

    def test_zero_returns_as_valid_integer(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['decimalValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        decimal_object = DecimalValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            decimal_object.decimal

    def test_zero_returns_as_valid_decimal(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        self.assertEqual(len(list(form.my_osid_object_form._my_map['texts'].keys())), 1)
        label = list(form.my_osid_object_form._my_map['texts'].keys())[0]
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        self.assertEqual(len(list(form.my_osid_object_form._my_map['integerValues'].keys())), 1)
        label = list(form.my_osid_object_form._my_map['integerValues'].keys())[0]
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        self.assertEqual(len(list(form.my_osid_object_form._my_map['decimalValues'].keys())), 1)
        label = list(form.my_osid_object_form._my_map['decimalValues'].keys())[0]
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        self.assertTrue(is_string(self.edx_base_object.showanswer))
        self.assertEqual(self.edx_base_object.showanswer, 'always')

    def test_can_get_markdown(self):
        self.assertTrue(is_string(self.edx_base_object.markdown))
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['attempts'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.attempts

    def test_getting_weight_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['weight'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.weight

    def test_getting_showanswer_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['showanswer'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        edx_base_object = edXBaseRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            edx_base_object.showanswer

    def test_getting_markdown_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['timeValue'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        time_value_object = TimeValueRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            time_value_object.time

    def test_can_get_time_string(self):
        self.assertTrue(is_string(self.time_value_object.time_str))
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
        cls.test_file = open(os.path.join(ABS_PATH, 'files', 'test_image.png'), 'rb')

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
        self.assertTrue(len(list(form.my_osid_object_form._my_map['fileIds'].keys())) == 1)
        label = list(form.my_osid_object_form._my_map['fileIds'].keys())[0]
        self.assertTrue(len(label), 24)

    def test_label_auto_generated_if_not_sent_to_add_file(self):
        form = FilesFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileIds'])
        form.add_file(DataInputStream(self.test_file))
        self.assertTrue(len(list(form.my_osid_object_form._my_map['fileIds'].keys())) == 1)
        label = list(form.my_osid_object_form._my_map['fileIds'].keys())[0]
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
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        asset_content = next(asset.get_asset_contents())
        self.test_file.seek(0)
        self.assertEqual(asset_content.get_data().read(),
                         self.test_file.read())
        form.clear_files()

    def test_can_update_asset(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
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
        self.assertTrue(len(list(form.my_osid_object_form._my_map['fileIds']['foo'].keys())), 1)
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


class TestFilesRecord(unittest.TestCase):
    """Tests for FilesRecord"""

    @classmethod
    def setUpClass(cls):
        mgr = get_repository_manager()
        form = mgr.get_repository_form_for_create([])
        form.display_name = 'Test repository'
        cls.repo = mgr.create_repository(form)

        form = cls.repo.get_asset_form_for_create([])
        form.display_name = 'Test asset'
        cls.asset = cls.repo.create_asset(form)

        cls.test_image = open(os.path.join(ABS_PATH, 'files', 'test_image.png'), 'rb')
        form = cls.repo.get_asset_content_form_for_create(cls.asset.ident, [])
        form.display_name = 'Test asset content'
        form.set_data(DataInputStream(cls.test_image))
        form.set_url('example.com')
        cls.repo.create_asset_content(form)
        cls.asset = cls.repo.get_asset(cls.asset.ident)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {
            'foo': {
                'assetId': str(cls.asset.ident),
                'assetContentId': str(cls.asset.get_asset_contents().next().ident),
                'assetContentTypeId': str(cls.asset.get_asset_contents().next().genus_type)
            }
        }
        obj_map['assignedBankIds'] = [str(cls.repo.ident)]

        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map,
                                     runtime=mgr._runtime)

        cls.item = FilesRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        cls.test_image.close()
        # Delete the asset
        cls.repo.delete_asset(cls.asset.ident)
        # Delete the test repository (used for file creation)
        mgr = get_repository_manager()
        mgr.delete_repository(cls.repo.ident)
        # No test bank to delete, so no need to clean it up here

    def test_can_get_files_map(self):
        self.test_image.seek(0)
        self.assertTrue(isinstance(self.item.files_map, dict))
        self.assertEqual(self.item.files_map, {
            'foo': base64.b64encode(self.test_image.read())
        })

    def test_can_check_files(self):
        self.assertTrue(self.item.has_files())

    def test_getting_files_map_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        files_object = FilesRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            files_object.files_map

    def test_can_get_files_url_map(self):
        self.assertTrue(isinstance(self.item.file_urls_map,
                                   dict))
        self.assertEqual(self.item.file_urls_map,
                         {'foo': self.asset.get_asset_contents().next().url})

    def test_getting_files_url_map_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        files_object = FilesRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            files_object.file_urls_map

    def test_can_get_files_when_has_url(self):
        self.assertTrue(isinstance(self.item.get_files(),
                                   dict))
        self.assertEqual(self.item.get_files(),
                         {'foo': self.asset.get_asset_contents().next().url})

    def test_can_get_files_when_no_url(self):
        self.test_image.seek(0)
        form = self.repo.get_asset_content_form_for_create(self.asset.ident, [])
        form.display_name = 'Test asset content'
        form.set_data(DataInputStream(self.test_image))
        self.repo.create_asset_content(form)
        asset = self.repo.get_asset(self.asset.ident)

        ac_list = asset.get_asset_contents()
        next(ac_list)
        second_ac = next(ac_list)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {
            'foo': {
                'assetId': str(asset.ident),
                'assetContentId': str(second_ac.ident),
                'assetContentTypeId': str(second_ac.genus_type)
            }
        }
        obj_map['assignedBankIds'] = [str(self.repo.ident)]

        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)

        item = FilesRecord(osid_object)
        self.test_image.seek(0)
        self.assertTrue(isinstance(item.get_files(),
                                   dict))
        self.assertEqual(item.get_files(),
                         {'foo': base64.b64encode(self.test_image.read())})

        # cleaning up the new asset content
        self.repo.delete_asset_content(second_ac.ident)

    def test_can_check_if_has_file(self):
        self.assertFalse(self.item.has_file('boo'))
        self.assertTrue(self.item.has_file('foo'))

    def test_can_get_asset_ids(self):
        asset_ids = self.item.get_asset_ids()
        self.assertTrue(isinstance(asset_ids, IdList))
        self.assertTrue(asset_ids.available() == 1)
        self.assertEqual(str(next(asset_ids)),
                         str(self.asset.ident))

    def test_can_get_asset_ids_map(self):
        asset_ids_map = self.item.get_asset_ids_map()
        self.assertTrue(isinstance(asset_ids_map, dict))
        self.assertIn('foo', asset_ids_map)
        self.assertEqual(asset_ids_map, {
            'foo': {
                'assetId': str(self.asset.ident),
                'assetContentId': str(self.asset.get_asset_contents().next().ident),
                'assetContentTypeId': str(self.asset.get_asset_contents().next().genus_type)
            }})

    def test_can_get_asset_id_by_label(self):
        self.assertTrue(isinstance(self.item.get_asset_id_by_label('foo'), Id))
        self.assertEqual(str(self.item.get_asset_id_by_label('foo')),
                         str(self.asset.ident))

    def test_getting_asset_id_by_label_throws_exception_if_not_exist(self):
        with self.assertRaises(errors.IllegalState):
            self.item.get_asset_id_by_label('boo')

    def test_can_get_file_by_label(self):
        self.test_image.seek(0)
        self.assertTrue(isinstance(self.item.get_file_by_label('foo'),
                                   DataInputStream))
        self.assertEqual(self.item.get_file_by_label('foo').read(),
                         self.test_image.read())

    def test_getting_file_by_label_throws_exception_if_not_exist(self):
        with self.assertRaises(errors.IllegalState):
            self.item.get_file_by_label('boo')

    def test_can_get_url_by_label(self):
        self.assertTrue(is_string(self.item.get_url_by_label('foo')))
        self.assertEqual(self.item.get_url_by_label('foo'),
                         'example.com')

    def test_getting_url_by_label_throws_exception_if_not_exist(self):
        with self.assertRaises(errors.IllegalState):
            self.item.get_url_by_label('boo')

    def test_can_delete(self):
        self.item._delete()
        # Though really nothing should happen since this method is
        #   `pass` in the implementation

    def test_object_map_updated_with_url(self):
        # Note that currently this does not handle the more complicated
        #   case of multilanguage altText or transcripts. Those are
        #   tested in `qbank` functional tests
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {
            'foo': {
                'assetId': str(self.asset.ident),
                'assetContentId': str(self.asset.get_asset_contents().next().ident),
                'assetContentTypeId': str(self.asset.get_asset_contents().next().genus_type)
            }
        }
        obj_map['assignedBankIds'] = [str(self.repo.ident)]
        obj_map['text'] = {
            'text': '<img src="AssetContent:foo" />'
        }
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)

        item = FilesRecord(osid_object)
        item._update_object_map(obj_map)
        self.assertEqual(obj_map['text']['text'],
                         '<img src="example.com"/>')

    def test_none_text_field_does_not_break(self):
        # Note that currently this does not handle the more complicated
        #   case of multilanguage altText or transcripts. Those are
        #   tested in `qbank` functional tests
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileIds'] = {
            'foo': {
                'assetId': str(self.asset.ident),
                'assetContentId': str(self.asset.get_asset_contents().next().ident),
                'assetContentTypeId': str(self.asset.get_asset_contents().next().genus_type)
            }
        }
        obj_map['assignedBankIds'] = [str(self.repo.ident)]
        obj_map['text'] = {
            'text': None
        }
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)

        item = FilesRecord(osid_object)
        item._update_object_map(obj_map)
        self.assertEqual(obj_map['text']['text'],
                         None)


class TestFileFormRecord(unittest.TestCase):
    """Tests for FileFormRecord"""

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
        cls.test_file = open(os.path.join(ABS_PATH, 'files', 'test_image.png'), 'rb')

    @classmethod
    def tearDownClass(cls):
        # NOTE: make sure to call form.clear_files() after any tests that
        #   adds a file to the form -- that will also delete the
        #   asset.
        cls.test_file.close()
        # Delete the test repository (used for file creation)
        mgr = get_repository_manager()
        mgr.delete_repository(cls.repo.ident)

    def test_can_set_file(self):
        form = FileFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileId'])
        form.set_file(DataInputStream(self.test_file),
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_name='Test asset',
                      asset_description='Test asset description')
        for key in ['assetId', 'assetContentTypeId']:
            self.assertIn(key,
                          form.my_osid_object_form._my_map['fileId'])
        self.assertEqual(form.my_osid_object_form._my_map['fileId']['assetContentTypeId'],
                         'repository.AssetContent%3Amy-type%40ODL.MIT.EDU')
        form.clear_file()

    def test_can_set_asset(self):
        form = FileFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileId'])
        asset_id = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        asset_content_type = Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU')
        form.set_asset(asset_id,
                       asset_content_type=asset_content_type)
        for key in ['assetId', 'assetContentTypeId']:
            self.assertIn(key,
                          form.my_osid_object_form._my_map['fileId'])
        self.assertEqual(str(asset_id),
                         form.my_osid_object_form._my_map['fileId']['assetId'])
        self.assertEqual(str(asset_content_type),
                         form.my_osid_object_form._my_map['fileId']['assetContentTypeId'])

    def test_cannot_send_none_to_set_asset(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_asset(None)

    def test_cannot_send_none_to_set_file(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_file(None)

    def test_asset_data_must_be_data_input_stream(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_file(self.test_file,
                          asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_id_must_be_id(self):
        form = FileFormRecord(self.osid_object_form)
        asset_id = 'repository.Asset%3A1%40ODL.MIT.EDU'
        asset_content_type = Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            form.set_asset(asset_id,
                           asset_content_type=asset_content_type)

    def test_asset_type_must_be_type_for_set_file(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_file(DataInputStream(self.test_file),
                          asset_type='repository.Asset%3Amy-type%40ODL.MIT.EDU',
                          asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_content_type_must_be_type_for_set_file(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_file(DataInputStream(self.test_file),
                          asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                          asset_content_type='repository.AssetContent%3Amy-type%40ODL.MIT.EDU',
                          asset_name='Test asset',
                          asset_description='Test asset description')

    def test_asset_content_type_must_be_type_for_set_asset(self):
        form = FileFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_asset(Id('repository.Asset%3A1%40ODL.MIT.EDU'),
                           asset_content_type='repository.AssetContent%3Amy-type%40ODL.MIT.EDU')

    def test_can_update_file(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['fileId'] = {}
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map,
                                          runtime=self.repo._runtime)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'
        self.test_file.seek(0)
        form = FileFormRecord(osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileId'])
        form.set_file(DataInputStream(self.test_file))
        self.assertIn('assetId', form.my_osid_object_form._my_map['fileId'])
        self.assertIn('assetContentTypeId', form.my_osid_object_form._my_map['fileId'])
        asset_id_str = form.my_osid_object_form._my_map['fileId']['assetId']
        asset = self.repo.get_asset(Id(asset_id_str))
        asset_content = next(asset.get_asset_contents())
        self.test_file.seek(0)
        self.assertEqual(asset_content.get_data().read(),
                         self.test_file.read())
        form.clear_file()

    def test_can_update_asset(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['fileId'] = {
            'assetId': 'repository.Asset%3Aold-id%40ODL.MIT.EDU',
            'assetContentTypeId': 'repository.AssetContent%3Aold-type%40ODL.MIT.EDU'
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map,
                                          runtime=self.repo._runtime)
        osid_object_form._authority = 'TESTING.MIT.EDU'
        osid_object_form._namespace = 'records.Testing'
        form = FileFormRecord(osid_object_form)
        self.assertIn('old-id',
                      form.my_osid_object_form._my_map['fileId']['assetId'])
        self.assertIn('old-type',
                      form.my_osid_object_form._my_map['fileId']['assetContentTypeId'])

        form.set_asset(Id('repository.Asset%3Anew-id%40ODL.MIT.EDU'),
                       asset_content_type=Type('repository.AssetContent%3Anew-type%40ODL.MIT.EDU'))
        self.assertTrue(len(list(form.my_osid_object_form._my_map['fileId'].keys())), 2)
        self.assertIn('new-id',
                      form.my_osid_object_form._my_map['fileId']['assetId'])
        self.assertIn('new-type',
                      form.my_osid_object_form._my_map['fileId']['assetContentTypeId'])

    def test_can_clear_file(self):
        form = FileFormRecord(self.osid_object_form)
        self.assertEqual({}, form.my_osid_object_form._my_map['fileId'])
        form.set_file(DataInputStream(self.test_file),
                      asset_type=Type('repository.Asset%3Amy-type%40ODL.MIT.EDU'),
                      asset_content_type=Type('repository.AssetContent%3Amy-type%40ODL.MIT.EDU'),
                      asset_name='Test asset',
                      asset_description='Test asset description')
        self.assertIn('assetId',
                      form.my_osid_object_form._my_map['fileId'])
        form.clear_file()
        self.assertEqual({}, form.my_osid_object_form._my_map['fileId'])

    def test_can_get_file_metadata(self):
        form = FileFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_file_metadata(), Metadata))


class TestFileRecord(unittest.TestCase):
    """Tests for FileRecord"""

    @classmethod
    def setUpClass(cls):
        mgr = get_repository_manager()
        form = mgr.get_repository_form_for_create([])
        form.display_name = 'Test repository'
        cls.repo = mgr.create_repository(form)

        form = cls.repo.get_asset_form_for_create([])
        form.display_name = 'Test asset'
        cls.asset = cls.repo.create_asset(form)

        cls.test_image = open(os.path.join(ABS_PATH, 'files', 'test_image.png'), 'rb')
        form = cls.repo.get_asset_content_form_for_create(cls.asset.ident, [])
        form.display_name = 'Test asset content'
        form.set_data(DataInputStream(cls.test_image))
        form.set_url('example.com')
        cls.repo.create_asset_content(form)
        cls.asset = cls.repo.get_asset(cls.asset.ident)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileId'] = {
            'assetId': str(cls.asset.ident),
            'assetContentTypeId': str(cls.asset.get_asset_contents().next().genus_type)
        }
        obj_map['assignedBankIds'] = [str(cls.repo.ident)]

        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map,
                                     runtime=mgr._runtime)

        cls.item = FileRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        cls.test_image.close()
        # Delete the asset
        cls.repo.delete_asset(cls.asset.ident)
        # Delete the test repository (used for file creation)
        mgr = get_repository_manager()
        mgr.delete_repository(cls.repo.ident)
        # No test bank to delete, so no need to clean it up here

    def test_can_get_file_asset_id(self):
        self.test_image.seek(0)
        self.assertTrue(isinstance(self.item.file_asset_id, Id))
        self.assertEqual(str(self.item.file_asset_id),
                         str(self.asset.ident))

    def test_can_check_has_file_asset(self):
        self.assertTrue(self.item.has_file_asset())

    def test_getting_file_asset_id_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileId'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        file_object = FileRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            file_object.file_asset_id

    def test_can_get_file_url(self):
        self.assertTrue(is_string(self.item.file_url))
        self.assertEqual(self.item.file_url,
                         'example.com')

    def test_can_check_has_file_url(self):
        self.assertTrue(self.item.has_file_url)

    def test_getting_file_url_when_has_none_throws_exception(self):
        self.test_image.seek(0)
        form = self.repo.get_asset_content_form_for_create(self.asset.ident, [])
        form.display_name = 'Test asset content'
        form.set_data(DataInputStream(self.test_image))
        form.set_genus_type(Type('asset-content%3Atest-type%40ODL.MIT.EDU'))
        self.repo.create_asset_content(form)
        asset = self.repo.get_asset(self.asset.ident)

        ac_list = asset.get_asset_contents()
        next(ac_list)
        second_ac = next(ac_list)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileId'] = {
            'assetId': str(asset.ident),
            'assetContentTypeId': str(second_ac.genus_type)
        }
        obj_map['assignedBankIds'] = [str(self.repo.ident)]

        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)

        item = FileRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            item.file_url

        # cleaning up the new asset content
        self.repo.delete_asset_content(second_ac.ident)

    def test_can_get_file(self):
        self.assertTrue(isinstance(self.item.file_,
                                   DataInputStream))
        self.test_image.seek(0)
        self.assertEqual(self.item.file_.read(),
                         self.test_image.read())

    def test_getting_file_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['fileId'] = {}
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        file_object = FileRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            file_object.file_


class TestColorCoordinateFormRecord(unittest.TestCase):
    """Tests for ColorCoordinateFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_color_coordinate(self):
        form = ColorCoordinateFormRecord(self.osid_object_form)
        self.assertEqual({},
                         form.my_osid_object_form._my_map['colorCoordinate'])
        coordinate = RGBColorCoordinate(hexstr='0a21ff',
                                        uncertainty_minus=[15, 15, 15],
                                        uncertainty_plus=[15, 15, 15])

        form.set_color_coordinate(coordinate)
        self.assertEqual(form.my_osid_object_form._my_map['colorCoordinate'], {
            'values': [10, 33, 255],
            'uncertaintyPlus': [15, 15, 15],
            'uncertaintyMinus': [15, 15, 15]
        })

    def test_color_coordinate_cannot_be_none(self):
        form = ColorCoordinateFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_color_coordinate(None)

    def test_color_coordinate_must_be_instance_of_coordinate(self):
        form = ColorCoordinateFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_color_coordinate('0a21ff')

    def test_can_clear_color_coordinate(self):
        form = ColorCoordinateFormRecord(self.osid_object_form)
        coordinate = RGBColorCoordinate(hexstr='0a21ff',
                                        uncertainty_minus=[15, 15, 15],
                                        uncertainty_plus=[15, 15, 15])
        form.set_color_coordinate(coordinate)
        self.assertEqual(form.my_osid_object_form._my_map['colorCoordinate'], {
            'values': [10, 33, 255],
            'uncertaintyPlus': [15, 15, 15],
            'uncertaintyMinus': [15, 15, 15]
        })
        form.clear_color_coordinate()
        self.assertEqual(form.my_osid_object_form._my_map['colorCoordinate'], {})

    def test_can_update_color_coordinate(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['colorCoordinate'] = {
            'values': [0, 0, 0],
            'uncertaintyMinus': [5, 5, 5],
            'uncertaintyPlus': [5, 5, 5]
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = ColorCoordinateFormRecord(osid_object_form)
        self.assertEqual([0, 0, 0],
                         form.my_osid_object_form._my_map['colorCoordinate']['values'])
        self.assertEqual([5, 5, 5],
                         form.my_osid_object_form._my_map['colorCoordinate']['uncertaintyMinus'])
        self.assertEqual([5, 5, 5],
                         form.my_osid_object_form._my_map['colorCoordinate']['uncertaintyPlus'])

        coordinate = RGBColorCoordinate(hexstr='0a21ff',
                                        uncertainty_minus=[15, 15, 15],
                                        uncertainty_plus=[15, 15, 15])
        form.set_color_coordinate(coordinate)
        self.assertEqual([10, 33, 255],
                         form.my_osid_object_form._my_map['colorCoordinate']['values'])
        self.assertEqual([15, 15, 15],
                         form.my_osid_object_form._my_map['colorCoordinate']['uncertaintyMinus'])
        self.assertEqual([15, 15, 15],
                         form.my_osid_object_form._my_map['colorCoordinate']['uncertaintyPlus'])

    def test_can_get_color_coordinate_metadata(self):
        form = ColorCoordinateFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_color_coordinate_metadata(), Metadata))


class TestColorCoordinateRecord(unittest.TestCase):
    """Tests for ColorCoordinateRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['colorCoordinate'] = {
            'values': [10, 33, 255],
            'uncertaintyMinus': [15, 15, 15],
            'uncertaintyPlus': [15, 15, 15]
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.color_coordinate_object = ColorCoordinateRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_color_coordinate(self):
        self.assertTrue(isinstance(self.color_coordinate_object.color_coordinate,
                                   RGBColorCoordinate))
        coordinate = self.color_coordinate_object.color_coordinate
        self.assertEqual(coordinate.values, [10, 33, 255])
        self.assertEqual(coordinate.uncertainty_minus, [15, 15, 15])
        self.assertEqual(coordinate.uncertainty_plus, [15, 15, 15])

    def test_can_check_has_color_coordinate(self):
        self.assertTrue(self.color_coordinate_object.has_color_coordinate())

    def test_getting_color_coordinate_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['colorCoordinate'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        color_coordinate_object = ColorCoordinateRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            color_coordinate_object.color_coordinate

    def test_object_map_updated(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['colorCoordinate'] = {
            'values': [10, 33, 255],
            'uncertaintyMinus': [15, 15, 15],
            'uncertaintyPlus': [15, 15, 15]
        }
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)

        color_coordinate_object = ColorCoordinateRecord(osid_object)
        color_coordinate_object._update_object_map(obj_map)
        self.assertEqual(obj_map['colorCoordinate']['values'],
                         [10, 33, 255])
        self.assertEqual(obj_map['colorCoordinate']['uncertaintyMinus'],
                         [15, 15, 15])
        self.assertEqual(obj_map['colorCoordinate']['uncertaintyPlus'],
                         [15, 15, 15])
        self.assertEqual(obj_map['colorCoordinate']['hexValue'],
                         '0a21ff')


class TestTemporalFormRecord(unittest.TestCase):
    """Tests for TemporalFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_start_date(self):
        form = TemporalFormRecord(self.osid_object_form)
        future_date = datetime.datetime.utcnow() + datetime.timedelta(days=4)
        start_date = DateTime(year=future_date.year,
                              month=future_date.month,
                              day=future_date.day,
                              hour=future_date.hour,
                              minute=future_date.minute,
                              second=future_date.second,
                              microsecond=future_date.microsecond)

        self.assertTrue(isinstance(form.my_osid_object_form._my_map['startDate'],
                                   DateTime))
        self.assertNotEqual(start_date,
                            form.my_osid_object_form._my_map['startDate'])

        form.set_start_date(start_date)
        self.assertEqual(form.my_osid_object_form._my_map['startDate'],
                         start_date)

    def test_can_set_end_date(self):
        form = TemporalFormRecord(self.osid_object_form)
        now_date = datetime.datetime.utcnow()
        end_date = DateTime(year=now_date.year,
                            month=now_date.month,
                            day=now_date.day,
                            hour=now_date.hour,
                            minute=now_date.minute,
                            second=now_date.second,
                            microsecond=now_date.microsecond)

        self.assertTrue(isinstance(form.my_osid_object_form._my_map['endDate'],
                                   DateTime))
        self.assertNotEqual(end_date,
                            form.my_osid_object_form._my_map['endDate'])

        form.set_end_date(end_date)
        self.assertEqual(form.my_osid_object_form._my_map['endDate'],
                         end_date)

    def test_start_date_cannot_be_none(self):
        form = TemporalFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_start_date(None)

    def test_end_date_cannot_be_none(self):
        form = TemporalFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_end_date(None)

    def test_start_date_must_be_instance_of_date_time(self):
        form = TemporalFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_start_date(datetime.datetime.utcnow())

    def test_end_date_must_be_instance_of_date_time(self):
        form = TemporalFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_end_date(datetime.datetime.utcnow())

    def test_can_update_start_date(self):
        now_date = datetime.datetime.utcnow()
        future_date = now_date + datetime.timedelta(days=4)
        date_1 = DateTime(year=now_date.year,
                          month=now_date.month,
                          day=now_date.day,
                          hour=now_date.hour,
                          minute=now_date.minute,
                          second=now_date.second,
                          microsecond=now_date.microsecond)

        date_2 = DateTime(year=future_date.year,
                          month=future_date.month,
                          day=future_date.day,
                          hour=future_date.hour,
                          minute=future_date.minute,
                          second=future_date.second,
                          microsecond=future_date.microsecond)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['startDate'] = date_1
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = TemporalFormRecord(osid_object_form)
        self.assertEqual(date_1,
                         form.my_osid_object_form._my_map['startDate'])

        form.set_start_date(date_2)
        self.assertEqual(date_2,
                         form.my_osid_object_form._my_map['startDate'])

    def test_can_update_end_date(self):
        now_date = datetime.datetime.utcnow()
        future_date = now_date + datetime.timedelta(days=4)
        date_1 = DateTime(year=now_date.year,
                          month=now_date.month,
                          day=now_date.day,
                          hour=now_date.hour,
                          minute=now_date.minute,
                          second=now_date.second,
                          microsecond=now_date.microsecond)

        date_2 = DateTime(year=future_date.year,
                          month=future_date.month,
                          day=future_date.day,
                          hour=future_date.hour,
                          minute=future_date.minute,
                          second=future_date.second,
                          microsecond=future_date.microsecond)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['endDate'] = date_1
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = TemporalFormRecord(osid_object_form)
        self.assertEqual(date_1,
                         form.my_osid_object_form._my_map['endDate'])

        form.set_end_date(date_2)
        self.assertEqual(date_2,
                         form.my_osid_object_form._my_map['endDate'])

    def test_can_clear_start_date(self):
        form = TemporalFormRecord(self.osid_object_form)
        default_start_date = form._start_date_metadata['default_date_time_values'][0]
        default_start_date = DateTime(year=default_start_date.year,
                                      month=default_start_date.month,
                                      day=default_start_date.day,
                                      hour=default_start_date.hour,
                                      minute=default_start_date.minute,
                                      second=default_start_date.second,
                                      microsecond=default_start_date.microsecond)
        future_date = datetime.datetime.utcnow() + datetime.timedelta(days=4)
        start_date = DateTime(year=future_date.year,
                              month=future_date.month,
                              day=future_date.day,
                              hour=future_date.hour,
                              minute=future_date.minute,
                              second=future_date.second,
                              microsecond=future_date.microsecond)
        form.set_start_date(start_date)
        self.assertEqual(form.my_osid_object_form._my_map['startDate'],
                         start_date)
        form.clear_start_date()
        self.assertEqual(form.my_osid_object_form._my_map['startDate'],
                         default_start_date)

    def test_can_clear_end_date(self):
        form = TemporalFormRecord(self.osid_object_form)
        default_end_date = form._end_date_metadata['default_date_time_values'][0]
        default_end_date = DateTime(**default_end_date)
        future_date = datetime.datetime.utcnow() + datetime.timedelta(days=4)
        end_date = DateTime(year=future_date.year,
                            month=future_date.month,
                            day=future_date.day,
                            hour=future_date.hour,
                            minute=future_date.minute,
                            second=future_date.second,
                            microsecond=future_date.microsecond)
        form.set_end_date(end_date)
        self.assertEqual(form.my_osid_object_form._my_map['endDate'],
                         end_date)
        form.clear_end_date()
        self.assertEqual(form.my_osid_object_form._my_map['endDate'],
                         default_end_date)

    def test_can_get_start_date_metadata(self):
        form = TemporalFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_start_date_metadata(), Metadata))

    def test_can_get_end_date_metadata(self):
        form = TemporalFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_end_date_metadata(), Metadata))


class TestTemporalRecord(unittest.TestCase):
    """Tests for TemporalRecord"""

    def check_is_effective(self, start_date, end_date, expected):
        temporal_object = self.create_temporal(start_date, end_date)
        self.assertEqual(temporal_object.is_effective(), expected)

    def create_temporal(self, start_date, end_date):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['startDate'] = start_date
        obj_map['endDate'] = end_date
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        return TemporalRecord(osid_object)

    @classmethod
    def setUpClass(cls):
        start_date = datetime.datetime.utcnow() + datetime.timedelta(days=2)
        cls.start_date = DateTime(year=start_date.year,
                                  month=start_date.month,
                                  day=start_date.day,
                                  hour=start_date.hour,
                                  minute=start_date.minute,
                                  second=start_date.second,
                                  microsecond=start_date.microsecond)
        end_date = datetime.datetime.utcnow() + datetime.timedelta(days=5)
        cls.end_date = DateTime(year=end_date.year,
                                month=end_date.month,
                                day=end_date.day,
                                hour=end_date.hour,
                                minute=end_date.minute,
                                second=end_date.second,
                                microsecond=end_date.microsecond)
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['startDate'] = cls.start_date
        obj_map['endDate'] = cls.end_date
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.temporal_object = TemporalRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_start_date(self):
        self.assertTrue(isinstance(self.temporal_object.start_date,
                                   DateTime))
        self.assertEqual(self.temporal_object.start_date,
                         self.start_date)

    def test_can_get_end_date(self):
        self.assertTrue(isinstance(self.temporal_object.end_date,
                                   DateTime))
        self.assertEqual(self.temporal_object.end_date,
                         self.end_date)

    def test_accurately_returns_is_effective(self):
        past = datetime.datetime.utcnow() - datetime.timedelta(days=1)
        past = DateTime(year=past.year,
                        month=past.month,
                        day=past.day,
                        hour=past.hour,
                        minute=past.minute,
                        second=past.second,
                        microsecond=past.microsecond)
        near_past = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
        near_past = DateTime(year=near_past.year,
                             month=near_past.month,
                             day=near_past.day,
                             hour=near_past.hour,
                             minute=near_past.minute,
                             second=near_past.second,
                             microsecond=near_past.microsecond)
        near_future = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        near_future = DateTime(year=near_future.year,
                               month=near_future.month,
                               day=near_future.day,
                               hour=near_future.hour,
                               minute=near_future.minute,
                               second=near_future.second,
                               microsecond=near_future.microsecond)
        future = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        future = DateTime(year=future.year,
                          month=future.month,
                          day=future.day,
                          hour=future.hour,
                          minute=future.minute,
                          second=future.second,
                          microsecond=future.microsecond)

        self.check_is_effective(past, near_past, False)
        self.check_is_effective(near_past, near_future, True)
        self.check_is_effective(near_past, future, True)
        self.check_is_effective(past, near_future, True)
        self.check_is_effective(near_future, future, False)


class TestSourceableFormRecord(unittest.TestCase):
    """Tests for SourceableFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_branding(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.my_osid_object_form._my_map['brandingIds'],
                                   list))
        self.assertEqual(len(form.my_osid_object_form._my_map['brandingIds']), 0)
        branding = [Id('repository.Asset%3A1%40ODL.MIT.EDU')]
        form.set_branding(branding)
        self.assertEqual(len(form.my_osid_object_form._my_map['brandingIds']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['brandingIds'][0],
                         'repository.Asset%3A1%40ODL.MIT.EDU')

    def test_can_set_provider(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['providerId'], '')
        provider = Id('resource.Resource%3A1%40ODL.MIT.EDU')
        form.set_provider(provider)
        self.assertEqual(form.my_osid_object_form._my_map['providerId'],
                         'resource.Resource%3A1%40ODL.MIT.EDU')

    def test_can_set_license(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['license']['text'], '')
        license_ = 'CC-BY'
        form.set_license(license_)
        self.assertEqual(form.my_osid_object_form._my_map['license']['text'],
                         'CC-BY')

    def test_branding_cannot_be_none(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_branding(None)

    def test_provider_cannot_be_none(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_provider(None)

    def test_license_cannot_be_none(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.set_license(None)

    def test_branding_must_be_a_list(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_branding(Id('repository.Asset%3A1%40ODL.MIT.EDU'))

    def test_provider_must_be_instance_of_id(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_provider('resource.Resource%3A1%40ODL.MIT.EDU')

    def test_license_must_be_instance_of_string(self):
        form = SourceableFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.set_license(2)

    def test_can_update_branding(self):
        id_1 = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        id_2 = Id('repository.Asset%3A2%40ODL.MIT.EDU')
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['brandingIds'] = [str(id_1)]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual([str(id_1)],
                         form.my_osid_object_form._my_map['brandingIds'])

        form.set_branding([id_2])
        self.assertEqual([str(id_2)],
                         form.my_osid_object_form._my_map['brandingIds'])

    def test_can_update_provider(self):
        id_1 = Id('resource.Resource%3A1%40ODL.MIT.EDU')
        id_2 = Id('resource.Resource%3A2%40ODL.MIT.EDU')
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['providerId'] = str(id_1)
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual(str(id_1),
                         form.my_osid_object_form._my_map['providerId'])

        form.set_provider(id_2)
        self.assertEqual(str(id_2),
                         form.my_osid_object_form._my_map['providerId'])

    def test_can_update_license(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['license'] = {
            'text': 'foo'
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual('foo',
                         form.my_osid_object_form._my_map['license']['text'])

        form.set_license('bar')
        self.assertEqual('bar',
                         form.my_osid_object_form._my_map['license']['text'])

    def test_can_clear_branding(self):
        id_1 = Id('repository.Asset%3A1%40ODL.MIT.EDU')
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['brandingIds'] = [str(id_1)]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual([str(id_1)],
                         form.my_osid_object_form._my_map['brandingIds'])

        form.clear_branding()
        self.assertEqual([],
                         form.my_osid_object_form._my_map['brandingIds'])

    def test_can_clear_provider(self):
        id_1 = Id('resource.Resource%3A1%40ODL.MIT.EDU')
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['providerId'] = str(id_1)
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual(str(id_1),
                         form.my_osid_object_form._my_map['providerId'])

        form.clear_provider()
        self.assertEqual('',
                         form.my_osid_object_form._my_map['providerId'])

    def test_can_clear_license(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['license'] = {
            'text': 'foo'
        }
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = SourceableFormRecord(osid_object_form)
        self.assertEqual('foo',
                         form.my_osid_object_form._my_map['license']['text'])

        form.clear_license()
        self.assertEqual('',
                         form.my_osid_object_form._my_map['license']['text'])

    def test_can_get_branding_metadata(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_branding_metadata(), Metadata))

    def test_can_get_provider_metadata(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_provider_metadata(), Metadata))

    def test_can_get_license_metadata(self):
        form = SourceableFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_license_metadata(), Metadata))


class TestSourceableRecord(unittest.TestCase):
    """Tests for SourceableRecord"""

    @classmethod
    def setUpClass(cls):
        mgr = get_repository_manager()
        form = mgr.get_repository_form_for_create([])
        form.display_name = 'Test repository'
        cls.repo = mgr.create_repository(form)

        form = cls.repo.get_asset_form_for_create([])
        form.display_name = 'Test asset'
        cls.asset = cls.repo.create_asset(form)

        mgr = get_resource_manager()
        cls.bin = mgr.get_bin(cls.repo.ident)

        form = cls.bin.get_resource_form_for_create([])
        form.display_name = 'Test resource'
        cls.resource = cls.bin.create_resource(form)

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['providerId'] = str(cls.resource.ident)
        obj_map['brandingIds'] = [str(cls.asset.ident)]
        obj_map['license'] = {
            'text': 'old-license',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map,
                                     runtime=mgr._runtime)
        cls.sourceable_object = SourceableRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        cls.repo.delete_asset(cls.asset.ident)

        mgr = get_repository_manager()
        mgr.delete_repository(cls.repo.ident)

        cls.bin.delete_resource(cls.resource.ident)

        mgr = get_resource_manager()
        mgr.delete_bin(cls.bin.ident)

    def test_can_get_provider_id(self):
        self.assertTrue(isinstance(self.sourceable_object.provider_id,
                                   Id))
        self.assertEqual(str(self.sourceable_object.provider_id),
                         str(self.resource.ident))

    def test_can_get_provider(self):
        self.assertTrue(isinstance(self.sourceable_object.provider,
                                   Resource))
        self.assertEqual(str(self.sourceable_object.provider.ident),
                         str(self.resource.ident))

    def test_can_get_branding_ids(self):
        self.assertTrue(isinstance(self.sourceable_object.branding_ids,
                                   IdList))
        self.assertEqual([str(bi) for bi in self.sourceable_object.branding_ids],
                         [str(self.asset.ident)])

    def test_can_get_branding(self):
        self.assertTrue(isinstance(self.sourceable_object.branding,
                                   AssetList))
        self.assertEqual(self.sourceable_object.branding.available(), 1)
        self.assertEqual(str(self.sourceable_object.branding.next().ident),
                         str(self.asset.ident))

    def test_can_get_license(self):
        self.assertTrue(isinstance(self.sourceable_object.license_,
                                   DisplayText))
        self.assertEqual(self.sourceable_object.license_.text,
                         'old-license')

    def test_getting_provider_id_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)
        sourceable_object = SourceableRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            sourceable_object.provider_id

    def test_getting_provider_when_has_none_throws_exception(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)
        sourceable_object = SourceableRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            sourceable_object.provider

    def test_getting_branding_ids_when_has_none_returns_empty_id_list(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)
        sourceable_object = SourceableRecord(osid_object)
        self.assertEqual(sourceable_object.branding_ids.available(), 0)
        self.assertTrue(isinstance(sourceable_object.branding_ids, IdList))

    def test_getting_branding_when_has_none_returns_empty_asset_list(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._runtime)
        sourceable_object = SourceableRecord(osid_object)
        self.assertEqual(sourceable_object.branding.available(), 0)
        self.assertTrue(isinstance(sourceable_object.branding, AssetList))


class TestMultiLanguageUtils(unittest.TestCase):
    """Tests for MultiLanguageUtils"""

    def remove_osid_object(self, form=False):
        if form:
            del self.ml_obj.my_osid_object_form
        else:
            del self.ml_obj.my_osid_object

    def set_no_proxy(self, form=False, map_initializer={}):
        osid_object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object_map.update(map_initializer)

        if form:
            self.ml_obj.my_osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                                             osid_object_map=osid_object_map)
        else:
            self.ml_obj.my_osid_object = OsidObject(object_name='TEST_OBJECT',
                                                    osid_object_map=osid_object_map)

    def set_proxy_with_no_locale(self, form=False, map_initializer={}):
        osid_object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object_map.update(map_initializer)

        if form:
            self.ml_obj.my_osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                                             osid_object_map=osid_object_map,
                                                             proxy=get_proxy())
        else:
            self.ml_obj.my_osid_object = OsidObject(object_name='TEST_OBJECT',
                                                    osid_object_map=osid_object_map,
                                                    proxy=get_proxy())

    def set_proxy_with_locale(self, locale, form=False, map_initializer={}):
        osid_object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object_map.update(map_initializer)

        if form:
            self.ml_obj.my_osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                                             osid_object_map=osid_object_map,
                                                             proxy=get_proxy(with_locale=locale))
        else:
            self.ml_obj.my_osid_object = OsidObject(object_name='TEST_OBJECT',
                                                    osid_object_map=osid_object_map,
                                                    proxy=get_proxy(with_locale=locale))

    @classmethod
    def setUpClass(cls):
        cls.ml_obj = MultiLanguageUtils()
        cls.default_language_type = DEFAULT_LANGUAGE_TYPE
        cls.default_format_type = DEFAULT_FORMAT_TYPE
        cls.default_script_type = DEFAULT_SCRIPT_TYPE
        cls.hindi_language_type = Type('639-2%3AHIN%40ISO')
        cls.hindi_script_type = Type('15924%3ADEVA%40ISO')
        cls.telugu_language_type = Type('639-2%3ATEL%40ISO')
        cls.telugu_script_type = Type('15924%3ATELU%40ISO')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_empty_display_text_returns_display_text_instance(self):
        self.assertTrue(isinstance(self.ml_obj._empty_display_text(),
                                   DisplayText))

    def test_empty_display_text_text_is_empty_string(self):
        self.assertEqual(self.ml_obj._empty_display_text().text,
                         '')

    def test_display_text_dict_for_object_converts_to_default_lang_when_no_proxy(self):
        self.set_no_proxy()
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        })
        self.remove_osid_object()

    def test_display_text_dict_for_form_converts_to_default_lang_when_no_proxy(self):
        self.set_no_proxy(form=True)
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        })
        self.remove_osid_object(form=True)

    def test_display_text_dict_for_object_converts_to_proxy_lang(self):
        self.set_proxy_with_locale('hi')
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        })
        self.remove_osid_object()

    def test_display_text_dict_for_form_converts_to_proxy_lang(self):
        self.set_proxy_with_locale('hi', form=True)
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        })
        self.remove_osid_object(form=True)

    def test_display_text_dict_for_object_converts_to_default_if_no_proxy_lang(self):
        self.set_proxy_with_no_locale()
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        })
        self.remove_osid_object()

    def test_display_text_dict_for_form_converts_to_default_if_no_proxy_lang(self):
        self.set_proxy_with_no_locale(form=True)
        self.assertTrue(isinstance(self.ml_obj._display_text_dict('foo'),
                                   dict))
        self.assertEqual(self.ml_obj._display_text_dict('foo'), {
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        })
        self.remove_osid_object(form=True)

    def test_dict_display_text_throws_exception_if_not_display_text(self):
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj._dict_display_text({
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            })

    def test_dict_display_text_converts_display_text_to_dict(self):
        result = self.ml_obj._dict_display_text(DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }))
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result['text'], 'foo')
        self.assertEqual(result['languageTypeId'], str(self.telugu_language_type))
        self.assertEqual(result['formatTypeId'], str(self.default_format_type))
        self.assertEqual(result['scriptTypeId'], str(self.telugu_script_type))

    def test_str_display_text_for_object_converts_string_to_display_text_no_proxy(self):
        self.set_no_proxy()
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.default_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_str_display_text_for_form_converts_string_to_display_text_no_proxy(self):
        self.set_no_proxy(form=True)
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.default_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.default_script_type))
        self.remove_osid_object(form=True)

    def test_str_display_text_for_object_converts_string_to_display_text_proxy(self):
        self.set_proxy_with_locale('te')
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.telugu_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.telugu_script_type))
        self.remove_osid_object()

    def test_str_display_text_for_form_converts_string_to_display_text_proxy(self):
        self.set_proxy_with_locale('te', form=True)
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.telugu_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.telugu_script_type))
        self.remove_osid_object(form=True)

    def test_str_display_text_for_object_converts_string_to_display_text_proxy_no_locale(self):
        self.set_proxy_with_no_locale()
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.default_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_str_display_text_for_form_converts_string_to_display_text_proxy_no_locale(self):
        self.set_proxy_with_no_locale(form=True)
        self.assertTrue(isinstance(self.ml_obj._str_display_text('foo'),
                                   DisplayText))
        self.assertEqual(self.ml_obj._str_display_text('foo').text, 'foo')
        self.assertEqual(str(self.ml_obj._str_display_text('foo').language_type),
                         str(self.default_language_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').format_type),
                         str(self.default_format_type))
        self.assertEqual(str(self.ml_obj._str_display_text('foo').script_type),
                         str(self.default_script_type))
        self.remove_osid_object(form=True)

    def test_add_or_replace_value_throws_exception_if_not_form(self):
        self.set_no_proxy()
        with self.assertRaises(errors.IllegalState):
            self.ml_obj.add_or_replace_value('foo', '123')
        self.remove_osid_object()

    def test_add_or_replace_value_throws_exception_for_non_display_text(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.add_or_replace_value('foo', {
                'text': 'new foo',
                'languageTypeId': str(self.telugu_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.telugu_script_type)
            })
        self.remove_osid_object(form=True)

    def test_add_or_replace_value_throws_exception_for_non_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.add_or_replace_value('foo',
                                             DisplayText(display_text_map={
                                                 'text': 'new foo',
                                                 'languageTypeId': str(self.telugu_language_type),
                                                 'formatTypeId': str(self.default_format_type),
                                                 'scriptTypeId': str(self.telugu_script_type)
                                             }),
                                             dictionary=[])
        self.remove_osid_object(form=True)

    def test_add_or_replace_value_throws_exception_if_field_not_in_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.add_or_replace_value('foo',
                                             DisplayText(display_text_map={
                                                 'text': 'new foo',
                                                 'languageTypeId': str(self.telugu_language_type),
                                                 'formatTypeId': str(self.default_format_type),
                                                 'scriptTypeId': str(self.telugu_script_type)
                                             }),
                                             dictionary={
                                                 'bim': 123,
                                                 'bam': 'string'
                                             })
        self.remove_osid_object(form=True)

    def test_add_or_replace_value_with_no_dictionary_kwarg_can_add_new_lang(self):
        self.set_no_proxy(form=True, map_initializer={'foo': [{
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }]})
        self.assertEqual(len(self.ml_obj.my_osid_object_form._my_map['foo']), 1)
        self.ml_obj.add_or_replace_value('foo', DisplayText(display_text_map={
            'text': 'new foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }))
        self.assertEqual(len(self.ml_obj.my_osid_object_form._my_map['foo']), 2)
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][1]['text'],
                         'new foo')
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][1]['languageTypeId'],
                         str(self.telugu_language_type))
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][1]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][1]['scriptTypeId'],
                         str(self.telugu_script_type))

        self.remove_osid_object(form=True)

    def test_add_or_replace_value_with_no_dictionary_kwarg_can_update_existing_lang(self):
        self.set_no_proxy(form=True, map_initializer={'foo': [{
            'text': 'old foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }]})
        self.assertEqual(len(self.ml_obj.my_osid_object_form._my_map['foo']), 1)
        self.ml_obj.add_or_replace_value('foo', DisplayText(display_text_map={
            'text': 'new foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }))
        self.assertEqual(len(self.ml_obj.my_osid_object_form._my_map['foo']), 1)
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['text'],
                         'new foo')
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['languageTypeId'],
                         str(self.telugu_language_type))
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['scriptTypeId'],
                         str(self.telugu_script_type))

        self.remove_osid_object(form=True)

    def test_add_or_replace_value_with_dictionary_kwarg_can_add_new_lang(self):
        self.set_no_proxy(form=True)
        dictionary_to_update = {
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        }
        self.ml_obj.add_or_replace_value('foo', DisplayText(display_text_map={
            'text': 'new foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }), dictionary=dictionary_to_update)
        self.assertEqual(len(dictionary_to_update['foo']), 2)
        self.assertEqual(dictionary_to_update['foo'][1]['text'],
                         'new foo')
        self.assertEqual(dictionary_to_update['foo'][1]['languageTypeId'],
                         str(self.telugu_language_type))
        self.assertEqual(dictionary_to_update['foo'][1]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(dictionary_to_update['foo'][1]['scriptTypeId'],
                         str(self.telugu_script_type))

        self.remove_osid_object(form=True)

    def test_add_or_replace_value_with_dictionary_kwarg_can_update_existing_lang(self):
        self.set_no_proxy(form=True)
        dictionary_to_update = {
            'foo': [{
                'text': 'old foo',
                'languageTypeId': str(self.telugu_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.telugu_script_type)
            }]
        }
        self.ml_obj.add_or_replace_value('foo', DisplayText(display_text_map={
            'text': 'new foo',
            'languageTypeId': str(self.telugu_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.telugu_script_type)
        }), dictionary=dictionary_to_update)
        self.assertEqual(len(dictionary_to_update['foo']), 1)
        self.assertEqual(dictionary_to_update['foo'][0]['text'],
                         'new foo')
        self.assertEqual(dictionary_to_update['foo'][0]['languageTypeId'],
                         str(self.telugu_language_type))
        self.assertEqual(dictionary_to_update['foo'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(dictionary_to_update['foo'][0]['scriptTypeId'],
                         str(self.telugu_script_type))

        self.remove_osid_object(form=True)

    def test_get_default_language_value_throws_exception_if_not_dictionary(self):
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_default_language_value('foo', {})

    def test_get_default_language_value_throws_exception_if_field_not_in_dictionary(self):
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_default_language_value('foo', {'bar': 'bim'})

    def test_get_default_language_value_returns_default_if_available(self):
        dictionary_to_inspect = {
            'foo': [{
                'text': 'my foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        }
        result = self.ml_obj.get_default_language_value('foo',
                                                        dictionary_to_inspect)
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'my foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))

    def test_get_default_language_value_returns_first_if_no_default(self):
        dictionary_to_inspect = {
            'foo': [{
                'text': 'my foo',
                'languageTypeId': str(self.telugu_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.telugu_script_type)
            }]
        }
        result = self.ml_obj.get_default_language_value('foo',
                                                        dictionary_to_inspect)
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'my foo')
        self.assertEqual(str(result.language_type),
                         str(self.telugu_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.telugu_script_type))

    def test_get_matching_language_value_throws_exception_on_forms(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.IllegalState):
            self.ml_obj.get_matching_language_value('foo', dictionary={
                'foo': []
            })
        self.remove_osid_object(form=True)

    def test_get_matching_language_value_throws_exception_if_not_dictionary(self):
        self.set_no_proxy()
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_matching_language_value('foo', dictionary=[])
        self.remove_osid_object()

    def test_get_matching_language_value_dictionary_returns_empty_display_text_if_field_not_in_dictionary(self):
        self.set_no_proxy()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'bar': []
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         '')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_no_dictionary_returns_empty_display_text_if_field_not_in_dictionary(self):
        self.set_no_proxy(map_initializer={
            'bar': []
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         '')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_no_dictionary_returns_empty_display_text_if_field_not_populated(self):
        self.set_no_proxy(map_initializer={
            'foo': []
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         '')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_dictionary_returns_empty_display_text_if_field_not_populated(self):
        self.set_no_proxy()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': []
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         '')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_returns_proxy_locale(self):
        self.set_proxy_with_locale('hi', map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_proxy_locale_returns_default_language(self):
        self.set_proxy_with_locale('te', map_initializer={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_proxy_locale_returns_first_available(self):
        self.set_proxy_with_locale('te', map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_no_proxy_returns_default_locale(self):
        self.set_no_proxy(map_initializer={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_no_proxy_returns_first_avail_lang(self):
        self.set_no_proxy(map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_proxy_no_locale_returns_default_locale(self):
        self.set_proxy_with_no_locale(map_initializer={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_no_dictionary_proxy_no_locale_returns_first_avail_lang(self):
        self.set_proxy_with_no_locale(map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        result = self.ml_obj.get_matching_language_value('foo')
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_returns_proxy_locale(self):
        self.set_proxy_with_locale('hi')
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_proxy_locale_returns_default_language(self):
        self.set_proxy_with_locale('te')
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_proxy_locale_returns_first_available(self):
        self.set_proxy_with_locale('te')
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_no_proxy_returns_default_locale(self):
        self.set_no_proxy()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_no_proxy_returns_first_avail_lang(self):
        self.set_no_proxy()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_proxy_no_locale_returns_default_language(self):
        self.set_proxy_with_no_locale()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'foo')
        self.assertEqual(str(result.language_type),
                         str(self.default_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.default_script_type))
        self.remove_osid_object()

    def test_get_matching_language_value_with_dictionary_proxy_no_locale_returns_first_avail_lang(self):
        self.set_proxy_with_no_locale()
        result = self.ml_obj.get_matching_language_value('foo', dictionary={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        self.assertTrue(isinstance(result, DisplayText))
        self.assertEqual(result.text,
                         'hindi foo')
        self.assertEqual(str(result.language_type),
                         str(self.hindi_language_type))
        self.assertEqual(str(result.format_type),
                         str(self.default_format_type))
        self.assertEqual(str(result.script_type),
                         str(self.hindi_script_type))
        self.remove_osid_object()

    def test_get_index_of_language_type_throws_exception_if_not_form(self):
        self.set_no_proxy()
        with self.assertRaises(errors.IllegalState):
            self.ml_obj.get_index_of_language_type('foo',
                                                   self.hindi_language_type,
                                                   dictionary={
                                                       'foo': []
                                                   })
        self.remove_osid_object()

    def test_get_index_of_language_type_throws_exception_if_not_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_index_of_language_type('foo',
                                                   self.hindi_language_type,
                                                   dictionary=[])
        self.remove_osid_object(form=True)

    def test_get_index_of_language_type_throws_exception_if_field_not_in_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_index_of_language_type('foo',
                                                   self.hindi_language_type,
                                                   dictionary={
                                                       'boo': 'bim'
                                                   })
        self.remove_osid_object(form=True)

    def test_get_index_of_language_type_returns_index_of_match_no_dictionary(self):
        self.set_no_proxy(form=True, map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }, {
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        result = self.ml_obj.get_index_of_language_type('foo',
                                                        self.hindi_language_type)
        self.assertEqual(result, 0)
        self.remove_osid_object(form=True)

    def test_get_index_of_language_type_raises_exception_if_no_match_no_dictionary(self):
        self.set_no_proxy(form=True, map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }, {
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_index_of_language_type('foo',
                                                   self.telugu_language_type)
        self.remove_osid_object(form=True)

    def test_get_index_of_language_type_returns_index_of_match_dictionary(self):
        self.set_no_proxy(form=True)
        result = self.ml_obj.get_index_of_language_type('foo',
                                                        self.hindi_language_type,
                                                        dictionary={
                                                            'foo': [{
                                                                'text': 'hindi foo',
                                                                'languageTypeId': str(self.hindi_language_type),
                                                                'formatTypeId': str(self.default_format_type),
                                                                'scriptTypeId': str(self.hindi_script_type)
                                                            }, {
                                                                'text': 'foo',
                                                                'languageTypeId': str(self.default_language_type),
                                                                'formatTypeId': str(self.default_format_type),
                                                                'scriptTypeId': str(self.default_script_type)
                                                            }]
                                                        })
        self.assertEqual(result, 0)
        self.remove_osid_object(form=True)

    def test_get_index_of_language_type_raises_exception_if_no_match_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.get_index_of_language_type('foo',
                                                   self.telugu_language_type,
                                                   dictionary={
                                                       'foo': [{
                                                           'text': 'hindi foo',
                                                           'languageTypeId': str(self.hindi_language_type),
                                                           'formatTypeId': str(self.default_format_type),
                                                           'scriptTypeId': str(self.hindi_script_type)
                                                       }, {
                                                           'text': 'foo',
                                                           'languageTypeId': str(self.default_language_type),
                                                           'formatTypeId': str(self.default_format_type),
                                                           'scriptTypeId': str(self.default_script_type)
                                                       }]
                                                   })
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_throws_exception_if_not_form(self):
        self.set_no_proxy()
        with self.assertRaises(errors.IllegalState):
            self.ml_obj.remove_field_by_language('foo',
                                                 self.hindi_language_type)
        self.remove_osid_object()

    def test_remove_field_by_language_language_type_must_be_instance_of_type(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.remove_field_by_language('foo',
                                                 str(self.hindi_language_type))
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_dictionary_must_be_dict(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.remove_field_by_language('foo',
                                                 self.hindi_language_type,
                                                 dictionary=[])
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_field_must_be_in_dictionary(self):
        self.set_no_proxy(form=True)
        with self.assertRaises(errors.InvalidArgument):
            self.ml_obj.remove_field_by_language('foo',
                                                 self.hindi_language_type,
                                                 dictionary={
                                                     'boo': 'bim'
                                                 })
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_no_change_if_language_type_not_present(self):
        self.set_no_proxy(form=True)
        dictionary_to_test = {
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        }
        self.ml_obj.remove_field_by_language('foo',
                                             self.telugu_language_type,
                                             dictionary=dictionary_to_test)
        self.assertTrue(len(list(dictionary_to_test.items())), 1)
        self.assertEqual(list(dictionary_to_test.keys())[0], 'foo')
        self.assertEqual(dictionary_to_test['foo'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_only_removes_the_one_language(self):
        self.set_no_proxy(form=True)
        dictionary_to_test = {
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }, {
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        }
        self.ml_obj.remove_field_by_language('foo',
                                             self.hindi_language_type,
                                             dictionary=dictionary_to_test)
        self.assertTrue(len(list(dictionary_to_test.items())), 1)
        self.assertEqual(list(dictionary_to_test.keys())[0], 'foo')
        self.assertEqual(dictionary_to_test['foo'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_no_change_if_language_type_not_present_no_dictionary(self):
        self.set_no_proxy(form=True, map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }]
        })
        self.ml_obj.remove_field_by_language('foo',
                                             self.telugu_language_type)
        self.assertTrue(len(self.ml_obj.my_osid_object_form._my_map['foo']), 1)
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.remove_osid_object(form=True)

    def test_remove_field_by_language_only_removes_the_one_language_no_dictionary(self):
        self.set_no_proxy(form=True, map_initializer={
            'foo': [{
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }, {
                'text': 'foo',
                'languageTypeId': str(self.default_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.default_script_type)
            }]
        })
        self.ml_obj.remove_field_by_language('foo',
                                             self.hindi_language_type)
        self.assertTrue(len(self.ml_obj.my_osid_object_form._my_map['foo']), 1)
        self.assertEqual(self.ml_obj.my_osid_object_form._my_map['foo'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.remove_osid_object(form=True)


class TestMultiLanguageFormRecord(unittest.TestCase):
    """Tests for MultiLanguageFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.default_language_type = DEFAULT_LANGUAGE_TYPE
        cls.default_format_type = DEFAULT_FORMAT_TYPE
        cls.default_script_type = DEFAULT_SCRIPT_TYPE
        cls.hindi_language_type = Type('639-2%3AHIN%40ISO')
        cls.hindi_script_type = Type('15924%3ADEVA%40ISO')
        cls.telugu_language_type = Type('639-2%3ATEL%40ISO')
        cls.telugu_script_type = Type('15924%3ATELU%40ISO')

        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_edit_description(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['descriptions'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'foo')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.default_script_type))

        form.edit_description(DisplayText(text='new foo',
                                          language_type=self.default_language_type,
                                          format_type=self.default_format_type,
                                          script_type=self.default_script_type))
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'new foo')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.default_script_type))

    def test_edit_description_requires_display_text(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['descriptions'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.edit_description('foo')

    def test_edit_description_throws_exception_if_language_not_exist(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['descriptions'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.edit_description(DisplayText(display_text_map={
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }))

    def test_can_add_display_name_new_language(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'],
                         [])
        form.add_display_name(DisplayText(display_text_map={
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'hindi foo')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

    def test_can_add_display_name_existing_language(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'],
                         [])
        form.add_display_name(DisplayText(display_text_map={
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'hindi foo')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

        form.add_display_name(DisplayText(display_text_map={
            'text': 'hindi foo 2',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'hindi foo 2')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

    def test_add_display_name_requires_display_text(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_display_name('foo')

    def test_can_add_description_new_language(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'],
                         [])
        form.add_description(DisplayText(display_text_map={
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'hindi foo')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

    def test_can_add_description_existing_language(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'],
                         [])
        form.add_description(DisplayText(display_text_map={
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'hindi foo')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

        form.add_description(DisplayText(display_text_map={
            'text': 'hindi foo 2',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }))
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'hindi foo 2')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.hindi_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.hindi_script_type))

    def test_add_description_requires_display_text(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.add_description('foo')

    def test_remove_description_requires_type(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.remove_description_by_language(str(self.default_language_type))

    def test_can_remove_description_by_language_type(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['descriptions'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        form.remove_description_by_language(self.default_language_type)
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 0)

    def test_remove_description_no_changes_if_language_not_exist(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['descriptions'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        form.remove_description_by_language(self.telugu_language_type)
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['text'],
                         'foo')
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['descriptions'][0]['scriptTypeId'],
                         str(self.default_script_type))

    def test_edit_display_name_throws_exception_if_language_not_exist(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['displayNames'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.edit_display_name(DisplayText(display_text_map={
                'text': 'hindi foo',
                'languageTypeId': str(self.hindi_language_type),
                'formatTypeId': str(self.default_format_type),
                'scriptTypeId': str(self.hindi_script_type)
            }))

    def test_can_edit_display_name(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['displayNames'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'foo')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.default_script_type))

        form.edit_display_name(DisplayText(text='new foo',
                                           language_type=self.default_language_type,
                                           format_type=self.default_format_type,
                                           script_type=self.default_script_type))
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'new foo')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.default_script_type))

    def test_edit_display_name_requires_display_text(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['displayNames'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.edit_display_name('foo')

    def test_remove_display_name_requires_type(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.InvalidArgument):
            form.remove_display_name_by_language(str(self.default_language_type))

    def test_remove_display_name_changes_nothing_if_language_not_present(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['displayNames'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        form.remove_display_name_by_language(self.telugu_language_type)
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['text'],
                         'foo')
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['languageTypeId'],
                         str(self.default_language_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['formatTypeId'],
                         str(self.default_format_type))
        self.assertEqual(form.my_osid_object_form._my_map['displayNames'][0]['scriptTypeId'],
                         str(self.default_script_type))

    def test_can_remove_display_name_by_language_type(self):
        object_map = deepcopy(utilities.TEST_OBJECT_MAP)
        object_map['displayNames'] = [{
            'text': 'foo',
            'languageTypeId': str(self.default_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.default_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=object_map)
        form = MultiLanguageFormRecord(osid_object_form)
        form.remove_display_name_by_language(self.default_language_type)
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 0)

    def test_can_clear_descriptions(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['descriptions'] = [{
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = MultiLanguageFormRecord(osid_object_form)
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 1)

        form.clear_descriptions()
        self.assertEqual(len(form.my_osid_object_form._my_map['descriptions']), 0)

    def test_can_clear_display_names(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['displayNames'] = [{
            'text': 'hindi foo',
            'languageTypeId': str(self.hindi_language_type),
            'formatTypeId': str(self.default_format_type),
            'scriptTypeId': str(self.hindi_script_type)
        }]
        osid_object_form = OsidObjectForm(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)
        form = MultiLanguageFormRecord(osid_object_form)
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 1)

        form.clear_display_names()
        self.assertEqual(len(form.my_osid_object_form._my_map['displayNames']), 0)

    def test_can_get_descriptions_metadata(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_descriptions_metadata(), Metadata))

    def test_can_get_display_names_metadata(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        self.assertTrue(isinstance(form.get_display_names_metadata(), Metadata))

    def test_add_display_name_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_display_name(None)

    def test_remove_display_name_by_language_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.remove_display_name_by_language(None)

    def test_edit_display_name_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.edit_display_name(None)

    def test_add_description_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.add_description(None)

    def test_remove_description_by_language_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.remove_description_by_language(None)

    def test_edit_description_throws_exception_if_passed_none(self):
        form = MultiLanguageFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NullArgument):
            form.edit_description(None)


class TestMultiLanguageRecord(unittest.TestCase):
    """Tests for MultiLanguageRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['descriptions'] = [{
            'text': 'foo description',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }]
        obj_map['displayNames'] = [{
            'text': 'foo name',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }]
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)
        cls.multi_language_object = MultiLanguageRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    # NOTE: we do not test for all possible scenarios of no
    #   entries, default language, proxy locale, etc., because
    #   those scenarios would be redundant with the tests for
    #   MultiLanguageUtils

    def test_can_get_description(self):
        self.assertTrue(isinstance(self.multi_language_object.description,
                                   DisplayText))
        desc = self.multi_language_object.description
        self.assertEqual(desc.text,
                         'foo description')
        self.assertEqual(str(desc.language_type),
                         '639-2%3AENG%40ISO')
        self.assertEqual(str(desc.format_type),
                         'TextFormats%3APLAIN%40okapia.net')
        self.assertEqual(str(desc.script_type),
                         '15924%3ALATN%40ISO')

    def test_can_get_display_name(self):
        self.assertTrue(isinstance(self.multi_language_object.display_name,
                                   DisplayText))
        name = self.multi_language_object.display_name
        self.assertEqual(name.text,
                         'foo name')
        self.assertEqual(str(name.language_type),
                         '639-2%3AENG%40ISO')
        self.assertEqual(str(name.format_type),
                         'TextFormats%3APLAIN%40okapia.net')
        self.assertEqual(str(name.script_type),
                         '15924%3ALATN%40ISO')


class QueryWrapper(OsidObjectQuery):
    def __init__(self):
        self._all_supported_record_type_ids = []
        super(QueryWrapper, self).__init__(None)


class TestMultiLanguageQueryRecord(unittest.TestCase):
    """Tests for MultiLanguageQueryRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_query = QueryWrapper()
        cls.multi_language_query = MultiLanguageQueryRecord(cls.osid_query)

    @classmethod
    def tearDownClass(cls):
        pass

    # NOTE: we do not test for all possible scenarios of no
    #   entries, default language, proxy locale, etc., because
    #   those scenarios would be redundant with the tests for
    #   MultiLanguageUtils

    def test_can_match_descriptions(self):
        osid_query = QueryWrapper()
        multi_language_query = MultiLanguageQueryRecord(osid_query)
        self.assertEqual(multi_language_query._my_osid_query._query_terms,
                         {})

        multi_language_query.match_descriptions('foo', True)
        self.assertIn('descriptions.text',
                      multi_language_query._my_osid_query._query_terms)
        self.assertEqual(multi_language_query._my_osid_query._query_terms['descriptions.text'],
                         {'$in': ['foo']})

    def test_can_clear_match_descriptions(self):
        osid_query = QueryWrapper()
        multi_language_query = MultiLanguageQueryRecord(osid_query)
        multi_language_query._my_osid_query._query_terms = {
            'descriptions.text': {
                '$in': ['foo']
            }
        }
        multi_language_query.clear_match_descriptions()
        self.assertEqual(multi_language_query._my_osid_query._query_terms,
                         {})

    def test_can_match_display_names(self):
        osid_query = QueryWrapper()
        multi_language_query = MultiLanguageQueryRecord(osid_query)
        self.assertEqual(multi_language_query._my_osid_query._query_terms,
                         {})

        multi_language_query.match_display_names('foo', True)
        self.assertIn('displayNames.text',
                      multi_language_query._my_osid_query._query_terms)
        self.assertEqual(multi_language_query._my_osid_query._query_terms['displayNames.text'],
                         {'$in': ['foo']})

    def test_can_clear_match_display_names(self):
        osid_query = QueryWrapper()
        multi_language_query = MultiLanguageQueryRecord(osid_query)
        multi_language_query._my_osid_query._query_terms = {
            'displayNames.text': {
                '$in': ['foo']
            }
        }
        multi_language_query.clear_match_display_names()
        self.assertEqual(multi_language_query._my_osid_query._query_terms,
                         {})

    def test_null_value_throws_exception_match_descriptions(self):
        with self.assertRaises(errors.NullArgument):
            self.multi_language_query.match_descriptions(None, True)

    def test_null_match_throws_exception_match_descriptions(self):
        with self.assertRaises(errors.NullArgument):
            self.multi_language_query.match_descriptions('foo', None)

    def test_null_value_throws_exception_match_display_names(self):
        with self.assertRaises(errors.NullArgument):
            self.multi_language_query.match_display_names(None, True)

    def test_null_match_throws_exception_match_display_names(self):
        with self.assertRaises(errors.NullArgument):
            self.multi_language_query.match_display_names('foo', None)

    def test_non_string_value_throws_exception_match_descriptions(self):
        with self.assertRaises(errors.InvalidArgument):
            self.multi_language_query.match_descriptions(123, True)

    def test_non_bool_match_throws_exception_match_descriptions(self):
        with self.assertRaises(errors.InvalidArgument):
            self.multi_language_query.match_descriptions('foo', 123)

    def test_non_string_value_throws_exception_match_display_names(self):
        with self.assertRaises(errors.InvalidArgument):
            self.multi_language_query.match_display_names(123, True)

    def test_non_bool_match_throws_exception_match_display_names(self):
        with self.assertRaises(errors.InvalidArgument):
            self.multi_language_query.match_display_names('foo', 123)
