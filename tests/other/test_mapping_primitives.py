"""Tests for osid.mapping.primitives objects implemented in primordium"""

import unittest
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate
from dlkit.primordium.mapping.spatial_units import RectangularSpatialUnit


class TestBasicCoordinates(unittest.TestCase):
    """Tests for dlkit.primordium.BasicCoordinates"""

    @classmethod
    def setUpClass(cls):
        cls.coordinate11 = BasicCoordinate([1, 1])
        cls.coordinate22 = BasicCoordinate([2, 2])
        cls.coordinate12 = BasicCoordinate([1, 2])
        cls.coordinate21 = BasicCoordinate([2, 1])
        cls.coordinate21a = BasicCoordinate([2, 1])

    def test_equal(self):
        """Tests equal"""
        self.assertEqual(self.coordinate21, self.coordinate21a)
        self.assertTrue(self.coordinate21 == self.coordinate21a)
        self.assertTrue(self.coordinate21 == self.coordinate21)
        self.assertFalse(self.coordinate21 == self.coordinate11)

    def test_not_equal(self):
        """Tests not equal"""
        self.assertNotEqual(self.coordinate11, self.coordinate21a)
        self.assertNotEqual(self.coordinate11, self.coordinate22)
        self.assertNotEqual(self.coordinate21, self.coordinate22)
        self.assertNotEqual(self.coordinate21, self.coordinate12)
        self.assertNotEqual(self.coordinate12, self.coordinate21)
        self.assertTrue(self.coordinate11 != self.coordinate22)

    def test_greater_than(self):
        """Tests greater than"""
        self.assertTrue(self.coordinate22 > self.coordinate11)
        self.assertFalse(self.coordinate12 > self.coordinate11)

    def test_greater_than_or_equal(self):
        """Tests greater than or equal"""
        self.assertTrue(self.coordinate22 >= self.coordinate11)
        self.assertTrue(self.coordinate12 >= self.coordinate11)
        self.assertFalse(self.coordinate11 >= self.coordinate22)

    def test_less_than(self):
        """Tests less than"""
        self.assertTrue(self.coordinate11 < self.coordinate22)
        self.assertFalse(self.coordinate11 < self.coordinate12)

    def test_less_than_or_equal(self):
        """Tests less than or equal"""
        self.assertTrue(self.coordinate11 <= self.coordinate22)
        self.assertTrue(self.coordinate11 <= self.coordinate12)
        self.assertFalse(self.coordinate22 <= self.coordinate11)


class TestRectangularSpatialAreas(unittest.TestCase):
    """Tests for dlkit.primordium.RectangularSpatialAreas"""

    @classmethod
    def setUpClass(cls):
        cls.coordinate11 = BasicCoordinate([1, 1])
        cls.coordinate22 = BasicCoordinate([2, 2])
        cls.coordinate12 = BasicCoordinate([1, 2])
        cls.coordinate21 = BasicCoordinate([2, 1])
        cls.inside_coordinate = BasicCoordinate([1.2, 1.4])
        cls.center_coordinate = BasicCoordinate([1.5, 1.5])
        cls.outside_coordinate1 = BasicCoordinate([2.2, 2.04])
        cls.outside_coordinate2 = BasicCoordinate([0.2, 0.997])
        cls.rect = RectangularSpatialUnit(coordinate=cls.coordinate11, width=1, height=1)

    def test_inside(self):
        """Tests less than"""
        self.assertTrue(self.inside_coordinate in self.rect)
        self.assertTrue(self.coordinate11 in self.rect)
        self.assertTrue(self.coordinate22 in self.rect)
        self.assertTrue(self.coordinate12 in self.rect)
        self.assertTrue(self.coordinate21 in self.rect)
        self.assertFalse(self.outside_coordinate1 in self.rect)
        self.assertFalse(self.outside_coordinate2 in self.rect)

    def test_center(self):
        self.assertEqual(self.center_coordinate, self.rect.get_center_coordinate())

    def test_spatial_unit_map(self):
        map = self.rect.get_spatial_unit_map()
        print('RT== ', str(map['recordTypes']))
        self.assertTrue(map['type'] == 'SpatialUnit')
        self.assertTrue(map['recordTypes'] == ['osid.mapping.SpatialUnit%3Arectangle%40ODL.MIT.EDU'])
        self.assertTrue(map['coordinateValues'] == self.coordinate11.get_values())
        self.assertTrue(map['width'] == 1)
        self.assertTrue(map['height'] == 1)
