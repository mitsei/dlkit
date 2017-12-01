import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.json_ import utilities as dlkit_utilities
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.records.assessment.clix.assessment_offered_records import *

from ... import utilities


class TestNofMAssessmentOfferedFormRecord(unittest.TestCase):
    """Tests for NofMAssessmentOfferedFormRecord"""
    def setUp(self):
        self.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        self.osid_object_form._authority = 'TESTING.MIT.EDU'
        self.osid_object_form._namespace = 'records.Testing'

        self.form = utilities.add_class(self.osid_object_form, NofMAssessmentOfferedFormRecord, initialize=True)

    def test_can_get_n_of_m_metadata(self):
        self.assertTrue(isinstance(self.form.get_n_of_m_metadata(), Metadata))

    def test_can_set_n_of_m(self):
        self.assertEqual(self.form._my_map['nOfM'], -1)
        self.form.set_n_of_m(2)
        self.assertEqual(self.form._my_map['nOfM'], 2)

    def test_setting_n_of_m_with_none_throws_exception(self):
        with self.assertRaises(errors.NullArgument):
            self.form.set_n_of_m(None)

    def test_setting_n_of_m_with_non_int_throws_exception(self):
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_n_of_m(float(1.2))
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_n_of_m('0')
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_n_of_m(True)

    def test_can_clear_n_of_m(self):
        self.form.set_n_of_m(5)
        self.assertEqual(self.form._my_map['nOfM'], 5)
        self.form.clear_n_of_m()
        self.assertEqual(self.form._my_map['nOfM'], -1)


class TestUnlockPreviousButtonAssessmentOfferedRecord(unittest.TestCase):
    """Tests for UnlockPreviousButtonAssessmentOfferedRecord"""
    def setUp(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['unlockPrevious'] = 'always'
        self.osid_object = OsidObject(object_name='TEST_OBJECT',
                                      osid_object_map=obj_map)

        self.prev_button_object = utilities.add_class(self.osid_object,
                                                      UnlockPreviousButtonAssessmentOfferedRecord)

    def test_can_get_unlock_previous(self):
        self.assertTrue(dlkit_utilities.is_string(self.prev_button_object.get_unlock_previous()))
        self.assertEqual(self.prev_button_object.get_unlock_previous(),
                         'always')

    def test_can_test_has_unlock_previous(self):
        self.assertTrue(self.prev_button_object.has_unlock_previous())

    def test_get_unlock_previous_throws_exception_if_no_unlock_previous(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        prev_button_object = utilities.add_class(osid_object, UnlockPreviousButtonAssessmentOfferedRecord)
        with self.assertRaises(errors.IllegalState):
            prev_button_object.unlock_previous

    def test_has_unlock_previous_false_if_none(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['unlockPrevious'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        prev_button_object = utilities.add_class(osid_object, UnlockPreviousButtonAssessmentOfferedRecord)
        self.assertFalse(prev_button_object.has_unlock_previous())

    def test_has_unlock_previous_false_if_not_in_map(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        prev_button_object = utilities.add_class(osid_object, UnlockPreviousButtonAssessmentOfferedRecord)
        self.assertFalse(prev_button_object.has_unlock_previous())


class TestUnlockPreviousButtonAssessmentOfferedFormRecord(unittest.TestCase):
    """Tests for UnlockPreviousButtonAssessmentOfferedFormRecord"""
    def setUp(self):
        self.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        self.osid_object_form._authority = 'TESTING.MIT.EDU'
        self.osid_object_form._namespace = 'records.Testing'

        self.form = utilities.add_class(self.osid_object_form,
                                        UnlockPreviousButtonAssessmentOfferedFormRecord,
                                        initialize=True)

    def test_can_get_unlock_previous_metadata(self):
        self.assertTrue(isinstance(self.form.get_unlock_previous_metadata(), Metadata))

    def test_can_set_unlock_previous(self):
        self.assertEqual(self.form._my_map['unlockPrevious'],
                         'always')
        self.form.set_unlock_previous('never')
        self.assertEqual(self.form._my_map['unlockPrevious'],
                         'never')

    def test_setting_unlock_previous_with_none_throws_exception(self):
        with self.assertRaises(errors.NullArgument):
            self.form.set_unlock_previous(None)

    def test_setting_unlock_previous_with_non_string_throws_exception(self):
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_unlock_previous(float(1.2))
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_unlock_previous(0)
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_unlock_previous(True)

    def test_can_clear_unlock_previous(self):
        self.form.set_unlock_previous('foo')
        self.assertEqual(self.form._my_map['unlockPrevious'], 'foo')
        self.form.clear_unlock_previous()
        self.assertEqual(self.form._my_map['unlockPrevious'], 'always')
